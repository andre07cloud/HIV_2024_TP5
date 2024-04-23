from .abstract_power_schedule import AbstractPowerSchedule
from common.abstract_seed import AbstractSeed


class PowerSchedule(AbstractPowerSchedule):

    def __init__(self) -> None:
        super().__init__()
    
        
    def _assign_energy(self, seeds: list[AbstractSeed]) -> None:
        """Assigns each seed the same energy"""
        for seed in seeds:
            seed_length = len(seed.data)
            energy = 1 / seed_length
            seed.energy = energy
        return seeds    
