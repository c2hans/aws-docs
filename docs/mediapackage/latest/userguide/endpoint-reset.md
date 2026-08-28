---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoint-reset.html
---

# Resetting an endpoint in AWS Elemental MediaPackage
<a name="endpoint-reset"></a>

These steps show how to reset an origin endpoint in MediaPackage. Resetting the endpoint clears previous content from endpoint egress. For information about when you might want to reset, see [Reset for AWS Elemental MediaPackage channels and endpoints](resetting.md).

You can use the MediaPackage console, the AWS CLI, or the MediaPackage API to reset an endpoint.

**To reset an endpoint (console)**

1. Access the channel that the endpoint is associated with, as described in [Viewing channel details in AWS Elemental MediaPackage](channels-view.md).

   The console shows all existing origin endpoints that are configured in MediaPackage.

1. Under **Origin endpoints**, choose the endpoint that you want to reset and then choose **Reset history**.

   MediaPackage might return old content from this endpoint in the first 30 seconds after the endpoint reset. For best results, when possible, wait 30 seconds from endpoint reset to send playback requests to this endpoint.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
