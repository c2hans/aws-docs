---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-portals-delete-portal.html
---

# Delete a portal in API Gateway
<a name="apigateway-portals-delete-portal"></a>

When you delete a portal, it cannot be recovered and you must disable it first. If you want to remove your portal from the web, you can disable it. This lets you modify your portal and republish it later.

## Delete a portal
<a name="apigateway-portals-delete-portal-delete"></a>

The following procedure shows how to delete a portal.

**To delete a portal**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. In the main navigation pane, choose **Portals**.

1. Choose a portal.

1. If your portal is not disabled, disable it by choosing **Actions**, **Disable portal**.

   It takes a few minutes for your portal to be disabled. You can monitor the **Publish status** to see when your portal publish status is disabled.

1. After you have unpublished your portal, you can delete it. To delete your portal, choose **Actions**, **Delete portal**. Confirm your choice and choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
