# Generic PCR Protocol

---

## Materials
- Template DNA
- Forward primer (10 µM working stock)
- Reverse primer (10 µM working stock)
- 2X Q5 PCR Mix 
- Nuclease-free water

## Protocol

### Standard 25 µL Reaction

| Component | Volume (µL) | Final Concentration |
|---|---|---|
| Nuclease-free water | 11.5 | — |
| Forward primer (10 µM) | 0.5 | 200 nM |
| Reverse primer (10 µM) | 0.5 | 200 nM |
| 2X Q5 PCR Mix | 12.5 | 0.5–1 U |
| Template DNA | 1.0 | 1–100 ng |
| **Total** | **25.0** | |

### Preparation Steps

1. Thaw all reagents and vortex briefly to mix.
2. Prepare a **master mix** containing the PCR Mix and both amplification primers.
3. Aliquot master mix into individual PCR tubes.
4. Add template DNA to each tube.
5. Cap tubes and briefly centrifuge (1,000 × g, 5 seconds) to collect contents.

### Thermal Cycling Conditions

| Step | Temperature | Time | Cycles |
|---|---|---|---|
| Initial denaturation | 95 °C | 3 min | 1 |
| Denaturation | 95 °C | 30 sec |  |
| Annealing | 55–65 °C* | 30 sec | 25–35 |
| Extension | 72 °C | 1 min/kb |  |
| Final extension | 72 °C | 5–10 min | 1 |
| Hold | 4 °C | ∞ | — |

*Since Q5 has a higher salt concentration and a higher binding temperature than *Taq* polymerase, use an online calculator to determine the melting temperature of your primers and adjust accordintly. [This one](https://tmcalculator.neb.com/#!/main) on NEB's website is my favorite.

### Verification

1. Prepare a **1–2% agarose gel** in 1× TAE buffer with Gel Green stain (10,000X stock).
2. Load 5–10 µL of PCR product alongside a DNA ladder of appropriate size range.
    - We use the 1kb plus ladder from NEB, which has a size range of 100 - 10,000 bases
    - Depending on your yield, you might need to load much less than 5 µl.
3. Run gel at 100 V for 60 minutes.
4. Visualize on the gel imaging system.
5. Confirm a single band of the expected size.

