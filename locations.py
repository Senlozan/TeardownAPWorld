from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import TeardownWorld

class TeardownLocation(Location):
    game = "Teardown"

LOCATION_NAME_TO_ID = {"The Lee Computers": 1,
    "The login devices": 2,
    "The Tower": 3,
    "Power Outage": 4,
    "Flooding": 5,
    "Making space": 6,
    "Classic Cars": 7,
    "The GPS devices": 8,
    "Art Return": 9,
    "The Car Wash": 10,
    "Fine Arts": 11,
    "Insurance Fraud": 12,
    "A Wet Affair": 13,
    "The BlueTide Computers": 14,
    "Motivational Reminder": 15,
    "An Assortment of Dishes": 16,
    "The secret ingredients": 17,
    "Droid dismount": 18,
    "The Old Building Problem":  19,
    "The shipping logs": 20,
    "Connecting the dots": 21,
    "The Chase": 22,
    "The BlueTide shortage": 23,
    "Truckload of trouble": 24,
    "Moving the goods": 25,
    "Havoc in paradise": 26,
    "Roborazzi": 27,
    "The droid abduction": 28,
    "Handle with care": 29,
    "Heavy lifting": 31,
    "Malice in Woonderland": 32,
    "Tool up": 33,
    "The Speed Deal": 34,
    "Covert chaos": 35,
    "Ornament ordeal": 36,
    "The pawn shop": 37,
    "Elena's revenge": 38,
    "The Quilez tools": 39,
    "Banana": 40,
    "Old Trowel": 41,
    "Pneumatic wrench": 42,
    "Hidden cash (harbor office)": 43,
    "Lee's tax deductible college fund": 44,
    "Tile cutter": 45,
    "Titanium screwdriver bits": 46,
    "Disc cutter": 47,
    "Hidden cash (transformer)": 48,
    "Power wrench": 49,
    "Diamond cutters": 50,
    "Hidden cash (factory)": 51,
    "Hidden cash (office)": 52,
    "Good Life by Enid Coumans": 53,
    "West Point Marina by Enid Coumans": 54,
    "Hidden cash (office 2nd floor)": 55,
    "50 Shades of Capitalism by Kerstin Straback": 56,
    "Lee's tax deductible pension fund": 57,
    "Circular saw": 58,
    "Assortment of tools": 59,
    "Electric screwdriver": 60,
    "Deposit bottles": 61,
    "Microscope": 62,
    "Bottle of Gulfmyra": 63,
    "Wallet": 64,
    "Agent B4 comic collection": 65,
    "Distance laser 1": 66,
    "Hidden cash (dumpster)": 67,
    "D-Gauss portable gaming console": 68,
    "Fishing gear": 69,
    "Bayran Sunglasses": 70,
    "Cash register": 71,
    "Decorative swordfish": 72,
    "Antique pirate hook": 73,
    "ProSuck vacuum cleaner": 74,
    "Antique pirate sword": 75,
    "Model ship": 76,
    "Antique pirate dagger": 77,
    "Newlander MP3 player": 78,
    "Binoculars": 79,
    "Antique compass": 80,
    "Bingo trophy": 81,
    "Cash box": 82,
    "Antique cannonball": 83,
    "Antique black powder gun": 84,
    "Assortment of tequilla": 85,
    "Marine flashlight": 86,
    "Walkie talkies": 87,
    "Marine sextant": 88,
    "Designer life vest": 89,
    "Electric sander": 90,
    "Antique silver coins": 91,
    "Bag of cash": 92,
    "Cigar box": 93,
    "Pressure calibration instrument": 94,
    "Lump of amethyst": 95,
    "Marinoil Premium Lubrication": 96,
    "Brand new Wanderman Sonar": 97,
    "Aluminium propeller": 98,
    "Mizaka premium spark plugs": 99,
    "Power drill": 100,
    "Telescope": 101,
    "Spare steeringwheel": 102,
    "Engraved lighter": 103,
    "Bag in box wine": 104,
    "Box of expensive Swiss chocolate": 105,
    "Precision thermometer": 106,
    "Gilded toilet brush": 107,
    "2nd prize in Woo Open 1994": 108,
    "BBQ Charcoal made from rare protected hardwood": 109,
    "Designer lamp Entwined angles by Berthold Bruckness": 110,
    "Jewelry box": 111,
    "Food processor": 112,
    "Silverware": 113,
    "Oysters": 114,
    "How to become a snooker champ - in 24 hours by Clue Baize": 115,
    "Wallet (Villa Gordon)": 116,
    "Popcorn machine maintenance manual": 117,
    "The ultimate collection of movie one-liners by Garth Pikett": 118,
    "Coin collection (Villa Gordon)": 119,
    "Bronze statue": 120,
    "Universal remote": 121,
    "Cable box": 122,
    "Expensive vintage sneakers": 123,
    "Rare genuine vintage band t-shirt": 124,
    "Credit card": 125,
    "Elevator maintenance manual": 126,
    "Exclusive make-up": 127,
    "Sleeping pills": 128,
    "Wallet (top floor)": 129,
    "Penthouse gardening by Liza Green": 130,
    "Dictaphone": 131,
    "A stash of emergency cash": 132,
    "Chef knives": 133,
    "Nice cooking pan": 134,
    "Russian caviar": 135,
    "Gordon's hidden birthday gift for Ms. Couman": 136,
    "Gordon's lost passport": 137,
    "Box of artisanal tomato soup": 138,
    "A vacuum cleaner (Villa Gordon)": 139,
    "Portable casette tape player": 140,
    "Pretty fancy bottle of rum": 141,
    "Electric drill (Villa Gordon)": 142,
    "Carburetor for Castanet 500L": 143,
    "Expensive callibration tool": 144,
    "The Lazy Express": 145,
    "Wallet (security office)": 146,
    "Engraved lighter (Freya's room)": 147,
    "What a fancy racing trophy": 148,
    "A car mechanics toolbox": 149,
    "Stack of gold bullions": 150,
    "Bag of cash (Hollowrock Island)": 151,
    "Air purifier": 152,
    "Dual line telephone": 153,
    "Extra potent nutrition": 154,
    "Fungimax synthetic yeast": 155,
    "TurboWipe pesticide": 156,
    "Tidyfresh premium detergent": 157,
    "Electric drill (Hollowrock Island)": 158,
    "Disc cutter (Hollowrock Island)": 159,
    "Old TV": 160,
    "Spare carbon arc lamp": 161,
    "A crock of gold": 162,
    "Synthetic tar": 163,
    "Fishing gear (Hollowrock Island)": 164,
    "Precision fishing scale": 165,
    "Portable FM radio": 166,
    "High-speed labeling device": 167,
    "Sakawana fishing knife": 168,
    "TV (Hollowrock Island)": 169,
    "Wallet (Hollowrock Island)": 170,
    "Ivory chess pieces": 171,
    "Rags and water bottles": 172,
    "Hand-drill and duct tape": 173,
    "Vacuum cleaner (Hollowrock Island)": 174,
    "Projector": 175,
    "Opus Juan vintage wine": 176,
    "Binoculars (Hollowrock Island)": 177,
    "Garden scissors": 178,
    "Alarm clock": 179,
    "Flat screen monitor": 180,
    "Essential one-liners by Dilip Sequoia": 181,
    "Bottle of gin": 182,
    "Digital pulse monitor watch": 183,
    "Cash register (Hollowrock Island)": 184,
    "Cash register (BT store)": 185,
    "BlueTide Extra Strong, limited edition": 186,
    "Sleeping Aid": 187,
    "High Quality Oil Paint": 188,
    "LIT yearly bonus": 189,
    "High viscosity oil": 190,
    "Harmonica B-minor": 191,
    "Reciprocating saw": 192,
    "Lost wallet (Frustrum)": 193,
    "Fishing lure": 194,
    "Wingman Precision Darts": 195,
    "Lost wallet (club)": 196,
    "Smoke Machine MkII": 197,
    "Gender Revolvers LP": 198,
    "Razor Shaver S": 199,
    "Frustrum Town Council Community Award: Fred Frustrum - Gas Attendant. 'You keep the town rolling'": 200,
    "Tribal Mask": 201,
    "Dehumidifier NM200": 202,
    "Questionable bone collection": 203,
    "Lost wallet (above tunnel)": 204,
    "Frederick Frustrums long lost hat": 205,
    "Lost engagement ring": 206,
    "Secret spices": 207,
    "Lost wallet (hotel)": 208,
    "Silk smooth fabric softener": 209,
    "Smooth Skin Plus": 210,
    "Industrial filter": 211,
    "Preasure meter": 212,
    "Gibbon Stereocaster": 213,
    "Bits set": 214,
    "How to look busy at work magazine": 215,
    "Holy Paula Taco spices": 216,
    "Very durable phone": 217,
    "Sandproof radio": 218,
    "Signature vinegar": 219,
    "Eau de toilette": 220,
    "RoflFX Effect Pedal": 221,
    "Famous underwear": 222,
    "Cheap garden scissors": 223,
    "How to open any safe in 4 easy steps": 224,
    "Limited edition video game hoodie": 225,
    "Fake demonstration cash": 226,
    "Stylish fur coat": 227,
    "Lost wallet (Evertides Mall)": 228,
    "Rare pink spray paint": 229,
    "Gold watch": 230,
    "Ruby necklace": 231,
    "Cheap vodka": 232,
    "MumboJumbo 3D 16MB VRAM": 233,
    "Taxfree profit": 234,
    "Deposited funds": 235,
    "Confiscated Skateboard": 236,
    "Red stapler": 237,
    "24k golden tie pin": 238,
    "Civet Coffee": 239,
    "Truffle juce": 240,
    "Flashlight (Evertides Mall)": 241,
    "Ultrasonic Distance Sensor": 242,
    "SURVIVAL 101 - Nuts, bark and berries": 243,
    "Distance sensor": 244,
    "Infrared Sensor": 245,
    "A pair of scuba diving oxygen tanks": 246,
    "High sensitivity moisture sensor": 247,
    "Continuous rotation servo motor": 248,
    "Half Ambient Light-sensor 9000": 249,
    "Water proof material sample": 250,
    "A deck of poker cards": 251,
    "Quilez corporate umbrella": 252,
    "Handrolled Muratori cigars": 253,
    "Office safe master key replica": 254,
    "What a beautiful bouquet of roses": 255,
    "A discarded bouquet of roses": 256,
    "A trashed bouquet of roses": 257,
    "Motivational reminder appreciation token /Gillian": 258,
    "Top 25 camping spots in Löckelle": 259,
    "A nice rock climbing hat": 260,
    "Outboard motor": 261,
    "Infrared Transmitter": 262,
    "Box of semi-conductors": 263,
    "Vault door gear motor": 264,
    "Gyroscope": 265,
    "AI core": 266,
    "High sensitivity microphone sensor": 267,
    "Bullet proof material sample": 268,
    "A fishing rod": 269,
    "A battery powered radio": 270,
    "Photoresistor Light Sensor": 271,
    "Helicopter maintenance manual": 272,
    "Explosion proof material sample": 273,
    "Expensive snorkel": 274,
    "A volley ball turned into a toy": 275,
    "Exotic fruit": 276,
    "Golden 28 inch rims": 277,
    "Lost wallet (Isla Estocastica)": 278,
    "A monkey hand, it's supposed to grant you wishes": 279,
    "Money counter": 280,
    "Diamond cane": 281,
    "Brass knuckles": 282,
    "Island life - Your guide to the Muratoris": 283,
    "Pineapple": 284,
    "Inflatable duck": 285,
    "Bird egg": 286,
    "Unused mortar shell": 287,
    "Golden grillz": 288,
    "Scuba tank": 289,
    "Tropical helmet": 290,
    "Tuning kit": 291,
    "Golden bullets": 292,
    "High precision scale": 293,
    "A really old message in a bottle": 294,
    "Marine supercharger": 295,
    "Dried out carburetor": 296,
    "A genuine pegleg": 297,
    "The last roll of TP": 298,
    "A skate, how did that end up here...": 299,
    "Old magazines": 300,
    "Chainsaw": 301,
    "Good grappa": 302,
    "Jetski engine": 303,
    "Machine grease": 304,
    "A teapot, short and stout...": 305,
    "Bayran deluxe sunglasses": 306,
    "Assortment of tools": 307,
    "Hammer": 308}

