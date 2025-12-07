from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class StartWithSprayCan(Toggle):
    """
    A tool you can use to plan out your route. Might come in handy.
    """

    display_name = "Start With Spray Can"

@dataclass
class TeardownOptions(PerGameCommonOptions):
    start_with_spray_can: StartWithSprayCan
