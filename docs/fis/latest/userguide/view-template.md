---
source_url: https://docs.aws.amazon.com/fis/latest/userguide/view-template.html
---

# View experiment templates
<a name="view-template"></a>

You can view the experiment templates that you created.

**To view an experiment template using the console**

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/).

1. In the navigation pane, choose **Experiment templates**.

1. To view information about a specific template, select the **Experiment template ID**.

1. In the **Details** section, you can view the description and stop conditions for the template.

1. To view the actions for the experiment template, choose **Actions**.

1. To view the targets for the experiment template, choose **Targets**.

1. To view the tags for the experiment template, choose **Tags**.

**To view an experiment template using the CLI**
Use the [list-experiment-templates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-experiment-templates.html) command to get a list of experiment templates, and use the [get-experiment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/get-experiment-template.html) command to get information about a specific experiment template.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
