---
source_url: https://docs.aws.amazon.com/marketplace/latest/storefrontguide/sso-storefront.html
---

# Setting up single sign-on for a storefront
<a name="sso-storefront"></a>

You can enable single sign-on (SSO) so buyers sign in to a storefront with your identity provider. AWS Marketplace Storefront supports Okta and Azure Entra ID.

**To configure storefront SSO**

1. Open the storefront, then choose the **SSO Configuration** tab.

1. Turn on **Enable SSO**.

1. For **Identity Provider**, choose Okta or Azure Entra ID.

1. Enter the **Client ID** and **Client Secret** from your identity provider application.

1. For Okta, enter the **Domain**. For Azure Entra ID, enter the **Tenant ID**.

1. Choose **Save**.

1. Choose **Test Connection** to verify the configuration.

## Related topics
<a name="sso-storefront-related"></a>
+ [Deployment](storefronts-creating-deploying.md#deployment)
+ [Setting up single sign-on for your organization](setting-up-sso.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
