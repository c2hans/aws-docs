---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-nuke-render.html
---

# Render Foundry Nuke scripts on Deadline Cloud
<a name="examples-jb-nuke-render"></a>

The [nuke\_render](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/nuke_render) job bundle renders Nuke scripts in headless mode with the `nuke -x` command. The job creates one task per frame using the Open Job Description parameter space feature, and is restricted to Linux workers through host requirements.

The bundle includes a sample `motionblur3d_10.nk` Nuke script based on Foundry's MotionBlur3D example, configured with relative file paths and a pre-configured Write node.

To run this bundle, your queue needs Nuke available through a queue environment that installs the `nuke` and `nuke-openjd` conda packages. The [nuke-16.0 conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/nuke-16.0) in the samples repository builds a Nuke conda package you can publish to your queue's S3 conda channel.

Submit the bundle with custom parameters:

```
deadline bundle submit nuke_render/ \
  --name "My Nuke Render" \
  -p Frames="1-10" \
  -p NukeScript={{path-to-script.nk}} \
  -p OutputDir={{path-for-outputs}}
```

Or open the GUI submitter:

```
deadline bundle gui-submit nuke_render/
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
