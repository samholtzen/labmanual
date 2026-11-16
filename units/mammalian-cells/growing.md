# Growing mammalian cells

Revisiting the ecological metaphor for cell culture I referenced in the section on [bacteria](/units/bacteria/culture.md#the-bacterial-culture-life-cycle), mammalian cell growth follows a similar model. In a growth vessel, adherent cells will use nutrients to divide and (for the most part) will continue to consume nutrients and divide until the population reaches carrying capacity. The carrying capacity of the growth vessel is defined not only by available nutrients, but also growth surface area and the accumulation of toxic metabolites. Population dynamics aside, these attributes of mammalian cell culture represent a handful of practical guidelines for the day-to-day maintenance of mammalian cell lines:

1. Cells like neighbors, but not too many.
2. Cells need plenty of nutrients.
3. Cells need a clean environment.

## Growth format

Mammalian cells in culture are either [**adherent**](/units/glossary.md#adherent) or in [**suspension**](/units/glossary.md#suspension), which determines the vessel we use to grow them. Adherent cells *adhere* to a surface in a monolayer and require anchoring to grow. Examples of these types of cells are epithelial cells or fibroblasts, where extensive [**extracellular matrix**](/units/glossary.md#extracellular-matrix) provides a scaffold for growth. In contrast, suspension cells are grown *free-floating* in media. Examples of these are cultured white blood cells or HeLa cells that have been trained to grow in suspension. By yield, suspension cells are preferable since they are only limited to the volume of the flask. Adherent cells, however, are the most common since many techniques like microscopy require a monolayer.

Most cells experience a type of negative feedback called [**contact inhibition**](/units/glossary.md#contact-inhibition). During normal growth and development, cell crowding cues adjacent cells to arrest their growth, mediated by mechanical and biochemical forces. Crowding in a cell culture dish changes the phenotype of the cell line from exponential growth to a state akin to stationary phase in bacteria. Immortalized cell lines experience contact inhibition to a lesser extent than others, but will still undergo phenotypic changes upon overcrowding.

## Growth media

There are as many media formulations as there are mammalian cells, but by far the most used media is DMEM (Dulbecco's Modified Eagle Medium), whose formulation is itself derived from Eagle's Minimum Essential Medium. Base DMEM contains the following:

- [**Amino acids**](/units/glossary.md#amino-acids)
  - All amino acids except aspartate, glutamate, asparagine, proline, and alanine.
- [**Vitamins**](/units/glossary.md#vitamins)
  - Choline, pantothenic acid, folic acid, niacinamide, pyridoxine, riboflavin, thiamine, inositol
- [**Inorganic salts**](/units/glossary.md#inorganic-salts)
  - Sodium, magnesium, calcium, iron, chloride, bicarbonate, phosphate
- [**Glucose**](/units/glossary.md#glucose)
- [**A pH indicator**](/units/glossary.md#ph-indicator) (typically phenol red)

Cells are never cultured in base DMEM. Instead, DMEM is supplemented with fetal bovine serum (FBS), which contains additional nutrients and growth factors that are required for cells to grow. Some formulations also require the addition of glutamine in the form of glutamine-alanine dipeptide and sodium pyruvate as an alternate energy source. An antibiotic penicillin/streptomycin is usually included to prevent accidental bacterial growth. This is what is referred to as [**complete media**](/units/glossary.md#complete-media).

## pH

Mammalian extracellular pH is precisely controlled at around 7.4, meaning that growth media should also match this precisely. Any changes in pH can cause cells to die very quickly. As such a [**buffer**](/units/glossary.md#buffer) is used to maintain media pH in response to increases or decreases in species that would otherwise alter the pH. The most common pH buffering system is the [**bicarbonate buffering system**](/units/glossary.md#bicarbonate-buffering-system), which uses dissolved sodium bicarbonate in equilibrium with atmospheric $CO_{2}$ in the following equations:

$$
CO_{2}(g) \leftrightarrow CO_{2}(aq) + 2H_{2}O \leftrightarrow H_{3}O^{+} + HCO_{3}^{-}
$$

As pH decreases and the solution becomes more acidic, the sodium bicarbonate and hydronium ion forms carbon dioxide and water. The water remains, but the $CO_2$ leaves into the atmosphere. To maintain the pH at 7.4, cells are kept under an atmosphere of 5% $CO_2$, much higher than the 0.04% in room air. Most cell culture media uses the bicarbonate buffer system, but others use a combination of bicarbonate and other organic acids such as MOPS or HEPES (part of a larger class called [**Good's Buffers**](/units/glossary.md#goods-buffers)).
