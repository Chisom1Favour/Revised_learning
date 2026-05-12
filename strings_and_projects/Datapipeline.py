@dataclass(frozen=True)
class PipeLineConfig:
    input_bucket: str
    output_bucket: str
    batch_size: int = 1000
    retry_delay_seconds: float = 0.5

    # Post-initilization validation
    def __post_init__(self):
        if self.batch_size <= 0:
            raise ValueError("Batch size must be positive")
        