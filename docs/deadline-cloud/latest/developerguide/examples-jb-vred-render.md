---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-vred-render.html
---

# Render Autodesk VRED scenes on Deadline Cloud
<a name="examples-jb-vred-render"></a>

The [vred\_render](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vred_render) job bundle renders VRED scenes using either VRED Core or VRED Pro in headless mode. It uses VRED's Python API through the `VRED_RenderScript_DeadlineCloud.py` script, which controls the rendering process, converts job template parameters into VRED API calls, and manages settings such as quality, resolution, and tiling.

The bundle provides two template options:
+ **Basic template** (`template.yaml`): Standard rendering functionality.
+ **Tiling template** (`template_tiling.yaml`): Adds region/tile-based rendering and a tile assembly step that combines rendered tiles into final images. To use this template, rename it to `template.yaml`.

The job parameters cover input and output paths, render settings such as image dimensions and DPI, render quality presets (Analytic, Realistic, Raytracing, NPR), NVIDIA DLSS options, frame control, animation settings, and tile-based rendering. When you use tile-based rendering, you must also enable GPU raytracing to prevent solid black tile outputs.

To run this bundle on a service-managed fleet, your queue needs access to the `deadline-cloud` conda channel and a GPU-enabled worker. The [vredcore-2026 conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/vredcore-2026) in the samples repository builds a VRED Core conda package. For tile assembly, the rendering environment must include the `imagemagick` conda package from the `conda-forge` channel.

Submit the bundle:

```
deadline bundle gui-submit vred_render/
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