class APQuestLocation(Location):
    game = "Teardown"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: TeardownWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: APQuestWorld) -> None:

    home = world.get_region("Löckelle Teardown Services")
    lee = world.get_region("Lee Chemicals")
    marina = world.get_region("West Point Marina")
    mansion = world.get_region("Villa Gordon")
    caveisland = world.get_region("Hollowrock Island")
    mall = world.get_region("Evertides Mall")
    frustrum = world.get_region("Frustrum")
    vacation = world.get_region("Muratori Beach")
    carib = world.get_region("Isla Estocastica")
    factory = world.get_region("Quilez Security")
    cullington = world.get_region("Cullington")

    home_locations = get_location_names_with_ids(
        ["Banana"]
    )
    home.add_locations(home_locations, TeardownLocation)

    lee_mission_locations = get_location_names_with_ids(
       ["The Lee Computers",
    "The login devices",
    "The Tower",
    "Power Outage",
    "Flooding",
    "Heavy lifting",
    "Malice in Woonderland"]
    )
    lee.add_locations(lee_mission_locations, TeardownLocation)

    marina_mission_locations = get_location_names_with_ids(
        ["Making space",
    "Classic Cars",
    "The GPS devices",
    "Art Return",
    "Tool up"]
    )
    marina.add_locations(marina_mission_locations, TeardownLocation)

    mansion_mission_locations = get_location_names_with_ids(
        [ "The Car Wash",
    "Fine Arts",
    "Insurance Fraud",
    "A Wet Affair",
    "The Speed Deal"]
    )
    mansion.add_locations(mansion_mission_locations, TeardownLocation)

    caveisland_mission_locations = get_location_names_with_ids(
        [    "The BlueTide Computers",
    "Motivational Reminder",
    "An Assortment of Dishes",
    "The secret ingredients",
    "Droid dismount"]
    )
    caveisland.add_locations(caveisland_mission_locations, TeardownLocation)

    mall_mission_locations = get_location_names_with_ids(
        [    "The Old Building Problem",
    "The shipping logs",
    "Connecting the dots",
    "Covert chaos",
    "Ornament ordeal"]
    )
    mall.add_locations(mall_mission_locations, TeardownLocation)

    frustrum_mission_locations = get_location_names_with_ids(
        ["The Chase",
    "The BlueTide shortage",
    "Truckload of trouble",
    "The pawn shop"]
    )
    frustrum.add_locations(frustrum_mission_locations, TeardownLocation)

    carib_mission_locations = get_location_names_with_ids(
        ["Moving the goods",
    "Havoc in paradise",
    "Elena's revenge"]
    )
    carib.add_locations(carib_mission_locations, TeardownLocation)

    factory_mission_locations = get_location_names_with_ids(
        ["Roborazzi",
    "The droid abduction",
    "Handle with care",
    "The Quilez tools"]
    )
    factory.add_locations(factory_mission_locations, TeardownLocation)

    lee_valuable_locations = get_location_names_with_ids(
        ["Old Trowel",
    "Pneumatic wrench",
    "Hidden cash (harbor office)",
    "Lee's tax deductible college fund",
    "Tile cutter",
    "Titanium screwdriver bits",
    "Disc cutter",
    "Hidden cash (transformer)",
    "Power wrench",
    "Diamond cutters",
    "Hidden cash (factory)",
    "Hidden cash (office)",
    "Good Life by Enid Coumans",
    "West Point Marina by Enid Coumans",
    "Hidden cash (office 2nd floor)",
    "50 Shades of Capitalism by Kerstin Straback",
    "Lee's tax deductible pension fund",
    "Circular saw",
    "Assortment of tools",
    "Electric screwdriver",
    "Deposit bottles",
    "Microscope",
    "Bottle of Gulfmyra",
    "Wallet",
    "Agent B4 comic collection",
    "Distance laser 1",
    "Hidden cash (dumpster)",
    "Assortment of tools",
    "Hammer"]
    )
    lee.add_locations(lee_valuable_locations, TeardownLocation)
    
    marina_valuable_locations = get_location_names_with_ids(
        ["D-Gauss portable gaming console",
    "Fishing gear",
    "Bayran Sunglasses",
    "Cash register",
    "Decorative swordfish",
    "Antique pirate hook",
    "ProSuck vacuum cleaner",
    "Antique pirate sword",
    "Model ship",
    "Antique pirate dagger",
    "Newlander MP3 player",
    "Binoculars",
    "Antique compass",
    "Bingo trophy",
    "Cash box",
    "Antique cannonball",
    "Antique black powder gun",
    "Assortment of tequilla",
    "Marine flashlight",
    "Walkie talkies",
    "Marine sextant",
    "Designer life vest",
    "Electric sander",
    "Antique silver coins",
    "Bag of cash",
    "Cigar box",
    "Pressure calibration instrument",
    "Lump of amethyst",
    "Marinoil Premium Lubrication",
    "Brand new Wanderman Sonar",
    "Aluminium propeller",
    "Mizaka premium spark plugs",
    "Power drill",
    "Telescope",
    ]
    )
    marina.add_locations(marina_valuable_locations, TeardownLocation)

    mansion_valuable_locations = get_location_names_with_ids(
        ["Spare steeringwheel",
    "Engraved lighter",
    "Bag in box wine",
    "Box of expensive Swiss chocolate",
    "Precision thermometer",
    "Gilded toilet brush",
    "2nd prize in Woo Open 1994",
    "BBQ Charcoal made from rare protected hardwood",
    "Designer lamp Entwined angles by Berthold Bruckness",
    "Jewelry box",
    "Food processor",
    "Silverware",
    "Oysters",
    "How to become a snooker champ - in 24 hours by Clue Baize",
    "Wallet (Villa Gordon)",
    "Popcorn machine maintenance manual",
    "The ultimate collection of movie one-liners by Garth Pikett",
    "Coin collection (Villa Gordon)",
    "Bronze statue",
    "Universal remote",
    "Cable box",
    "Expensive vintage sneakers",
    "Rare genuine vintage band t-shirt",
    "Credit card",
    "Elevator maintenance manual",
    "Exclusive make-up",
    "Sleeping pills",
    "Wallet (top floor)",
    "Penthouse gardening by Liza Green",
    "Dictaphone",
    "A stash of emergency cash",
    "Chef knives",
    "Nice cooking pan",
    "Russian caviar",
    "Gordon's hidden birthday gift for Ms. Couman",
    "Gordon's lost passport",
    "Box of artisanal tomato soup",
    "A vacuum cleaner (Villa Gordon)",
    "Portable casette tape player",
    "Pretty fancy bottle of rum",
    "Electric drill (Villa Gordon)",
    "Carburetor for Castanet 500L",
    "Expensive callibration tool",
    "The Lazy Express",
    "Wallet (security office)",
    "Engraved lighter (Freya's room)",
    "What a fancy racing trophy",
    "A car mechanics toolbox"]
    )
    mansion.add_locations(mansion_valuable_locations, TeardownLocation)

    caveisland_valuable_locations = get_location_names_with_ids(
        ["Stack of gold bullions",
    "Bag of cash (Hollowrock Island)",
    "Air purifier",
    "Dual line telephone",
    "Extra potent nutrition",
    "Fungimax synthetic yeast",
    "TurboWipe pesticide",
    "Tidyfresh premium detergent",
    "Electric drill (Hollowrock Island)",
    "Disc cutter (Hollowrock Island)",
    "Old TV",
    "Spare carbon arc lamp",
    "A crock of gold",
    "Synthetic tar",
    "Fishing gear (Hollowrock Island)",
    "Precision fishing scale",
    "Portable FM radio",
    "High-speed labeling device",
    "Sakawana fishing knife",
    "TV (Hollowrock Island)",
    "Wallet (Hollowrock Island)",
    "Ivory chess pieces",
    "Rags and water bottles",
    "Hand-drill and duct tape",
    "Vacuum cleaner (Hollowrock Island)",
    "Projector",
    "Opus Juan vintage wine",
    "Binoculars (Hollowrock Island)",
    "Garden scissors",
    "Alarm clock",
    "Flat screen monitor",
    "Essential one-liners by Dilip Sequoia",
    "Bottle of gin",
    "Digital pulse monitor watch",
    "Cash register (Hollowrock Island)",
    "Cash register (BT store)",
    "BlueTide Extra Strong, limited edition",
    "Sleeping Aid"]
    )
    caveisland.add_locations(caveisland_valuable_locations, TeardownLocation)

    mall_valuable_locations = get_location_names_with_ids(
        ["How to look busy at work magazine",
    "Holy Paula Taco spices",
    "Very durable phone",
    "Sandproof radio",
    "Signature vinegar",
    "Eau de toilette",
    "RoflFX Effect Pedal",
    "Famous underwear",
    "Cheap garden scissors",
    "How to open any safe in 4 easy steps",
    "Limited edition video game hoodie",
    "Fake demonstration cash",
    "Stylish fur coat",
    "Lost wallet (Evertides Mall)",
    "Rare pink spray paint",
    "Gold watch",
    "Ruby necklace",
    "Cheap vodka",
    "MumboJumbo 3D 16MB VRAM",
    "Taxfree profit",
    "Deposited funds",
    "Confiscated Skateboard",
    "Red stapler",
    "24k golden tie pin",
    "Civet Coffee",
    "Truffle juce",
    "Flashlight (Evertides Mall)"]
    )
    mall.add_locations(mall_valuable_locations, TeardownLocation)

    frustrum_valuable_locations = get_location_names_with_ids(
        ["High Quality Oil Paint",
    "LIT yearly bonus",
    "High viscosity oil",
    "Harmonica B-minor",
    "Reciprocating saw",
    "Lost wallet (Frustrum)",
    "Fishing lure",
    "Wingman Precision Darts",
    "Lost wallet (club)",
    "Smoke Machine MkII",
    "Gender Revolvers LP",
    "Razor Shaver S",
    "Frustrum Town Council Community Award: Fred Frustrum - Gas Attendant. 'You keep the town rolling'",
    "Tribal Mask",
    "Dehumidifier NM200",
    "Questionable bone collection",
    "Lost wallet (above tunnel)",
    "Frederick Frustrums long lost hat",
    "Lost engagement ring",
    "Secret spices",
    "Lost wallet (hotel)",
    "Silk smooth fabric softener",
    "Smooth Skin Plus",
    "Industrial filter",
    "Preasure meter",
    "Gibbon Stereocaster",
    "Bits set"]
    )
    frustrum.add_locations(frustrum_valuable_locations, TeardownLocation)

    carib_valuable_locations = get_location_names_with_ids(
        ["Expensive snorkel",
    "A volley ball turned into a toy",
    "Exotic fruit",
    "Golden 28 inch rims",
    "Lost wallet (Isla Estocastica)",
    "A monkey hand, it's supposed to grant you wishes",
    "Money counter",
    "Diamond cane",
    "Brass knuckles",
    "Island life - Your guide to the Muratoris",
    "Pineapple",
    "Inflatable duck",
    "Bird egg",
    "Unused mortar shell",
    "Golden grillz",
    "Scuba tank",
    "Tropical helmet",
    "Tuning kit",
    "Golden bullets",
    "High precision scale",
    "A really old message in a bottle",
    "Marine supercharger",
    "Dried out carburetor",
    "A genuine pegleg",
    "The last roll of TP",
    "A skate, how did that end up here...",
    "Old magazines",
    "Chainsaw",
    "Good grappa",
    "Jetski engine",
    "Machine grease",
    "A teapot, short and stout...",
    "Bayran deluxe sunglasses"]
    )
    carib.add_locations(carib_valuable_locations, TeardownLocation)

    factory_valuable_locations = get_location_names_with_ids(
        ["Ultrasonic Distance Sensor",
    "SURVIVAL 101 - Nuts, bark and berries",
    "Distance sensor",
    "Infrared Sensor",
    "A pair of scuba diving oxygen tanks",
    "High sensitivity moisture sensor",
    "Continuous rotation servo motor",
    "Half Ambient Light-sensor 9000",
    "Water proof material sample",
    "A deck of poker cards",
    "Quilez corporate umbrella",
    "Handrolled Muratori cigars",
    "Office safe master key replica",
    "What a beautiful bouquet of roses",
    "A discarded bouquet of roses",
    "A trashed bouquet of roses",
    "Motivational reminder appreciation token /Gillian",
    "Top 25 camping spots in Löckelle",
    "A nice rock climbing hat",
    "Outboard motor",
    "Infrared Transmitter",
    "Box of semi-conductors",
    "Vault door gear motor",
    "Gyroscope",
    "AI core",
    "High sensitivity microphone sensor",
    "Bullet proof material sample",
    "A fishing rod",
    "A battery powered radio",
    "Photoresistor Light Sensor",
    "Helicopter maintenance manual",
    "Explosion proof material sample"]
    )
    factory.add_locations(factory_valuable_locations, TeardownLocation)

