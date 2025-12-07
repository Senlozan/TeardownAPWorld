from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import TeardownWorld

def set_all_rules(world: TeardownWorld) -> None:

    set_completion_condition(world)


def set_completion_condition(world: TeardownWorld) -> None:

    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
