
### Goal ###
This script is aimed to sort files to folders according to their name.

### Input fiels pattern ###

Assuming that all follwing files located in a single folder:

Tul-92_S45_R2_insilico-FT-9_16bp_164bp_4u_OUT.fastq_FAREADS.fasta

Tul-92_S45_R2_insilico-FT-6_16bp_129bp_2u_OUT.fastq_FAREADS.fasta 

Tul-92_S45_R2_insilico-FT-2_16bp_139bp_2u_OUT.fastq_FAREADS.fasta

Tul-7_S39_R2_insilico-FT-9_16bp_164bp_4u_OUT.fastq_FAREADS.fasta

Tul-7_S39_R2_insilico-FT-6_16bp_129bp_2u_OUT.fastq_FAREADS.fasta

Tul-7_S39_R2_insilico-FT-2_16bp_139bp_2u_OUT.fastq_FAREADS.fasta



### Result ###
After script implmentation the files will be sorted in two different folders according to file names.

For example:

Files with following name pattern will be moved to the created folder called Tul-92_S45_R:

      Tul-92_S45_R2_insilico-FT-9_16bp_164bp_4u_OUT.fastq_FAREADS.fasta

      Tul-92_S45_R2_insilico-FT-6_16bp_129bp_2u_OUT.fastq_FAREADS.fasta 

      Tul-92_S45_R2_insilico-FT-2_16bp_139bp_2u_OUT.fastq_FAREADS.fasta

Files with following name pattern will be moved to the created folder called Tul-7_S39_R:

      Tul-7_S39_R2_insilico-FT-9_16bp_164bp_4u_OUT.fastq_FAREADS.fasta

      Tul-7_S39_R2_insilico-FT-6_16bp_129bp_2u_OUT.fastq_FAREADS.fasta

      Tul-7_S39_R2_insilico-FT-2_16bp_139bp_2u_OUT.fastq_FAREADS.fasta

As a result, there are two folders where we have loci files that correspond to folder name  

### Command line example 

python3 mv_to_folder.py /path/to/directory #This command will sort all fasta files according to their name and put them into separate folders 

Note: the script should be executed in same direcrory with fasta files, "./" argument can be used as path for current directory

Written by Shevtsov V.

#For any questions please open issue on github or email me at xatabadich(at)gmail.com

Note: script must be run in the same directory where files located.
