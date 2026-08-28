---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/using-a-preset-to-specify-a-job-output.html
---

# Specifying a preset
<a name="using-a-preset-to-specify-a-job-output"></a>

When you specify the outputs of your MediaConvert job, you can use an output preset instead of choosing each output setting separately.

**To specify a preset for an output using the MediaConvert console:**

1. Create a job in the usual way, as described in [Creating a job](getting-started.md#create-a-job).

1. Create output groups as described in [Step 3: Create output groups](setting-up-a-job.md#specify-output-groups).
**Tip**
Many jobs have one output for each type of device that will play the video created by the job.

1. On the **Create job** page, in the **Job** pane on the left, choose an output. Outputs are listed in the **Output groups** section, under their output group.

1. In the **Output settings** pane, choose an output preset from the **Preset** dropdown list. For more information about individual settings, choose the **Info** link next to each setting.
**Note**
The **Preset** dropdown list shows only the presets that work with the type of output group that the output is in.

1. For **Name modifier**, type a set of characters that will distinguish the files created from this output. For example, you might use **-DASH-lo-res** for the output in your DASH output group that has the lowest resolution.

1. Repeat these steps for each output in your job that you want to specify with a preset.

1. Finish creating the job as described in [Creating a job](getting-started.md#create-a-job).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
