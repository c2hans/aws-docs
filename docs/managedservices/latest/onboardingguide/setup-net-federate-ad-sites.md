---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-federate-ad-sites.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Active Directory sites and services
<a name="setup-net-federate-ad-sites"></a>

To reduce login latency, add the VPC CIDR range to your Active Directory sites and services (**Start -> Administrative Tools -> Active Directory Sites and Services**). Add the VPC CIDR range to an Active Directory Site that contains Domain Controllers that are closest to AWS.

Provide the AD site name of the site that you dedicated for AMS to your CSDM. AMS will rename the default site on the AMS side of AD to match the provided name.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
