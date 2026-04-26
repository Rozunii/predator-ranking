# Predator Ranking - Who Ruled the Earth?

> *A data science pipeline that ranks every major vertebrate predator in geological history using fossil records, scientific literature, and AI-powered data extraction.*

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![PBDB](https://img.shields.io/badge/Data-Paleobiology%20Database-green?style=flat-square)](https://paleobiodb.org/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=flat-square)]()

---

## Project Overview

This is a **dual-purpose project**: a professional data science portfolio piece and the engine behind a YouTube documentary video.

The goal is to answer one deceptively simple question:

**Who was the most dominant predator in the history of life on Earth?**

To answer it rigorously, this project builds a multi-source data pipeline that collects, cleans, and scores **3,800+ predator** spanning 540 million years of geological history.

---

## What I'm Learning & Building

This project is designed as a progressive learning roadmap. Each phase introduces a new tool or concept:

| Phase | Tools | Status |
|---|---|---|
| **1. Data Collection** | REST APIs, `requests`, `pandas` | Complete |
| **2. Data Processing** | `pandas`, taxonomic imputation | In Progress |
| **3. Body Mass Estimation** | RAG, LangChain, PubMed/BioRxiv | Planned |
| **4. Modern Predators** | PanTHERIA, EltonTraits datasets | Planned |
| **5. Multi-Agent Pipeline** | LangGraph, ChromaDB | Planned |
| **6. Visualization** | Matplotlib animated, Blender + bpy | Planned |

---

## Data Sources

| Source | Type | What it provides |
|---|---|---|
| [Paleobiology Database (PBDB)](https://paleobiodb.org/) | REST API | Fossil genera, temporal range, diet, environment |
| [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/) | RAG / Web Scraping | Body mass estimates from scientific literature |
| [BioRxiv](https://www.biorxiv.org/) | RAG / Web Scraping | Preprint paleontology papers |
| [PanTHERIA](https://esajournals.onlinelibrary.wiley.com/doi/10.1890/08-1494.1) | Static Dataset | Body mass and diet for modern mammals |
| [EltonTraits 1.0](https://esajournals.onlinelibrary.wiley.com/doi/10.1890/13-1917.1) | Static Dataset | Diet composition for modern birds and mammals |
| [GBIF](https://www.gbif.org/) | REST API | Geographic coordinates (modern species only) |

> **Note:** IUCN Red List API v4 was evaluated and discarded its terms of service do not permit use in ML training pipelines.

---

## Ranking Metrics

Biomass consumed was considered and discarded no direct fossil data exists to calculate it without fabricating assumptions. Instead, the ranking uses four defensible metrics:

1. **Body Mass Dominance** - Relative size estimated via RAG over scientific literature.
2. **Temporal Dominance** - Duration of presence in the fossil record (millions of years).
3. **Geographic Dominance** - Range of documented fossil occurrences across regions.
4. **Ecological Terror Index** - Combined weighted score across the three metrics above.

---

## Scope & Methodology

**In scope:** Vertebrate megapredators - marine and terrestrial, fossil and modern.

Includes: Dinosauria, Chondrichthyes (sharks), Mosasauridae, Plesiosauria, Crocodylomorpha, Felidae, Cetacea, Placodermi, Boidae, Phorusrhacidae.

**Out of scope:** Invertebrates and micro-predators. The scale difference makes cross-comparison ecologically meaningless a different project entirely.

---

## Project Structure

```
predator_ranking/
├── data/
│   ├── raw/              
│   └── processed/        
├── notebooks/
│   └── 01_exploracion_pbdb.ipynb
├── src/
│   ├── __init__.py
│   ├── collectors/
│   │   ├── __init__.py
│   │   └── pbdb.py      
│   ├── processors/
│   │   └── __init__.py   
│   └── visualization/
│       └── __init__.py   
├── main.py
├── requirements.txt
└── .gitignore
```
---

## Author

**Rozunii** Data Science & AI student building at the intersection of science and storytelling.

[![GitHub](https://img.shields.io/badge/GitHub-Rozunii-black?style=flat-square&logo=github)](https://github.com/Rozunii)

---