def create_events(world: TeardownWorld) -> None:

    home = world.get_region("Löckelle Teardown Services")
    lee = world.get_region("Lee Chemicals")
    marina = world.get_region("West Point Marina")
    mansion = world.get_region("Villa Gordon")
    caveisland = world.get_region("Hollowrock Island")
    mall = world.get_region("Evertides Mall")
    frustrum = world.get_region("Frustrum")
    vacation = world.get_region("Muratori Beach")
    carib = world.get_region("Isla Estocastica")
    factory = world.get_region("Quilez Security")
    cullington = world.get_region("Cullington")

    lee.add_event(
        "Lee Missions Complete", "Lee Cleared", location_type=TeardownLocation, item_type=items.TeardownItem
    )

    marina.add_event(
        "Marina Missions Complete", "Marina Cleared", location_type=TeardownLocation, item_type=items.TeardownItem
    )

    mansion.add_event(
        "Villa Missions Complete", "Villa Cleared", location_type=TeardownLocation, item_type=items.TeardownItem
    )

    caveisland.add_event(
        "Hollowrock Missions Complete", "Hollowrock Cleared", location_type=TeardownLocation, item_type=items.TeardownItem
    )

    mall.add_event(
        "Mall Missions Complete", "Mall Cleared", location_type=TeardownLocation, item_type=items.TeardownItem
    )

    frustrum.add_event(
        "Frustrum Missions Complete", "Frustrum Cleared", location_type=TeardownLocation, item_type=items.TeardownItem
    )

    carib.add_event(
        "Estocastica Missions Complete", "Estocastica Cleared", location_type=TeardownLocation, item_type=items.TeardownItem
    )

    factory.add_event(
        "Quilez Missions Complete", "Quilez Cleared", location_type=TeardownLocation, item_type=items.TeardownItem
    )

    cullington.add_event(
        "The Final Diversion", "Victory", location_type=TeardownLocation, item_type=items.TeardownItem
    )
