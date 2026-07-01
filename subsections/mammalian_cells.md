# Mammalian cells

Isolation and maintenance of mammalian cells *ex vivo* (in one form or another) has been around since the 19th century, but techniques that were used back then bear little resemblance to those we use today. Like bacterial cells, culturing mammalian cells requires temperature control, nutrients, and a growth substrate. Mammalian cells, though, require a finer touch and constant monitoring to ensure their survival.

Mammalian cells in culture are divided into two broad categories: primary and immortal. Primary cells are those that are harvested from an organism and either are **terminally differentiated** (lack the ability to divide) or have a limited number of cell divisions before **senescence**. Juxtapose this with immortalized cell lines, which have the ability to divide (almost) infinitely, given the proper nutrients and conditions.

## Henrietta Lacks

One of the oldest and most commonly used cell lines used today is the HeLa cell line. In 1951, [Henrietta Lacks](https://en.wikipedia.org/wiki/Henrietta_Lacks) visited Johns Hopkins Hospital and was diagnosed with cervical cancer. During the biopsy of her cervix, tissue was harvested without her consent and the cancerous cells were propagated *in vitro*. It was the first cell line that was able to divide indefinitely, instead of other cell lines that died. This feature of the cell line began the mammalian cell revolution, eventually leading to exceptional and lucrative breakthroughs in modern science.

In the following 70 years, various scientific and pharmaceutical companies profited from Lacks's cells (now called HeLa cells), licensing and selling wild-type and engineered variants as protected intellectual property. It wasn't until 2021 that Lacks's estate began to sue them for unjust enrichment. The estate has settled with Novartis and Thermo Fisher and still has active suits against others. Lacks's case offers a chilling example of the intersection between medical racism and scientific progress in the mid-20th century that continues today. This is an [article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3516052/) reviewing the book [*The Immortal Life of Henrietta Lacks*](https://en.wikipedia.org/wiki/The_Immortal_Life_of_Henrietta_Lacks) that summarizes Lacks's case as well as other cases of medical racism in the United States. The history of science is at the same time beautiful and disturbing. Understanding our collective past allows us to make scientific discoveries while preserving human dignity.

Informed consent is now a prerequisite for tissue donation, and as such a wide variety of cell lines have been ethically collected and propagated from patient samples. Many of these lines are available for purchase from the American Type Culture Collection ([ATCC](atcc.org)), a nonprofit that stores bacterial strains and various eukaryotic cell lines for scientific use.

## Growing mammalian cells

Revisiting the ecological metaphor for cell culture I referenced in the section on [bacteria](/subsections/bacteria.md), mammalian cell growth follows a similar model. In a growth vessel, adherent cells will use nutrients to divide and (for the most part) will continue to consume nutrients and divide until the population reaches carrying capacity. The carrying capacity of the growth vessel is defined not only by available nutrients, but also growth surface area and the accumulation of toxic metabolites. Population dynamics aside, these attributes of mammalian cell culture represent a handful of practical guidelines for the day-to-day maintenance of mammalian cell lines:

1. Cells like neighbors, but not too many.
2. Cells need plenty of nutrients.
3. Cells need a clean environment.

### Growth format

Mammalian cells in culture are either **adherent** or in **suspension**, which determines the vessel we use to grow them. Adherent cells *adhere* to a surface in a monolayer and require anchoring to grow. Examples of these types of cells are epithelial cells or fibroblasts, where extensive **extracellular matrix** provides a scaffold for growth. In contrast, suspension cells are grown *free-floating* in media. Examples of these are cultured white blood cells or HeLa cells that have been trained to grow in suspension. By yield, suspension cells are preferable since they are only limited to the volume of the flask. Adherent cells, however, are the most common since many techniques like microscopy require a monolayer.

Most cells experience a type of negative feedback called **contact inhibition**. During normal growth and development, cell crowding cues adjacent cells to arrest their growth, mediated by mechanical and biochemical forces. Crowding in a cell culture dish changes the phenotype of the cell line from exponential growth to a state akin to stationary phase in bacteria. Immortalized cell lines experience contact inhibition to a lesser extent than others, but will still undergo phenotypic changes upon overcrowding.

### Growth media

There are as many media formulations as there are mammalian cells, but by far the most used media is DMEM (Dulbecco's Modified Eagle Medium), whose formulation is itself derived from Eagle's Minimum Essential Medium. Base DMEM contains the following:

- **Amino acids**
  - All amino acids except aspartate, glutamate, asparagine, proline, and alanine.
- **Vitamins**
  - Choline, pantothenic acid, folic acid, niacinamide, pyridoxine, riboflavin, thiamine, inositol
- **Inorganic salts**
  - Sodium, magnesium, calcium, iron, chloride, bicarbonate, phosphate
- **Glucose**
- **A pH indicator** (typically phenol red)

Cells are never cultured in base DMEM. Instead, DMEM is supplemented with fetal bovine serum (FBS), which contains additional nutrients and growth factors that are required for cells to grow. Some formulations also require the addition of glutamine in the form of glutamine-alanine dipeptide and sodium pyruvate as an alternate energy source. An antibiotic penicillin/streptomycin is usually included to prevent accidental bacterial growth. This is what is referred to as **complete media**.

### pH

Mammalian extracellular pH is precisely controlled at around 7.4, meaning that growth media should also match this precisely. Any changes in pH can cause cells to die very quickly. As such a **buffer** is used to maintain media pH in response to increases or decreases in species that would otherwise alter the pH. The most common pH buffering system is the **bicarbonate buffering system**, which uses dissolved sodium bicarbonate in equilibrium with atmospheric $CO_{2}$ in the following equations:

$$
CO_{2}(g) \leftrightarrow CO_{2}(aq) + 2H_{2}O \leftrightarrow H_{3}O^{+} + HCO_{3}^{-}
$$

As pH decreases and the solution becomes more acidic, the sodium bicarbonate and hydronium ion forms carbon dioxide and water. The water remains, but the $CO_2$ leaves into the atmosphere. To maintain the pH at 7.4, cells are kept under an atmosphere of 5% $CO_2$, much higher than the 0.04% in room air. Most cell culture media uses the bicarbonate buffer system, but others use a combination of bicarbonate and other organic acids such as MOPS or HEPES (part of a larger class called **Good's Buffers**).

## Maintaining mammalian cells

Once cells touch the plate, a timer starts. Because most cell lines proliferate following the logistic curves discussed previously, cells will deplete nutrients and get overcrowded over time. This requires a consistent schedule of moving cells from a higher density to a lower density. We call this process **passaging** or **splitting** (these terms are practically the same, semantically there is a slight difference).

### Passaging adherent cells

Adherent cells, while they proliferate, lay down a complex network of glycoproteins called the **extracellular matrix**. This matrix is composed of proteins, polysaccharides and metal cations (mostly calcium) that cooperate to form a sticky, robust layer on which cells will grow and move. In order to remove cells from their extracellular matrix and allow them to be split effectively, we must first detach cells from their matrix. To do this, we use **trypsin** (a mixture of proteases) and **EDTA** (a metal ion chelator).

Trypsin is a complex mixture of proteases that are derived from porcine pancreases. They are natural digestive enzymes that break down the peptide bonds in proteins. These proteins are then dissolved into the solution and the cells are allowed to detach from the plate. That said, cells are sticky and have proteins that interact via intermolecular bonds mediated by calcium. Even if we just treated the cells with trypsin, the cells will still clump together due to intercellular interactions mediated by these calcium-dependent proteins. This is why we add EDTA, which binds to calcium and strip it from the calcium dependent proteins. The cells lose the ability to clump, leaving us with a single-cell suspension.

A typical workflow for splitting cells is as follows:

1. **Wash the cells with PBS two times**

    Excess protein and metal ions from leftover growth media will interfere with efficient digestion of extracellular matrix. PBS will remove proteins and metal ions that will compete for trypsin and EDTA.

2. **Add trypsin and incubate for 5-10 minutes**

    As said before, trypsin and EDTA cooperate to break down the extracellular matrix and release the intercellular bonds that hold cells both to the plate and to each other.

3. **Quench the trypsin reaction with complete growth media**

    Like everything in mammalian cell culture, trypsinizing is a balancing act. Too short of an incubation and cells will not come off of the plate; too long, and the trypsin and EDTA will start disrupting membrane proteins, leading to issues with cell viability. To stop the reaction, we resupply excess protein and calcium using complete growth media.

4. **Centrifugation of cells**

    EDTA is not itself toxic, but it can interfere with growth if left on media without sufficient excess calcium to overcome its chelation effects. Centrifuging cells gently pellets them, allowing you to remove the media and resuspend the cells in a known volume of fresh media.

5. **Count the cell suspension**

    We then count the cell suspension to determine how many cells we have to work with. You can do this using an automated cell counter (like the Countess II) or a hemocytometer and microscope.

6. **Seed new cells in a fresh plate**

    We plate a subset of our harvested cells in a new plate along with fresh media in a process called **seeding**. Seeding density varies widely with cell type. Some cells prefer growing with a lot of neighbors, some proliferate at a lower density.

When working with an established cell line, there are very often protocols in place that standardize the practice of cell maintenance. If you are working with a new cell line that requires more intensive methods development, there are several knobs to turn here to optimize the maintenance of your cell line:

1. **The number of PBS washes**: some cells secrete trypsin inhibitors and have a high amount of extracellular calcium that makes it difficult for trypsin to digest the extracellular matrix. Optimizing the number of washes can help with trypsin efficiency downstream. Lower exposure to trypsin/EDTA is always better. For recalcitrant cell lines, washing quickly with trypsin can help remove trypsin inhibitors and excess EDTA before the longer incubation.
2. **The concentration of trypsin/EDTA**: some cell lines (like HEK293 cells) are only *weakly* attached to the growth dish, and benefit from lower concentrations of trypsin/EDTA. Others like MCF10a cells are notoriously hardy and require 15-20 minutes of high trypsin/EDTA. In addition to trypsin/EDTA, there are other non-enzymatic methods of cell dissociation and gentler enzyme cocktails like Accutase that are used with particularly delicate cell lines.
3. **Trypsin quenching with growth media or PBS**: for routine passaging, resuspension in growth media is perfectly fine. For other applications like single-cell RNA-seq or plating cells in a new growth media, the media you choose to resuspend the cells in will impact your downstream experiment. Plan accordingly!
4. **Speed and duration of centrifugation**: mammalian cells can vary widely in size, shape, and fragility. It is important to ensure that centrifugation is not too aggressive in case your cell line of interest is fragile or small.
5. **Seeding density**: some cells (like embryonic stem cells) prefer to have neighbors that can secrete growth factors and signal through cell-cell interactions. Others (like HeLa or HEK293 cells) are less picky about having neighbors.

>When in doubt, ask these questions about your cell line: what organ system does it come from? Are there any established protocols for cell lines in that same organ system? Are there any special requirements for this cell line in the documentation? 

## Storing mammalian cells

### Freezing cells

As cells are passaged multiple times, they begin to take on morphological and phenotypic changes. In order to reduce issues such as senescence and cell cycle withdrawal, we will freeze down cells to cryogenic temperature (below -150 ºC). Much like bacteria, mammalian cells cannot survive being frozen in a purely water-based media, and require an anti-ice additive to maintain viable after thawing. Instead of glycerol like in bacterial cell culture, we use dimethyl sulfoxide (DMSO), which prevents ice crystal formation.

A typical workflow for freezing cells is as follows:

1. **Follow the steps from the section on splitting cells through the resuspension and counting step.**
2. **Adjust the media volume to yield a 1 million cells/mL concentration.**

    When freezing cells down, we usually freeze 1 million cells per cryovial.

3. **Add 5-10% sterile DMSO to the cell suspension.**

    DMSO inhibits ice crystal formation, but is toxic to cells in high concentrations for a long time. After this step, work quickly to prevent cytotoxicity.

4. **Aliquot 1 mL of this suspension into a cryogenic vial**

    Cryogenic vials (cryovials) are usually internally threaded, preventing contamination from exterior buffers and allowing room for expansion of the frozen mixture without rupturing the lid of the vial.

5. **Freeze slowly using a Mr. Frosty**

    There is a bit of debate whether or not this is actually important, but cell suspensions are usually frozen slowly (-1ºC/min) and thawed quickly (+100ºC/min). In order to accomplish the first, we use a bath of isopropanol at room temperature to control the rate of cooling. We place the vials into this bath, then we transfer it to the -80 ºC freezer, where the temperature slowly cools.

6. **Transfer the vials to a liquid nitrogen cell bank**

    Cells are unstable at -80 ºC and lose viability over only a few weeks at these temperatures. We store them on liquid nitrogen at -150 ºC, where they are viable for years or decades.

### Thawing cells

Cells are usually frozen slowly and thawed quickly. We try to minimize the time cells spend in DMSO and at temperatures between -150ºC and 37ºC by thawing cells and removing DMSO quickly.

A typical workflow for freezing cells is as follows:

1. **Start a water bath set at 37ºC is ready for the cells to facilitate thawing.**
2. **Remove a vial of cells from the cryostorage and immediately place in the 37ºC water bath.**

3. **When cells are thawed fully, transfer to 10X volume of full growth media**

    DMSO is toxic to cells, and diluting it down to lower levels will aid in rescuing cell viability.

4. **Centrifuge the cells**

    Pelleting the cells will allow you to aspirate off the DMSO-containing media and add fresh media to the cells

5. **Resuspend the cells and plate.**
