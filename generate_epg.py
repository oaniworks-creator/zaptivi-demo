import datetime
import os

epg_file = os.path.join(os.path.dirname(__file__), "demo_epg.xml")

channels_data = [
    {
        "id": "demo_cosmos",
        "name": "COSMOS 4K",
        "programs": [
            ("Galactic Frontiers", "Deep-space astrophysics and nebula mappings.", 60),
            ("Wonders of the Andromeda Core", "Deep interstellar phenomena at the heart of our nearest neighbor.", 55),
            ("Stargazers Live", "Live high-altitude telescope skywatch and comet tracking.", 65),
            ("Black Hole Horizons", "The event horizon telescope and gravitational physics.", 50),
            ("The Interstellar Medium", "Cosmic dust and the stellar cradle of new solar systems.", 60),
            ("Solar Storm Chronicles", "Solar flares and geomagnetic interactions in the outer atmosphere.", 45)
        ]
    },
    {
        "id": "demo_aurora",
        "name": "AURORA PLANET",
        "programs": [
            ("Glaciers of the South", "Ice shelf dynamics and polar expeditions in Antarctica.", 45),
            ("Aurora Borealis: Northern Lights", "Ultra-high-definition time-lapse captures of geomagnetic storms.", 65),
            ("Fjords of Scandinavia", "Coastal explorations tracing the steep valleys of western Norway.", 50),
            ("Icelandic Geysers & Hot Springs", "Geothermal power and tectonic rifts in the sub-arctic.", 70),
            ("Midnight Sun Expeditions", "Summer in the arctic circle where the sun never sets.", 45),
            ("Alpine Wonders", "High alpine ecosystems and seasonal migrations.", 60)
        ]
    },
    {
        "id": "demo_nova",
        "name": "NOVA 1 UHD",
        "programs": [
            ("Wild Patagonia: Realm of the Snow Leopard", "Elusive hunters mastering mountain ridges in extreme winter.", 50),
            ("Ocean Secrets: Deep Trench Expedition", "Deep-sea submersibles exploring the Mariana Trench.", 45),
            ("Kingdom of the Polar Bear", "Survival along the melting ice edges of Svalbard.", 75),
            ("Forest Canopies of Madagascar", "Unique biodiversity in the ancient tropical rain forests.", 90),
            ("The Great Serengeti Crossing", "Massive herds navigating predator-filled waters in East Africa.", 45),
            ("Dawn Over the Amazon", "Canopy awakening along the tributaries of the Amazon Basin.", 50)
        ]
    },
    {
        "id": "demo_horizon",
        "name": "HORIZON WILD",
        "programs": [
            ("Savannah Dawn Chronicles", "Predators and grazers beginning their day on the open plain.", 60),
            ("Majestic Predators: Mountain Realm", "Documentary following cougars and mountain goats.", 65),
            ("Amazon Untamed: River Giants", "Freshwater behemoths and biodiversity along the Rio Negro.", 35),
            ("Wings of the Highlands", "Raptors soaring through high thermals over the Andes.", 50),
            ("Creatures of the Midnight Sun", "Arctic foxes and migratory caribou herds.", 45),
            ("Secrets of the Coral Triangle", "Diving the richest marine habitat on Earth.", 80)
        ]
    },
    {
        "id": "demo_apex",
        "name": "APEX SPORTS 1",
        "programs": [
            ("World Touring Championship: Grand Final", "Live sprint finish from Silverstone Circuit.", 110),
            ("Apex Matchday Highlights", "Post-match telemetry, interviews, and podium ceremony.", 40),
            ("Pro Karting Invitational", "Young drivers battling for top-tier open wheel seats.", 80),
            ("Speedway Championship Live", "Oval track dirt bike racing under the floodlights.", 110),
            ("Motorsport Legends: Turbo Era", "Classic archival footage and engineering retrospectives.", 30),
            ("Pre-Race Trackside Analysis", "Tire compounds and weather forecast breakdown.", 45)
        ]
    },
    {
        "id": "demo_velocity",
        "name": "VELOCITY RACING",
        "programs": [
            ("Monza Superbike Championship", "High-octane motorcycle racing from the Temple of Speed.", 85),
            ("Pit Lane Live Analysis", "Telemetry breakdown, gear ratios, and suspension dynamics.", 35),
            ("Rallycross Legends", "Dirt, asphalt, and jumps in European championship stages.", 90),
            ("Hillclimb Challenge 2026", "Precision time attacks on narrow Alpine mountain passes.", 30),
            ("Turbo Supercup Highlights", "GT3 endurance cars racing into the sunset.", 60),
            ("Telemetry & Tech Review", "Aerodynamic tunnels and brake pressure data reviews.", 40)
        ]
    },
    {
        "id": "demo_pulse",
        "name": "PULSE CINEMA 4K",
        "programs": [
            ("The Astral Horizon (2025)", "Deep space expedition discovers an artifact orbiting a dying star.", 115),
            ("Chronicles of the Deep", "Submerged archaeological discovery beneath the Mediterranean shelf.", 110),
            ("Neon Odyssey: 2099", "Atmospheric retro-futuristic detective thriller.", 95),
            ("Echoes of the Canyon", "Desert mystery drama shot in crisp 65mm format.", 120),
            ("The Silent Orbit", "Astronaut stranded on an automated communications outpost.", 85),
            ("Midnight in Kyoto", "Neo-noir crime drama through neon-lit streets.", 100)
        ]
    },
    {
        "id": "demo_solaris",
        "name": "SOLARIS DOCS",
        "programs": [
            ("Origins of the Cosmos: Webb Telescope", "Earliest galaxies captured by deep infrared space observatories.", 40),
            ("The Quantum Enigma", "Leading physicists demonstrate fundamental laws shaping reality.", 50),
            ("Mysteries of Dark Matter", "Underground particle detectors searching for hidden mass.", 60),
            ("Voyage to the Gas Giants", "Juno and Cassini spacecraft trajectories around Jupiter and Saturn.", 45),
            ("Future Cities on Mars", "Architectural and biological challenges of off-world colonies.", 50),
            ("Life in Extreme Climates", "Microorganisms thriving in hydrothermal vents and acidic pools.", 45)
        ]
    },
    {
        "id": "demo_spectrum",
        "name": "SPECTRUM ARTS",
        "programs": [
            ("Philharmonic Gala Concert Live", "Beethoven's 9th Symphony performed by international soloists.", 80),
            ("Modern Sculpture in Architecture", "Monumental public installations in global design capitals.", 45),
            ("Jazz Under the Stars", "Live quartet improvisation recorded in Montreux.", 60),
            ("The Art of Cinematography", "Directors of photography discuss lighting and aspect ratios.", 80),
            ("Operatic Arias at Sunset", "Acoustic open-air performance from the Arena di Verona.", 40),
            ("Masterclass: Renaissance Oil Painting", "Pigments, glazes, and historical restoration techniques.", 50)
        ]
    },
    {
        "id": "demo_news",
        "name": "GLOBAL NEWS 24",
        "programs": [
            ("World News Live & Markets Update", "Global headline reports, economic indicators, and correspondents.", 30),
            ("Tech Innovations Round-up", "Advancements in robotics, clean energy, and space transport.", 15),
            ("Global Perspective: Asia-Pacific", "In-depth diplomatic and trade analysis across Asian markets.", 45),
            ("The World Tonight", "Evening flagship news hour and investigative reporting.", 30),
            ("Financial Frontiers", "Commodities, foreign exchange, and central bank commentary.", 15),
            ("International Correspondent Notebook", "Behind the scenes reporting on major world events.", 45)
        ]
    }
]

