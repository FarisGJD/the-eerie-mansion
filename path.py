"""
Game Paths
"""

# Winning Game Path (Path 1)

p1_correct_path = {
        "p1": """\nYou enter and find an empty room with two doors on either side.
                \rThe first looks ordinary and unassuming, however the second
                \rhas a trail of tiny spiders walking towards and underneath
                \rit. They look as if they are fleeing from something.\n""",

        "p2": """\nYou enter into a dimly lit room illuminated by a crack in the
                \rroof. As you close the door the ceiling collapses, trapping
                \ryou inside. You look around to find a lone door ahead, with
                \rno way back or alternate path. You have no choice but to
                \renter.\n
                \rYou walk inside and struggle to see anything. You remember
                \rthe damaged switch board and begin to worry. Could the rest
                \rof your journey be in virtual darkness? While walking around
                \ryou trip over an object. You go back to inspect it. By a
                \rstroke of luck, you find a flash light. You will finally be
                \rable to see. There are three doors in front of you.\n""",

        "p3": """\nYou open the second door to find a library filled with books
                \rthat are covered in dust and cobwebs. As you search through
                \rthe literature, you lift a biographic novel which triggers a
                \rmechanism, revealing a fake bookcase with three doors
                \rbehind it.\n""",

        "p3i": """You enter the room and find two doors side by side. The
                \rfirst has a blacked-out window next to it. You try and look
                \rthrough but cannot discern anything. As you scramble,
                \rdesperate to gather your surroundings you find a tiny
                \rscratched off surface and look through. You realise you ares
                \rthree stories above a garden. You try to look for more clues
                \rand see what appears to be the beginnings of staircase
                \rhandle connected to the first door.""",

        "p4": """\nYou open the door to find a long hallway leading one direction,
                \rthis looks promising. You start your journey trying to
                \rlocate the end......It feels like you have been walking for
                \rhours. You finally reach a cross roads which departs to
                \rthree doors.\n""",

        "p5": """\nAs you open the door you walk through a thick layer of cobwebs.
                \rYou see two doors, the first looks untouched while the second
                \rappears to be covered in fang marks.\n""",

        "p6": """\nYou walk into an icy, cold room. As you look around your breath
                \rstarts to produce condensation due to the extreme
                \rtemperature. You see two doors both looking ordinary. As you
                \rclosely inspect them you find the handle of the second door
                \rto be covered in dry blood.\n""",

        "p7": """\nYou enter to see a massive greenhouse sheltering large exotic
                \rplants. As you walk through you hear scuttering all around
                \ryou. You find a piece of paper titled “Experiment Report, By
                \rDr. Charles Falken”.\n""",

        "p8": """\nYou enter a room to find heaps of spider eggs and
                \rexoskeletons the size of cars. You see two doors both with a
                \rstrange clear substance on them. As you touch an inspect it
                \ryour hand starts to burn. Could it be venom?\n""",

        "p9": """\nAmid opening the door you are stupefied by the odour of
                \rrotting matter dissipating within, though there is nothing
                \rproducing it. As you walk around you hear a deafening
                \rhissing noise coming from the only two doors in front of you.
                \rScared you think of heading back but realise this is the
                \ronly way out.\n""",

        "p10": """\nYou enter the room, shocked and horrified by what you see.
                \rSeveral silk cocoons, blood and human remains are scattered
                \rthroughout. As you try to exit from where you entered, a
                \rspider web shoots from across the room blocking the
                \rdoor.\n
                \rOH NO!!! IT IS A COLOSSAL TARANTULA THE SIZE OF A HOUSE. It
                \rstarts running straight towards you. Petrified, you curl
                \rinto a ball, clutching your flashlight. As you accept your
                \rimpending doom your flashlight suddenly goes off. What? How
                \rcould this be? The tarantula starts retreating swiftly. You
                \rbegin to understand why the switch board was damaged and why
                \rthe tiny spiders were fleeing once the light turned on in
                \rthe attic.\n
                \rYou aim the flashlight directly at the tarantula and slowly
                \rstart making your way pass it and enter a door, running downs
                \ra flight of stairs. Is this the end?\n"""
}

# Winning Game Path, Additions (Path 1)

p1_correct_path_additions = {
        "p3a": """\nLifting the novel triggers a mechanism, revealing a fake
                \rbookcase with two doors behind it.\n""",

        "p7a": """\nYou finish reading the report and realise you are being
                \rwatched by hunderds of tarantulas. Their fangs dripping
                \rwith venom, burning holes in the ground. Quick there are
                \rtwo doors in front of you.\n""",
}

