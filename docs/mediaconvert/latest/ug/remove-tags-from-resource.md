---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/remove-tags-from-resource.html
---

# Removing tags from an AWS Elemental MediaConvert resource
<a name="remove-tags-from-resource"></a>

The following procedure shows you how to remove tags from existing job templates, output presets, and queues using the AWS Elemental MediaConvert console.

To do this using the API, see the `PUT` method in the [Tags](https://docs.aws.amazon.com/mediaconvert/latest/apireference/tags.html) endpoint section of the *MediaConvert API Reference*.

**To remove tags from a job template, output preset, or queue (console)**

1. Open the MediaConvert console at [https://console.aws.amazon.com/mediaconvert](https://console.aws.amazon.com/mediaconvert).

1. Choose the three-bar icon on the left to access the left navigation pane.

1. Choose **Job templates**, **Output presets**, or **Queues**.

1. Choose the name of the specific resource that has tags that you want to change.

1. Choose the **Update**, **Edit queue**, or **Update preset** button in the upper right.

1. Next to any tag that you want to delete, choose **Remove**.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
