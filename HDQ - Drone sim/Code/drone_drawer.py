# drone_drawer.py
import turtle
import math


def draw_motor(t, radius, outline_color, fill_color):
    """Draws a detailed 2D motor with concentric circles."""
    t.pendown()
    # Outer casing
    t.fillcolor(fill_color)
    t.pencolor(outline_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Inner motor detail
    t.fillcolor("#555555")  # Darker grey for the core
    t.begin_fill()
    t.circle(radius * 0.6)
    t.end_fill()
    t.penup()


def draw_propeller(t, length, color):
    """Draws a stylized, curved two-blade propeller."""
    t.pendown()
    t.pencolor(color)
    t.pensize(3)

    # Draw two curved blades, rotating 180 degrees for the second
    for _ in range(2):
        # Draw one blade using two arcs to create an 'S' curve
        t.circle(length * 0.7, 60)
        t.circle(-length * 0.7, 60)
        # Go back to the center and rotate for the next blade
        t.setposition(t.xcor(), t.ycor())  # Should already be at the center
        t.right(180)

    t.penup()


def draw_drone(num_motors, parent_canvas):
    """
    Draws a visually appealing, detailed 2D drone sketch onto a Tkinter canvas.
    """
    parent_canvas.delete("all")
    screen = turtle.TurtleScreen(parent_canvas)
    screen.tracer(0)  # Turn off screen updates for instant drawing
    screen.bgcolor("#000000")

    t = turtle.RawTurtle(screen)
    t.speed(0)
    t.hideturtle()
    t.penup()

    # --- Drawing Parameters ---
    center_x, center_y = 0, 0
    body_radius = 45
    arm_length = 100
    motor_radius = 15
    prop_length = 40
    arm_base_width = 20  # Width of the arm at the body
    arm_tip_width = 10  # Width of the arm at the motor

    # --- Draw Central Body ---
    t.goto(center_x, center_y - body_radius)
    t.pendown()
    t.fillcolor("#222222")
    t.pencolor("#FFFFFF")
    t.pensize(2)
    t.begin_fill()
    t.circle(body_radius)
    t.end_fill()
    t.penup()

    # Add a detail circle to the body
    t.goto(center_x, center_y - (body_radius * 0.6))
    t.pendown()
    t.circle(body_radius * 0.6)
    t.penup()

    # --- Calculate Arm Angles ---
    angles = [i * (360 / num_motors) for i in range(num_motors)]

    # --- Draw Arms, Motors, and Propellers ---
    for angle_deg in angles:
        angle_rad = math.radians(angle_deg)

        # Calculate start and end points for the tapered arm polygon
        start_x_offset = (arm_base_width / 2) * math.sin(angle_rad)
        start_y_offset = -(arm_base_width / 2) * math.cos(angle_rad)

        end_x_offset = (arm_tip_width / 2) * math.sin(angle_rad)
        end_y_offset = -(arm_tip_width / 2) * math.cos(angle_rad)

        motor_pos_x = center_x + arm_length * math.cos(angle_rad)
        motor_pos_y = center_y + arm_length * math.sin(angle_rad)

        # Define the 4 corners of the tapered arm
        p1 = (center_x + start_x_offset, center_y + start_y_offset)
        p2 = (center_x - start_x_offset, center_y - start_y_offset)
        p3 = (motor_pos_x - end_x_offset, motor_pos_y - end_y_offset)
        p4 = (motor_pos_x + end_x_offset, motor_pos_y + end_y_offset)

        # Draw the arm as a filled polygon
        t.goto(p1)
        t.pendown()
        t.fillcolor("#333333")
        t.begin_fill()
        t.goto(p2)
        t.goto(p3)
        t.goto(p4)
        t.goto(p1)
        t.end_fill()
        t.penup()

        # Draw the motor at the end of the arm
        t.goto(motor_pos_x, motor_pos_y - motor_radius)
        draw_motor(t, motor_radius, "#FFFFFF", "#111111")

        # Draw the propeller on top of the motor
        t.goto(motor_pos_x, motor_pos_y)
        draw_propeller(t, prop_length, "#00FFFF")

    screen.update()  # Update the screen once all drawing is complete