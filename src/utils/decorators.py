from tenacity import RetryCallState


def decreasing_wait(retry_state: RetryCallState) -> float:
    initial_wait = 2
    decrease_factor = 0.75
    wait_time = initial_wait * (decrease_factor ** retry_state.attempt_number)
    return wait_time
