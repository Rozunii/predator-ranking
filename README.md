# Predator Ranking - Who Ruled the Earth?

> *A data science pipeline that ranks the most iconic apex predators in geological history using fossil records, scientific literature, and AI-powered data extraction.*

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![PBDB](https://img.shields.io/badge/Data-Paleobiology%20Database-green?style=flat-square)](https://paleobiodb.org/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=flat-square)]()

---

## Project Overview

This is a **dual-purpose project**: a professional data science portfolio piece and the engine behind a YouTube documentary video.

The goal is to answer one deceptively simple question:

**Who was the most dominant predator in the history of life on Earth?**

To answer it rigorously, this project builds a multi-source data pipeline that collects, cleans, and scores **132 curated apex predator species** spanning 540 million years of geological history from the Cambrian seas to the present day.

---

## What I'm Learning & Building

This project is designed as a progressive learning roadmap. Each phase introduces a new tool or concept:

| Phase | Tools | Status |
|---|---|---|
| **1. Data Collection** | REST APIs, `requests`, `pandas` | ✅ Complete |
| **2. Data Processing** | `pandas`, environment and diet imputation | ✅ Complete |
| **3. Exploratory Analysis** | `matplotlib`, `seaborn`, `numpy` | ✅ Complete |
| **4. Body Mass Estimation** | RAG, LangChain, PubMed/BioRxiv | Planned |
| **5. Modern Predators** | PanTHERIA, EltonTraits datasets | Planned |
| **6. Multi-Agent Pipeline** | LangGraph, ChromaDB | Planned |
| **7. Visualization** | Matplotlib animated, Blender + bpy | Planned |

---

## Data Sources

| Source | Type | What it provides |
|---|---|---|
| [Paleobiology Database (PBDB)](https://paleobiodb.org/) | REST API | Fossil species, temporal range, diet, environment |
| [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/) | RAG / Web Scraping | Body mass estimates from scientific literature |
| [BioRxiv](https://www.biorxiv.org/) | RAG / Web Scraping | Preprint paleontology papers |
| [PanTHERIA](https://esajournals.onlinelibrary.wiley.com/doi/10.1890/08-1494.1) | Static Dataset | Body mass and diet for modern mammals |
| [EltonTraits 1.0](https://esajournals.onlinelibrary.wiley.com/doi/10.1890/13-1917.1) | Static Dataset | Diet composition for modern birds and mammals |
| [GBIF](https://www.gbif.org/) | REST API | Geographic coordinates (modern species only) |

> **Note:** IUCN Red List API v4 was evaluated and discarded — its terms of service do not permit use in ML training pipelines.

---

## Ranking Metrics

Biomass consumed was considered and discarded - no direct fossil data exists to calculate it without fabricating assumptions. Instead, the ranking uses four defensible metrics:

1. **Body Mass Dominance** - Relative size estimated via RAG over scientific literature. Taxonomic imputation applied for species with no direct estimate.
2. **Temporal Dominance** - Duration of presence in the fossil record (millions of years).
3. **Geographic Dominance** - Range of documented fossil occurrences across regions.
4. **Individual Biomass Consumption** - Estimated annual caloric intake per individual, extracted via RAG from metabolic and dietary studies.
5. **Ecological Terror Index** - Combined weighted score across the three metrics above.

---

## Scope & Methodology

**In scope:** 132 curated apex predator species - vertebrates and invertebrates, marine and terrestrial, fossil and modern. Species were selected based on scientific relevance, fossil record quality, and narrative impact across all geological eras from the Cambrian to the present.

**Out of scope:** Micro-predators and species without sufficient scientific literature. The scale difference makes cross-comparison ecologically meaningless a different project entirely.

**Methodology note:** 7 species in the curated list returned no records in PBDB. These will be recovered in the RAG phase through direct extraction from scientific literature, with citations included.

---

## Project Structure

```
predator_ranking/
├── data/
│   ├── raw/              
│   └── processed/        
├── notebooks/
│   ├── 01_exploracion_pbdb.ipynb
│   └── 02_exploracion_especies_curadas.ipynb
├── src/
│   ├── __init__.py
│   ├── config.py         
│   ├── collectors/
│   │   ├── __init__.py
│   │   └── pbdb.py       
│   ├── processors/
│   │   ├── __init__.py
│   │   └── cleaner.py    
│   └── visualization/
│       └── __init__.py   
├── main.py
├── requirements.txt
└── .gitignore
```

---

## Current Dataset Stats

| Metric | Value |
|---|---|
| Fossil species collected | 94 |
| Total curated species (fossil + modern) | 132 |
| Temporal range | 540 Ma to Present |
| Geological eras covered | Cambrian through Holocene |
| Data source | Paleobiology Database API v1.2 |

---

## Roadmap

- [x] PBDB collector with species-level queries
- [x] Environment imputation from taxonomic class
- [x] Diet imputation for curated predator list
- [x] Exploratory analysis notebook with key findings
- [ ] PanTHERIA + EltonTraits integration for modern predators
- [ ] RAG pipeline for body mass estimation from literature
- [ ] LangGraph multi-agent orchestration
- [ ] Scoring and ranking engine
- [ ] Timeline animation (Matplotlib to Blender)

---

## Author

**Rozunii** - Data Science & AI student building at the intersection of science and storytelling.

[![GitHub](https://img.shields.io/badge/GitHub-Rozunii-black?style=flat-square&logo=github)](https://github.com/Rozunii)

---