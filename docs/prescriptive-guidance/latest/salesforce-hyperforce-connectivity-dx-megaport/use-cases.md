---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/salesforce-hyperforce-connectivity-dx-megaport/use-cases.html
---

# Use cases
<a name="use-cases"></a>

The use cases in the following sections provide examples for how you can enable your users to have private, reliable connectivity to Hyperforce.
+ [Branch offices](branch-offices.md)
+ [VPN-connected workforce](vpn-workforce.md)
+ [Multicloud virtual desktop infrastructure](multicloud-vdi.md)

## Key considerations
<a name="key-considerations.1152564c-e748-5dfc-ad12-639adbb8420a"></a>
+ Hyperforce can be used for both private and public connectivity.
+ You can use any combination of the use cases that are described.
+ Both new Salesforce users and users who are migrating from Salesforce-managed data center infrastructure can use Hyperforce. The use cases cover both scenarios.
+ Migration of data from a Salesforce-managed data center instance to Hyperforce is managed by Salesforce behind the scenes, and doesn't use the network architecture described in these use cases.
+ Some aspects of user application logins to Hyperforce still require network connectivity to Salesforce-managed data centers. For this reason, if you require fully private connectivity, you must use SEC with Direct Connect.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
