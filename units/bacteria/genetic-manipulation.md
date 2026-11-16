# Genetic manipulation

Bacterial genomes and genotypes can be manipulated using tools such as [**transformation**](/units/glossary.md#transformation), or introducing external genetic material into an organism. This can be simple (e.g. genetic recombination, mutagenesis) or complex (e.g. CRISPR/Cas9 editing, phage integrase). Before a bacteria can be successfully transformed, we must first do three things:

1. Ensure the bacteria are receptive to genetic manipulation.
2. Introduce the foreign DNA or mutagen to the cell.
3. Select only the cells that are transformed.

## Bacterial competence and transformation

A bacterium is described as [**competent**](/units/glossary.md#competent) if it can take up exogenous DNA from its environment. In nature, bacteria are constantly exchanging genetic information that can aid in environmental fitness in a process called [**horizontal gene transfer**](/units/glossary.md#horizontal-gene-transfer). The most common way of bacterial transformation in the environment is by the use of the F-pilus, which acts as a bridge that connects two bacteria sharing genetic information. Since most *E. coli* strains used in cloning have been engineered to lack the F-pilus genes, we instead use one of the other means of generating competent bacteria: chemical competence and electrocompetence.

A bacteria is said to have "chemical competence" if it can be transformed through the process of [**heat shock**](/units/glossary.md#heat-shock). During this process, a bacterial cell is incubated with the external DNA, the plasmid of interest, and calcium ions. The calcium ions neutralize the negative charge on both the DNA and the membrane of the bacterium, overcoming the repulsion and allowing them to be brought close to each other. The sample is then heated from 4 ºC to 42 ºC for a short period of time, generating small holes in the bacterial cell membrane and allowing the plasmid to enter the cell. After cooling, the plasmid is locked in the cell and it is considered "transformed". Chemical transformation is fast but is quite inefficient, useful for routine cloning.

A bacteria is "electrocompetent" if it can be electroporated. In this technique, a bacterial culture is suspended in a solution of DNA without salts and subjected to a strong electric field. The field rips holes in the plasma membrane and forces the plasmids into the bacteria. After the field is removed, the holes heal and the bacterium is considered "transformed". Electroporation requires more intensive preparation of competent cells and is more prone to failure due to electrical shorts, but boasts a very high transformation efficiency compared to chemical transformation. This is why electroporation is used for cloning large libraries of plasmids instead of individual clones.

Competent cells are always captured during early [**log phase**](/units/glossary.md#log-phase). At this point, the cells are growing rapidly and are more receptive to external DNA than they are during stationary phase. This is why timing is again so crucial to efficient transformation.

## Selection of transformants

Immediately after transformation, the billions of bacteria in the sample are a mixed population: cells with the plasmid of interest and cells without. We are then required to *select*, somehow, the cells that were successfully transformed. In most plasmids, we include a [**selection marker**](/units/glossary.md#selection-marker), a gene that confers resistance to an antibiotic. When we apply this antibiotic to the mixed population, the cells that do not harbor the modification will die, leaving a population containing cells that were transformed successfully.
