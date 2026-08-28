---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-delete.html
---

# Deleting an endpoint
<a name="endpoints-delete"></a>

Endpoints can serve content until they're deleted. Delete the endpoint if it should no longer respond to playback requests. You must delete all endpoints from a channel before you can delete the channel.

**Warning**
If you delete an endpoint, the playback URL stops working.

You can use the AWS Elemental MediaPackage console, the AWS CLI, or the MediaPackage API to delete an endpoint. For information about deleting an endpoint through the AWS CLI or MediaPackage API, see the [AWS Elemental MediaPackage API Reference](https://docs.aws.amazon.com/mediapackage/latest/apireference/).

**To delete an endpoint (console)**

1. Access the channel that the endpoint is associated with, as described in [Viewing channel details](channels-view.md).

1. On the details page for the channel, under **Origin endpoints**, select the origin endpoint that you want to delete.

1. Select **Delete**.

1. In the **Delete endpoints** confirmation dialog box, choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
