---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints-view.html
---

# Viewing an origin endpoint in AWS Elemental MediaPackage
<a name="endpoints-view"></a>

These steps shows how to view all origin endpoints that are configured in AWS Elemental MediaPackage. You can view the details about a specific endpoint to obtain its playback URL, the packaging settings, and the manifests within the endpoint. You can use the MediaPackage console, the AWS CLI, or the MediaPackage API to view the details of an endpoint.

**To view an origin endpoint**

1. Access the channel that the endpoint is associated with, as described in [Viewing channel details in AWS Elemental MediaPackage](channels-view.md).

   The console shows all existing origin endpoints that are configured in MediaPackage.

1. (Optional) To adjust your viewing preferences, choose **Preferences**. For example, you can adjust the page size and properties that you want to view.

1. To view more information about a specific origin endpoint, select that origin endpoint from the **Origin Endpoints** list. For downstream device requests, you must provide the endpoint URL from the **Endpoint URL** field or the CloudFront CDN URL.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
