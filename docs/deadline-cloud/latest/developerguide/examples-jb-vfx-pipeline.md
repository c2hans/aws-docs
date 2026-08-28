---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-vfx-pipeline.html
---

# Run a VFX studio pipeline on Deadline Cloud
<a name="examples-jb-vfx-pipeline"></a>

The [vfx\_pipeline](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vfx_pipeline) sample on the GitHub website is a working shot-render-and-publish pipeline for a studio moving renders to a cloud farm. Every section of its README starts from a piece of pipeline you already run: a render scheduler, always-on render nodes, a mounted NAS, a set-project tool, or a publish step. Each section shows the Deadline Cloud mechanism it becomes.

Almost everything in the sample is a placeholder to swap for your own tooling. Blender stands in for your DCC, a trivial Python add-on for your third-party or in-house plugins, a small launcher script for your environment manager, and a local directory for your shared network drive. There is no first-party submitter; the sample is for studios that drive submission from their own launcher.

The job's step graph renders one task per frame, encodes a preview movie and thumbnail in parallel, then publishes a Version to Autodesk Flow Production Tracking (ShotGrid) with credentials read from AWS Secrets Manager. The DCC and plugins reach the farm as conda packages built from recipes included in the sample and installed at run time by a conda queue environment. Finished outputs return to shared storage through `deadline queue sync-output`.

The README includes a walkthrough that builds the packages, publishes the conda channel to Amazon S3, and submits a shot. For the building blocks the sample uses, see [Open Job Description (OpenJD) templates for Deadline Cloud](build-job-bundle.md), [Conda recipe examples for Deadline Cloud](examples-conda-recipes.md), and [Queue environment examples for Deadline Cloud](examples-queue-environments.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
