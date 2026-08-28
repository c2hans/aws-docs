---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-blender-render.html
---

# Render Blender scenes on Deadline Cloud
<a name="examples-jb-blender-render"></a>

The [blender\_render](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/blender_render) job bundle shows how to support a CLI application in about 100 lines of YAML. Most of the template is parameter metadata that defines parameter names, types, defaults, and user interface controls. The step definition includes a parameter space that creates a task for each frame in the Frames job parameter, and a short script that substitutes job parameters and the Frame task parameter into a command for each task.

Submit the bundle with the GUI submitter:

```
deadline bundle gui-submit blender_render/
```

Or submit from the CLI with parameter values:

```
deadline bundle submit blender_render/ \
    -p BlenderSceneFile={{path-to-scene.blend}} \
    -p OutputDir={{path-for-outputs}}
```

To run this bundle, your queue needs Blender available through a queue environment. The [blender-4.5 conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/blender-4.5) and other Blender recipes in the samples repository build conda packages you can publish to your queue's S3 conda channel.

For more information about job bundles, see [Open Job Description (OpenJD) templates for Deadline Cloud](build-job-bundle.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
