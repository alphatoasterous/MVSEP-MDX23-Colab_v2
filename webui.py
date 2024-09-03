import gradio as gr
import inference
import os
from pathlib import Path
import webbrowser as web


def path_output(input_file, output_folder, vocals_only, format):
    filename = Path(input_file).stem
    output_format = ".flac" if format == "FLAC" else ".wav"

    instrum = f"{output_folder}/{filename}_instrum{output_format}"
    instrum2 = f"{output_folder}/{filename}_instrum2{output_format}"
    vocals = f"{output_folder}/{filename}_vocals{output_format}"
    bass = f"{output_folder}/{filename}_bass{output_format}"
    drums = f"{output_folder}/{filename}_drums{output_format}"
    other = f"{output_folder}/{filename}_other{output_format}"

    files: list[str] = []

    if Path(instrum).exists():
        files.append(instrum)
    if Path(vocals).exists():
        files.append(vocals)
    if not vocals_only:
        if Path(instrum).exists():
            files.append(instrum2)
        if Path(instrum).exists():
            files.append(bass)
        if Path(instrum).exists():
            files.append(drums)
        if Path(instrum).exists():
            files.append(other)
    return files

def main():
    css = """
.button {
    width: 50%;
    margin: 0 auto;
}
"""

    with gr.Blocks(theme='NoCrypt/miku', css=css) as app:
        gr.HTML("<h1>MVSep-MDX23 Gradio Fork 🐭</h1>")
        with gr.Group():
            gr.Markdown("Input/Output config")
            with gr.Row():
                input_audio = gr.Audio(
                    label="Upload audio",
                    type="filepath")
                with gr.Column():
                    output_format = gr.Dropdown(
                        label="Output format",
                        choices=["FLAC", "PCM_16", "FLOAT"],
                        value="FLAC",
                        interactive=True)

                    separation_mode = gr.Dropdown(
                        label="Separation model",
                        choices=["Vocal/Instrumental", "4-stems"],
                        value="Vocal/Instrumental",
                        interactive=True)

                    input_gain = gr.Slider(
                        label="Input gain",
                        minimum=-6,
                        maximum=0,
                        step=3,
                        value=0)

                    restore_gain = gr.Checkbox(
                        label="Restore gain after separation")

                    filter_vocals = gr.Checkbox(
                        label="Filter vocals below 50hz")

        with gr.Group():
            with gr.Group():
                gr.Markdown("Models configuration")

                BigShifts = gr.Slider(
                    label="BigShifts",
                    minimum=1,
                    maximum=41,
                    step=1,
                    value=4,
                    interactive=True,
                    info="If BigShifts = 1, then it's turned off")
            with gr.Group():
                use_BSRoformer = gr.Checkbox(
                    label="Use BSRoformer model",
                    value=True,
                    interactive=True)

                BSRoformer_model = gr.Dropdown(
                    label="BSRofomer model",
                    choices=["ep_317_1297", "ep_368_1296"],
                    value="ep_317_1297",
                    interactive=True)

                weight_BSRoformer = gr.Slider(
                    label="Weight BSRoformer",
                    maximum=10,
                    step=1,
                    value=10,
                    interactive=True
                )

                overlap_BSRoformer = gr.Slider(
                    label="Overlap BSRoformer",
                    maximum=10,
                    step=1,
                    value=2,
                    interactive=False,
                    info="Don't touch that"
                )
            with gr.Group():
                use_InstVoc = gr.Checkbox(
                    label="Use InstVoc",
                    value=True,
                    interactive=True
                )

                weight_InstVoc = gr.Slider(
                    label="Weight InstVoc",
                    maximum=10,
                    step=1,
                    value=4,
                    interactive=True
                )

                overlap_InstVoc = gr.Slider(
                    label="Overlap InstVoc",
                    maximum=10,
                    step=1,
                    value=2,
                    interactive=False,
                    info="Don't touch that"
                )
            with gr.Group():
                use_VitLarge = gr.Checkbox(
                    label="Use VitLarge",
                    value=True,
                    interactive=True
                )

                weight_VitLarge = gr.Slider(
                    label="Weight VitLarge",
                    maximum=10,
                    step=1,
                    value=1,
                    interactive=True
                )

                overlap_VitLarge = gr.Slider(
                    label="Overlap VitLarge",
                    maximum=10,
                    step=1,
                    value=1,
                    info="Don't touch that"
                )

            with gr.Group():
                use_InstHQ4 = gr.Checkbox(
                    label="Use InstHQ4",
                    value=False,
                    interactive=True)

                weight_InstHQ4 = gr.Slider(
                    label="Weight VitLarge",
                    maximum=10,
                    step=1,
                    value=2,
                    interactive=True
                )

                overlap_InstHQ4 = gr.Slider(
                    label="Overlap InstHQ4",
                    maximum=10,
                    step=0.1,
                    value=0.1,
                    interactive=True
                )
            with gr.Group():
                use_VocFT = gr.Checkbox(
                    label="Use VocFT",
                    value=False,
                    interactive=True)

                weight_VocFT = gr.Slider(
                    label="Weight InstHQ4",
                    maximum=10,
                    step=1,
                    value=2,
                    interactive=True
                )

                overlap_VocFT = gr.Slider(
                    label="Overlap VocFT",
                    maximum=10,
                    step=0.1,
                    value=0.1,
                    interactive=True
                )
            with gr.Group():
                overlap_demucs = gr.Slider(
                    label="Overlap demucs",
                    maximum=10,
                    step=0.1,
                    value=0.1,
                    interactive=True,
                    info="demucs works only with 4-stems mode"
                )

        with gr.Group():
            with gr.Row():
                output_folder = gr.Textbox(value=os.path.abspath(os.getcwd()).replace('\\', '/') + "/output",
                                           label="Output path")

                with gr.Column():
                    gr.Markdown("Render configuration")
                    cpu = gr.Checkbox(
                        label="Use CPU",
                        value=False)

                    large_gpu = gr.Checkbox(
                        label="Use large gpu memory")

                    single_onnx = gr.Checkbox(
                        label="Use single onnx")
        with gr.Group(elem_classes=["button"]):
            separate_button = gr.Button(value="Separate")

        audio_output = gr.File(label="Output")

        @separate_button.click(inputs=[
            input_audio,
            output_folder,
            single_onnx,
            large_gpu,
            cpu,
            overlap_demucs,
            overlap_VocFT,
            overlap_InstHQ4,
            overlap_BSRoformer,
            overlap_InstVoc,
            overlap_VitLarge,
            weight_InstVoc,
            weight_VocFT,
            weight_InstHQ4,
            weight_VitLarge,
            weight_BSRoformer,
            BigShifts,
            separation_mode,
            use_BSRoformer,
            BSRoformer_model,
            use_InstVoc,
            use_VitLarge,
            use_InstHQ4,
            use_VocFT,
            output_format,
            input_gain,
            restore_gain,
            filter_vocals
        ], outputs=audio_output)
        def handle_separate(input_audio,
                            output_folder,
                            single_onnx,
                            large_gpu,
                            cpu,
                            overlap_demucs,
                            overlap_VocFT,
                            overlap_InsHQ4,
                            overlap_BSRoformer,
                            overlap_InstVoc,
                            overlap_VitLarge,
                            weight_InstVoc,
                            weight_VocFT,
                            weight_InstHQ4,
                            weight_VitLarge,
                            weight_BSRoformer,
                            BigShifts,
                            separation_mode,
                            use_BSRoformer,
                            BSRoformer_model,
                            use_InstVoc,
                            use_VitLarge,
                            use_InstHQ4,
                            use_VocFT,
                            output_format,
                            input_gain,
                            restore_gain,
                            filter_vocals):
            options = {
                "input_audio": [input_audio],
                "output_folder": output_folder,
                "large_gpu": large_gpu,
                "single_onnx": single_onnx,
                "cpu": cpu,
                "overlap_demucs": overlap_demucs,
                "overlap_VOCFT": overlap_VocFT,
                "overlap_InstHQ4": overlap_InstHQ4,
                "overlap_VitLarge": overlap_VitLarge,
                "overlap_InstVoc": overlap_InstVoc,
                "overlap_BSRoformer": overlap_BSRoformer,
                "weight_InstVoc": weight_InstVoc,
                "weight_VOCFT": weight_VocFT,
                "weight_InstHQ4": weight_InstHQ4,
                "weight_VitLarge": weight_VitLarge,
                "weight_BSRoformer": weight_BSRoformer,
                "BigShifts": BigShifts,
                "vocals_only": True if separation_mode == 'Vocal/Instrumental' else False,
                "use_BSRoformer": use_BSRoformer,
                "BSRoformer_model": BSRoformer_model,
                "use_InstVoc": use_InstVoc,
                "use_VitLarge": use_VitLarge,
                "use_InstHQ4": use_InstHQ4,
                "use_VOCFT": use_VocFT,
                "output_format": output_format,
                "input_gain": input_gain,
                "restore_gain": restore_gain,
                "filter_vocals": filter_vocals,
            }
            print(options)
            inference.options = options
            inference.predict_with_model(options)


            return path_output(input_audio, output_folder, True if separation_mode == 'Vocal/Instrumental' else False ,output_format)
    web.open('http://127.0.0.1:7860/')
    app.launch()
    

if __name__ == "__main__":
    main()