# Generate schedule starting 2 days ago through 5 days in the future (total 7 days)
now = datetime.datetime.now(datetime.timezone.utc)
base_time = (now - datetime.timedelta(days=2)).replace(hour=0, minute=0, second=0, microsecond=0)
end_time = now + datetime.timedelta(days=5)

fmt = "%Y%m%d%H%M%S +0000"

lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<!DOCTYPE tv SYSTEM "xmltv.dtd">',
    '<tv generator-info-name="ZapTivi-Demo-Generator">'
]

# Channels
for ch in channels_data:
    lines.append(f'  <channel id="{ch["id"]}">')
    lines.append(f'    <display-name>{ch["name"]}</display-name>')
    lines.append('  </channel>')

# Programmes
for ch in channels_data:
    current = base_time
    prog_idx = 0
    progs = ch["programs"]
    while current < end_time:
        p_title, p_desc, p_dur = progs[prog_idx % len(progs)]
        p_start = current
        p_stop = current + datetime.timedelta(minutes=p_dur)
        
        start_str = p_start.strftime(fmt)
        stop_str = p_stop.strftime(fmt)
        
        lines.append(f'  <programme start="{start_str}" stop="{stop_str}" channel="{ch["id"]}">')
        lines.append(f'    <title lang="en">{p_title}</title>')
        lines.append(f'    <desc lang="en">{p_desc}</desc>')
        lines.append('  </programme>')
        
        current = p_stop
        prog_idx += 1

lines.append('</tv>')

with open(epg_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Successfully generated {epg_file} with {len(lines)} lines.")
