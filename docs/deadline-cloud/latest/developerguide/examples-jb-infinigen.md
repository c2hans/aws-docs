---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-infinigen.html
---

# Generate procedural 3D scenes with Infinigen on Deadline Cloud
<a name="examples-jb-infinigen"></a>

The [infinigen\_scene\_gen](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/infinigen_scene_gen) job bundle generates photorealistic 3D scenes using [Infinigen](https://infinigen.org/) on Deadline Cloud GPU workers. The bundle supports indoor rooms (dining room, bedroom, kitchen, bathroom) and outdoor nature landscapes (desert, forest, mountain, coast, arctic). Each seed produces a unique scene with different layout, furniture, materials, terrain, and vegetation. Seeds fan out as independent tasks for parallel execution across the GPU fleet.

Each scene produces rendered RGB images (1280×720), HDR EXR files, material segmentation labels, render passes (diffuse color, ambient occlusion, glossy), and camera intrinsics and extrinsics. When `RenderGroundTruth=True`, a second pass provides depth, normals, and segmentation ground truth.

The bundle requires the `infinigen` conda package built from the [Build an Infinigen conda package for Deadline Cloud](examples-conda-infinigen.md) recipe, a [conda queue environment with improved caching](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_improved_caching.yaml), and a GPU-capable Linux service-managed fleet (such as the [CUDA farm CloudFormation template](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm)).

From the `job_bundles` directory, submit the job:

```
# Single indoor dining room (~15 min)
deadline bundle submit infinigen_scene_gen/ \
  -p Frames="0-0" \
  -p SceneType="indoor" \
  -p SceneConfig="fast_solve.gin singleroom.gin" \
  -p RoomType="DiningRoom"
```

```
# 10 unique bedrooms in parallel
deadline bundle submit infinigen_scene_gen/ \
  -p Frames="0-9" \
  -p SceneType="indoor" \
  -p RoomType="Bedroom"
```

```
# Desert landscape
deadline bundle submit infinigen_scene_gen/ \
  -p Frames="0-0" \
  -p SceneType="nature" \
  -p SceneConfig="desert.gin simple.gin"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
