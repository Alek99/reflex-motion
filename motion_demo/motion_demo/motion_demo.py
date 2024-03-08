"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_motion import motion

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            motion(
                rx.button(
                    "Bounce me!",
                ),
                while_hover={"scale": 1.2},
                while_tap={"scale": 0.9},
                transition={"type": "spring", "stiffness": 400, "damping": 17},
            ),
            motion( 
                rx.button(
                    "Spin me!",
                    variant="soft",
                ),
                initial={"scale": 1},
                while_hover={"scale": 1.2, "rotate": 45},
                while_tap={"scale": 0.9},
                transition={"type": "spring", "stiffness": 260, "damping": 20},
            ),
            motion( 
                rx.button(
                    "Move me!",
                    variant="soft",
                ),
                while_tap={
                    "scale": 1.4, 
                    "rotate": -90, 
                    "border_radius": "100%",    
                    "translateX": "100px",
                    "translateY": "-100px",
                },
            ),
            align="start",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
