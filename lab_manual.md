# A Practical Introduction to Molecular Biology

## Table of Contents

- [Section 1: Plasmid Cloning](#section-1-plasmid-cloning)
  - [1.1 Background: Molecular Biology Fundamentals](#11-background-molecular-biology-fundamentals)
  - [1.2 Lab-Specific Resources](#12-lab-specific-resources)
  - [1.3 Protocol: Restriction Enzyme Cloning](#13-protocol-restriction-enzyme-cloning)
  - [1.4 Protocol: Golden Gate Assembly](#14-protocol-golden-gate-assembly)
- [Section 2: Mammalian Cell Culture](#section-2-mammalian-cell-culture)
  - [2.1 Background](#21-background)
  - [2.2 Lab-Specific Resources](#22-lab-specific-resources)
  - [2.3 Protocol: Routine Cell Maintenance](#23-protocol-routine-cell-maintenance)
  - [2.4 Protocol: Transient Transfection](#24-protocol-transient-transfection)
- [Section 3: Live-Cell Imaging of Biosensors](#section-3-live-cell-imaging-of-biosensors)
  - [3.1 Background](#31-background)
  - [3.2 Lab-Specific Resources](#32-lab-specific-resources)
  - [3.3 Protocol: Sample Preparation for Live Imaging](#33-protocol-sample-preparation-for-live-imaging)
  - [3.4 Protocol: Time-Lapse Acquisition](#34-protocol-time-lapse-acquisition)
  - [3.5 Protocol: Image Analysis](#35-protocol-image-analysis)
---

## Section 1: Plasmid Cloning

Cloning is the process of assembling a DNA construct — typically a gene of interest in a defined vector backbone — so that it can be propagated in bacteria and expressed in a target organism. You will learn two complementary cloning strategies: classical restriction enzyme/ligation cloning and the modern Golden Gate assembly method.

### 1.1 Background: Molecular Biology Fundamentals

#### 1.1.1 DNA, Plasmids, and Vectors

A plasmid is a circular piece of DNA, with no start or end. Circular DNA is highly stable, since it has no free 5’ or 3’-hydroxyl ends for **nucleases** to target. Plasmids were originally derived from bacteria, which harbor various kind of plasmids encoding genes for reproduction, antibiotic resistance, and virulence. Humans can take advantage of plasmids as a vector for genetic alteration or introduction of a perturbation to an organism. Plasmids can vary widely, but those used for routine gene expression contain the following: 

- **Origin of replication**: the region of the plasmid that allows it to be propagated inside of a bacterium.

- **Antibiotic resistance**: a selection marker. Cells carrying this gene grow in the presence of an antibiotic, thus showing which cells are carrying the plasmid we want. Cells that are untransformed (not carrying the plasmid) die.

- **Multiple cloning site (MCS)**: The site where (in traditional restriction/ligation cloning) the gene of interest can be inserted. The MCS is usually sandwiched between the promoter and the terminator.

- **Promoter**: The region of the plasmid that recruits the transcription machinery in the target organism. Notably, this gene is not expressed in the bacterium.

- **Terminator**: The region of the plasmid that signals the transcription machinery to stop synthesizing mRNA. Usually coupled with a **poly-adenylation** (polyA) signal.

Because a plasmid is circular and double stranded and thus a palindrome, the features encoded in this DNA have a pre-defined direction based on the biochemistry of transcription and replication. We read a sequence from 5' to 3', meaning the first base of the sequence is that which has a free 5'-OH group, and the end base has a free 3'-OH. An example of a plasmid is below, with the features marked in bold, the direction we read the feature as an arrow, and some examples of the sequences. Origins of replication and MCS do not have a read direction.

![A prototypical plasmid](media/plasmid.png)

#### 1.1.2 Restriction Enzymes

**Nucleases** are a class of enzyme that acts to break down nucleic acids (DNA, RNA, etc). DNases (DNA nucleases), come in two flavors: exonuclease and endonucleases. Exonucleases, like their name suggests, act to digest DNA from its terminal 5'-OH or 3'-OH ends and are highly efficient at degrading DNA. In contrast, endonucleases cut DNA from inside and can be **nonspecific** or cut only at a recognized sequence (restriction endonucleases).

![nucleases](media/restriction_enzymes.png)


Type II and type IIS restriction enzymes are commonly used in molecular cloning due to their ability to recognize and cut at specific sequences of DNA. Type II enzymes recognize palindromic sequences of DNA and cut, leaving either sticky (ends with single-stranded overhangs) or blunt (coherent base paired) ends. Type IIS enzymes recognize a specific sequence, but do not cleave it. Instead, they cut specific sequences downstream, leaving sticky ends that can be any sequence.

Like everything in biology, restriction enzymes are not perfect. Oftentimes, there is a **consensus** sequence where enzymes cut, but this sequence is not always strictly obeyed. Therefore, enzymes exhibit **star activity**, or off-target cutting. An example of this is the restriction enzyme BamHI, where the most common cutting sequence is `G|GATCC` but depending on salt concentration and pH, it can cut at other sites.


#### 1.1.3 DNA Ligation

As you may have recognized, when using the correct restriction enzymes on both your backbone and your insert, you will have palindromic sequences that can base pair. This is the main reason we use Type II restriction enzymes: to guide assembly of two or more pieces of DNA based on their end homology. Restriction digests can give us these pieces of DNA, but we use DNA ligation to stitch them together.

The most common form of DNA ligase used in the lab is T4 DNA ligase, an enzyme that catalyzes the formation of a **phosphodiester** bond between a 5'-phosphate and an adjacent 3'-OH group. T4 ligase uses ATP to catalyze the reaction to join two DNA molecules with homology.


![T4 ligase](media/t4_ligase.png)

#### 1.1.4 Golden Gate Assembly

Traditional **restriction/ligation** cloning using type II enzymes and a T4 ligase is useful for joining one or two inserts into vector. This requires *multiple* restriction enzymes, each with a different recognition sequence. Since the pool of palindromic sequences between 5 and 6 nucleotides in length is limited, increasing the number of inserts becomes very difficult. This is why we turn to type IIS restriction enzymes for multi-insert cloning.

Recall in [section 1.1.2](#112-restriction-enzymes), type IIS restriction enzymes do not cut at their cognate recongition sequence, but instead cut asymmetrically. This leaves an sticky-end of *any* nucleotide sequence `NNNN`. If designed correctly, the sequences of overhanging DNA in each of your fragments will complement with each other, allowing for **annealing** and subsequent ligation with T4 ligase. This technique was originally published in 2008, under the name [Golden Gate](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0003647).

Although it requires some very precise design, one can design a vector that has a self-excising type IIS restriction site that matches directly with the overhangs left from the type IIS site on the fragments you want to insert. Since the overhangs can be any sequence of `NNNN`, one can theoretically ligate up to 128 fragments simultaneously in one reaction. In reality, though, Golden Gate is rarely used to ligate more than 7 fragments due to mismatches during annealing.

---

### 1.3 Protocols: Restriction Enzyme Cloning

#### [1.3.1 PCR Amplification of Insert](./protocols/pcr.md)

#### 1.3.2 [Restriction Digest](./protocols/restriction_digest.md)

> 📝 *[Single and double digest setup, buffer choice, incubation conditions, heat inactivation, and gel verification.]*

#### 1.3.3 Gel Extraction & Cleanup

> 📝 *[Agarose gel preparation, band excision, gel extraction kit procedure, and elution/quantification.]*

#### 1.3.4 Ligation Reaction

> 📝 *[Molar ratio calculation, reaction setup (volumes, temperature, time), ligation controls, and transformation.]*

#### [1.3.5 Bacterial Transformation](./protocols/chemical_transformation_of_e_coli.md)

---

### 1.4 Protocol: Golden Gate Assembly

#### 1.4.1 [One-Pot Assembly Reaction](protocols/golden_gate.md)

#### 1.4.2 Transformation & Verification

#### [1.4.3 Bacterial Transformation](./protocols/chemical_transformation_of_e_coli.md)

## Section 2: Mammalian Cell Culture

Mammalian cell culture is the foundation of most experiments in the lab. Maintaining healthy, mycoplasma-free cells is a critical skill and a shared responsibility. This section covers the biology of the cell lines you will use, aseptic technique, and routine maintenance procedures.

### 2.1 Background

#### 2.1.1 The HeLa Cell Line

> 📝 *[Provide a brief history of HeLa cells, their biological characteristics (immortal, aneuploid, HeLa-specific contamination risk), doubling time, and why they are a workhorse for cell biology experiments.]*

#### 2.1.2 Other Cell Lines Used in the Lab

> 📝 *[List additional cell lines with their origin, key properties, and relevant experimental uses.]*

#### 2.1.3 Aseptic Technique

> 📝 *[Explain the principles behind sterile technique: biosafety cabinet use, UV sterilization, spray-down procedures, working clean, and common contamination sources (bacteria, fungi, mycoplasma).]*

#### 2.1.4 Media, Supplements, and Reagents

> 📝 *[Describe basal media (DMEM, RPMI, etc.), serum (FBS — lot testing, heat inactivation), L-glutamine/GlutaMAX, antibiotics policy in the lab, and the CO2/bicarbonate buffering system.]*

---

### 2.2 Lab-Specific Resources

| Resource | Details |
|---|---|
| Incubator location and CO2/temperature settings | `[PLACEHOLDER]` |
| Biosafety cabinet number and certification date | `[PLACEHOLDER]` |
| Cell line registry / passage number tracking system | `[PLACEHOLDER]` |
| Mycoplasma testing schedule and method | `[PLACEHOLDER]` |
| Liquid nitrogen tank location and cell stock inventory | `[PLACEHOLDER]` |
| Waste disposal procedures for biological material | `[PLACEHOLDER]` |

---

### 2.3 Protocol: Routine Cell Maintenance

#### 2.3.1 Daily Observation

> 📝 *[Describe how to assess confluence and cell health under the microscope, what healthy vs. stressed cells look like, and when to passage.]*

#### 2.3.2 Passaging Cells

> 📝 *[Step-by-step: aspirate media, PBS wash, trypsin addition (volume, incubation time), neutralization, counting (hemocytometer or automated counter), seeding density recommendations for HeLa and other lines, and flask labeling convention.]*

#### 2.3.3 Freezing Cells for Long-Term Storage

> 📝 *[Freezing medium recipe (FBS + DMSO), controlled-rate freezing (Mr. Frosty procedure), transfer to liquid nitrogen, and cryovial labeling standards.]*

#### 2.3.4 Thawing Cells

> 📝 *[Rapid thaw, dilution to remove DMSO, centrifugation, resuspension, and first-passage monitoring.]*

---

### 2.4 Protocol: Transient Transfection

#### 2.4.1 Reagent Choice

> 📝 *[Overview of lipid-based transfection (Lipofectamine, FuGENE) vs. polymer-based (PEI) vs. electroporation; which methods are used in the lab.]*

#### 2.4.2 Transfection Procedure

> 📝 *[Cell seeding density the day before, DNA:reagent ratio, complex formation steps, media change timing, and expected transfection efficiency for HeLa.]*

#### 2.4.3 Verification of Expression

> 📝 *[How to check for successful expression: fluorescence microscopy, western blot, or flow cytometry, depending on your construct.]*

---

## Section 3: Live-Cell Imaging of Biosensors

Live-cell imaging allows you to observe dynamic biological processes in real time. You will use genetically encoded biosensors — fluorescent protein-based reporters that change their signal in response to specific molecular events — to track cellular signaling over time.

### 3.1 Background

#### 3.1.1 Fluorescent Proteins & Genetically Encoded Biosensors

> 📝 *[Describe GFP and its derivatives (color variants, photostability, maturation time), FRET-based vs. intensity-based biosensors, and what molecular events the lab's biosensors are designed to report (e.g., kinase activity, second messengers, protein–protein interaction).]*

#### 3.1.2 Principles of Fluorescence Microscopy

> 📝 *[Explain excitation/emission spectra, fluorescence filters, widefield vs. confocal vs. spinning disk confocal, objective lens choices (magnification, NA, working distance), and immersion media.]*

#### 3.1.3 Phototoxicity and Photobleaching

> 📝 *[Why minimizing light exposure matters for live cells: phototoxicity mechanisms, photobleaching kinetics, and practical strategies (reduced illumination, fast cameras, optimized frame rates).]*

#### 3.1.4 Environmental Control During Imaging

> 📝 *[Importance of maintaining 37°C, 5% CO2, and humidity during time-lapse experiments; stage-top incubator vs. enclosed chamber systems available in the lab.]*

---

### 3.2 Lab-Specific Resources

| Resource | Details |
|---|---|
| Microscope(s) for live imaging and booking procedure | `[PLACEHOLDER]` |
| Acquisition software and version | `[PLACEHOLDER]` |
| Biosensor constructs available and spectral properties | `[PLACEHOLDER]` |
| Imaging dishes/plates used (glass-bottom, polymer, etc.) | `[PLACEHOLDER]` |
| CO2-independent media or buffering approach during imaging | `[PLACEHOLDER]` |
| Image analysis software | `[PLACEHOLDER]` |

---

### 3.3 Protocol: Sample Preparation for Live Imaging

#### 3.3.1 Cell Seeding onto Imaging Dishes

> 📝 *[Appropriate cell density, coating substrates (fibronectin, poly-L-lysine, collagen) if used, and lead time before imaging (hours to overnight).]*

#### 3.3.2 Transfection for Biosensor Expression

> 📝 *[Reference Section 2.4, with specific notes on DNA amount for biosensor constructs and time post-transfection optimal for imaging (to ensure expression without overexpression artifacts).]*

#### 3.3.3 Media Preparation for Imaging

> 📝 *[HEPES-buffered media or CO2-independent formulation, phenol-red-free considerations, drug/stimulus stock preparation and working concentrations.]*

---

### 3.4 Protocol: Time-Lapse Acquisition

#### 3.4.1 Microscope Setup

> 📝 *[Startup sequence, laser/lamp warmup, stage incubator equilibration time, objective selection, and Köhler illumination check.]*

#### 3.4.2 Acquisition Settings

> 📝 *[Channel configuration (laser lines/filters for your biosensor), exposure time, frame interval, total duration, Z-stack vs. single plane, and multi-position acquisition if used.]*

#### 3.4.3 Focusing and Finding Cells

> 📝 *[How to locate transfected cells by brief epifluorescence, setting up autofocus (hardware or software), and selecting representative fields.]*

#### 3.4.4 Applying Stimuli During Imaging

> 📝 *[Drug addition protocol during live imaging (perfusion vs. manual addition), timing relative to acquisition start, and controls (vehicle-only, unstimulated).]*

---

### 3.5 Protocol: Image Analysis

#### 3.5.1 Data Organization and File Formats

> 📝 *[Lab naming convention for image files, where to save data, file format (proprietary vs. OME-TIFF), and backup procedure.]*

#### 3.5.2 Basic Analysis in Fiji/ImageJ

> 📝 *[Opening files, inspecting LUTs and pixel intensities, drawing ROIs, measuring mean fluorescence intensity over time, background subtraction, and generating time-series plots.]*

#### 3.5.3 Ratiometric Analysis (if applicable)

> 📝 *[For FRET-based or dual-channel biosensors: how to compute ratio images, normalization approaches, and interpreting ratio changes as biological signal.]*

#### 3.5.4 Downstream Statistical Analysis

> 📝 *[How to export data to Excel or Python/R, typical statistical tests used in the lab for time-series comparisons, and plot conventions for figures.]*

---

### 3.6 Troubleshooting

| Symptom | Possible Causes & Actions |
|---|---|
| Cells dying during imaging | Reduce illumination intensity, shorten exposure, check temperature/CO2, try anti-phototoxicity additives (Trolox, OxyFluor) |
| Rapid photobleaching | Reduce laser power, consider a more photostable fluorescent protein variant |
| Biosensor shows no response | Verify expression level, confirm stimulus is active, check filter set and channel assignment |
| Focal drift over time | Use hardware autofocus or apply post-acquisition drift correction in Fiji |
| High background / low SNR | Adjust exposure, check for media autofluorescence, optimize cell density |

> 📝 *[Add microscope-specific or biosensor-specific troubleshooting notes.]*

---

### 3.7 Key Terms & Further Reading

**Key terms:** biosensor, FRET, genetically encoded indicator, fluorescent protein, photobleaching, phototoxicity, widefield, confocal, spinning disk, NA, working distance, point spread function, ROI, ratiometric imaging, time-lapse, z-stack, OME-TIFF

**Further reading:**
- `[PLACEHOLDER — suggest a live-cell imaging review]`
- `[PLACEHOLDER — key paper for the biosensor used in the project]`
