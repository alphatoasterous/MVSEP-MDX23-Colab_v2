

# MVSep-MDX23 Gradio Fork v2.4 🐭


#####  Gradio web interface for MVSep-MDX23

------------

## Usage
Excecute start.bat and just wait until Web UI opens! 
You can configure models (not everything) if you want to experiment.

## Preview
![Preview](https://i.imgur.com/78lVl4L.jpeg "Preview")


------------




## Original README

Adaptation of MVSep-MDX23 algorithm for Colab, with few tweaks:

https://colab.research.google.com/github/jarredou/MVSEP-MDX23-Colab_v2/blob/v2.4/MVSep-MDX23-Colab.ipynb

Recent changes:
<font size=2>

**v2.4**
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

[**v2.3**](https://github.com/jarredou/MVSEP-MDX23-Colab_v2/tree/v2.3)
* HQ3-Instr model replaced by VitLarge23 (thanks to MVSep)
* Improved MDXv2 processing (thanks to Anjok)
* Improved BigShifts algo (v2)
* BigShifts processing added to MDXv3 & VitLarge
* Faster folder batch processing

<br>
<font size=2>
<br>

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

---

Original work by ZFTurbo/MVSep : https://github.com/ZFTurbo/MVSEP-MDX23-music-separation-model
