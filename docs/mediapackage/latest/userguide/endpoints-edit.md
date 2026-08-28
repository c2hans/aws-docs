---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints-edit.html
---

# Editing an endpoint in AWS Elemental MediaPackage
<a name="endpoints-edit"></a>

Edit the packaging preferences on an endpoint in MediaPackage to optimize the viewing experience. You can't change the container type after you save an endpoint or greyed-out fields. To serve content with a different packager, create a different endpoint.

Any edits you make that impact the video output may not be reflected for a few minutes.

You can use the MediaPackage console, MediaPackage API, or AWS CLI to edit an origin endpoint. When you're editing an origin endpoint, don't put sensitive identifying information like customer account numbers into free-form fields such as the name or description field. MediaPackage doesn’t require that you supply any customer data. This includes when you work with MediaPackage using the MediaPackage console, MediaPackage API, AWS CLI, or AWS SDKs. Any data that you enter into MediaPackage might get picked up for inclusion in diagnostic logs or Amazon CloudWatch Events.

**To edit an endpoint**

1. Access the channel that the endpoint is associated with, as described in [Viewing channel details in AWS Elemental MediaPackage](channels-view.md).

   The console shows all existing origin endpoints that are configured in MediaPackage.

1. Under **Origin endpoints**, choose the endpoint that you want to edit and then choose **Edit endpoint**.

1. Edit the endpoint options that you want to change.

1. Choose **Edit**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
