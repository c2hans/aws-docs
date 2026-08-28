---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-presets.html
---

# Working with output presets
<a name="working-with-presets"></a>

Output presets reduce the amount of time it takes to configure a job by providing pre-configured output settings. You can also use presets as a reference for recommended settings.

This chapter provides step-by-step instructions on how to work with MediaConvert presets. In addition to applying presets to jobs or templates, you can also create, modify, delete, and list presets.

Presets apply to a single output of a transcoding job. If you want to apply settings for an *entire* job, see [Working with job templates](working-with-job-templates.md).

You can use a system preset with settings already configured for you, or you can create a custom preset with your own settings. You can create a custom preset from scratch, starting with only the default settings, or you can duplicate a system preset, adjust it to suit your workflow, and then save it as a custom preset.

**Topics**
+ [Specifying a preset](using-a-preset-to-specify-a-job-output.md)
+ [Creating a preset](creating-preset-from-scratch.md)
+ [Creating a preset, based on a system preset](create-custom-preset-from-system-preset.md)
+ [Modifying a preset](modifying-presets.md)
+ [Listing presets](listing-presets.md)
+ [Deleting a custom preset](deleting-a-preset.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
