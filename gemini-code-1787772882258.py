import json

# Define the 50 activities dataset
activities = [
    # 1. Financial Literacy & Money Smart
    {
        "id": 1,
        "title": "3-Gullak Allocation System",
        "category": "finance",
        "age": "3-5",
        "duration": "15 mins",
        "desc": "Split weekly pocket money or cash gifts into Kharacha (Spend), Bachat (Save), and Daan (Give).",
        "materials": ["3 clear jars/containers", "Labels/Markers", "Coins or cash notes"],
        "steps": [
            "Label three jars: Kharacha (Spend - 60%), Bachat (Save - 30%), and Daan (Give - 10%).",
            "Whenever money is received, count the total together.",
            "Helper child deposit coins into each jar following the percentage rule.",
            "Discuss what goal the Bachat jar is saving for (e.g. toy, book)."
        ],
        "learning": "Basic financial discipline, basic math, and delayed gratification."
    },
    {
        "id": 2,
        "title": "Supermarket Math Detective",
        "category": "finance",
        "age": "6-8",
        "duration": "30 mins",
        "desc": "Calculate price per gram or per item during grocery runs to find the smartest buy.",
        "materials": ["Notepad/Phone calculator", "Grocery list", "Store items"],
        "steps": [
            "Pick two items of different sizes (e.g., 250g vs 500g pulse pack).",
            "Calculate price per 100g for both options.",
            "Identify which option offers better value for money.",
            "Keep a tally of savings made during the shopping trip."
        ],
        "learning": "Unit pricing, mental division, and smart consumer habits."
    },
    {
        "id": 3,
        "title": "Festival Lifafa Planner",
        "category": "finance",
        "age": "6-8",
        "duration": "20 mins",
        "desc": "Budget cash gifts received during Diwali, Rakhi, or Eid into short and long-term targets.",
        "materials": ["Envelopes (Lifafas)", "Savings tracker sheet", "Pen"],
        "steps": [
            "Collect festive cash gifts and calculate total sum.",
            "Allocate 50% to long-term Bachat (bank/PPF/digital gold), 30% to immediate wish list, and 20% to charity.",
            "Write the goal on the envelope and track deposit dates."
        ],
        "learning": "Windfall management and long-term wealth building."
    },
    {
        "id": 4,
        "title": "Needs vs. Wants Sorting Battle",
        "category": "finance",
        "age": "3-5",
        "duration": "15 mins",
        "desc": "Speed-sort household items and picture cards into essential needs vs. optional wants.",
        "materials": ["2 Baskets labeled 'Zaroorat' & 'Khwahish'", "Flashcards/real items (bread, shoes, arcade ticket, toy)"],
        "steps": [
            "Place items in a central pile.",
            "Set a 1-minute timer.",
            "Pick an item and quickly place it in 'Zaroorat' (Need) or 'Khwahish' (Want).",
            "Review items at the end and discuss debatable choices."
        ],
        "learning": "Prioritization, critical thinking, and impulse control."
    },
    {
        "id": 5,
        "title": "Nimbu Pani Enterprise",
        "category": "finance",
        "age": "9-10",
        "duration": "45 mins",
        "desc": "Set up a weekend lemonade stall to learn cost price, selling price, and net profit.",
        "materials": ["Lemons, Sugar, Water, Ice", "Paper cups", "Price board & cash box"],
        "steps": [
            "Calculate raw material costs (e.g., ₹50 total).",
            "Decide price per cup (e.g., ₹10/cup) based on target margin.",
            "Sell to family/neighbors and track revenue.",
            "Calculate Profit = Revenue - Total Expense."
        ],
        "learning": "Entrepreneurship basics, P&L calculations, and customer service."
    },
    {
        "id": 6,
        "title": "Interest Multiplier Machine",
        "category": "finance",
        "age": "6-8",
        "duration": "10 mins/week",
        "desc": "Parents pay a 10% monthly 'Bachat Bonus' matching reward for money untouched in the save jar.",
        "materials": ["Save Jar", "Parent ledger notebook", "Bonus coins"],
        "steps": [
            "Count funds in the Save Gullak on the 1st of every month.",
            "For every ₹100 kept safely without spending, parent adds ₹10 bonus.",
            "Record interest added in a visual growth chart."
        ],
        "learning": "Compound interest concepts and incentives for saving."
    },
    {
        "id": 7,
        "title": "Weekly Budget Master",
        "category": "finance",
        "age": "9-10",
        "duration": "15 mins/week",
        "desc": "Track daily personal expenses in a mini pocket ledger and analyze weekly variance.",
        "materials": ["Mini pocket notebook", "Pen"],
        "steps": [
            "Set a weekly budget limit (e.g., ₹200).",
            "Write every small expense down daily (bus fare, stationery, snack).",
            "Sum total at weekend and calculate remaining balance."
        ],
        "learning": "Expense tracking, accountability, and bookkeeping."
    },
    {
        "id": 8,
        "title": "Bargain Boss Mental Math",
        "category": "finance",
        "age": "Youth & Parents",
        "duration": "20 mins",
        "desc": "Practice mental calculations of percentage discounts and final payable amounts at local markets.",
        "materials": ["Flashcards with price tags & discount %"],
        "steps": [
            "Draw a flashcard (e.g. ₹800 shirt at 25% off).",
            "Calculate discount value in head (₹200).",
            "State final price within 10 seconds (₹600)."
        ],
        "learning": "Percentage mental math and commercial awareness."
    },
    {
        "id": 9,
        "title": "Daan & Kindness Tracker",
        "category": "finance",
        "age": "3-5",
        "duration": "30 mins",
        "desc": "Use 10% of allowance to purchase food, animal feed, or clothes for community helpers.",
        "materials": ["Daan Gullak", "Shopping list for donations"],
        "steps": [
            "Pool funds accumulated in the Daan Gullak.",
            "Decide target recipient (e.g., stray dogs feed, security guard tea/biscuits).",
            "Buy items directly with child's involvement and distribute."
        ],
        "learning": "Empathy, community solidarity, and purposeful spending."
    },
    {
        "id": 10,
        "title": "Barter Trade Simulator",
        "category": "finance",
        "age": "6-8",
        "duration": "20 mins",
        "desc": "Swap household items or cards to discover the limitations of barter vs money standard.",
        "materials": ["5 random toys/books per player"],
        "steps": [
            "Assign items to players without money.",
            "Try trading items to get what you want (e.g., pencil for eraser).",
            "Experience 'double coincidence of wants' problem.",
            "Discuss why currency makes trade easier."
        ],
        "learning": "Origin of money, valuation, and trade negotiation."
    },

    # 2. Vedic Math, Logic & Brain Puzzles
    {
        "id": 11,
        "title": "Vedic Math Multiplication Blitz",
        "category": "math",
        "age": "9-10",
        "duration": "20 mins",
        "desc": "Learn the Ekadhikena Purvena sutra to multiply numbers ending in 5 instantly.",
        "materials": ["Paper", "Pen", "Timer"],
        "steps": [
            "Learn formula for numbers ending in 5 (e.g. 35 x 35).",
            "Multiply first digit by its successor: 3 x (3+1) = 12.",
            "Append 25 at the end: 1225!",
            "Solve 10 practice problems in under 2 minutes."
        ],
        "learning": "Vedic mathematics shortcuts and numerical speed."
    },
    {
        "id": 12,
        "title": "Chaturanga Knight Path Challenge",
        "category": "math",
        "age": "6-8",
        "duration": "25 mins",
        "desc": "Solve chess knight move puzzles inspired by ancient Indian Chaturanga strategy.",
        "materials": ["Chessboard", "Knight piece", "Coins as markers"],
        "steps": [
            "Place knight on starting square.",
            "Move in L-shapes to visit marked squares without stepping on red squares.",
            "Count total moves taken to finish path."
        ],
        "learning": "Spatial reasoning, grid coordinates, and forward planning."
    },
    {
        "id": 13,
        "title": "Rangoli Symmetry & Tessellation",
        "category": "math",
        "age": "6-8",
        "duration": "30 mins",
        "desc": "Design traditional dot-grid Rangoli patterns to explore geometry, reflection, and symmetry.",
        "materials": ["Dot grid paper or chalk", "Colored pens/powders"],
        "steps": [
            "Draw a 5x5 or 7x7 dot matrix.",
            "Create a quadrant design and mirror it across horizontal and vertical axes.",
            "Identify line symmetry and rotational symmetry angles."
        ],
        "learning": "Geometric transformations, rotational symmetry, and pattern recognition."
    },
    {
        "id": 14,
        "title": "Desi Sudoku Quest",
        "category": "math",
        "age": "3-5",
        "duration": "15 mins",
        "desc": "Grid puzzle using Indian symbols (Lotus, Diya, Peacock, Mango) instead of numbers.",
        "materials": ["4x4 printed grids", "Symbol stickers/cutouts"],
        "steps": [
            "Fill a 4x4 grid so every row, column, and 2x2 box has all 4 unique symbols.",
            "Start with 2 pre-filled clues per row.",
            "Complete grid without repeating any icon in a line."
        ],
        "learning": "Deductive logic, visual scanning, and elimination reasoning."
    },
    {
        "id": 15,
        "title": "Memory Palace Storyteller",
        "category": "math",
        "age": "Youth & Parents",
        "duration": "20 mins",
        "desc": "Ancient Indian mnemonic technique associating list items with rooms in your house.",
        "materials": ["List of 15 random items/capitals"],
        "steps": [
            "Visualize your home entrance, living room, kitchen, etc.",
            "Place bizarre mental imagery of each item at specific rooms in order.",
            "Walk through home in your mind to recall all 15 items flawlessly."
        ],
        "learning": "Mnemonic memory systems, visualization, and rapid recall."
    },
    {
        "id": 16,
        "title": "Panchatantra Logic Flowcharts",
        "category": "math",
        "age": "9-10",
        "duration": "30 mins",
        "desc": "Convert fable decision paths into flowchart logic statements (If-Else loops).",
        "materials": ["Paper", "Colored pens"],
        "steps": [
            "Read a Panchatantra tale (e.g. The Monkey and the Crocodile).",
            "Identify key decision points (e.g. IF Monkey trusts Crocodile THEN go to river ELSE stay on tree).",
            "Draw standardized flowchart shapes (Diamond decision, Rectangle action)."
        ],
        "learning": "Computational thinking, conditional logic, and diagramming."
    },
    {
        "id": 17,
        "title": "Visual Abacus Bead Speedrun",
        "category": "math",
        "age": "6-8",
        "duration": "15 mins",
        "desc": "Perform double-digit addition using imaginary abacus bead movements.",
        "materials": ["Abacus frame or mental image guide"],
        "steps": [
            "Visualize upper bead = 5, lower beads = 1.",
            "Call out numbers rapidly (e.g., +12, +5, -2, +15).",
            "Move fingers in air corresponding to bead movements and announce total."
        ],
        "learning": "Mental arithmetic speed, concentration, and working memory."
    },
    {
        "id": 18,
        "title": "Dadi-Nani Paheliyan (Riddle Night)",
        "category": "math",
        "age": "Youth & Parents",
        "duration": "20 mins",
        "desc": "Solve classic Indian verbal logic riddles and word puzzles over evening tea.",
        "materials": ["Riddle cards list"],
        "steps": [
            "Read aloud a traditional riddle (e.g., 'Ek kahanikarak, bina muh ke bole...').",
            "Teams brainstorm answers under a 60-second clock.",
            "Award points for logical deductions and creative answers."
        ],
        "learning": "Lateral thinking, linguistic comprehension, and family bonding."
    },
    {
        "id": 19,
        "title": "Cryptic Rupee Codebreaker",
        "category": "math",
        "age": "9-10",
        "duration": "25 mins",
        "desc": "Solve cryptarithm equations where digits are replaced by letters of Indian cities.",
        "materials": ["Puzzle sheet", "Pencil"],
        "steps": [
            "Given equation: GOA + GOA = MUM (where each letter represents a digit 0-9).",
            "Deduce digit values using carryover rules and number logic.",
            "Verify solution by checking arithmetic substitution."
        ],
        "learning": "Algebraic reasoning, variable substitution, and systemic trial-and-error."
    },
    {
        "id": 20,
        "title": "Tulika Origami Geometry",
        "category": "math",
        "age": "6-8",
        "duration": "20 mins",
        "desc": "Fold paper square into 3D geometric polyhedrons to explore angles and planes.",
        "materials": ["Square paper sheets"],
        "steps": [
            "Fold square paper into Sonobe modular units.",
            "Identify acute, right, and obtuse angles created by crease lines.",
            "Interlock 6 units to construct a 3D paper cube."
        ],
        "learning": "3D geometry, spatial manipulation, and angle properties."
    },

    # 3. Indic Science, Nature & STEM Explorers
    {
        "id": 21,
        "title": "Balcony Botanical Germination Lab",
        "category": "stem",
        "age": "3-5",
        "duration": "10 mins/day",
        "desc": "Germinate mustard (Sarson) and Bengal gram (Chana) seeds in cotton to log growth stages.",
        "materials": ["Cotton wool", "Small cups", "Sarson/Chana seeds", "Water spray"],
        "steps": [
            "Place damp cotton in cups with 5 seeds.",
            "Spray water daily and place in indirect sunlight.",
            "Measure shoot length with ruler daily and plot on growth chart."
        ],
        "learning": "Plant biology, scientific logging, and environmental factors."
    },
    {
        "id": 22,
        "title": "Nakshatra Sky Constellation Finder",
        "category": "stem",
        "age": "Youth & Parents",
        "duration": "30 mins",
        "desc": "Map night sky star patterns to traditional Indian Nakshatras and Zodiac constellations.",
        "materials": ["Star map chart or stargazing app", "Flashlight with red filter"],
        "steps": [
            "Observe the night sky from terrace/balcony.",
            "Locate Saptarishi (Ursa Major) and Dhruva Tara (Pole Star).",
            "Identify current Nakshatra position relative to moon placement."
        ],
        "learning": "Astronomy, celestial navigation, and seasonal cycles."
    },
    {
        "id": 23,
        "title": "Paper Plate Shadow Sundial",
        "category": "stem",
        "age": "6-8",
        "duration": "30 mins",
        "desc": "Construct an outdoor solar clock to track Earth's rotation using shadow angles.",
        "materials": ["Paper plate", "Straw/Pencil", "Compass", "Marker"],
        "steps": [
            "Poke straw through plate center.",
            "Align plate using compass facing North at 12:00 PM.",
            "Mark shadow lines every hour from 9 AM to 4 PM.",
            "Use it the next day to tell time without a watch!"
        ],
        "learning": "Solar geometry, Earth's rotation, and time measurement history."
    },
    {
        "id": 24,
        "title": "Cardboard Solar Box Cooker",
        "category": "stem",
        "age": "9-10",
        "duration": "45 mins",
        "desc": "Harness solar thermal energy using foil reflectors to warm food or melt cheese.",
        "materials": ["Shoebox", "Aluminum foil", "Plastic wrap", "Black paper"],
        "steps": [
            "Line shoebox interior with black construction paper.",
            "Cover box flap with aluminum foil to act as reflector mirror.",
            "Seal box opening with clear plastic wrap creating greenhouse traps.",
            "Place in direct sunlight and measure internal temperature rise."
        ],
        "learning": "Renewable solar energy, thermodynamics, and thermal insulation."
    },
    {
        "id": 25,
        "title": "Haldi Kitchen pH Indicator",
        "category": "stem",
        "age": "6-8",
        "duration": "20 mins",
        "desc": "Use turmeric powder solution as a natural chemical indicator for acids and bases.",
        "materials": ["Turmeric powder + water", "Lemon juice", "Soap solution", "Paper strips"],
        "steps": [
            "Dip white paper strips into turmeric water and let dry (yellow indicator strips).",
            "Drop lemon juice (acid): remains yellow.",
            "Drop detergent solution (base): turns deep red/brown!",
            "Test vinegar, milk, and baking soda."
        ],
        "learning": "Acid-base chemistry, natural indicators, and chemical reactions."
    },
    {
        "id": 26,
        "title": "Jal-Tarang Musical Sound Waves",
        "category": "stem",
        "age": "3-5",
        "duration": "25 mins",
        "desc": "Fill glass bowls with varying water levels to play scale frequencies of Indian ragas.",
        "materials": ["6-8 ceramic/glass bowls", "Water", "Wooden drumsticks/spoons"],
        "steps": [
            "Fill bowls with increasing amounts of water.",
            "Tap rim gently to hear pitch differences (more water = lower pitch).",
            "Tune bowls to notes Sa-Re-Ga-Ma-Pa-Dha-Ni-Sa.",
            "Play simple nursery tunes or classical notes."
        ],
        "learning": "Acoustics, sound frequency, and resonance principles."
    },
    {
        "id": 27,
        "title": "Eco-Brick Waste Auditor",
        "category": "stem",
        "age": "Youth & Parents",
        "duration": "1 week",
        "desc": "Audit household non-recyclable plastic packaging and pack into dense plastic bottle bricks.",
        "materials": ["1-liter plastic bottle", "Clean dry plastic wrappers", "Wooden stick"],
        "steps": [
            "Collect clean single-use soft plastic packaging over a week.",
            "Pack plastics tightly into bottle using stick until weight exceeds 330g.",
            "Weigh and log total plastic diverted from landfills.",
            "Use eco-bricks for garden boundary building."
        ],
        "learning": "Waste management, environmental auditing, and structural reuse."
    },
    {
        "id": 28,
        "title": "Village Well Pulley Physics",
        "category": "stem",
        "age": "6-8",
        "duration": "30 mins",
        "desc": "Build a mechanical pulley system to measure mechanical advantage in lifting heavy weights.",
        "materials": ["Empty thread spool", "Pencil axis", "String", "Small cup with weights"],
        "steps": [
            "Mount thread spool on pencil to rotate smoothly.",
            "Pass string over spool with cup attached on one end.",
            "Compare force needed to lift cup directly vs. using pulley.",
            "Add second pulley wheel to double mechanical advantage."
        ],
        "learning": "Simple machines, friction reduction, and mechanical advantage."
    },
    {
        "id": 29,
        "title": "Calibrated Rain Gauge Station",
        "category": "stem",
        "age": "9-10",
        "duration": "25 mins",
        "desc": "Build a weather station measurement cylinder to log daily monsoon rainfall millimeters.",
        "materials": ["Clear plastic bottle", "Ruler", "Tape", "Small stones"],
        "steps": [
            "Cut top funnel off bottle and place stones in base for stability.",
            "Invert top cut funnel downward into bottle body.",
            "Tape millimeter ruler vertically on outer wall starting above stones.",
            "Measure water volume after monsoon rains and calculate depth in mm."
        ],
        "learning": "Meteorology, fluid measurement, and data charting."
    },
    {
        "id": 30,
        "title": "Kinetic Paper Wind Turbine",
        "category": "stem",
        "age": "3-5",
        "duration": "20 mins",
        "desc": "Craft a pinwheel turbine to observe conversion of wind speed into mechanical rotation.",
        "materials": ["Square paper", "Pin", "Pencil with eraser", "Scissors"],
        "steps": [
            "Cut diagonal lines toward center of square paper.",
            "Fold alternating corner points into center and secure with pin onto eraser head.",
            "Blow air on blades to test rotational speed.",
            "Experiment with blade angle modifications for maximum RPM."
        ],
        "learning": "Wind energy conversion, aerodynamics, and rotational torque."
    },

    # 4. Creative Arts, Heritage & Storytelling
    {
        "id": 31,
        "title": "Madhubani Folk Motif Studio",
        "category": "art",
        "age": "6-8",
        "duration": "30 mins",
        "desc": "Paint Mithila Madhubani art featuring double borders, fine hatch lines, and natural themes.",
        "materials": ["Paper", "Fine tip black pen", "Watercolors"],
        "steps": [
            "Draw iconic fish, peacock, or sun focal figure.",
            "Outline all shapes with characteristic double ink lines.",
            "Fill internal negative space with geometric hatching pattern.",
            "Color using bright primary palettes."
        ],
        "learning": "Indian folk art history, fine motor precision, and pattern density."
    },
    {
        "id": 32,
        "title": "Kathputli Puppet Theatre",
        "category": "art",
        "age": "3-5",
        "duration": "45 mins",
        "desc": "Craft Rajasthani string puppets using old socks, fabric scraps, and yarn.",
        "materials": ["Old socks", "Buttons/Eyes", "Fabric scraps", "String & Stick"],
        "steps": [
            "Stuff sock top with cotton ball to create puppet head.",
            "Attach button eyes and yarn hair.",
            "Tie strings to head and hands, connecting to a wooden cross control bar.",
            "Perform a short Panchatantra folk play behind a cardboard stage."
        ],
        "learning": "Dramatic expression, textile reuse, and traditional storytelling."
    },
    {
        "id": 33,
        "title": "3D Cardboard Monument Architect",
        "category": "art",
        "age": "9-10",
        "duration": "60 mins",
        "desc": "Reconstruct structural scale models of Indian heritage architecture (e.g. Konark wheel).",
        "materials": ["Cardboard boxes", "Glue gun/Tape", "Craft knife", "Paints"],
        "steps": [
            "Study architectural features of chosen monument (arches, pillars, domes).",
            "Draft scale measurements on corrugated cardboard.",
            "Cut, assemble, and paint intricate relief features.",
            "Present historical significance speech to family."
        ],
        "learning": "Architectural geometry, scale modeling, and historical heritage."
    },
    {
        "id": 34,
        "title": "Folk Tale Choose-Your-Own-Adventure",
        "category": "art",
        "age": "6-8",
        "duration": "30 mins",
        "desc": "Write a branching story script based on Akbar-Birbal or Tenali Raman tales.",
        "materials": ["Story chart cards", "Markers"],
        "steps": [
            "Choose a central mystery or dilemma.",
            "Create 2 decision choices at the end of every page.",
            "Write different consequences leading to 3 distinct endings.",
            "Read aloud with family making real-time votes."
        ],
        "learning": "Creative writing, non-linear logic, and narrative structure."
    },
    {
        "id": 35,
        "title": "Terracotta Clay Pot Sculpting",
        "category": "art",
        "age": "3-5",
        "duration": "40 mins",
        "desc": "Hand-build clay lamps (diyas) or small vessels using ancient coil techniques.",
        "materials": ["Air-dry clay / Terracotta clay", "Water", "Sculpting tools"],
        "steps": [
            "Roll clay into long snake coils.",
            "Spiral coil base and build walls upwards by smoothing inner/outer seams.",
            "Pinch top edge to form diya oil spout shape.",
            "Let dry and paint with metallic festive paint."
        ],
        "learning": "Tactile motor control, ceramics basics, and traditional craft."
    },
    {
        "id": 36,
        "title": "Recycled Rhythm Jhunjhuna",
        "category": "art",
        "age": "3-5",
        "duration": "20 mins",
        "desc": "Build musical shakers tuned with different pulses (rice, Rajma, chana) for rhythmic beats.",
        "materials": ["Empty plastic containers", "Dried pulses/rice", "Tape & Decorative paper"],
        "steps": [
            "Fill 3 containers with different seeds (Rice = high treble, Rajma = deep bass).",
            "Seal cap securely with colored tape.",
            "Decorate outer surface with folk stickers.",
            "Play along to classical taals (Teental, Keherwa)."
        ],
        "learning": "Rhythm perception, acoustic frequency variation, and percussion."
    },
    {
        "id": 37,
        "title": "Multi-Script Indic Calligraphy",
        "category": "art",
        "age": "Youth & Parents",
        "duration": "25 mins",
        "desc": "Master basic strokes of Devanagari, Tamil, and Gurmukhi script calligraphic letterforms.",
        "materials": ["Chisel tip calligraphy marker", "Grid guide sheets"],
        "steps": [
            "Hold chisel nib at fixed 45-degree angle.",
            "Practice core vertical stroke, Shirorekha (top line), and loops.",
            "Write family names in authentic traditional calligraphy styles."
        ],
        "learning": "Linguistic calligraphy, fine motor control, and orthography."
    },
    {
        "id": 38,
        "title": "Raga & Emotion Expressive Painting",
        "category": "art",
        "age": "6-8",
        "duration": "30 mins",
        "desc": "Listen to classical Indian ragas and paint abstract colors corresponding to the Rasa (emotion).",
        "materials": ["Raga music tracks (Bhairavi, Megh, Darbari)", "Paints", "Large paper"],
        "steps": [
            "Play morning/evening raga track on speakers.",
            "Discuss mood evoke (e.g. Raga Megh = rain & joy, Raga Darbari = majestic calm).",
            "Paint fluid abstract shapes and colors matching rhythm tempo."
        ],
        "learning": "Cross-modal sensory association, classical music appreciation, and art."
    },
    {
        "id": 39,
        "title": "Joint-Family 4-Panel Comic Strip",
        "category": "art",
        "age": "9-10",
        "duration": "35 mins",
        "desc": "Illustrate funny household moments featuring family members as comic superheroes.",
        "materials": ["A4 paper split in 4 panels", "Pens", "Colors"],
        "steps": [
            "Brainstorm a humorous household incident (e.g., searching for missing TV remote).",
            "Characterize family members with signature superhero capes/quirks.",
            "Draft dialogue speech bubbles and draw 4 sequential scenes."
        ],
        "learning": "Visual sequencing, humor, dialogue writing, and character design."
    },
    {
        "id": 40,
        "title": "Heritage Currency Collector Quest",
        "category": "art",
        "age": "Youth & Parents",
        "duration": "25 mins",
        "desc": "Explore historical Indian coins and currency notes to decode historical motifs and languages.",
        "materials": ["Collection of coins/notes", "Magnifying glass", "Notebook"],
        "steps": [
            "Examine 15 official regional language translations on Indian Rupee notes.",
            "Identify heritage monuments printed on notes (Rani ki Vav, Hampi, Sanchi Stupa).",
            "Create a mini heritage guide cataloging coin metals and symbols."
        ],
        "learning": "Numismatics, Indian history, geography, and multi-linguism."
    },

    # 5. Family Fitness, Mindfulness & Culture
    {
        "id": 41,
        "title": "Surya Namaskar Form Master",
        "category": "fitness",
        "age": "3-5",
        "duration": "15 mins",
        "desc": "Gamified 12-pose Yoga sequence timing posture alignment and synchronized breathing.",
        "materials": ["Yoga mat", "12-pose visual reference poster"],
        "steps": [
            "Flow through 12 poses (Pranamasana to Parvatasana).",
            "Hold each posture for 5 deep belly breaths.",
            "Perform 3 full rounds together as morning energizer."
        ],
        "learning": "Flexibility, body awareness, and breath control."
    },
    {
        "id": 42,
        "title": "Pitthu (Lagori) Physics & Agility",
        "category": "fitness",
        "age": "6-8",
        "duration": "30 mins",
        "desc": "Play traditional 7-stone stack game balancing throwing precision and team evasion.",
        "materials": ["7 flat stones/plastic tiles", "Soft sponge ball"],
        "steps": [
            "Stack 7 stones in center circle.",
            "Striker throws ball from distance to knock down stack.",
            "Seekers try to restack stones while avoiding getting tagged by soft ball."
        ],
        "learning": "Hand-eye coordination, team tactics, and physical agility."
    },
    {
        "id": 43,
        "title": "Bharat Quest Family Quiz Night",
        "category": "fitness",
        "age": "Youth & Parents",
        "duration": "40 mins",
        "desc": "Intergenerational trivia challenge covering Indian space achievements, sports, and geography.",
        "materials": ["Quiz cards", "Buzzer bell", "Scoreboard"],
        "steps": [
            "Form mixed teams (Kid + Parent/Grandparent).",
            "Ask questions across 4 rounds: History, Science/ISRO, Culture, Sports.",
            "Award 'Bharat Ratna' trophy card to winning team."
        ],
        "learning": "General knowledge, family bonding, and fast recall."
    },
    {
        "id": 44,
        "title": "Zero-Waste Kitchen Recipe Chef",
        "category": "fitness",
        "age": "9-10",
        "duration": "40 mins",
        "desc": "Cook delicious traditional snacks using leftover ingredients and vegetable peels.",
        "materials": ["Lauki peels or stale roti", "Spices", "Cooking utensils"],
        "steps": [
            "Prepare 'Chhatpata Lauki Chilka Subzi' or 'Roti Chivda' using kitchen leftovers.",
            "Learn nutritional benefits of fiber-rich vegetable peels.",
            "Calculate food waste saved from garbage bin."
        ],
        "learning": "Culinary skills, zero-waste lifestyle, and nutrition."
    },
    {
        "id": 45,
        "title": "Anulom-Vilom Breath Pacer",
        "category": "fitness",
        "age": "3-5",
        "duration": "10 mins",
        "desc": "Guided alternate-nostril Pranayama exercise using visualization for calm and focus.",
        "materials": ["Quiet seating space", "Visual breathing pacing circle"],
        "steps": [
            "Sit in Sukhasana with spine straight.",
            "Close right nostril with thumb, inhale deeply through left nostril for 4 counts.",
            "Close left nostril, exhale through right nostril for 4 counts.",
            "Repeat cycle for 10 rounds before homework or bedtime."
        ],
        "learning": "Stress reduction, lung capacity, and emotional self-regulation."
    },
    {
        "id": 46,
        "title": "Desi Spelling Bee Sprint",
        "category": "fitness",
        "age": "6-8",
        "duration": "20 mins",
        "desc": "Fast-paced spelling bee focused on Indian English loanwords (e.g., Bungalow, Avatar, Juggernaut).",
        "materials": ["Word list cards", "Timer"],
        "steps": [
            "Draw word card and state origin history.",
            "Spell word aloud under 15 seconds.",
            "Use word in an original sentence."
        ],
        "learning": "Etymology, vocabulary expansion, and public speaking confidence."
    },
    {
        "id": 47,
        "title": "State River Map Puzzle Master",
        "category": "fitness",
        "age": "9-10",
        "duration": "25 mins",
        "desc": "Map major Indian river systems (Ganga, Indus, Godavari, Narmada) to origin states.",
        "materials": ["Blank outline map of India", "Blue markers", "State labels"],
        "steps": [
            "Trace river paths from Himalayas or Western Ghats to the oceans.",
            "Identify major dams and state capitals along river banks.",
            "Quiz team members on east-flowing vs west-flowing rivers."
        ],
        "learning": "Indian geography, hydrology, and spatial mapping."
    },
    {
        "id": 48,
        "title": "Dada-Dadi Oral History Interview",
        "category": "fitness",
        "age": "Youth & Parents",
        "duration": "30 mins",
        "desc": "Kids interview grandparents to record audio/video stories of childhood in early India.",
        "materials": ["Phone voice recorder", "List of 5 interview questions"],
        "steps": [
            "Prepare questions (e.g., 'What was your favorite childhood game?', 'How did you spend summer holidays?').",
            "Conduct structured audio recording interview.",
            "Archive recording in family digital memory album."
        ],
        "learning": "Oral history preservation, active listening, and intergenerational empathy."
    },
    {
        "id": 49,
        "title": "Rapid-Fire Desi Charades",
        "category": "fitness",
        "age": "3-5",
        "duration": "20 mins",
        "desc": "Act out famous historical figures, Panchatantra animals, or Indian proverbs without speaking.",
        "materials": ["Prompt cards", "Timer"],
        "steps": [
            "Player picks a card (e.g. Maharana Pratap, Clever Crow, Thali).",
            "Act out clue using gestures only.",
            "Team guesses item within 45 seconds."
        ],
        "learning": "Non-verbal communication, body language, and dramatic expression."
    },
    {
        "id": 50,
        "title": "Neighborhood Eco-Bingo Safari",
        "category": "fitness",
        "age": "3-5",
        "duration": "40 mins",
        "desc": "Outdoor walking bingo identifying local trees (Neem, Peepal, Banyan) and native birds.",
        "materials": ["Bingo grid card", "Pencil", "Magnifying glass"],
        "steps": [
            "Walk in local park or neighborhood.",
            "Check off grid boxes upon spotting Neem leaf, Myna bird, Earthworm cast, etc.",
            "First to complete row shouts 'BINGO!' and explains one plant benefit."
        ],
        "learning": "Local biodiversity awareness, observation skills, and outdoor movement."
    }
]

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Khel-Gyan | India Play & Learn Hub for Kids, Parents & Youth</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Rozha+One&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        'saffron': '#FF9933',
                        'saffron-dark': '#E68019',
                        'india-green': '#138808',
                        'india-green-dark': '#0F6B06',
                        'navy-blue': '#000080',
                        'warm-cream': '#FDFBF7',
                        'card-bg': '#FFFFFF'
                    }},
                    fontFamily: {{
                        'outfit': ['Outfit', 'sans-serif'],
                        'rozha': ['Rozha One', 'serif']
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{
            font-family: 'Outfit', sans-serif;
            background-color: #F8F9FA;
            color: #2D3748;
        }}
        .hero-gradient {{
            background: linear-gradient(135deg, #FFF4E6 0%, #E6F4EA 100%);
        }}
        .gullak-card {{
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        .gullak-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 24px -10px rgba(0,0,0,0.15);
        }}
        /* Custom Scrollbar */
        ::-webkit-scrollbar {{
            width: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: #F1F1F1;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #FF9933;
            border-radius: 4px;
        }}
        /* Wheel Animation */
        @keyframes spinSlow {{
            from {{ transform: rotate(0deg); }}
            to {{ transform: rotate(360deg); }}
        }}
        .spinning {{
            animation: spinSlow 0.5s linear infinite;
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col">

    <!-- Top Announcement Bar -->
    <div class="bg-navy-blue text-white text-xs md:text-sm text-center py-2 px-4 flex justify-between items-center">
        <div class="container mx-auto flex justify-between items-center">
            <span><i class="fa-solid fa-flag text-saffron mr-2"></i> 100% Free Open-Access Platform for Indian Families & Schools</span>
            <a href="#deploy-guide" class="underline hover:text-saffron transition font-medium text-xs">Deploy Free on GitHub / Vercel <i class="fa-solid fa-arrow-right ml-1"></i></a>
        </div>
    </div>

    <!-- Navigation Bar -->
    <nav class="bg-white border-b border-gray-200 sticky top-0 z-40 shadow-sm">
        <div class="container mx-auto px-4 py-3 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-full bg-saffron text-white flex items-center justify-center font-bold text-xl shadow-md">
                    <i class="fa-solid fa-coins"></i>
                </div>
                <div>
                    <h1 class="font-rozha text-2xl text-navy-blue leading-none">खेल-GYAN</h1>
                    <p class="text-[10px] text-gray-500 font-bold uppercase tracking-widest">India Play & Learn Hub</p>
                </div>
            </div>
            
            <div class="hidden md:flex items-center space-x-6 font-medium text-sm text-gray-700">
                <a href="#gullak-tool" class="hover:text-saffron transition"><i class="fa-solid fa-jar text-saffron mr-1"></i> 3-Gullak Allocator</a>
                <a href="#wheel-section" class="hover:text-saffron transition"><i class="fa-solid fa-dharmachakra text-navy-blue mr-1"></i> Daily Wheel</a>
                <a href="#activities-directory" class="hover:text-saffron transition"><i class="fa-solid fa-cubes text-india-green mr-1"></i> 50 Activities</a>
                <a href="#deploy-guide" class="hover:text-saffron transition"><i class="fa-solid fa-rocket mr-1"></i> Free Deployment</a>
            </div>

            <a href="#gullak-tool" class="bg-saffron hover:bg-saffron-dark text-white px-4 py-2 rounded-xl text-sm font-bold shadow transition flex items-center">
                <i class="fa-solid fa-calculator mr-2"></i> Try Gullak Tool
            </a>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-gradient py-12 px-4 border-b border-orange-100">
        <div class="container mx-auto max-w-5xl text-center">
            <span class="bg-orange-100 text-saffron-dark px-3.5 py-1 rounded-full text-xs font-bold tracking-wide uppercase inline-block mb-3">
                <i class="fa-solid fa-sparkles mr-1"></i> Financial Literacy & STEM for Indian Kids
            </span>
            <h2 class="text-3xl md:text-5xl font-extrabold text-navy-blue mb-4 leading-tight">
                Empowering Young Minds with <span class="text-saffron">Desi Intelligence</span> & Fun
            </h2>
            <p class="text-gray-600 text-base md:text-lg max-w-2xl mx-auto mb-8">
                From the 3-Gullak Money Allocator to Vedic Math, Indic STEM, and Heritage Arts — discover 50 interactive, screen-light activities designed for kids (ages 3-10), parents, and youth.
            </p>

            <!-- Quick Stats -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-3xl mx-auto bg-white p-4 rounded-2xl shadow-sm border border-gray-100 mb-8">
                <div class="border-r border-gray-100 last:border-0">
                    <div class="text-2xl font-black text-saffron">50+</div>
                    <div class="text-xs text-gray-500 font-medium">Free Activities</div>
                </div>
                <div class="border-r border-gray-100 last:border-0">
                    <div class="text-2xl font-black text-india-green">₹ INR</div>
                    <div class="text-xs text-gray-500 font-medium">3-Gullak System</div>
                </div>
                <div class="border-r border-gray-100 last:border-0">
                    <div class="text-2xl font-black text-navy-blue">Ages 3-10</div>
                    <div class="text-xs text-gray-500 font-medium">& Youth / Parents</div>
                </div>
                <div>
                    <div class="text-2xl font-black text-purple-600">100%</div>
                    <div class="text-xs text-gray-500 font-medium">Screen-Light & Free</div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 1: Interactive 3-Gullak Money Allocator Tool -->
    <section id="gullak-tool" class="py-12 bg-white border-b border-gray-200">
        <div class="container mx-auto px-4 max-w-5xl">
            <div class="text-center mb-8">
                <span class="bg-green-100 text-india-green-dark px-3 py-1 rounded-full text-xs font-bold tracking-wide uppercase">
                    Interactive Financial Tool
                </span>
                <h2 class="text-2xl md:text-4xl font-extrabold text-navy-blue mt-2">
                    <i class="fa-solid fa-jar text-saffron mr-2"></i> Interactive 3-Gullak Pocket Money Allocator
                </h2>
                <p class="text-gray-600 text-sm md:text-base max-w-xl mx-auto mt-1">
                    Teach money management using traditional Indian Gullaks (Kharacha, Bachat, and Daan).
                </p>
            </div>

            <div class="bg-warm-cream border-2 border-orange-200 rounded-3xl p-6 md:p-8 shadow-sm">
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                    
                    <!-- Controls Left Panel -->
                    <div class="lg:col-span-5 bg-white p-6 rounded-2xl border border-orange-100 shadow-sm space-y-5">
                        <h3 class="font-bold text-navy-blue text-lg border-b pb-2 flex items-center">
                            <i class="fa-solid fa-sliders text-saffron mr-2"></i> Customize Settings
                        </h3>

                        <!-- Allowance Slider -->
                        <div>
                            <div class="flex justify-between text-sm font-bold text-gray-700 mb-1">
                                <span>Weekly Money (₹)</span>
                                <span class="text-saffron font-black text-base" id="allowance-display">₹100</span>
                            </div>
                            <input type="range" id="allowance-slider" min="20" max="1000" step="10" value="100" 
                                   class="w-full accent-saffron h-2 bg-gray-200 rounded-lg cursor-pointer">
                            <div class="flex justify-between text-[11px] text-gray-400 mt-1">
                                <span>₹20</span>
                                <span>₹500</span>
                                <span>₹1,000</span>
                            </div>
                        </div>

                        <!-- Age Group Selection -->
                        <div>
                            <label class="block text-sm font-bold text-gray-700 mb-1">Child Age Group</label>
                            <select id="age-selector" class="w-full bg-gray-50 border border-gray-300 text-gray-800 text-sm rounded-xl p-2.5 font-medium focus:ring-saffron focus:border-saffron">
                                <option value="3-5">Ages 3–5 (Tactile & Coins)</option>
                                <option value="6-8" selected>Ages 6–8 (Goal Savings & Interest)</option>
                                <option value="9-10">Ages 9–10 (Budgeting & Cards)</option>
                            </select>
                        </div>

                        <!-- Split Preset Buttons -->
                        <div>
                            <label class="block text-sm font-bold text-gray-700 mb-1">Allocation Strategy</label>
                            <div class="grid grid-cols-3 gap-2">
                                <button onclick="setPreset(60, 30, 10)" id="preset-std" class="preset-btn bg-saffron text-white py-2 px-2 rounded-xl text-xs font-bold transition text-center shadow-sm">
                                    Standard<br><span class="text-[10px] font-normal">60 / 30 / 10</span>
                                </button>
                                <button onclick="setPreset(34, 33, 33)" id="preset-eq" class="preset-btn bg-gray-100 hover:bg-gray-200 text-gray-700 py-2 px-2 rounded-xl text-xs font-bold transition text-center">
                                    Equal<br><span class="text-[10px] font-normal">34 / 33 / 33</span>
                                </button>
                                <button onclick="setPreset(40, 50, 10)" id="preset-sav" class="preset-btn bg-gray-100 hover:bg-gray-200 text-gray-700 py-2 px-2 rounded-xl text-xs font-bold transition text-center">
                                    Super Saver<br><span class="text-[10px] font-normal">40 / 50 / 10</span>
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Visual Jars Right Panel -->
                    <div class="lg:col-span-7 space-y-4">
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                            
                            <!-- Spend Gullak -->
                            <div class="gullak-card bg-white p-5 rounded-2xl border border-red-100 shadow-sm text-center relative overflow-hidden">
                                <div class="w-12 h-12 rounded-full bg-red-100 text-red-600 flex items-center justify-center mx-auto mb-2 text-xl font-bold">
                                    <i class="fa-solid fa-bag-shopping"></i>
                                </div>
                                <h4 class="font-black text-gray-800 text-base">Kharacha (Spend)</h4>
                                <span class="text-xs font-bold text-red-500 bg-red-50 px-2 py-0.5 rounded-full inline-block mb-2" id="spend-pct">60%</span>
                                <div class="text-2xl font-black text-gray-900 mb-1" id="spend-amount">₹60.00</div>
                                <p class="text-[11px] text-gray-500 leading-tight">Instant treats, stickers, local market snacks, or small stationery.</p>
                            </div>

                            <!-- Save Gullak -->
                            <div class="gullak-card bg-white p-5 rounded-2xl border border-green-100 shadow-sm text-center relative overflow-hidden">
                                <div class="w-12 h-12 rounded-full bg-green-100 text-india-green flex items-center justify-center mx-auto mb-2 text-xl font-bold">
                                    <i class="fa-solid fa-piggy-bank"></i>
                                </div>
                                <h4 class="font-black text-gray-800 text-base">Bachat (Save)</h4>
                                <span class="text-xs font-bold text-india-green bg-green-50 px-2 py-0.5 rounded-full inline-block mb-2" id="save-pct">30%</span>
                                <div class="text-2xl font-black text-gray-900 mb-1" id="save-amount">₹30.00</div>
                                <p class="text-[11px] text-gray-500 leading-tight">Diwali/Rakhi festive lifafas saved for big targets (sports gear, books).</p>
                            </div>

                            <!-- Give Gullak -->
                            <div class="gullak-card bg-white p-5 rounded-2xl border border-blue-100 shadow-sm text-center relative overflow-hidden">
                                <div class="w-12 h-12 rounded-full bg-blue-100 text-navy-blue flex items-center justify-center mx-auto mb-2 text-xl font-bold">
                                    <i class="fa-solid fa-hand-holding-heart"></i>
                                </div>
                                <h4 class="font-black text-gray-800 text-base">Daan (Give)</h4>
                                <span class="text-xs font-bold text-navy-blue bg-blue-50 px-2 py-0.5 rounded-full inline-block mb-2" id="give-pct">10%</span>
                                <div class="text-2xl font-black text-gray-900 mb-1" id="give-amount">₹10.00</div>
                                <p class="text-[11px] text-gray-500 leading-tight">Temple Hundi, feeding strays, or buying treats for helpers.</p>
                            </div>

                        </div>

                        <!-- Dynamic Tip Box -->
                        <div class="bg-amber-50 border border-amber-200 p-4 rounded-2xl flex items-start space-x-3">
                            <i class="fa-solid fa-lightbulb text-saffron text-xl mt-0.5"></i>
                            <div>
                                <h5 class="font-bold text-gray-800 text-xs uppercase tracking-wide">Parent Parenting Tip (<span id="tip-age-label">Ages 6-8</span>)</h5>
                                <p class="text-xs text-gray-600 mt-0.5" id="parent-tip">
                                    Introduce a "Parent Match" (e.g. adding ₹10 for every ₹100 kept in the Bachat Gullak for a full month) to teach the concept of earning interest!
                                </p>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 2: Daily Challenge Random Generator -->
    <section id="wheel-section" class="py-12 bg-gray-50 border-b border-gray-200">
        <div class="container mx-auto px-4 max-w-4xl text-center">
            <span class="bg-purple-100 text-purple-700 px-3 py-1 rounded-full text-xs font-bold tracking-wide uppercase">
                Gamified Daily Discovery
            </span>
            <h2 class="text-2xl md:text-3xl font-extrabold text-navy-blue mt-2 mb-2">
                <i class="fa-solid fa-dharmachakra text-navy-blue mr-2"></i> Daily Activity Picker
            </h2>
            <p class="text-gray-600 text-sm max-w-lg mx-auto mb-6">
                Can't decide which activity to do today? Click the wheel to generate a fun, hands-on task!
            </p>

            <div class="bg-white p-6 md:p-8 rounded-3xl border border-gray-200 shadow-sm max-w-xl mx-auto text-center space-y-5">
                <div class="w-24 h-24 mx-auto rounded-full bg-orange-50 border-4 border-saffron flex items-center justify-center text-saffron text-4xl shadow-inner" id="wheel-icon">
                    <i class="fa-solid fa-dice text-saffron"></i>
                </div>
                
                <div id="selected-activity-display">
                    <h3 class="font-bold text-xl text-navy-blue" id="random-title">Ready to Spin?</h3>
                    <p class="text-xs text-gray-500 mt-1" id="random-desc">Click below to pick a random activity from our catalog of 50!</p>
                </div>

                <div class="flex justify-center space-x-3">
                    <button onclick="spinWheel()" id="spin-btn" class="bg-saffron hover:bg-saffron-dark text-white px-6 py-3 rounded-2xl font-extrabold text-sm shadow-md transition flex items-center">
                        <i class="fa-solid fa-rotate mr-2"></i> Pick Random Activity
                    </button>
                    <button onclick="openModalFromRandom()" id="view-random-btn" class="hidden bg-navy-blue hover:bg-blue-900 text-white px-5 py-3 rounded-2xl font-bold text-sm shadow-md transition">
                        View Details <i class="fa-solid fa-arrow-right ml-1"></i>
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 3: 50 Interactive Activities Directory -->
    <section id="activities-directory" class="py-12 bg-white flex-grow">
        <div class="container mx-auto px-4 max-w-6xl">
            <div class="text-center mb-8">
                <span class="bg-blue-100 text-navy-blue px-3 py-1 rounded-full text-xs font-bold tracking-wide uppercase">
                    Full Learning Catalog
                </span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-navy-blue mt-2">
                    50 Educational & Addictive Activities
                </h2>
                <p class="text-gray-600 text-sm max-w-xl mx-auto mt-1">
                    Filter by category or age group to find screen-light activities for home, school, or weekends.
                </p>
            </div>

            <!-- Filter Controls -->
            <div class="bg-warm-cream p-4 rounded-2xl border border-gray-200 mb-8 space-y-4">
                <div class="grid grid-cols-1 md:grid-cols-12 gap-3">
                    <!-- Search Input -->
                    <div class="md:col-span-6 relative">
                        <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-3 text-gray-400 text-sm"></i>
                        <input type="text" id="search-input" onkeyup="filterActivities()" placeholder="Search activities (e.g., Gullak, Vedic Math, Solar)..." 
                               class="w-full pl-10 pr-4 py-2.5 bg-white border border-gray-300 rounded-xl text-sm font-medium focus:ring-saffron focus:border-saffron">
                    </div>

                    <!-- Category Filter -->
                    <div class="md:col-span-3">
                        <select id="category-filter" onchange="filterActivities()" class="w-full bg-white border border-gray-300 text-gray-800 text-sm rounded-xl py-2.5 px-3 font-medium focus:ring-saffron focus:border-saffron">
                            <option value="all">All Categories (50)</option>
                            <option value="finance">💰 Financial Literacy (10)</option>
                            <option value="math">🧠 Vedic Math & Logic (10)</option>
                            <option value="stem">🔬 Indic Science & STEM (10)</option>
                            <option value="art">🎨 Arts & Heritage (10)</option>
                            <option value="fitness">🧘 Fitness & Culture (10)</option>
                        </select>
                    </div>

                    <!-- Age Filter -->
                    <div class="md:col-span-3">
                        <select id="age-filter" onchange="filterActivities()" class="w-full bg-white border border-gray-300 text-gray-800 text-sm rounded-xl py-2.5 px-3 font-medium focus:ring-saffron focus:border-saffron">
                            <option value="all">All Age Groups</option>
                            <option value="3-5">Ages 3–5</option>
                            <option value="6-8">Ages 6–8</option>
                            <option value="9-10">Ages 9–10</option>
                            <option value="Youth & Parents">Youth & Parents</option>
                        </select>
                    </div>
                </div>

                <!-- Category Pills -->
                <div class="flex flex-wrap gap-2 pt-1 border-t border-gray-200">
                    <button onclick="setCategoryPill('all')" class="cat-pill px-3 py-1 bg-navy-blue text-white rounded-lg text-xs font-bold transition">All</button>
                    <button onclick="setCategoryPill('finance')" class="cat-pill px-3 py-1 bg-white hover:bg-gray-100 text-gray-700 rounded-lg text-xs font-bold transition">💰 Financial Literacy</button>
                    <button onclick="setCategoryPill('math')" class="cat-pill px-3 py-1 bg-white hover:bg-gray-100 text-gray-700 rounded-lg text-xs font-bold transition">🧠 Vedic Math & Logic</button>
                    <button onclick="setCategoryPill('stem')" class="cat-pill px-3 py-1 bg-white hover:bg-gray-100 text-gray-700 rounded-lg text-xs font-bold transition">🔬 Indic STEM</button>
                    <button onclick="setCategoryPill('art')" class="cat-pill px-3 py-1 bg-white hover:bg-gray-100 text-gray-700 rounded-lg text-xs font-bold transition">🎨 Arts & Heritage</button>
                    <button onclick="setCategoryPill('fitness')" class="cat-pill px-3 py-1 bg-white hover:bg-gray-100 text-gray-700 rounded-lg text-xs font-bold transition">🧘 Fitness & Culture</button>
                </div>
            </div>

            <!-- Activity Cards Grid -->
            <div id="activities-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Dynamically Populated by JS -->
            </div>

            <div id="no-results" class="hidden text-center py-12">
                <i class="fa-solid fa-face-meh text-4xl text-gray-300 mb-3"></i>
                <h4 class="font-bold text-gray-600">No matching activities found</h4>
                <p class="text-xs text-gray-400">Try adjusting your search terms or filter drop-downs.</p>
            </div>
        </div>
    </section>

    <!-- SECTION 4: Free Deployment Guide for Parents/Schools -->
    <section id="deploy-guide" class="py-12 bg-gray-900 text-white border-t border-gray-800">
        <div class="container mx-auto px-4 max-w-4xl">
            <div class="text-center mb-8">
                <span class="bg-saffron text-white px-3 py-1 rounded-full text-xs font-bold tracking-wide uppercase">
                    Free Web Hosting Guide
                </span>
                <h2 class="text-2xl md:text-3xl font-extrabold text-white mt-2">
                    How to Host This Website for Free
                </h2>
                <p class="text-gray-400 text-sm max-w-xl mx-auto mt-1">
                    Deploy this standalone web app onto GitHub Pages or Vercel with zero hosting costs.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                
                <!-- Option A: GitHub Pages -->
                <div class="bg-gray-800 border border-gray-700 p-6 rounded-2xl space-y-3">
                    <div class="flex items-center space-x-3">
                        <i class="fa-brands fa-github text-3xl text-saffron"></i>
                        <div>
                            <h3 class="font-bold text-lg text-white">GitHub Pages (Free)</h3>
                            <p class="text-xs text-gray-400">Best for lifelong hosting & custom subdomains</p>
                        </div>
                    </div>
                    <ol class="list-decimal list-inside text-xs text-gray-300 space-y-2 pt-2 border-t border-gray-700">
                        <li>Create a free account on <code class="bg-gray-900 px-1 py-0.5 rounded text-saffron">github.com</code>.</li>
                        <li>Create a new public repository named <code class="bg-gray-900 px-1 py-0.5 rounded text-saffron">khel-gyan</code>.</li>
                        <li>Upload this <code class="bg-gray-900 px-1 py-0.5 rounded text-saffron">index.html</code> file to the repository.</li>
                        <li>Go to <strong>Settings &gt; Pages</strong> and select main branch.</li>
                        <li>Your app is instantly live at <code class="bg-gray-900 px-1 py-0.5 rounded text-green-400">yourname.github.io/khel-gyan</code>!</li>
                    </ol>
                </div>

                <!-- Option B: Vercel -->
                <div class="bg-gray-800 border border-gray-700 p-6 rounded-2xl space-y-3">
                    <div class="flex items-center space-x-3">
                        <i class="fa-solid fa-triangle-circle-square text-3xl text-india-green"></i>
                        <div>
                            <h3 class="font-bold text-lg text-white">Vercel / Netlify (Free)</h3>
                            <p class="text-xs text-gray-400">1-Click Drag & Drop hosting</p>
                        </div>
                    </div>
                    <ol class="list-decimal list-inside text-xs text-gray-300 space-y-2 pt-2 border-t border-gray-700">
                        <li>Go to <code class="bg-gray-900 px-1 py-0.5 rounded text-saffron">vercel.com</code> or <code class="bg-gray-900 px-1 py-0.5 rounded text-saffron">netlify.com</code>.</li>
                        <li>Sign up for a free Hobby account.</li>
                        <li>Drag & drop the folder containing <code class="bg-gray-900 px-1 py-0.5 rounded text-saffron">index.html</code>.</li>
                        <li>Vercel instantly deploys and provides an SSL-secured link (<code class="bg-gray-900 px-1 py-0.5 rounded text-green-400">khel-gyan.vercel.app</code>).</li>
                    </ol>
                </div>

            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-navy-blue text-gray-400 text-xs py-6 border-t border-blue-900 text-center">
        <div class="container mx-auto px-4">
            <p class="font-bold text-white mb-1">Khel-Gyan India Play & Learn Hub</p>
            <p>Designed for Indian Parents, Educators, and Kids. Built with open-web standards.</p>
        </div>
    </footer>

    <!-- Activity Detail Modal Popup -->
    <div id="activity-modal" class="fixed inset-0 bg-black/60 z-50 flex items-center justify-center p-4 hidden backdrop-blur-sm">
        <div class="bg-white rounded-3xl max-w-2xl w-full max-h-[90vh] overflow-y-auto p-6 md:p-8 relative shadow-2xl">
            <button onclick="closeModal()" class="absolute top-5 right-5 w-9 h-9 bg-gray-100 hover:bg-gray-200 text-gray-600 rounded-full flex items-center justify-center transition">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>

            <div class="flex items-center space-x-2 mb-2">
                <span id="modal-cat" class="bg-orange-100 text-saffron-dark text-[11px] font-bold px-3 py-0.5 rounded-full uppercase">Category</span>
                <span id="modal-age" class="bg-blue-100 text-navy-blue text-[11px] font-bold px-3 py-0.5 rounded-full">Age</span>
                <span id="modal-duration" class="bg-gray-100 text-gray-600 text-[11px] font-bold px-3 py-0.5 rounded-full"><i class="fa-regular fa-clock mr-1"></i> 20 mins</span>
            </div>

            <h3 id="modal-title" class="text-2xl font-extrabold text-navy-blue mb-3">Activity Title</h3>
            <p id="modal-desc" class="text-sm text-gray-600 mb-6 leading-relaxed">Activity description text goes here...</p>

            <!-- Required Materials -->
            <div class="bg-warm-cream p-4 rounded-2xl border border-orange-100 mb-6">
                <h4 class="font-bold text-xs text-navy-blue uppercase tracking-wider mb-2 flex items-center">
                    <i class="fa-solid fa-box text-saffron mr-2"></i> Required Materials
                </h4>
                <ul id="modal-materials" class="list-disc list-inside text-xs text-gray-700 space-y-1">
                    <!-- Materials dynamically added -->
                </ul>
            </div>

            <!-- Step-by-Step Instructions -->
            <div class="mb-6">
                <h4 class="font-bold text-xs text-navy-blue uppercase tracking-wider mb-3 flex items-center">
                    <i class="fa-solid fa-list-check text-india-green mr-2"></i> Step-by-Step Guide
                </h4>
                <ol id="modal-steps" class="space-y-3 text-xs text-gray-700">
                    <!-- Steps dynamically added -->
                </ol>
            </div>

            <!-- Learning Outcome -->
            <div class="bg-green-50 p-4 rounded-2xl border border-green-200 flex items-start space-x-3">
                <i class="fa-solid fa-graduation-cap text-india-green text-xl mt-0.5"></i>
                <div>
                    <h5 class="font-bold text-xs text-india-green-dark uppercase tracking-wide">Key Learning Outcome</h5>
                    <p id="modal-learning" class="text-xs text-gray-700 mt-0.5">Outcome statement...</p>
                </div>
            </div>
        </div>
    </div>

    <!-- JavaScript Application Logic -->
    <script>
        // Load dataset from python generated JSON
        const activitiesData = {json.dumps(activities)};

        let activeRandomId = null;

        // Category icons mapping
        const categoryIcons = {{
            'finance': 'fa-solid fa-coins text-saffron',
            'math': 'fa-solid fa-brain text-purple-600',
            'stem': 'fa-solid fa-flask text-india-green',
            'art': 'fa-solid fa-palette text-pink-500',
            'fitness': 'fa-solid fa-heart-pulse text-red-500'
        }};

        const categoryNames = {{
            'finance': 'Financial Literacy',
            'math': 'Vedic Math & Logic',
            'stem': 'Indic STEM',
            'art': 'Arts & Heritage',
            'fitness': 'Fitness & Culture'
        }};

        // Render Cards
        function renderActivities(list) {{
            const grid = document.getElementById('activities-grid');
            const noRes = document.getElementById('no-results');
            grid.innerHTML = '';

            if (list.length === 0) {{
                noRes.classList.remove('hidden');
                return;
            }} else {{
                noRes.classList.add('hidden');
            }}

            list.forEach(act => {{
                const card = document.createElement('div');
                card.className = "bg-white p-5 rounded-2xl border border-gray-200 shadow-sm hover:shadow-md transition flex flex-col justify-between";
                card.innerHTML = `
                    <div>
                        <div class="flex justify-between items-start mb-3">
                            <span class="text-xs font-bold px-2.5 py-1 rounded-lg bg-gray-100 text-gray-700 flex items-center">
                                <i class="${{categoryIcons[act.category]}} mr-1.5"></i> ${{categoryNames[act.category]}}
                            </span>
                            <span class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-blue-50 text-navy-blue">
                                Age ${{act.age}}
                            </span>
                        </div>
                        <h3 class="font-bold text-base text-navy-blue mb-1.5 line-clamp-1">${{act.title}}</h3>
                        <p class="text-xs text-gray-500 leading-relaxed mb-4 line-clamp-2">${{act.desc}}</p>
                    </div>
                    <div class="pt-3 border-t border-gray-100 flex justify-between items-center">
                        <span class="text-[11px] font-medium text-gray-400">
                            <i class="fa-regular fa-clock mr-1"></i> ${{act.duration}}
                        </span>
                        <button onclick="openModal(${{act.id}})" class="bg-saffron hover:bg-saffron-dark text-white px-3 py-1.5 rounded-xl text-xs font-bold transition">
                            View Guide <i class="fa-solid fa-chevron-right ml-1 text-[10px]"></i>
                        </button>
                    </div>
                `;
                grid.appendChild(card);
            }});
        }}

        // Search & Filter Logic
        function filterActivities() {{
            const searchVal = document.getElementById('search-input').value.toLowerCase();
            const catVal = document.getElementById('category-filter').value;
            const ageVal = document.getElementById('age-filter').value;

            const filtered = activitiesData.filter(act => {{
                const matchesSearch = act.title.toLowerCase().includes(searchVal) || 
                                      act.desc.toLowerCase().includes(searchVal) ||
                                      act.learning.toLowerCase().includes(searchVal);
                const matchesCat = (catVal === 'all') || (act.category === catVal);
                const matchesAge = (ageVal === 'all') || (act.age === ageVal);

                return matchesSearch && matchesCat && matchesAge;
            }});

            renderActivities(filtered);
        }}

        function setCategoryPill(cat) {{
            document.getElementById('category-filter').value = cat;
            // Highlight active button style
            const buttons = document.querySelectorAll('.cat-pill');
            buttons.forEach(btn => {{
                btn.className = "cat-pill px-3 py-1 bg-white text-gray-700 rounded-lg text-xs font-bold transition";
            }});
            event.target.className = "cat-pill px-3 py-1 bg-navy-blue text-white rounded-lg text-xs font-bold transition";
            filterActivities();
        }}

        // Modal Handler
        function openModal(id) {{
            const act = activitiesData.find(a => a.id === id);
            if (!act) return;

            document.getElementById('modal-title').innerText = act.title;
            document.getElementById('modal-cat').innerText = categoryNames[act.category];
            document.getElementById('modal-age').innerText = `Age ${{act.age}}`;
            document.getElementById('modal-duration').innerHTML = `<i class="fa-regular fa-clock mr-1"></i> ${{act.duration}}`;
            document.getElementById('modal-desc').innerText = act.desc;
            document.getElementById('modal-learning').innerText = act.learning;

            // Materials list
            const matList = document.getElementById('modal-materials');
            matList.innerHTML = act.materials.map(m => `<li>${{m}}</li>`).join('');

            // Steps list
            const stepList = document.getElementById('modal-steps');
            stepList.innerHTML = act.steps.map((s, idx) => `
                <li class="flex items-start space-x-2">
                    <span class="w-5 h-5 rounded-full bg-saffron text-white text-[10px] font-bold flex items-center justify-center shrink-0 mt-0.5">${{idx + 1}}</span>
                    <span>${{s}}</span>
                </li>
            `).join('');

            document.getElementById('activity-modal').classList.remove('hidden');
        }}

        function closeModal() {{
            document.getElementById('activity-modal').classList.add('hidden');
        }}

        // 3-Gullak Interactive Calculator Logic
        const slider = document.getElementById('allowance-slider');
        const allowanceDisplay = document.getElementById('allowance-display');
        const ageSelector = document.getElementById('age-selector');
        
        let currentSpendPct = 60;
        let currentSavePct = 30;
        let currentGivePct = 10;

        const parentTips = {{
            '3-5': 'Use physical coins and clear plastic Gullaks. Keep target savings goals extremely short (3 to 5 days) to match their attention span.',
            '6-8': 'Introduce a "Parent Match" (e.g. adding ₹10 for every ₹100 kept in the Bachat Gullak for a full month) to teach the basic concept of interest!',
            '9-10': 'Teach Zaroorat (Needs) vs Khwahish (Wants). Introduce supervised prepaid kid digital cards for school trips while maintaining physical Gullaks for local errands.'
        }};

        function updateGullak() {{
            const amount = parseFloat(slider.value);
            allowanceDisplay.innerText = `₹${{amount.toLocaleString('en-IN')}}`;

            const spend = (amount * (currentSpendPct / 100)).toFixed(2);
            const save = (amount * (currentSavePct / 100)).toFixed(2);
            const give = (amount * (currentGivePct / 100)).toFixed(2);

            document.getElementById('spend-amount').innerText = `₹${{spend}}`;
            document.getElementById('save-amount').innerText = `₹${{save}}`;
            document.getElementById('give-amount').innerText = `₹${{give}}`;

            document.getElementById('spend-pct').innerText = `${{currentSpendPct}}%`;
            document.getElementById('save-pct').innerText = `${{currentSavePct}}%`;
            document.getElementById('give-pct').innerText = `${{currentGivePct}}%`;

            const age = ageSelector.value;
            document.getElementById('tip-age-label').innerText = `Ages ${{age}}`;
            document.getElementById('parent-tip').innerText = parentTips[age];
        }}

        function setPreset(spend, save, give) {{
            currentSpendPct = spend;
            currentSavePct = save;
            currentGivePct = give;

            document.querySelectorAll('.preset-btn').forEach(b => {{
                b.className = "preset-btn bg-gray-100 hover:bg-gray-200 text-gray-700 py-2 px-2 rounded-xl text-xs font-bold transition text-center";
            }});
            event.currentTarget.className = "preset-btn bg-saffron text-white py-2 px-2 rounded-xl text-xs font-bold transition text-center shadow-sm";

            updateGullak();
        }}

        slider.addEventListener('input', updateGullak);
        ageSelector.addEventListener('change', updateGullak);

        // Daily Wheel Spinner
        function spinWheel() {{
            const icon = document.getElementById('wheel-icon');
            const spinBtn = document.getElementById('spin-btn');
            const viewBtn = document.getElementById('view-random-btn');

            icon.classList.add('spinning');
            spinBtn.disabled = true;

            setTimeout(() => {{
                icon.classList.remove('spinning');
                spinBtn.disabled = false;

                const randomIndex = Math.floor(Math.random() * activitiesData.length);
                const picked = activitiesData[randomIndex];
                activeRandomId = picked.id;

                document.getElementById('random-title').innerText = picked.title;
                document.getElementById('random-desc').innerText = `Category: ${{categoryNames[picked.category]}} | Age: ${{picked.age}}`;
                viewBtn.classList.remove('hidden');
            }}, 600);
        }}

        function openModalFromRandom() {{
            if (activeRandomId) {{
                openModal(activeRandomId);
            }}
        }}

        // Initial Initialization
        window.onload = function() {{
            renderActivities(activitiesData);
            updateGullak();
        }};
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("File index.html generated successfully!")