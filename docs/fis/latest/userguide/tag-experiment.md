---
source_url: https://docs.aws.amazon.com/fis/latest/userguide/tag-experiment.html
---

# Tag an experiment
<a name="tag-experiment"></a>

You can apply tags to experiments to help you organize them. You can also implement [tag-based IAM policies](security_iam_service-with-iam.md#security_iam_service-with-iam-tags) to control access to experiments.

**To tag an experiment using the console**

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/).

1. In the navigation pane, choose **Experiments**.

1. Select the experiment and choose **Actions**, **Manage tags**.

1. To add a new tag, choose **Add new tag**, and specify a key and value.

   To remove a tag, choose **Remove** for the tag.

1. Choose **Save**.

**To tag an experiment using the CLI**
Use the [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/tag-resource.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
