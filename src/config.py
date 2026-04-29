"""
config.py
=========
Constantes y listas de especies del proyecto Predator Ranking.

Contiene las listas curadas de megadepredadores vertebrados e invertebrados
que conforman el scope del proyecto, divididas por fuente de datos.

Listas disponibles:
    ESPECIES_FOSILES: Especies extintas a consultar en PBDB.
    ESPECIES_MODERNAS: Especies actuales a consultar en PanTHERIA y EltonTraits.
"""

ESPECIES_FOSILES = [
    # CÁMBRICO
    ("Anomalocaris canadensis", "Radiodonta", "Invertebrado"),
    ("Aegirocassis benmoulai", "Radiodonta", "Invertebrado"),
    ("Peytoia nathorsti", "Radiodonta", "Invertebrado"),
    ("Hurdia victoria", "Radiodonta", "Invertebrado"),
    ("Timorebestia koprii", "Chaetognatha", "Invertebrado"),

    # ORDOVÍCICO
    ("Cameroceras trentonense", "Nautiloidea", "Invertebrado"),
    ("Endoceras proteiforme", "Nautiloidea", "Invertebrado"),
    ("Pentecopterus decorahensis", "Eurypterida", "Invertebrado"),

    # SILÚRICO
    ("Jaekelopterus rhenaniae", "Eurypterida", "Invertebrado"),
    ("Brontoscorpio anglicus", "Eurypterida", "Invertebrado"),
    ("Megalograptus ohioensis", "Eurypterida", "Invertebrado"),

    # DEVÓNICO
    ("Dunkleosteus terrelli", "Placodermi", "Placodermi"),
    ("Hyneria lindae", "Tetrapodomorpha", "Sarcopterygii"),
    ("Rhizodus hibberti", "Rhizodontida", "Sarcopterygii"),
    ("Helicoprion bessonowi", "Chondrichthyes", "Chondrichthyes"),
    ("Edestus heinrichi", "Chondrichthyes", "Chondrichthyes"),
    ("Orthacanthus senckenbergianus", "Chondrichthyes", "Chondrichthyes"),
    ("Titanichthys agassizi", "Placodermi", "Placodermi"),

    # CARBONÍFERO
    ("Arthropleura armata", "Myriapoda", "Invertebrado"),
    ("Pulmonoscorpius kirktonensis", "Scorpiones", "Invertebrado"),
    ("Meganeura monyi", "Odonatoptera", "Invertebrado"),
    ("Crassigyrinus scoticus", "Tetrapoda", "Amphibia"),

    # PÉRMICO
    ("Inostrancevia alexandri", "Gorgonopsia", "Synapsida"),
    ("Gorgonops torvus", "Gorgonopsia", "Synapsida"),
    ("Rubidgea atrox", "Gorgonopsia", "Synapsida"),
    ("Anteosaurus magnificus", "Dinocephalia", "Synapsida"),
    ("Prionosuchus plummeri", "Temnospondyli", "Amphibia"),

    # TRIÁSICO
    ("Postosuchus kirkpatricki", "Rauisuchia", "Reptilia"),
    ("Fasolasuchus tenax", "Rauisuchia", "Reptilia"),
    ("Saurosuchus galilei", "Rauisuchia", "Reptilia"),
    ("Thalattoarchon saurophagis", "Ichthyosauria", "Reptilia"),
    ("Cymbospondylus youngorum", "Ichthyosauria", "Reptilia"),
    ("Shonisaurus sikanniensis", "Ichthyosauria", "Reptilia"),
    ("Mastodonsaurus giganteus", "Temnospondyli", "Amphibia"),
    ("Nothosaurus giganteus", "Sauropterygia", "Reptilia"),

    # JURÁSICO
    ("Allosaurus fragilis", "Dinosauria", "Reptilia"),
    ("Torvosaurus tanneri", "Dinosauria", "Reptilia"),
    ("Megalosaurus bucklandii", "Dinosauria", "Reptilia"),
    ("Ceratosaurus nasicornis", "Dinosauria", "Reptilia"),
    ("Liopleurodon ferox", "Plesiosauria", "Reptilia"),
    ("Pliosaurus funkei", "Plesiosauria", "Reptilia"),
    ("Dakosaurus maximus", "Crocodylomorpha", "Reptilia"),
    ("Hybodus hauffianus", "Chondrichthyes", "Chondrichthyes"),
    ("Metriorhynchus superciliosus", "Crocodylomorpha", "Reptilia"),

    # CRETÁCICO
    ("Tyrannosaurus rex", "Dinosauria", "Reptilia"),
    ("Spinosaurus aegyptiacus", "Dinosauria", "Reptilia"),
    ("Giganotosaurus carolinii", "Dinosauria", "Reptilia"),
    ("Carcharodontosaurus saharicus", "Dinosauria", "Reptilia"),
    ("Acrocanthosaurus atokensis", "Dinosauria", "Reptilia"),
    ("Carnotaurus sastrei", "Dinosauria", "Reptilia"),
    ("Majungasaurus crenatissimus", "Dinosauria", "Reptilia"),
    ("Baryonyx walkeri", "Dinosauria", "Reptilia"),
    ("Utahraptor ostrommaysorum", "Dinosauria", "Reptilia"),
    ("Deinonychus antirrhopus", "Dinosauria", "Reptilia"),
    ("Velociraptor mongoliensis", "Dinosauria", "Reptilia"),
    ("Tarbosaurus bataar", "Dinosauria", "Reptilia"),
    ("Mosasaurus hoffmannii", "Mosasauridae", "Reptilia"),
    ("Tylosaurus proriger", "Mosasauridae", "Reptilia"),
    ("Prognathodon saturator", "Mosasauridae", "Reptilia"),
    ("Hainosaurus bernardi", "Mosasauridae", "Reptilia"),
    ("Elasmosaurus platyurus", "Plesiosauria", "Reptilia"),
    ("Kronosaurus queenslandicus", "Plesiosauria", "Reptilia"),
    ("Xiphactinus audax", "Ichthyodectiformes", "Actinopterygii"),
    ("Cretoxyrhina mantelli", "Chondrichthyes", "Chondrichthyes"),
    ("Squalicorax falcatus", "Chondrichthyes", "Chondrichthyes"),
    ("Quetzalcoatlus northropi", "Pterosauria", "Reptilia"),
    ("Hatzegopteryx thambema", "Pterosauria", "Reptilia"),
    ("Pteranodon longiceps", "Pterosauria", "Reptilia"),
    ("Tropeognathus mesembrinus", "Pterosauria", "Reptilia"),

    # PALEOCENO
    ("Titanoboa cerrejonensis", "Boidae", "Reptilia"),
    ("Gastornis giganteus", "Gastornithidae", "Aves"),
    ("Ambulocetus natans", "Cetacea", "Mammalia"),

    # EOCENO
    ("Basilosaurus isis", "Cetacea", "Mammalia"),
    ("Andrewsarchus mongoliensis", "Andrewsarchidae", "Mammalia"),
    ("Hyaenodon gigas", "Hyaenodonta", "Mammalia"),
    ("Gigantophis garstini", "Boidae", "Reptilia"),
    ("Patriofelis ferox", "Oxyaenidae", "Mammalia"),

    # OLIGOCENO
    ("Brygmophyseter shigensis", "Cetacea", "Mammalia"),
    ("Entelodon magnus", "Entelodontidae", "Mammalia"),
    ("Eusmilus sicarius", "Nimravidae", "Mammalia"),

    # MIOCENO
    ("Otodus megalodon", "Chondrichthyes", "Chondrichthyes"),
    ("Livyatan melvillei", "Cetacea", "Mammalia"),
    ("Machairodus aphanistus", "Felidae", "Mammalia"),
    ("Dinofelis barlowi", "Felidae", "Mammalia"),
    ("Amphicyon ingens", "Amphicyonidae", "Mammalia"),
    ("Kelenken guillermoi", "Phorusrhacidae", "Aves"),
    ("Argentavis magnificens", "Teratornithidae", "Aves"),
    ("Vasuki indicus", "Madtsoiidae", "Reptilia"),

    # PLIOCENO
    ("Phorusrhacos longissimus", "Phorusrhacidae", "Aves"),
    ("Titanis walleri", "Phorusrhacidae", "Aves"),
    ("Smilodon populator", "Felidae", "Mammalia"),
    ("Thylacoleo carnifex", "Thylacoleonidae", "Mammalia"),
    ("Megistotherium osteothlastes", "Hyaenodonta", "Mammalia"),

    # PLEISTOCENO
    ("Smilodon fatalis", "Felidae", "Mammalia"),
    ("Arctodus simus", "Ursidae", "Mammalia"),
    ("Arctotherium angustidens", "Ursidae", "Mammalia"),
    ("Panthera spelaea", "Felidae", "Mammalia"),
    ("Panthera atrox", "Felidae", "Mammalia"),
    ("Hieraaetus moorei", "Accipitridae", "Aves"),
    ("Megalania prisca", "Varanidae", "Reptilia"),
    ("Thylacosmilus atrox", "Sparassodonta", "Mammalia"),
]

