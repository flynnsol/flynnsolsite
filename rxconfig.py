import reflex as rx

config = rx.Config(
    app_name="flynnsol",
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="dark",
                accent_color="amber",
                gray_color="slate",
                radius="medium",
                has_background=True,
            )
        ),
    ]
)