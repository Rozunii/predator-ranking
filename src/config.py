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
    ("Panthera leo", "Felidae", "Mammalia"),
    ("Panthera tigris", "Felidae", "Mammalia"),
    ("Panthera onca", "Felidae", "Mammalia"),
    ("Panthera pardus", "Felidae", "Mammalia"),
    ("Acinonyx jubatus", "Felidae", "Mammalia"),
    ("Crocuta crocuta", "Hyaenidae", "Mammalia"),
    ("Ursus arctos", "Ursidae", "Mammalia"),
    ("Ursus maritimus", "Ursidae", "Mammalia"),
    ("Canis lupus", "Canidae", "Mammalia"),
    ("Lycaon pictus", "Canidae", "Mammalia"),
    ("Crocodylus niloticus", "Crocodylomorpha", "Reptilia"),
    ("Crocodylus porosus", "Crocodylomorpha", "Reptilia"),
    ("Varanus komodoensis", "Varanidae", "Reptilia"),
    ("Harpia harpyja", "Accipitridae", "Aves"),
    ("Aquila chrysaetos", "Accipitridae", "Aves"),
    ("Stephanoaetus coronatus", "Accipitridae", "Aves"),

    # MODERNOS MARINOS
    ("Orcinus orca", "Cetacea", "Mammalia"),
    ("Physeter macrocephalus", "Cetacea", "Mammalia"),
    ("Carcharodon carcharias", "Chondrichthyes", "Chondrichthyes"),
    ("Galeocerdo cuvier", "Chondrichthyes", "Chondrichthyes"),
    ("Sphyrna mokarran", "Chondrichthyes", "Chondrichthyes"),
    ("Somniosus microcephalus", "Chondrichthyes", "Chondrichthyes"),

    # MODERNOS SERPIENTES
    ("Eunectes murinus", "Boidae", "Reptilia"),
    ("Python reticulatus", "Pythonidae", "Reptilia"),
    ("Ophiophagus hannah", "Elapidae", "Reptilia"),
]