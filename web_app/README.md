# Text to handwriting


Model https://github.com/pnshiralkar/text-to-handwriting with updates (tendorflow 2) and modifications.

Implementation of handwriting generation using recurrent neural networks in tensorflow 2. 
Based on Alex Graves paper (https://arxiv.org/abs/1308.0850). 
using model: https://github.com/pnshiralkar/text-to-handwriting . 

## Install and Use
* Download zip or clone this repo and cd into the repo folder
* Install dependencies : `pip install -r requirements.txt` OR `pip3 install -r requirements.txt`
* **Run and Use :**
   * `python handwrite.py --text "Some text with minimum 50 characters" <optional arguments>`
   * `python handwrite.py --text-file /path/to/input/text.file <optional arguments>`
* Optional Arguments :
    * `--style` : Style of handwriting (0 to 7, defaults to 0)
    * `--bias` : Bias in handwriting. More bias is more unclear handwriting (0.00 to 1.00 , defaults to 0.9)
    * `--color` : Color of handwriting in RGB format ,defaults to 0,0,150 (ballpen blue)
    * `--output` : Path to output pdf file (E.g. ~/assignments/ads1.pdf), defaults to ./handwritten.pdf
    * For more information on usage, run `python handwrite.py -h`
    

