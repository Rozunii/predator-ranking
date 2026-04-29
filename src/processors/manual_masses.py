"""
processors/manual_masses.py
===========================
Masas corporales curadas manualmente para especies sin datos en RAG.

Cada entrada incluye masa en kg y fuente científica primaria.
Los valores en gramos se calculan en el pipeline multiplicando por 1000.

Formato:
    {
        'Nombre especie': {
            'masa_kg': float,
            'fuente': str  # Autor(es), Año, Revista/Fuente, DOI si disponible
        }
    }
"""

MASAS_MANUALES = {

    'Liopleurodon ferox': {
        'masa_kg': 7800,
        'fuente': 'Zhao (2024). Body reconstruction and size estimation of plesiosaurs. bioRxiv. doi:10.1101/2024.02.15.578844'
    },
    'Pliosaurus funkei': {
        'masa_kg': 12724,
        'fuente': 'Zhao (2024). Body reconstruction and size estimation of plesiosaurs. bioRxiv. doi:10.1101/2024.02.15.578844'
    },
    'Dunkleosteus terrelli': {
        'masa_kg': 1764,
        'fuente': 'Engelman (2023). Giant, swimming mouths: oral dimensions of extant sharks do not accurately predict body size in Dunkleosteus terrelli. PeerJ. doi:10.7717/peerj.15131'
    },
    'Carcharodontosaurus saharicus': {
        'masa_kg': 6233,
        'fuente': 'Sereno et al. (2022). Spinosaurus aegyptiacus: resolving weighty matters. ResearchGate / PeerJ'
    },
    'Giganotosaurus carolinii': {
        'masa_kg': 6827,
        'fuente': 'Sereno et al. (2022). Spinosaurus aegyptiacus: resolving weighty matters. ResearchGate / PeerJ'
    },
    'Tyrannosaurus rex': {
        'masa_kg': 8870,
        'fuente': 'Volumetric model of specimen "Sue" (FMNH PR2081). Widely cited in paleontological literature.'
    },
    'Velociraptor mongoliensis': {
        'masa_kg': 25,
        'fuente': 'Campione & Evans (2020). High-precision body mass predictors for small mammals. ResearchGate'
    },
    'Anomalocaris canadensis': {
        'masa_kg': 3.5,
        'fuente': 'Estimated from 1m body length and radiodont volumetric model. Daley & Budd (2010). New anomalocaridid appendages from the Burgess Shale. Palaeontology.'
    },
    'Peytoia nathorsti': {
        'masa_kg': 2.5,
        'fuente': 'Estimated from appendage/body ratio in hurdiids. Daley et al. (2009). The Burgess Shale anomalocaridid Hurdia. Science.'
    },
    'Hurdia victoria': {
        'masa_kg': 3.0,
        'fuente': 'Daley & Budd (2010). New anomalocaridid appendages from the Burgess Shale. Palaeontology. doi:10.1111/j.1475-4983.2009.00910.x'
    },
    'Timorebestia koprii': {
        'masa_kg': 0.45,
        'fuente': 'Estimated from giant chaetognath morphology (~30cm). Jakob Vinther et al. (2023). Science Advances.'
    },
    'Cameroceras trentonense': {
        'masa_kg': 100,
        'fuente': 'Estimated from orthocone shell volume revision. Wikipedia: Cameroceras, citing Teichert & Kummel (1960). Shell volume methodology.'
    },
    'Endoceras proteiforme': {
        'masa_kg': 100,
        'fuente': 'Estimated from 5.73m shell length, Museum of Comparative Zoology specimen. Wikipedia: Endoceras.'
    },
    'Pentecopterus decorahensis': {
        'masa_kg': 1,
        'fuente': 'Estimated from eurypterid scaling. Lamsdell et al. (2015). The oldest described eurypterid. BMC Evolutionary Biology.'
    },
    'Jaekelopterus rhenaniae': {
        'masa_kg': 200,
        'fuente': 'Scaled from 46cm chelicera to ~2.5m body length. Braddy et al. (2008). Giant claw reveals the largest ever arthropod. Biology Letters. doi:10.1098/rsbl.2007.0491'
    },
    'Brontoscorpio anglicus': {
        'masa_kg': 1,
        'fuente': 'Estimated from eurypterid body plan scaling. General paleontological consensus.'
    },
    'Megalograptus ohioensis': {
        'masa_kg': 1,
        'fuente': 'Estimated from eurypterid scaling. General paleontological consensus.'
    },
    'Hyneria lindae': {
        'masa_kg': 2000,
        'fuente': 'Estimated from 4-5m body length, tetrapodomorph fish scaling. Wikipedia: Hyneria, citing Thomson (1968).'
    },
    'Rhizodus hibberti': {
        'masa_kg': 4000,
        'fuente': 'Estimated from confirmed 7m length, ambush predator morphology. Prehistoric Life Wiki: Rhizodus.'
    },
    'Helicoprion bessonowi': {
        'masa_kg': 680,
        'fuente': 'Tapanila et al. (2013). Jaws for a spiral-tooth whorl: CT images reveal novel adaptation and phylogeny in fossil Helicoprion. Biology Letters. doi:10.1098/rsbl.2013.0057'
    },
    'Edestus heinrichi': {
        'masa_kg': 200,
        'fuente': 'Estimated from body length ~4m, chondrichthyan scaling. General paleontological consensus.'
    },
    'Arthropleura armata': {
        'masa_kg': 50,
        'fuente': 'Guinness World Records: Largest land arthropod ever. Confirmed 2.6m length, myriapod volumetric model. doi:10.1093/zoolinnean/zlad138 (2024 head fossil study)'
    },
    'Pulmonoscorpius kirktonensis': {
        'masa_kg': 0.5,
        'fuente': 'Estimated from ~70cm body length, scorpion volumetric scaling. General paleontological consensus.'
    },
    'Meganeura monyi': {
        'masa_kg': 0.15,
        'fuente': 'Estimated from biomechanical model of giant dragonfly. Wikipedia: Meganeura, citing Cannell (2018).'
    },
    'Crassigyrinus scoticus': {
        'masa_kg': 20,
        'fuente': 'Estimated from 1.5m body length, early tetrapod scaling. General paleontological consensus.'
    },
    'Inostrancevia alexandri': {
        'masa_kg': 300,
        'fuente': 'Wikipedia: Largest prehistoric animals. Inostrancevia latifrons skull >60cm, total length ~3.5m, estimated 300kg.'
    },
    'Rubidgea atrox': {
        'masa_kg': 150,
        'fuente': 'Estimated from skull ~45cm, largest African gorgonopsian. Wikipedia: Largest prehistoric animals.'
    },
    'Anteosaurus magnificus': {
        'masa_kg': 600,
        'fuente': 'Wikipedia: Anteosaurus, citing Boonstra (1954) and Smith & Keyser (2000). 5-6m length, dinocephalian scaling.'
    },
    'Prionosuchus plummeri': {
        'masa_kg': 2000,
        'fuente': 'Estimated from 9m body length, 1.6m skull, temnospondyl aquatic scaling. Dinopedia: Prionosuchus.'
    },
    'Postosuchus kirkpatricki': {
        'masa_kg': 300,
        'fuente': 'Estimated from ~7m body length, rauisuchian scaling. Wikipedia: Largest prehistoric animals.'
    },
    'Fasolasuchus tenax': {
        'masa_kg': 2000,
        'fuente': 'Estimated from 8-10m body length, largest known rauisuchian. Wikipedia: Largest prehistoric animals.'
    },
    'Saurosuchus galilei': {
        'masa_kg': 500,
        'fuente': 'Estimated from ~7m body length, rauisuchian scaling. Wikipedia: Largest prehistoric animals.'
    },
    'Thalattoarchon saurophagis': {
        'masa_kg': 4000,
        'fuente': 'Estimated from 8.6m body length, ichthyosaur volumetric scaling. Fröbisch et al. (2013). PNAS.'
    },
    'Shonisaurus sikanniensis': {
        'masa_kg': 81500,
        'fuente': 'Nicholls & Manabe (2004). Giant ichthyosaurs of the Triassic. Journal of Vertebrate Paleontology. Wikipedia: Shonisaurus.'
    },
    'Mastodonsaurus giganteus': {
        'masa_kg': 500,
        'fuente': 'Estimated from 4-6m body length, temnospondyl aquatic scaling. General paleontological consensus.'
    },
    'Nothosaurus giganteus': {
        'masa_kg': 150,
        'fuente': 'Estimated from ~4m body length, sauropterygian scaling. General paleontological consensus.'
    },
    'Allosaurus fragilis': {
        'masa_kg': 1500,
        'fuente': 'Christiansen & Farina (2004). Mass prediction in theropod dinosaurs. Historical Biology. doi:10.1080/08912960412331284313'
    },
    'Torvosaurus tanneri': {
        'masa_kg': 2000,
        'fuente': 'Estimated from 9-10m body length, megalosaurid scaling. Wikipedia: Torvosaurus.'
    },
    'Megalosaurus bucklandii': {
        'masa_kg': 700,
        'fuente': 'Estimated from ~6m body length, tetanuran scaling. Wikipedia: Megalosaurus.'
    },
    'Dakosaurus maximus': {
        'masa_kg': 600,
        'fuente': 'Estimated from ~5m body length, metriorhynchid scaling. Wikipedia: Dakosaurus.'
    },
    'Hybodus hauffianus': {
        'masa_kg': 50,
        'fuente': 'Estimated from ~2m body length, hybrid shark scaling. General paleontological consensus.'
    },
    'Metriorhynchus superciliosus': {
        'masa_kg': 200,
        'fuente': 'Estimated from ~3m body length, metriorhynchid scaling. Wikipedia: Metriorhynchus.'
    },
    'Spinosaurus aegyptiacus': {
        'masa_kg': 6397,
        'fuente': 'Sereno et al. (2022). Spinosaurus is not an aquatic dinosaur. eLife / PMC. doi:10.7554/eLife.80092'
    },
    'Acrocanthosaurus atokensis': {
        'masa_kg': 6180,
        'fuente': 'Bates et al. (2009). Palaeogravity calculation based on weight and mass estimates of Acrocanthosaurus atokensis. ResearchGate.'
    },
    'Carnotaurus sastrei': {
        'masa_kg': 1500,
        'fuente': 'Estimated from ~8m body length, abelisaurid scaling. Wikipedia: Carnotaurus.'
    },
    'Majungasaurus crenatissimus': {
        'masa_kg': 1100,
        'fuente': 'Estimated from ~7m body length, abelisaurid scaling. Wikipedia: Majungasaurus.'
    },
    'Baryonyx walkeri': {
        'masa_kg': 1200,
        'fuente': 'Estimated from ~8m body length, spinosaurid scaling. Wikipedia: Baryonyx.'
    },
    'Tarbosaurus bataar': {
        'masa_kg': 5000,
        'fuente': 'Scaled relative to Tyrannosaurus rex from limb bone proportions. Wikipedia: Tarbosaurus.'
    },
    'Mosasaurus hoffmannii': {
        'masa_kg': 13882,
        'fuente': 'Grigoriev (2024). Mosasaurus hoffmanni body mass estimation based on 3D model. Tomsk State University. vital.lib.tsu.ru'
    },
    'Tylosaurus proriger': {
        'masa_kg': 8000,
        'fuente': 'Estimated from 10-14m body length, mosasaurid 1:7 skull-body ratio. Reddit: Naturewasmetal — Current Size Estimates of Large Mosasaurs (2024).'
    },
    'Prognathodon saturator': {
        'masa_kg': 2000,
        'fuente': 'Estimated from ~8m body length, mosasaurid scaling. Wikipedia: Prognathodon.'
    },
    'Hainosaurus bernardi': {
        'masa_kg': 2500,
        'fuente': 'Estimated from ~10m body length, mosasaurid scaling. Wikipedia: Hainosaurus.'
    },
    'Elasmosaurus platyurus': {
        'masa_kg': 2000,
        'fuente': 'Zhao (2024). Body reconstruction and size estimation of plesiosaurs. bioRxiv. doi:10.1101/2024.02.15.578844'
    },
    'Kronosaurus queenslandicus': {
        'masa_kg': 11000,
        'fuente': 'McHenry (2009). The palaeoecology of the Cretaceous pliosaur Kronosaurus queenslandicus. Open Research Newcastle.'
    },
    'Xiphactinus audax': {
        'masa_kg': 250,
        'fuente': 'Estimated from ~5m body length, ichthyodectiform scaling. Wikipedia: Xiphactinus.'
    },
    'Cretoxyrhina mantelli': {
        'masa_kg': 1000,
        'fuente': 'Estimated from ~6m body length, lamniform scaling. Wikipedia: Cretoxyrhina.'
    },
    'Squalicorax falcatus': {
        'masa_kg': 200,
        'fuente': 'Estimated from ~2m body length, anacoracid shark scaling. Wikipedia: Squalicorax.'
    },
    'Hatzegopteryx thambema': {
        'masa_kg': 250,
        'fuente': 'Estimated 225-250kg from pneumatized bone structure. Wikipedia: Hatzegopteryx, citing Buffetaut et al. (2002). CRAS.'
    },
    'Pteranodon longiceps': {
        'masa_kg': 20,
        'fuente': 'Estimated from footprint scaling. Estimating body weight from footprints: Application to pterosaurs. ResearchGate.'
    },
    'Tropeognathus mesembrinus': {
        'masa_kg': 30,
        'fuente': 'Estimated from ~8.5m wingspan, pterosaur pneumatic scaling. Wikipedia: Tropeognathus.'
    },
    'Titanoboa cerrejonensis': {
        'masa_kg': 1135,
        'fuente': 'Head et al. (2009). Giant boid snake from the Palaeocene neotropics reveals hotter past equatorial temperatures. Nature. doi:10.1038/nature07671'
    },
    'Ambulocetus natans': {
        'masa_kg': 300,
        'fuente': 'Estimated from skeletal remains. Thewissen et al. (1994). Fossil evidence for the origin of aquatic locomotion in archaeocete whales. Science.'
    },
    'Basilosaurus isis': {
        'masa_kg': 7000,
        'fuente': 'Snively et al. (2015). Bone-Breaking Bite Force of Basilosaurus isis estimated by Finite Element Analysis. PLOS One. doi:10.1371/journal.pone.0118380'
    },
    'Andrewsarchus mongoliensis': {
        'masa_kg': 600,
        'fuente': 'Estimated from skull proportions compared to entelodont relatives. Wikipedia: Largest prehistoric animals. Only skull known.'
    },
    'Hyaenodon gigas': {
        'masa_kg': 400,
        'fuente': 'Estimated from limb bone regression. Egi (2001). Body mass estimates in extinct mammals from limb bone dimensions: North American Hyaenodontids. Palaeontology.'
    },
    'Gigantophis garstini': {
        'masa_kg': 100,
        'fuente': 'Estimated from ~10m body length, boid scaling relative to Titanoboa. Wikipedia: Gigantophis.'
    },
    'Patriofelis ferox': {
        'masa_kg': 80,
        'fuente': 'Estimated from oxyaenid body plan scaling. Wikipedia: Patriofelis.'
    },
    'Brygmophyseter shigensis': {
        'masa_kg': 10000,
        'fuente': 'Estimated from near-complete skeleton, physeteroid scaling. Wikipedia: Brygmophyseter.'
    },
    'Eusmilus sicarius': {
        'masa_kg': 100,
        'fuente': 'Estimated from nimravid body plan scaling. Wikipedia: Eusmilus.'
    },
    'Livyatan melvillei': {
        'masa_kg': 57000,
        'fuente': 'Estimated from 3m skull, scaled via Zygophyseter body proportions. Wikipedia: Livyatan, citing Lambert et al. (2010). Nature.'
    },
    'Machairodus aphanistus': {
        'masa_kg': 200,
        'fuente': 'Anton et al. (2004). First known complete skulls of Machairodus aphanistus. Journal of Vertebrate Paleontology.'
    },
    'Dinofelis barlowi': {
        'masa_kg': 100,
        'fuente': 'Estimated from felid body plan scaling. Wikipedia: Dinofelis.'
    },
    'Amphicyon ingens': {
        'masa_kg': 200,
        'fuente': 'Estimated from amphicyonid body plan scaling. Wikipedia: Amphicyon.'
    },
    'Kelenken guillermoi': {
        'masa_kg': 250,
        'fuente': 'Estimated from 3m height, phorusrhacid scaling. Wikipedia: Kelenken, citing Bertelli et al. (2007). Journal of Paleontology.'
    },
    'Vasuki indicus': {
        'masa_kg': 1000,
        'fuente': 'Datta & Bajpai (2024). Vasuki indicus from the Middle Eocene of India. Scientific Reports. doi:10.1038/s41598-024-58377-0'
    },
    'Phorusrhacos longissimus': {
        'masa_kg': 130,
        'fuente': 'Estimated from phorusrhacid body plan scaling. Wikipedia: Phorusrhacos.'
    },
    'Titanis walleri': {
        'masa_kg': 150,
        'fuente': 'Estimated from phorusrhacid body plan scaling. Wikipedia: Titanis.'
    },
    'Thylacoleo carnifex': {
        'masa_kg': 130,
        'fuente': 'Estimated from thylacoleonid body plan scaling. Wikipedia: Thylacoleo.'
    },
    'Megistotherium osteothlastes': {
        'masa_kg': 880,
        'fuente': 'Savage (1973). Megistotherium, an enormous creodont mammal. Quarterly Journal of the Geological Society. Wikipedia: Megistotherium.'
    },
    'Smilodon populator': {
        'masa_kg': 400,
        'fuente': 'Christiansen & Harris (2005). Body size of Smilodon (Mammalia: Felidae). Journal of Morphology. doi:10.1002/jmor.10252'
    },
    'Smilodon fatalis': {
        'masa_kg': 220,
        'fuente': 'Christiansen & Harris (2005). Body size of Smilodon (Mammalia: Felidae). Journal of Morphology. doi:10.1002/jmor.10252'
    },
    'Arctotherium angustidens': {
        'masa_kg': 1587,
        'fuente': 'Soibelzon & Schubert (2011). The largest known bear, Arctotherium angustidens, from the early Pleistocene of Argentina. Journal of Paleontology.'
    },
    'Panthera spelaea': {
        'masa_kg': 250,
        'fuente': 'Estimated from cave lion skeletal remains, felid scaling. Wikipedia: Panthera spelaea.'
    },
    'Panthera atrox': {
        'masa_kg': 350,
        'fuente': 'Wikipedia: Largest prehistoric animals, citing Sorkin (2008). American lion size estimate up to 363kg.'
    },
    'Thylacosmilus atrox': {
        'masa_kg': 120,
        'fuente': 'Estimated from sparassodont body plan scaling. Wikipedia: Thylacosmilus.'
    },

    'Gorgonops torvus': {
        'masa_kg': 98,
        'fuente': 'Estimated from gorgonopsid skull ~30cm, body ~1.5m. Wikipedia: Gorgonops, citing Sigogneau-Russell (1989). Theriodontia. Handbuch der Paläoherpetologie.'
    },
    'Ceratosaurus nasicornis': {
        'masa_kg': 524,
        'fuente': 'Paul (1988). Predatory Dinosaurs of the World. Simon & Schuster. Holotype skeleton USNM 4735 estimated at 524 kg.'
    },
    'Utahraptor ostrommaysorum': {
        'masa_kg': 500,
        'fuente': 'Estimated from dromaeosaurid femur scaling. Wikipedia: Utahraptor, citing Kirkland et al. (1993). Journal of Vertebrate Paleontology.'
    },
    'Deinonychus antirrhopus': {
        'masa_kg': 70,
        'fuente': 'Ostrom (1969). Osteology of Deinonychus antirrhopus. Peabody Museum Bulletin 30.'
    },
    'Quetzalcoatlus northropi': {
        'masa_kg': 250,
        'fuente': 'Estimated from pneumatized azhdarchid bone structure. Wikipedia: Quetzalcoatlus, citing Witton & Habib (2010). PLOS ONE. doi:10.1371/journal.pone.0013982'
    },
    'Otodus megalodon': {
        'masa_kg': 48000,
        'fuente': 'Cooper et al. (2022). The extinct shark Otodus megalodon was a transoceanic superpredator. Science Advances. doi:10.1126/sciadv.abm9424. Estimate for ~16m individual.'
    },
    'Argentavis magnificens': {
        'masa_kg': 72,
        'fuente': 'Campbell & Tonni (1983). Size and locomotion in teratorns. Auk 100. Reevaluated in Wikipedia: Argentavis.'
    },
    'Arctodus simus': {
        'masa_kg': 1000,
        'fuente': 'Estimated from ursid femur scaling, short-faced bear. Wikipedia: Arctodus, citing Sorkin (2006). Historical Biology.'
    },
    'Megalania prisca': {
        'masa_kg': 1917,
        'fuente': 'Wroe et al. (2004). Megafaunal extinction in the late Quaternary and the global overkill hypothesis. Alcheringa. Wikipedia: Megalania.'
    },
}