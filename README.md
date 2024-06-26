# Reflex Motion

A Reflex wrapper for [Framer Motion](https://www.framer.com/motion/), a production-ready motion library for React.

<div align="center">
    <img src="/docs/demo.gif" alt="Reflex Motion Demo" />
</div>

# Installation

```bash
pip install reflex-motion
```

# Usage

Right now Reflex Motion is a simple wrapper around Framer Motion. It provides a single component, `motion`, which is a drop-in replacement for `motion.div` from Framer Motion.

Import like so:
```python
from reflex_motion import motion
```

Use in your Reflex ui:
```python
motion(
    rx.button(
        "Bounce me!",
    ),
    while_hover={"scale": 1.2},
    while_tap={"scale": 0.9},
    transition={"type": "spring", "stiffness": 400, "damping": 17},
)
```

There are a few different props motion supports:

# Props

**inital**: The initial state of the animation. This is the state the animation will start in when the component is first rendered.

**animate**: The state the animation will end in. This is the state the animation will end in when the component is first rendered.

**while_hover**: The state the animation will be in while the user is hovering over the component.

**while_tap**: The state the animation will be in while the user is tapping on the component.

**while_in_view**: The state the animation will be in while the component is in view.

**while_focus**: The state the animation will be in while the component is focused.

### Animation Props

| Name      | Key | Values | Description |
| ----------- | ----------- | ----------- | ----------- |
| Translate     | 'x', 'y', 'z' | int | The amount to translate the component by. |
| Scale   | 'scale', 'scale_x', 'scale_y' | int | The amount to scale the component by. |
| Rotate   | 'rotate', 'rotate_x', 'rotate_y', 'rotate_z' | int | The amount to rotate the component by. |
| Skew   | 'skew', 'skew_x', 'skew_y' | int | The amount to skew the component by. |


Additionally you can pass in any Reflex style prop (css prop).

## Transitions

**transition**: The transition to use when animating between states. This can be a single transition or an array of transitions.

| Name      | Key | Values | Description |
| ----------- | ----------- | ----------- | ----------- |
| Type    |  'type' | 'tween', 'spring', 'keyframes' | The type of transition to use. |
| Easing | 'ease' | 'linear', 'ease_in', 'ease_out', 'ease_in_out', 'circ_in', 'circ_out', 'circ_in_out', 'back_in', 'back_out', 'back_in_out' | The easing function to use for the transition. |
| Duration   |  'duration' | int | The duration of the transition in milliseconds. |
| Delay   | 'delay' | int | The delay before the transition starts in milliseconds. |

Additonally you can pass in any of the  **Animation Props** and **Reflex style prop (css prop)**.

# Examples

## Transition

```python 
motion( 
    rx.button(
        "Spin me!",
        variant="soft",
    ),
    initial={"scale": 1},
    while_hover={"scale": 1.2, "rotate": 45},
    while_tap={"scale": 0.9},
    transition={"type": "spring", "stiffness": 260, "damping": 20},
)
```

