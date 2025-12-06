from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import TeardownWorld

def create_and_connect_regions(world: TeardownWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: APQuestWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    home = Region("Löckelle Teardown Services", world.player, world.multiworld)
    lee = Region("Lee Chemicals", world.player, world.multiworld)
    marina = Region("West Point Marina", world.player, world.multiworld)
    mansion = Region("Villa Gordon", world.player, world.multiworld)
    caveisland = Region("Hollowrock Island", world.player, world.multiworld)
    mall = Region("Evertides Mall", world.player, world.multiworld)
    frustrum = Region("Frustrum", world.player, world.multiworld)
    vacation = Region("Muratori Beach", world.player, world.multiworld)
    carib = Region("Isla Estocastica", world.player, world.multiworld)
    factory = Region("Quilez Security", world.player, world.multiworld)
    cullington = Region("Cullington", world.player, world.multiworld)

    regions = [home, lee, marina, mansion, caveisland, mall, frustrum, vacation, carib, factory, cullington]

    world.multiworld.regions += regions

def connect_regions(world: APQuestWorld) -> None:

    home = world.get_region("Löckelle Teardown Services")
    lee = world.get_region("Lee Chemicals")
    marina = world.get_region("West Point Marina")
    mansion = world.get_region("Villa Gordon")
    caveisland = world.get_region("Hollowrock Island")
    mall = world.get_region("Evertides Mall")
    frustrum = world.get_region("Frustrum")
    vacation = world.get_region("Muratori Beach")
    carib = world.get_region("Isla Estocastica")
    factory = world.get_region("Quilez Security")
    cullington = world.get_region("Cullington")

    home.connect(lee, "Löckelle Teardown Services to Lee Chemicals")
    home.connect(marina, "Löckelle Teardown Services to West Point Marina")
    home.connect(mansion, "Löckelle Teardown Services to Villa Gordon")
    home.connect(caveisland, "Löckelle Teardown Services to Hollowrock Island")
    home.connect(mall, "Löckelle Teardown Services to Evertides Mall")
    home.connect(frustrum, "Löckelle Teardown Services to Frustrum")
    home.connect(factory, "Löckelle Teardown Services to Quilez Security")
    home.connect(cullington, "Löckelle Teardown Services to Cullington", lambda state: state.has("Finale", world.player))
    home.connect(vacation, "Löckelle Teardown Services to Muratori Beach")
    vacation.connect(carib, "Muratori Beach to Isla Estocastica")
