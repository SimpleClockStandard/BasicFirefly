"""
Behave environment hooks for doc_brown clock test suite.

Before implementing steps, replace the stub objects below with real
device/simulator interfaces (e.g. a serial bridge, hardware-in-the-loop
harness, or software emulator of the CC1352R + RTC).
"""


def before_all(context):
    """Global setup: configure shared test infrastructure."""
    # TODO: initialize hardware-in-the-loop harness or simulator
    context.tolerance_ms = 1
    context.max_drift_seconds = 3
    context.light_show_min = 0
    context.light_show_max = 255


def before_scenario(context, scenario):
    """Reset device state before each scenario."""
    # TODO: reset/power-cycle device under test or simulator
    context.clock = None
    context.clocks = []
    context.leader = None
    context.i2c_response = None


def after_scenario(context, scenario):
    """Clean up after each scenario."""
    # TODO: power down or release any hardware handles
    pass


def after_all(context):
    """Global teardown."""
    # TODO: disconnect from test harness
    pass
