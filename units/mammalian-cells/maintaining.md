# Maintaining mammalian cells

Once cells touch the plate, a timer starts. Because most cell lines proliferate following the logistic curves discussed previously, cells will deplete nutrients and get overcrowded over time. This requires a consistent schedule of moving cells from a higher density to a lower density. We call this process [**passaging**](/units/glossary.md#passaging) or [**splitting**](/units/glossary.md#splitting) (these terms are practically the same, semantically there is a slight difference).

## Passaging adherent cells

Adherent cells, while they proliferate, lay down a complex network of glycoproteins called the [**extracellular matrix**](/units/glossary.md#extracellular-matrix). This matrix is composed of proteins, polysaccharides and metal cations (mostly calcium) that cooperate to form a sticky, robust layer on which cells will grow and move. In order to remove cells from their extracellular matrix and allow them to be split effectively, we must first detach cells from their matrix. To do this, we use [**trypsin**](/units/glossary.md#trypsin) (a mixture of proteases) and [**EDTA**](/units/glossary.md#edta) (a metal ion chelator).

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

    We plate a subset of our harvested cells in a new plate along with fresh media in a process called [**seeding**](/units/glossary.md#seeding). Seeding density varies widely with cell type. Some cells prefer growing with a lot of neighbors, some proliferate at a lower density.

When working with an established cell line, there are very often protocols in place that standardize the practice of cell maintenance. If you are working with a new cell line that requires more intensive methods development, there are several knobs to turn here to optimize the maintenance of your cell line:

1. **The number of PBS washes**: some cells secrete trypsin inhibitors and have a high amount of extracellular calcium that makes it difficult for trypsin to digest the extracellular matrix. Optimizing the number of washes can help with trypsin efficiency downstream. Lower exposure to trypsin/EDTA is always better. For recalcitrant cell lines, washing quickly with trypsin can help remove trypsin inhibitors and excess EDTA before the longer incubation.
2. **The concentration of trypsin/EDTA**: some cell lines (like HEK293 cells) are only *weakly* attached to the growth dish, and benefit from lower concentrations of trypsin/EDTA. Others like MCF10a cells are notoriously hardy and require 15-20 minutes of high trypsin/EDTA. In addition to trypsin/EDTA, there are other non-enzymatic methods of cell dissociation and gentler enzyme cocktails like Accutase that are used with particularly delicate cell lines.
3. **Trypsin quenching with growth media or PBS**: for routine passaging, resuspension in growth media is perfectly fine. For other applications like single-cell RNA-seq or plating cells in a new growth media, the media you choose to resuspend the cells in will impact your downstream experiment. Plan accordingly!
4. **Speed and duration of centrifugation**: mammalian cells can vary widely in size, shape, and fragility. It is important to ensure that centrifugation is not too aggressive in case your cell line of interest is fragile or small.
5. **Seeding density**: some cells (like embryonic stem cells) prefer to have neighbors that can secrete growth factors and signal through cell-cell interactions. Others (like HeLa or HEK293 cells) are less picky about having neighbors.

>When in doubt, ask these questions about your cell line: what organ system does it come from? Are there any established protocols for cell lines in that same organ system? Are there any special requirements for this cell line in the documentation? 
