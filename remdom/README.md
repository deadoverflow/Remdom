Remdom is a python module for generating pseudo-random numbers using something called count-switch-replay (CSR). 

This pretty much means that if repetitions are detected in generated numbers, 
algorithm will replay the entire generation process while updateing the seed until it finds numbers with 
no repetitions at all. 
This leaves us with maximum of 9 decimal long random numbers with no repetitions at all!

Notice that this is in fact beta version and may not be stable all the time but it is expected
to work 95% of the time.
You can report any unusial activity here and it will be reviewed.


USAGE:

Firstly it is important to import the remdom module, so lets go ahead and do that.

import remdom


Then to generate a random number simply call:

remdom.random(seed, decimals) 

Where "decimals" stand for amount of decimals in the random number
This function will return integer that will not contain any repetitions.

It is important to tell that futher versions of remdom module may even remove 0 as part of generated numbers to remove number rounding.
But it is still under consideration since it would drop to only 8 maximum number digits.


Have fun using this module!