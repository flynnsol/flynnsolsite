"""Brand colors and shared style dictionaries, derived from the logo marks in res/.

NAVY/CREAM are the two extremes that swap meaning between dark and light mode
(background vs. text), so anywhere they're used for something the user
actually reads, use the reactive TEXT_* constants below (built with
rx.color_mode_cond) rather than the raw hex — a hardcoded CREAM stays cream
even against a light background and disappears. GOLD is the accent and reads
fine unchanged in both modes.
"""

import reflex as rx

NAVY = "#0A0D14"
NAVY_SOFT = "#11151F"
GOLD = "#D9A34B"
CREAM = "#F5F2EC"

FONT_FAMILY = "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
MONO_FAMILY = "'JetBrains Mono', 'Fira Code', ui-monospace, monospace"

CONTENT_WIDTH = "980px"

# Reactive text colors — safe to use as `color=...` anywhere; they track the
# live color mode instead of being frozen to one hex value.
TEXT = rx.color_mode_cond(light=NAVY, dark=CREAM)
TEXT_DD = rx.color_mode_cond(light=f"{NAVY}DD", dark=f"{CREAM}DD")
TEXT_CC = rx.color_mode_cond(light=f"{NAVY}CC", dark=f"{CREAM}CC")
TEXT_99 = rx.color_mode_cond(light=f"{NAVY}99", dark=f"{CREAM}99")
TEXT_77 = rx.color_mode_cond(light=f"{NAVY}77", dark=f"{CREAM}77")

CARD_BG = rx.color_mode_cond(light="#FFFFFF", dark=NAVY_SOFT)
NAV_BG = rx.color_mode_cond(light=f"{CREAM}D9", dark=f"{NAVY}D9")

page_container_style = {
    "max_width": CONTENT_WIDTH,
    "margin": "0 auto",
    "padding": "2em 1.5em 5em",
    "width": "100%",
    "min_height": "100vh",
}

card_style = {
    "background": CARD_BG,
    "border": f"1px solid {GOLD}22",
    "border_radius": "14px",
    "padding": "1.5em",
    "transition": "transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease",
    "_hover": {
        "transform": "translateY(-4px)",
        "box_shadow": f"0 12px 32px -8px {GOLD}40",
        "border_color": f"{GOLD}88",
    },
}

# Full color spec (not just a hover delta) for the button look used across
# the site, built from the raw GOLD hex rather than Radix's
# `color_scheme="amber"` — Radix's amber palette is a different, brighter
# hue than our GOLD, which is what made "gold" look inconsistent between
# buttons/badges (amber-based) and everything else (raw GOLD hex). Only
# `background`/`color`/`border` are set — no size, padding, or font
# properties — so the button's own `variant`/`size` still controls its box
# model; this only recolors it.
#
# Hollow gold outline at rest, fills solid gold on hover.
outline_button_hover = {
    "background": "transparent",
    "color": GOLD,
    "border": f"1px solid {GOLD}",
    "cursor": "pointer",
    "transition": "background 0.2s ease, color 0.2s ease",
    "_hover": {
        "background": GOLD,
        "color": NAVY,
    },
}

# Shared gold color tokens for "soft" chip/badge-style elements (skill
# chips, tag badges, status badges) so they match GOLD exactly instead of
# drifting toward Radix's amber palette.
gold_soft_style = {
    "background": f"{GOLD}1A",
    "color": GOLD,
    "border": f"1px solid {GOLD}44",
}

skill_chip_style = {
    **gold_soft_style,
    "border_radius": "999px",
    "padding": "0.35em 0.9em",
    "font_size": "0.85em",
    "font_weight": "500",
    "transition": "transform 0.15s ease, background 0.15s ease",
    "_hover": {
        "transform": "translateY(-2px)",
        "background": f"{GOLD}33",
    },
}