ESPECIES_MODERNAS = [
    # MODERNOS TERRESTRES
    ("Panthera leo", "Felidae", "Mammalia", 'terrestrial'),
    ("Panthera tigris", "Felidae", "Mammalia", 'terrestrial'),
    ("Panthera onca", "Felidae", "Mammalia", 'terrestrial'),
    ("Panthera pardus", "Felidae", "Mammalia", 'terrestrial'),
    ("Acinonyx jubatus", "Felidae", "Mammalia", 'terrestrial'),
    ("Crocuta crocuta", "Hyaenidae", "Mammalia", 'terrestrial'),
    ("Ursus arctos", "Ursidae", "Mammalia", 'terrestrial'),
    ("Ursus maritimus", "Ursidae", "Mammalia", 'terrestrial'),
    ("Canis lupus", "Canidae", "Mammalia", 'terrestrial'),
    ("Lycaon pictus", "Canidae", "Mammalia", 'terrestrial'),
    ("Crocodylus niloticus", "Crocodylomorpha", "Reptilia", 'freshwater'),
    ("Crocodylus porosus", "Crocodylomorpha", "Reptilia", 'freshwater'),
    ("Varanus komodoensis", "Varanidae", "Reptilia", 'terrestrial'),
    ("Harpia harpyja", "Accipitridae", "Aves", 'terrestrial'),
    ("Aquila chrysaetos", "Accipitridae", "Aves", 'terrestrial'),
    ("Stephanoaetus coronatus", "Accipitridae", "Aves", 'terrestrial'),

    # MODERNOS MARINOS
    ("Orcinus orca", "Cetacea", "Mammalia", 'marine'),
    ("Physeter macrocephalus", "Cetacea", "Mammalia", 'marine'),
    ("Carcharodon carcharias", "Chondrichthyes", "Chondrichthyes", 'marine'),
    ("Galeocerdo cuvier", "Chondrichthyes", "Chondrichthyes", 'marine'),
    ("Sphyrna mokarran", "Chondrichthyes", "Chondrichthyes", 'marine'),
    ("Somniosus microcephalus", "Chondrichthyes", "Chondrichthyes", 'marine'),

    # MODERNOS SERPIENTES
    ("Eunectes murinus", "Boidae", "Reptilia", 'terrestrial'),
    ("Python reticulatus", "Pythonidae", "Reptilia", 'terrestrial'),
    ("Ophiophagus hannah", "Elapidae", "Reptilia", 'terrestrial'),
]

