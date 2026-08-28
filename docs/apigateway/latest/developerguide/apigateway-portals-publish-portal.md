---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-publish-portal.html
---

# Publish a portal in API Gateway
<a name="apigateway-portals-publish-portal"></a>

For API consumers to access your portal, you must publish it. A portal URL can be discovered by anyone on the internet. We recommend that you preview and secure your portal before publishing it.

## Considerations
<a name="apigateway-portals-publish-considerations"></a>

It might take API Gateway a few minutes to publish your portal. You can monitor the **Publish status** in the console.

## Publish a portal
<a name="apigateway-portals-publish-procedure"></a>

The following procedure shows how to publish a portal.

**To publish a portal**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. In the main navigation pane, choose **Portals**.

1. Choose a portal.

1. Choose **Publish portal**.

1. (Optional) For **Description of changes**, enter a description of your change.

   When you publish a portal, we recommend that you always provide a brief description of your changes.

1. Choose **Publish**.

   It takes API Gateway a few minutes to finish publishing your portal. API Gateway provides a link to your portal when it's available.

To delete your portal, you must disable it first. For more information, see [Disable a portal in API Gateway](apigateway-portals-disable-portal.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
