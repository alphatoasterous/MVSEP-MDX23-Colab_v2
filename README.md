# Russian Translation for MVSep-MDX23 Colab Fork v2.5
Please support the upstream developer!

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Q5Q811R5YI)  
# MVSep-MDX23 Colab Fork v2.5

Adaptation of MVSep-MDX23 algorithm for Colab, with few tweaks:

https://colab.research.google.com/github/jarredou/MVSEP-MDX23-Colab_v2/blob/v2.5/MVSep-MDX23-Colab.ipynb  
<br>  

Recent changes:  


**v2.5.1** *(24 SEPT 2024)*  
* better memory management (use `--large_gpu` to keep all models in memory during folder batch processing)

**v2.5** *(13 AUG 2024)*  
* Kim's MelBand-Roformer model added  


**v2.4** *(7 APR 2024)*  
* BS-Roformer models from viperx added
* MDX-InstHQ4 model added as optionnal
* Flac output
* Control input volume gain
* Filter vocals below 50Hz option
* Better chunking algo (no clicks)
* Some code cleaning

</font>
<br>

<details>
    <summary>Full changelog :</summary>
<br>
<font size=2>
<br>

[**v2.3**](https://github.com/jarredou/MVSEP-MDX23-Colab_v2/tree/v2.3)
* HQ3-Instr model replaced by VitLarge23 (thanks to MVSep)
* Improved MDXv2 processing (thanks to Anjok)
* Improved BigShifts algo (v2)
* BigShifts processing added to MDXv3 & VitLarge
* Faster folder batch processing

[**v2.2.2**](https://github.com/jarredou/MVSEP-MDX23-Colab_v2/tree/v2.2)
* Improved MDXv3 chunking code (thanks to HymnStudio)
* D1581 demo model replaced by new InstVocHQ MDXv3 model.
<br>

**v2.2.1**
* Added custom weights feature
* Fixed some bugs
* Fixed input: you can use a file or a folder as input now
<br>

**v2.2**
* Added MDXv3 compatibility
* Added MDXv3 demo model D1581 in vocals stem multiband ensemble.
* Added VOC-FT Fullband SRS instead of UVR-MDX-Instr-HQ3.
* Added 2stems feature : output only vocals/instrum (faster processing)
* Added 16bit output format option
* Added "BigShift trick" for MDX models
* Added separated overlap values for MDX, MDXv3 and Demucs
* Fixed volume compensation fine-tuning for MDX-VOC-FT
<br>

[**v2.1 (by deton24)**](https://github.com/deton24/MVSEP-MDX23-Colab_v2.1)
* Updated with MDX-VOC-FT instead of Kim Vocal 2
<br>

[**v2.0**](https://github.com/jarredou/MVSEP-MDX23-Colab_v2/tree/2.0)
* Updated with new Kim Vocal 2 & UVR-MDX-Instr-HQ3 models
* Folder batch processing
* Fixed high frequency bleed in vocals
* Fixed volume compensation for MDX models
<br>
</font>
</details>
<br>

Credits:
* [ZFTurbo/MVSep](https://github.com/ZFTurbo/MVSEP-MDX23-music-separation-model)
* Models by [Demucs](https://github.com/facebookresearch/demucs), [Anjok](https://github.com/Anjok07/ultimatevocalremovergui), [Kimberley Jensen](https://github.com/KimberleyJensen), [aufr33](https://github.com/aufr33) & viperx
* Adaptation & tweaks by [jarredou](https://github.com/jarredou/MVSEP-MDX23-Colab_v2/)
</font>
