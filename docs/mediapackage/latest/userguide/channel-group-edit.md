---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/channel-group-edit.html
---

# Editing a channel group in AWS Elemental MediaPackage
<a name="channel-group-edit"></a>

This guides shows how to edit the description on a channel group for easier identification later from the AWS Elemental MediaPackage console. You can't edit the name of the channel group.

You can use the MediaPackage console, MediaPackage API, or AWS CLI to edit a channel group. When you're editing a channel group, don't put sensitive identifying information like customer account numbers into free-form fields such as the name or description field. MediaPackage doesn’t require that you supply any customer data. This includes when you work with MediaPackage using the MediaPackage console, MediaPackage API, AWS CLI, or AWS SDKs. Any data that you enter into MediaPackage might get picked up for inclusion in diagnostic logs or Amazon CloudWatch Events.

**To edit a channel group**

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/).

   The console shows all existing channel groups that are configured in MediaPackage.

1. Select the name of the channel group that you want to edit.

1. On the channel group's details page, choose **Edit**.

1. Edit the description for easier identification later.

1. Choose **Edit**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
