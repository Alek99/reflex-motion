"""Reflex custom component Motion."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

import reflex as rx
from typing import Any, Dict, List, Optional, Set, Union


class Motion(rx.Component):
    """Motion component."""

    # The React library to wrap.
    library = "framer-motion"

    # The React component tag.
    tag = "motion.div"

    # The initial state of the component.
    initial: rx.Var[Dict[str, Union[float, str]]]

    # The animate state of the component.
    animate: rx.Var[Dict[str, Union[float, str]]]

    # The transition 
    transition: rx.Var[Dict[str, Union[float, str]]]

    # What the component does when it's hovered.
    while_hover: rx.Var[Dict[str, Union[float, str]]]

    # What the component does when it's tapped.
    while_tap: rx.Var[Dict[str, Union[float, str]]]

    # What the component does when it's in view.
    while_in_view: rx.Var[Dict[str, Union[float, str]]]

    # What the component does when its focused.
    while_focus: rx.Var[Dict[str, Union[float, str]]]

    # What the component does when it's out of view.
    viewport: rx.Var[Union[str, List[str]]]


motion = Motion.create