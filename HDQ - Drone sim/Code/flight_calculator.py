# flight_calculator.py
# This file contains the core logic for flight dynamics calculations.
import numpy as np
# --- MODIFIED: Imports are now from separate data files ---
from component_data import MOTOR_PERFORMANCE_DATA
from battery_data import BATTERY_DATABASE


def interpolate(x, x_points, y_points):
    """Performs linear interpolation."""
    if not x_points or not y_points: return 0
    if x <= x_points[0]: return y_points[0]
    if x >= x_points[-1]: return y_points[-1]

    for i in range(len(x_points) - 1):
        if x_points[i] <= x < x_points[i + 1]:
            y = y_points[i] + (x - x_points[i]) * (y_points[i + 1] - y_points[i]) / (x_points[i + 1] - x_points[i])
            return y
    return y_points[-1]


def calculate_thrust_coefficients(performance_data, prop_diameter_in=5.0, air_density=1.225):
    """
    Calculates thrust coefficient C_T for all throttle points in performance_data.

    Parameters:
        performance_data: dict of throttle -> motor data
        prop_diameter_in: prop diameter in inches (default 5")
        air_density: rho in kg/m^3 (default sea level 1.225)

    Returns:
        ct_table: dict of throttle -> C_T
        mean_ct: average C_T across all points
    """
    D = prop_diameter_in * 0.0254  # Convert inches to meters
    ct_table = {}
    for throttle, data in performance_data.items():
        thrust_N = data['thrust_g'] / 1000 * 9.81  # g -> N
        n = data['rpm'] / 60  # RPM -> rev/s
        if n > 0 and thrust_N > 0:
            C_T = thrust_N / (air_density * n ** 2 * D ** 4)
            ct_table[throttle] = C_T
        else:
            ct_table[throttle] = 0.0

    mean_ct = np.mean(list(ct_table.values())) if ct_table else 0.0
    return ct_table, mean_ct


def calculate_hover_metrics(motor, kv_str, prop, payload_g, frame_g, accessories_g, num_motors, battery_specs):
    """
    Computes all hover-related metrics for the drone.
    Fully rewritten to fix throttle/thrust interpolation and energy calculations.
    """
    try:
        kv = int(kv_str)

        # --- 1. Total Mass (battery included) ---
        total_mass_g = payload_g + frame_g + accessories_g + battery_specs["weight_g"]
        required_thrust_g = total_mass_g
        thrust_per_motor_g = required_thrust_g / num_motors

        # --- 2. Load Motor Performance Data ---
        performance = MOTOR_PERFORMANCE_DATA[motor][kv][prop]

        throttles = np.array(sorted(performance.keys()))                   # throttle %
        thrusts   = np.array([performance[t]["thrust_g"] for t in throttles])
        powers    = np.array([performance[t]["power_w"]  for t in throttles])
        currents  = np.array([performance[t]["current"]  for t in throttles])

        max_thrust_motor = thrusts.max()

        # --- 3. Hover Feasibility Check ---
        if thrust_per_motor_g >= max_thrust_motor:
            return {"error": "Total weight exceeds maximum thrust capability."}

        # --- 4. Invert thrust(throttle) → throttle(thrust) ---
        # Now correct: thrusts are X, throttles are Y

        # 4a. Find the minimum data point (usually the first one)
        min_thrust_motor = thrusts.min()
        min_throttle = throttles.min()

        # 4b. If the required thrust is less than the minimum measured thrust,
        #     we must assume the minimum recorded throttle/power/current.
        if thrust_per_motor_g < min_thrust_motor:
            # Clamp to the minimum measured throttle, as this is the operational floor.
            hover_throttle = min_throttle
        else:
            # Interpolate normally
            hover_throttle = np.interp(thrust_per_motor_g, thrusts, throttles)

        # Now compute power/current AT that throttle (this step is now safe)
        hover_power_motor = np.interp(hover_throttle, throttles, powers)
        hover_current_motor = np.interp(hover_throttle, throttles, currents)

        # --- 5. CT Calculation (unchanged) ---
        ct_table, mean_ct = calculate_thrust_coefficients(performance)
        estimated_max_thrust = thrusts.max()

        # --- 6. System Totals ---
        total_power   = hover_power_motor * num_motors
        total_current = hover_current_motor * num_motors
        total_max_thrust_g = max_thrust_motor * num_motors
        thrust_to_weight = total_max_thrust_g / total_mass_g

        # --- 7. Battery / Flight Time ---
        capacity_ah = battery_specs["capacity_mah"] / 1000
        max_continuous_current = capacity_ah * battery_specs["c_rating"]

        if "voltage" in battery_specs:
            voltage = battery_specs["voltage"]
            energy_wh = capacity_ah * voltage * 0.8
            flight_time_min = (energy_wh / total_power) * 60 if total_power > 0 else float("inf")
        else:
            flight_time_min = (capacity_ah * 0.8 / total_current) * 60 if total_current > 0 else float("inf")

        return {
            "total_mass_g": round(total_mass_g, 2),
            "required_thrust_g": round(required_thrust_g, 2),
            "thrust_per_motor_g": round(thrust_per_motor_g, 2),
            "hover_throttle_%": round(hover_throttle, 1),
            "total_power_w": round(total_power, 2),
            "total_current_a": round(total_current, 2),
            "thrust_to_weight_ratio": round(thrust_to_weight, 2),
            "thrust_coefficients_table": {k: round(v, 4) for k, v in ct_table.items()},
            "mean_thrust_coefficient": round(mean_ct, 4),
            "estimated_max_thrust_g": round(estimated_max_thrust, 2),
            "flight_time_min": round(flight_time_min, 2),
            "max_battery_current_a": round(max_continuous_current, 2),
            "battery_status": "OK" if total_current <= max_continuous_current else "WARNING: Exceeds C-Rating!",
            "graph_data": {
                "throttles": throttles.tolist(),
                "thrusts": thrusts.tolist(),
                "hover_throttle": hover_throttle,
                "hover_thrust": thrust_per_motor_g,
            },
            "error": None
        }

    except Exception as e:
        return {"error": f"Calculation error: {e}"}
