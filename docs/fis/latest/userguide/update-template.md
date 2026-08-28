---
source_url: https://docs.aws.amazon.com/fis/latest/userguide/update-template.html
---

# Update an experiment template
<a name="update-template"></a>

You can update an existing experiment template. When you update an experiment template, the changes do not affect any running experiments that use the template.

**To update an experiment template using the console**

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/).

1. In the navigation pane, choose **Experiment templates**.

1. Select the experiment template, and choose **Actions**, **Update experiment template**.

1. Modify the template details as needed, and choose **Update experiment template**.

**To update an experiment template using the CLI**
Use the [update-experiment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/update-experiment-template.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
