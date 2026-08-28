---
source_url: https://docs.aws.amazon.com/marketplace/latest/storefrontguide/setting-up-sso.html
---

# Setting up single sign-on for your organization
<a name="setting-up-sso"></a>

Single sign-on (SSO) lets your organization members sign in to AWS Marketplace Storefront with your identity provider. AWS Marketplace Storefront supports Okta and Azure Entra ID. Only organization Owners can configure SSO.

**To configure organization SSO**

1. Choose your profile avatar in the top-right corner, choose **Organization Settings**, then choose the **SSO Configuration** tab.

1. Turn on **Enable SSO**.

1. For **Identity Provider**, choose Okta or Azure Entra ID.

1. Enter the **Client ID** and **Client Secret** from your identity provider application.

1. For Okta, enter the **Domain** (for example, yourcompany.okta.com). For Azure Entra ID, enter the **Tenant ID**.

1. Choose **Save**.

1. Choose **Test Connection** to verify the configuration. The page shows the date of the last connection check.

## Related topics
<a name="setting-up-sso-related"></a>
+ [Managing team members](organizations-storefront.md#managing-team-members)
+ [Security settings](organizations-storefront.md#security-settings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
