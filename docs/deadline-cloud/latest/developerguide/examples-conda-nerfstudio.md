---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-conda-nerfstudio.html
---

# Build a NeRF Studio conda package for Deadline Cloud
<a name="examples-conda-nerfstudio"></a>

The [nerfstudio](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nerfstudio) rattler-build recipe packages [NeRF Studio](https://docs.nerf.studio/) plus the following:
+ The [Splatfacto in the Wild](https://docs.nerf.studio/nerfology/methods/splatw.html) external model.
+ NeRF Studio dependencies that are not yet available on conda-forge.
+ The [nerfstudio/gsplat](https://github.com/nerfstudio-project/gsplat) package's `simple_trainer.py` example, available as the command `gsplat_simple_trainer`.
+ The [KevinXu02/splatfacto-w](https://github.com/KevinXu02/splatfacto-w) package's `export_script.py`, available as the command `splatfactow_export`.

To build this recipe, deploy the [CUDA farm CloudFormation template](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm) to create a Deadline Cloud farm with a CUDA fleet for the build, then submit the package build job:

```
./submit-package-job nerfstudio
```

To reuse conda environments between jobs, attach the [conda\_queue\_env\_improved\_caching.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/conda_queue_env_improved_caching.yaml) queue environment to your queue. Because the dependency closure of NeRF Studio contains many gigabytes of packages, caching saves significant time and bandwidth.

For a job bundle that uses this package, see [Train 3D Gaussian Splatting from video on Deadline Cloud](examples-jb-gaussian-splatting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
