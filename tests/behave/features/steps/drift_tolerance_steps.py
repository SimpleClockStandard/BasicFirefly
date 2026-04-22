from behave import given, when, then


# ---------------------------------------------------------------------------
# Drift accumulation
# ---------------------------------------------------------------------------

@given("a clock initialized with accurate time")
def step_given_clock_initialized_with_accurate_time(context):
    raise NotImplementedError("Step not yet implemented")


@given("no radio sync pulses are received")
def step_given_no_radio_sync_pulses(context):
    raise NotImplementedError("Step not yet implemented")


@when("{years:d} year(s) of simulated time elapses")
def step_when_n_years_elapses(context, years):
    # Store years so the Then step can compute the allowed drift window
    context.simulated_years = years
    raise NotImplementedError("Step not yet implemented")


@then("the RTC drift should be no more than {max_drift:d} seconds in either direction")
def step_then_drift_within_n_seconds_bidirectional(context, max_drift):
    # Drift must satisfy: -max_drift <= actual_drift <= max_drift
    raise NotImplementedError("Step not yet implemented")


# ---------------------------------------------------------------------------
# Re-sync after N years offline (within trust window)
# ---------------------------------------------------------------------------

@given("a clock that has drifted {seconds:d} seconds from true time")
def step_given_clock_drifted_n_seconds(context, seconds):
    context.drift_seconds = seconds
    raise NotImplementedError("Step not yet implemented")


@given("a clock that has drifted +{seconds:d} seconds from true time")
def step_given_clock_drifted_positive(context, seconds):
    context.drift_seconds = +seconds
    raise NotImplementedError("Step not yet implemented")


@given("a clock that has drifted -{seconds:d} seconds from true time")
def step_given_clock_drifted_negative(context, seconds):
    context.drift_seconds = -seconds
    raise NotImplementedError("Step not yet implemented")


@given("the drift is within the expected window of {years:d} year(s)")
def step_given_drift_within_window(context, years):
    # Acceptable window: abs(drift) <= years * 3
    raise NotImplementedError("Step not yet implemented")


@when("a valid beacon sync pulse is received")
def step_when_valid_beacon_pulse_received(context):
    raise NotImplementedError("Step not yet implemented")


@then("the clock should correct to within 1 millisecond of true time")
def step_then_clock_corrects_to_1ms(context):
    raise NotImplementedError("Step not yet implemented")


@then("the clock should be marked as trusted")
def step_then_clock_marked_trusted(context):
    raise NotImplementedError("Step not yet implemented")


# ---------------------------------------------------------------------------
# Rejection — drift exceeds trust window
# ---------------------------------------------------------------------------

@given("the drift exceeds the expected window of {years:d} year(s)")
def step_given_drift_exceeds_window(context, years):
    # abs(drift) > years * 3 — clock cannot be trusted
    raise NotImplementedError("Step not yet implemented")


@then("the clock should be rejected as untrustworthy")
def step_then_clock_rejected_as_untrustworthy(context):
    raise NotImplementedError("Step not yet implemented")


@then("the beacon should not snap to the drifted clock's time")
def step_then_beacon_does_not_snap(context):
    raise NotImplementedError("Step not yet implemented")