ENTORNO_POR_CLASE = {
    'Reptilia': 'terrestrial',
    'Aves': 'terrestrial',
    'Chondrichthyes': 'marine',
    'Mammalia': 'terrestrial',
    'Placodermi': 'marine',
    'Saurischia': 'terrestrial',
    'Invertebrado': 'marine',
    'Sarcopterygii': 'marine',
    'Actinopterygii': 'marine',
}

ENTORNO_EXCEPCIONES = {
    'Arthropleura armata': 'terrestrial',
    'Jaekelopterus rhenaniae': 'freshwater',
    'Pentecopterus decorahensis': 'marine',
    'Mosasaurus hoffmannii': 'marine',
    'Tylosaurus proriger': 'marine',
    'Prognathodon saturator': 'marine',
    'Hainosaurus bernardi': 'marine',
    'Hatzegopteryx thambema': 'terrestrial',
    'Pteranodon longiceps': 'terrestrial',
    'Tropeognathus mesembrinus': 'terrestrial',
    'Livyatan melvillei': 'marine',
    'Brygmophyseter shigensis': 'marine'
}

DIETA_EXCEPCIONES = {
    'Andrewsarchus mongoliensis': 'carnivore',
    'Thylacoleo carnifex': 'carnivore',
    'Megistotherium osteothlastes': 'carnivore',
    'Arctodus simus': 'carnivore',
    'Arctotherium angustidens': 'carnivore'
}