---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-federate-ad-routing.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Active Directory name suffix routing
<a name="setup-net-federate-ad-routing"></a>

After the one-way forest trust has been established, complete the following steps to validate suffix routing:

1. Under **Start > All Programs > Administrative Tools**, click **Active Directory Domains and Trusts**.

   The Active Directory Domains and Trusts console opens.

1. Right-click your corporate domain and click **Properties**

   The Properties dialog for that domain opens.

1. Click the **Trusts** tab.

   The Trusts page opens.

1. Click the Amazon domain name and click **Properties**.

   The Properties page for the Amazon domain trust opens.

1. Click **Name Suffix Routing** and click **Refresh**.

   Make sure there are no conflicts to ensure that the Service Principal Names (SPNs) can resolve over the trust.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
