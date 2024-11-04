"""Reflex custom component Motion."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

import reflex as rx
from typing import Dict, List, Union

MOTION_PRIMITIVE_VALUE = Union[float, str, int, List[Union[float, str, int]]]

MOTION_MAPPING = Dict[str, MOTION_PRIMITIVE_VALUE]

MOTION_VALUE = Dict[str, Union[MOTION_PRIMITIVE_VALUE, MOTION_MAPPING]]

class Motion(rx.Component):
    """Motion component."""

    # The React library to wrap.
    library = "framer-motion"

    # The React component tag.
    tag = "motion.div"

    # The initial state of the component.
    initial: rx.Var[MOTION_VALUE]

    # The animate state of the component.
    exit: rx.Var[MOTION_VALUE]

    # The animate state of the component.
    animate: rx.Var[MOTION_VALUE]

    # The transition 
    transition: rx.Var[MOTION_VALUE]

    # What the component does when it's hovered.
    while_hover: rx.Var[MOTION_VALUE]

    # What the component does when it's tapped.
    while_tap: rx.Var[MOTION_VALUE]

    # What the component does when it's in view.
    while_in_view: rx.Var[MOTION_VALUE]

    # What the component does when its focused.
    while_focus: rx.Var[MOTION_VALUE]

    # What the component does when it's out of view.
    viewport: rx.Var[Dict[str, Union[str, bool, int, float]]]

    # If the component should animate on layout changes.
    layout: rx.Var[bool]

    # If the component is the root of the layout.
    layout_root: rx.Var[bool]

motion = Motion.create

class AnimatePrescence(rx.Component):
    """AnimatePresence component."""

    # The React library to wrap.
    library = "framer-motion"

    # The React component tag.
    tag = "AnimatePresence"

animate_presence = AnimatePrescence.create
