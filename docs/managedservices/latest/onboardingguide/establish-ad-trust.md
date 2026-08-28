---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/establish-ad-trust.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Establish an Active Directory (AD) trust
<a name="establish-ad-trust"></a>

Before you begin to establish an Active Directory (AD) trust for your AWS Managed Services (AMS) account, make sure that the appropriate firewall ports are open.

The trust from the AMS-managed Active Directory and your corporate directory service allows you to use your corporate-managed credentials to access AMS-managed instances to perform development, test, or administrative functions.

Creating a trust connection is a two-part exercise:

First, configure a conditional forward, a DNS configuration so DNS queries know which DNS server to go to.

Second, configure a trust, an Active Directory (AD) construct to allow access from users in one domain to use resources in another domain.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
