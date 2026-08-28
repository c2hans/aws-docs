---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-conda-unreal-engine.html
---

# Build an Epic Unreal Engine conda package for Deadline Cloud
<a name="examples-conda-unreal-engine"></a>

The [unreal-engine](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/unreal-engine) conda recipe builds an Epic Unreal Engine conda package.

Unlike other recipes in this repository, this one is designed to be built *locally* on a machine where Unreal Engine is already installed. Unreal Engine packages are large (UE 5.6 is approximately 20 GiB across about 80,000 files), so submitting them to a queue as a job attachment is impractical.

To use the recipe:

1. Install Unreal Engine on your Windows machine. The default source path in the recipe is the Epic Games Launcher path `C:\Program Files\Epic Games\UE_5.6`. Adjust `recipe/recipe.yaml` for your version or custom source build location.

1. Install [rattler-build](https://rattler-build.prefix.dev/) and enable Windows long path support.

1. Build and publish the package to your conda channel:

   ```
   rattler-build publish {{path-to-recipe-file}} --to {{publish-conda-channel}}
   ```

The recipe README includes step-by-step instructions for adapting it to your Unreal Engine version, including custom source builds.

The samples repository also includes [unreal-engine-openjd](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/unreal-engine-openjd), which builds the Unreal Engine Open Job Description adaptor with rattler-build for Windows and Python 3.13.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
