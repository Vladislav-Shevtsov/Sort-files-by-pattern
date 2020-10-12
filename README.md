
### Goal ###
This script is aimed to sort files to folders according to their name.

### Input fiels pattern ###

Assuming that all follwing files located in a single folder:

Tul-92_S45_R2_insilico-FT-9_16bp_164bp_4u_OUT.fastq_FAREADS.fasta

Tul-92_S45_R2_insilico-FT-6_16bp_129bp_2u_OUT.fastq_FAREADS.fasta 

Tul-92_S45_R2_insilico-FT-2_16bp_139bp_2u_OUT.fastq_FAREADS.fasta

Tul-92_S45_R1_Ft-InSil6_5bp_94bp_3u_OUT.fastq_FAREADS.fasta

Tul-92_S45_R1_Ft-InSil3_4bp_152bp_3u_OUT.fastq_FAREADS.fasta

Tul-92_S45_R1_Ft-InSil14_17bp_168bp_2u_OUT.fastq_FAREADS.fasta

Tul-7_S39_R2_insilico-FT-9_16bp_164bp_4u_OUT.fastq_FAREADS.fasta

Tul-7_S39_R2_insilico-FT-6_16bp_129bp_2u_OUT.fastq_FAREADS.fasta

Tul-7_S39_R2_insilico-FT-2_16bp_139bp_2u_OUT.fastq_FAREADS.fasta

Tul-7_S39_R2_insilico-FT-1_18bp_125bp_2u_OUT.fastq_FAREADS.fasta

### Result ###
After script implmentation the files will be sorted in two different folders according to file names.

For example:

Files with following name pattern will be moved to the created folder called Tul-92_S45_R:

Tul-92_S45_R2_insilico-FT-9_16bp_164bp_4u_OUT.fastq_FAREADS.fasta

Tul-92_S45_R2_insilico-FT-6_16bp_129bp_2u_OUT.fastq_FAREADS.fasta 

Tul-92_S45_R2_insilico-FT-2_16bp_139bp_2u_OUT.fastq_FAREADS.fasta

Tul-92_S45_R1_Ft-InSil6_5bp_94bp_3u_OUT.fastq_FAREADS.fasta

Tul-92_S45_R1_Ft-InSil3_4bp_152bp_3u_OUT.fastq_FAREADS.fasta

Tul-92_S45_R1_Ft-InSil14_17bp_168bp_2u_OUT.fastq_FAREADS.fasta

Files with following name pattern will be moved to the created folder called Tul-7_S39_R:

Tul-7_S39_R2_insilico-FT-9_16bp_164bp_4u_OUT.fastq_FAREADS.fasta

Tul-7_S39_R2_insilico-FT-6_16bp_129bp_2u_OUT.fastq_FAREADS.fasta

Tul-7_S39_R2_insilico-FT-2_16bp_139bp_2u_OUT.fastq_FAREADS.fasta

Tul-7_S39_R2_insilico-FT-1_18bp_125bp_2u_OUT.fastq_FAREADS.fasta

As a result, we have two folders where we have files that correspond to folder name  

Written by Vladislav Shevtsov xatabadich(at)gmail.com

Note, script must be run in the same directory where files located.
