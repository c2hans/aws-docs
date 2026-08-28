---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-documenting-api-with-console.html
---

# Publish API documentation using the API Gateway console
<a name="apigateway-documenting-api-with-console"></a>

The following procedure describes how to publish a documentation version.

**To publish a documentation version using the API Gateway console**

1. In the main navigation pane, choose **Documentation**.

1. Choose **Publish documentation**.

1. Set up the publication:

   1. For **Stage**, select a stage.

   1. For **Version**, enter a version identifier, e.g., `1.0.0`.

   1. (Optional) For **Description**, enter a description.

1. Choose **Publish**.

You can now proceed to download the published documentation by exporting the documentation to an external OpenAPI file. To learn more, see [Export a REST API from API Gateway](api-gateway-export-api.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