# Lossing Game Path (Path 1)

p1_losing_path = {
        "p1": """AS YOU OPEN THE DOOR YOU IMMEDIATELY START FALLING,
                \rREALISING THE FLOOR WAS COMPLETELY MISSING, PLUMMETING TO
                \rYOUR DEATH.""",

        "p2": """INSTANT DEATH!! THE PREVIOUS ROOMS MECHANISM TRIGGERS AN
                \rCROSSBOW AND ARROW, PIERCING STRAIGHT THROUGH YOUR SKULL.""",

        "p3": """YOU ENTER A PITCH-BLACK ROOM AND ARE UNABLE TO SEE.
                \rUNEXPECTEDLY THE LIGHTS TURN ON AND A SWINGING GUILLOTINE
                \rSLICES YOU IN HALF.""",

        "p3i": """AS YOU OPEN THE DOOR YOU FEEL A BREEZE EMANATING FROM THE
                \rOTHER SIDE. EXITED YOU QUICKLY WALK THROUGH TO FIND THE
                \rSTAIRCASE WAS A DECOY WITH NO STEPS. YOU FALL DOWN THREE
                \rSTOREIS TO YOUR DEATH.""",
        
        "p3ii": """YOU WALK INTO A BEDROOM THAT LOOKS RECENTLY LIVED IN. THIS
                \rMEANS SOMEONE ELSE MIGHT BE NEARBY AND ABLE TO HELP.
                \rSUDDENLY YOU HEAR A LOUD THUD AND NOTICE A CHANDELIER ABOVE
                \rYOU. IT SWIFTLY BECOMES UNDONE AND FALLS, KNOCKING YOU
                \rOUT......AS YOU FALL IN AND OUT OF CONSIOUNESS YOU NOTICE A
                \rDARK FIGURE STANDING ABOVE YOU WITH A NEEDLE IN HAND.""",

        "p4": """YOU WALK THROUGH THE DOOR AND ARE GREETED WITHIN AN INCLINING
                \rPATH. AS YOU MAKE YOUR WAY THROUGH YOU HEAR A RUMBLING NOISE.
                \rYOU NOTICE AN OBJECT HURTLING TOWARDS YOU. OH NO, IT’S A
                \rMASSIVE BOULDER.""",

        "p5": """YOU REACH A DEAD END WITH NO WAY OUT.""",

        "p6": """YOU ENTER A ROOM COVERED IN GREEN SMOKE. AS SOON AS YOU TAKE
                \rA BREATH YOU COLLAPSE AND LOSE CONSCIOUSNESS.""",

        "p7": """AS YOU WALK INSIDE YOU NOITCE THAT THE FLOOR IS FLOODED AND
                \rCONNECTED TO THE NEIGHBOURING ROOM. YOU BEGIN TO WALK TO THE
                \rONLY DOOR INFRONT OF YOU. ALL THE SUDDEN A LOOSE, ACTIVE
                \rWIRE FALLS TO THE GROUND ELECTROCUTING YOU.""",

        "p8": """YOU WALK INTO A DARK ROOM, BARELY ABLE TO SEE. YOU DELVE
                \rDEEPER INTO THE SPACE, TRYING TO FEEL FOR ANYTHING FAMILIAR.
                \rBY A STROKE OF LUCK, YOU FIND A LIGHT SWITCH ATTACHED TO THE
                \rWALL. YOU TURN ON THE LIGHT……AND FIND YOURSELF SURROUNDED BY
                \rTHOUSANDS OF TARANTULAS, INSTANTLY ATTACKING YOU.""",

        "p9": """YOU WALK INTO A TRAP AND FALL INTO A WATER HOLE. YOU'RE NOT
                \rALONE. SUDDENLY YOU FEEL SOMETHING BITING YOUR LEG, DRAGGING
                \rYOU UNDER.""",

        "p10": ""
}

# Losing Game Path (Path 2)

p2_losing_path = {
        "p1": """YOU ENTER A ROOM WITH FLICKERING LIGHTING. YOU LOOK AROUND
                \rAND FIND A DISHEVELLED MAN STANDING IN THE CORNER,
                \rHAUNTINGLY GLARING AT YOU……, OH NO!!! HE STARTS RUNNING
                \rTOWARDS YOU WITH A KNIFE IN HAND SCREAMING SPIDERS!
                \rSPIDERS!."""
}

# Gmae Path (Path 3)

p3_game_path = {

}