import tkinter as tk
from tkinter import ttk
from component_data import MOTOR_PERFORMANCE_DATA
from battery_data import BATTERY_DATABASE
from flight_calculator import calculate_hover_metrics
from drone_drawer import draw_drone

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- Theme Configuration ---
BG_COLOR = "#000000"
FRAME_BG_COLOR = "#101010"
FG_COLOR = "#FFFFFF"
ENTRY_BG = "#222222"
BUTTON_BORDER = "#FFFFFF"
BUTTON_ACTIVE_BG = "#333333"
FONT_FAMILY = "Times New Roman"

DRONE_TYPES = {
    "Tricopter (3 Motors)": 3,
    "Quadcopter (4 Motors)": 4,
    "Hexacopter (6 Motors)": 6,
    "Octocopter (8 Motors)": 8,
}


class HyDroQuadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HyDroQuad Flight Dynamics Simulator")
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>', lambda e: self.root.attributes('-fullscreen', False))
        self.root.configure(bg=BG_COLOR)

        self.setup_styles()

        # --- Main Layout Frames ---
        left_frame = tk.Frame(self.root, bg=FRAME_BG_COLOR, padx=30, pady=40)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, expand=False, padx=(20, 10))

        self.right_frame = tk.Frame(self.root, bg=BG_COLOR, padx=40, pady=40)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.populate_input_frame(left_frame)
        self.populate_output_frame(self.right_frame)

        # --- NEW: Add Calligraphy Signature ---
        # A nice script font like "Segoe Script" or "Brush Script MT" works well.
        # We use a try-except block in case the specific font isn't installed.
        try:
            calligraphy_font = ("Segoe Script", 20, "italic")
        except tk.TclError:
            calligraphy_font = ("cursive", 20, "italic")  # Fallback font

        style = ttk.Style()
        style.configure("Calligraphy.TLabel", font=calligraphy_font, background=BG_COLOR, foreground=FG_COLOR)

        signature_label = ttk.Label(self.root, text="HyDroQuad", style="Calligraphy.TLabel")
        signature_label.place(relx=1.0, rely=1.0, x=-25, y=-15, anchor='se')

    def populate_input_frame(self, parent):
        title_label = ttk.Label(parent, text="System Configuration", font=(FONT_FAMILY, 24, "bold"),
                                style="Title.TLabel")
        title_label.pack(pady=(0, 40))

        self.drone_type_var = self.create_combobox(parent, "Drone Type:", list(DRONE_TYPES.keys()))
        self.battery_var = tk.StringVar()
        self.battery_combo = self.create_combobox(parent, "Select Battery:", list(BATTERY_DATABASE.keys()),
                                                  var=self.battery_var)
        self.battery_var.trace_add('write', self.update_battery_weight)

        # Battery Weight Display
        self.battery_weight_label = ttk.Label(parent, text="Battery Weight: -", font=(FONT_FAMILY, 12))
        self.battery_weight_label.pack(pady=(0, 10))
        self.motor_var = self.create_combobox(parent, "Select Motor:", list(MOTOR_PERFORMANCE_DATA.keys()))
        self.motor_var.trace_add('write', self.update_kv_options)
        self.kv_var = tk.StringVar()
        self.kv_combo = self.create_combobox(parent, "Select Motor KV:", [], var=self.kv_var)
        self.kv_var.trace_add('write', self.update_prop_options)
        self.prop_var = tk.StringVar()
        self.prop_combo = self.create_combobox(parent, "Select Propeller:", [], var=self.prop_var)
        self.update_kv_options()
        self.payload_weight = self.create_input_row(parent, "Payload Weight (g):", 500.0)
        self.frame_weight = self.create_input_row(parent, "Frame Weight (g):", 500.0)
        self.accessories_weight = self.create_input_row(parent, "Accessories Weight (g):", 500.0)
        calculate_button = ttk.Button(parent, text="Calculate Flight Metrics", command=self.run_simulation, padding=12,
                                      style="TButton")
        calculate_button.pack(pady=(50, 0), ipady=5, fill=tk.X)

    def populate_output_frame(self, parent, results=None):
        for widget in parent.winfo_children():
            widget.destroy()

        if results is None:
            output_label = ttk.Label(parent, text="Metrics and Graphs will be displayed here.",
                                     font=(FONT_FAMILY, 18, "italic"), style="Placeholder.TLabel", anchor="center")
            output_label.pack(expand=True)
            return

        if results.get("error"):
            error_label = ttk.Label(parent, text=f"Error: {results['error']}", font=(FONT_FAMILY, 16), foreground="red",
                                    style="Placeholder.TLabel", anchor="center", wraplength=500)
            error_label.pack(expand=True)
        else:
            parent.grid_columnconfigure(0, weight=1)
            parent.grid_columnconfigure(1, weight=1)
            parent.grid_rowconfigure(0, weight=1)
            parent.grid_rowconfigure(1, weight=1)

            metrics_frame = ttk.Frame(parent, style="Output.TFrame")
            metrics_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 20), pady=(0, 10))
            graph_frame = ttk.Frame(parent, style="Output.TFrame")
            graph_frame.grid(row=0, column=1, sticky="nsew", pady=(0, 10))
            drone_sketch_frame = ttk.Frame(parent, style="Output.TFrame")
            drone_sketch_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(10, 0))

            self.drone_canvas = tk.Canvas(drone_sketch_frame, width=400, height=300, bg=BG_COLOR, highlightthickness=0)
            self.drone_canvas.pack(fill=tk.BOTH, expand=True)

            results_text = (
                f"Total Mass: {results['total_mass_g']} g\n"
                f"Hover Thrust: {results['thrust_per_motor_g']} g/motor\n"
                f"Hover Throttle: {results['hover_throttle_%']} %\n\n"
                f"Total Power (Hover): {results['total_power_w']} W\n"
                f"Total Current (Hover): {results['total_current_a']} A\n"
                f"Thrust/Weight Ratio: {results['thrust_to_weight_ratio']}:1\n\n"
                f"Est. Flight Time (Hover): {results['flight_time_min']} min\n\n"
                f"Battery Status: {results['battery_status']}\n"
                f"Max Battery Current: {results['max_battery_current_a']} A"
            )

            ct_table_text = "\nThrust Coefficients (C_T) per throttle:\n"
            for throttle, ct in results.get('thrust_coefficients_table', {}).items():
                ct_table_text += f"{throttle}%: {ct}\n"
            ct_table_text += f"\nMean Thrust Coefficient: {results.get('mean_thrust_coefficient', 0)}"

            results_label = ttk.Label(metrics_frame, text=results_text + "\n\n" + ct_table_text, font=(FONT_FAMILY, 16),
                                      style="Placeholder.TLabel", justify=tk.LEFT)
            results_label.pack(anchor="nw")




            self.create_thrust_graph(graph_frame, results['graph_data'])
            num_motors = DRONE_TYPES.get(self.drone_type_var.get(), 4)
            draw_drone(num_motors, self.drone_canvas)

    def run_simulation(self):
        motor = self.motor_var.get()
        kv = self.kv_var.get()
        prop = self.prop_var.get()
        drone_type = self.drone_type_var.get()
        num_motors = DRONE_TYPES.get(drone_type, 4)
        battery_name = self.battery_var.get()
        battery_specs = BATTERY_DATABASE.get(battery_name)

        if not battery_specs:
            self.populate_output_frame(self.right_frame, {"error": "Please select a valid battery."})
            return

        payload = self.payload_weight.get()
        frame = self.frame_weight.get()
        accessories = self.accessories_weight.get()

        results = calculate_hover_metrics(motor, kv, prop, payload, frame, accessories, num_motors, battery_specs)
        self.populate_output_frame(self.right_frame, results)

    def create_thrust_graph(self, parent, data):
        fig = plt.Figure(figsize=(6, 4), dpi=100, facecolor=BG_COLOR)
        ax = fig.add_subplot(111, facecolor=ENTRY_BG)
        ax.plot(data['throttles'], data['thrusts'], color='#00FFFF', marker='o', linestyle='-', label='Empirical Data')
        ax.plot(data['hover_throttle'], data['hover_thrust'], color='#FF003C', marker='X', markersize=12,
                linestyle='None', label='Hover Point')
        ax.set_title('Thrust vs. Throttle', color=FG_COLOR, fontname=FONT_FAMILY, fontsize=14)
        ax.set_xlabel('Throttle (%)', color=FG_COLOR, fontname=FONT_FAMILY, fontsize=12)
        ax.set_ylabel('Thrust per Motor (g)', color=FG_COLOR, fontname=FONT_FAMILY, fontsize=12)
        ax.tick_params(axis='x', colors=FG_COLOR)
        ax.tick_params(axis='y', colors=FG_COLOR)
        for spine in ax.spines.values():
            spine.set_color(FG_COLOR)
        ax.legend(facecolor=FRAME_BG_COLOR, edgecolor=FG_COLOR, labelcolor=FG_COLOR)
        ax.grid(True, linestyle='--', alpha=0.3)
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(".", background=FRAME_BG_COLOR, foreground=FG_COLOR, font=(FONT_FAMILY, 12))
        style.configure("Title.TLabel", font=(FONT_FAMILY, 24, "bold"))
        style.configure("Placeholder.TLabel", background=BG_COLOR, foreground=FG_COLOR)
        style.configure("Output.TFrame", background=BG_COLOR)
        style.configure("TFrame", background=FRAME_BG_COLOR)
        style.map('TCombobox', fieldbackground=[('readonly', ENTRY_BG)], foreground=[('readonly', FG_COLOR)])
        self.root.option_add('*TCombobox*Listbox.background', ENTRY_BG)
        self.root.option_add('*TCombobox*Listbox.foreground', FG_COLOR)
        self.root.option_add('*TCombobox*Listbox.selectBackground', FG_COLOR)
        self.root.option_add('*TCombobox*Listbox.selectForeground', BG_COLOR)
        style.configure("TButton", font=(FONT_FAMILY, 14), background=FRAME_BG_COLOR, foreground=FG_COLOR,
                        borderwidth=1, relief="solid", bordercolor=FRAME_BG_COLOR)
        style.map("TButton", background=[('pressed', BUTTON_ACTIVE_BG), ('active', FRAME_BG_COLOR)],
                  bordercolor=[('active', BUTTON_BORDER)])
        style.configure('TEntry', fieldbackground=ENTRY_BG, foreground=FG_COLOR, insertcolor=FG_COLOR,
                        font=(FONT_FAMILY, 12))

    def create_combobox(self, parent, label_text, values, var=None):
        if var is None:
            var = tk.StringVar()
        row_frame = ttk.Frame(parent)
        row_frame.pack(fill=tk.X, pady=8)

        label = ttk.Label(row_frame, text=label_text, width=20)
        label.pack(side=tk.LEFT, padx=(0, 10))

        # Add a "- Select -" placeholder at the top of the list
        values_with_placeholder = ["- Select -"] + values
        combo = ttk.Combobox(row_frame, textvariable=var, values=values_with_placeholder, state="readonly",
                             font=(FONT_FAMILY, 11))
        combo.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Set default to placeholder
        combo.current(0)

        return var if label_text not in ["Select Motor KV:", "Select Propeller:"] else combo

    def create_input_row(self, parent, label_text, default_value):
        var = tk.DoubleVar(value=default_value)
        row_frame = ttk.Frame(parent)
        row_frame.pack(fill=tk.X, pady=8)
        label = ttk.Label(row_frame, text=label_text, width=20)
        label.pack(side=tk.LEFT, padx=(0, 10))
        entry = ttk.Entry(row_frame, textvariable=var, justify='center')
        entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
        return var

    def update_kv_options(self, *args):
        selected_motor = self.motor_var.get()
        kv_options = list(MOTOR_PERFORMANCE_DATA.get(selected_motor, {}).keys())
        self.kv_combo['values'] = kv_options
        if kv_options:
            self.kv_combo.current(0)
        else:
            self.kv_combo.set('')

    def update_prop_options(self, *args):
        selected_motor = self.motor_var.get()
        selected_kv_str = self.kv_var.get()
        if not selected_kv_str:
            self.prop_combo['values'] = []
            self.prop_combo.set('')
            return
        selected_kv = int(selected_kv_str)
        prop_options = list(MOTOR_PERFORMANCE_DATA.get(selected_motor, {}).get(selected_kv, {}).keys())
        self.prop_combo['values'] = prop_options
        if prop_options:
            self.prop_combo.current(0)
        else:
            self.prop_combo.set('')

    def update_battery_weight(self, *args):
        """Update the displayed battery weight when a battery is selected."""
        selected_battery = self.battery_var.get()
        if selected_battery in BATTERY_DATABASE:
            weight = BATTERY_DATABASE[selected_battery].get('weight_g', '-')
            self.battery_weight_label.config(text=f"Battery Weight: {weight} g")
        else:
            self.battery_weight_label.config(text="Battery Weight: -")


if __name__ == "__main__":
    root = tk.Tk()
    app = HyDroQuadApp(root)
    root.mainloop()

