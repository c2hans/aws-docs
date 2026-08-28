---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/channels-delete.html
---

# Deleting a channel in AWS Elemental MediaPackage
<a name="channels-delete"></a>

These steps show how to delete a channel to stop AWS Elemental MediaPackage from receiving further content. Before you can delete the channel, you must delete the channel's origin endpoints as described in [Deleting an endpoint in AWS Elemental MediaPackage](endpoints-delete.md). You can use the MediaPackage console, the AWS CLI, or the MediaPackage API to delete a channel.

**To delete a channel**

1. Access the channel group that the channel is associated with, as described in [Viewing channel group details in AWS Elemental MediaPackage](channel-group-view.md).

1. Select the name of the channel that you want to delete.

1. Choose **Delete**.

1. Choose **Delete** in the confirmation dialog box.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
