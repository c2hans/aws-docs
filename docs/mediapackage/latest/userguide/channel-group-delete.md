---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/channel-group-delete.html
---

# Deleting a channel group from AWS Elemental MediaPackage
<a name="channel-group-delete"></a>

This guides shows how to delete a channel group to stop AWS Elemental MediaPackage from receiving content. Before you can delete the channel group, you must delete the channel group's channels and endpoints. For instructions, see [Deleting a channel in AWS Elemental MediaPackage](channels-delete.md) and [Deleting an endpoint in AWS Elemental MediaPackage](endpoints-delete.md). You can use the MediaPackage console, MediaPackage API, or AWS CLI to delete a channel group.

**Warning**
If you delete a channel group, you'll lose access to the egress domain URL. If that happens, you must create a new channel group to replace it.

**To delete a channel group**

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/).

   The console shows all existing channel groups that are configured in MediaPackage.

1. Select the name of the channel group that you want to delete.

1. Choose **Delete**.

1. Choose **Delete** in the confirmation dialog box.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
