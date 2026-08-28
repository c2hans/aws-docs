---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-prview-portal.html
---

# Preview a portal in API Gateway
<a name="apigateway-portals-prview-portal"></a>

You can preview your portal before you publish it. API Gateway creates a short-lived URL that you can use to preview the version of your portal that customers will see once your portal is published.

## Considerations
<a name="apigateway-portals-preview-portal-considerations"></a>

The following considerations might impact how you preview a portal:
+ Try it is not enabled for your preview portal. For more information, see [Enable try it for an API Gateway product REST endpoint in your portal](apigateway-portals-try-it.md).

## Preview a portal
<a name="apigateway-portals-preview-portal-preview"></a>

The following procedure shows how to preview a portal.

**To preview a portal**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. In the main navigation pane, choose **Portals**.

1. Choose a portal.

1. Choose **Generate portal preview**.

   Do not refresh your page.

1. After API Gateway generates your preview, choose **Open portal preview**.

   Your portal preview will open in a new tab.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
