---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/patching.html
---

# Patching
<a name="patching"></a>

 Organizations can automate their patching strategy for mutable compute environments and keep mutable instances in-line with the defined patch baseline of that application environment by using AWS Systems Manager Patch Manager and AWS Lambda. A tagging strategy for mutable instances within these environments can be managed by assigning said instances to **Patch Groups** and **Maintenance Windows**. See the following examples for a Dev → Test → Prod split. AWS prescriptive guidance is available for the [patch management of mutable instances.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patch-management-hybrid-cloud/welcome.html)

 *Table 10 - Operational tags can be environment specific*

|  Development  |  Staging  |  Production  |
| --- | --- | --- |
|  <pre>{<br />"Tags": [<br />{<br />"Key": "Maintenance Window",<br />"ResourceId": "i-012345678ab9ab111",<br />"ResourceType": "instance",<br />"Value": "cron(30 23 ? * TUE#1 *)"<br />},<br />{<br />"Key": "Name",<br />"ResourceId": "i-012345678ab9ab222",<br />"ResourceType": "instance",<br />"Value": "WEBAPP"<br />},<br />{<br />"Key": "Patch Group",<br />"ResourceId": "i-012345678ab9ab333",<br />"ResourceType": "instance",<br />"Value": "WEBAPP-DEV-AL2"<br />}<br />]<br />}<br /></pre>  |  <pre>{<br />"Tags": [<br />{<br />"Key": "Maintenance Window",<br />"ResourceId": "i-012345678ab9ab444",<br />"ResourceType": "instance",<br />"Value": "cron(30 23 ? * TUE#2 *)"<br />},<br />{<br />"Key": "Name",<br />"ResourceId": "i-012345678ab9ab555",<br />"ResourceType": "instance",<br />"Value": "WEBAPP"<br />},<br />{<br />"Key": "Patch Group",<br />"ResourceId": "i-012345678ab9ab666",<br />"ResourceType": "instance",<br />"Value": "WEBAPP-TEST-AL2"<br />}<br />]<br />}<br /></pre>  |  <pre>{<br />"Tags": [<br />{<br />"Key": "Maintenance Window",<br />"ResourceId": "i-012345678ab9ab777",<br />"ResourceType": "instance",<br />"Value": "cron(30 23 ? * TUE#3 *)"<br />},<br />{<br />"Key": "Name",<br />"ResourceId": "i-012345678ab9ab888",<br />"ResourceType": "instance",<br />"Value": "WEBAPP"<br />},<br />{<br />"Key": "Patch Group",<br />"ResourceId": "i-012345678ab9ab999",<br />"ResourceType": "instance",<br />"Value": "WEBAPP-PROD-AL2"<br />}<br />]<br />}<br /></pre>  |

 Zero-day vulnerabilities can also be managed by having tags defined to complement your patching strategy. Refer to [Avoid zero-day vulnerabilities with same-day security patching using AWS Systems Manager](https://aws.amazon.com/blogs/mt/avoid-zero-day-vulnerabilities-same-day-security-patching-aws-systems-manager/) for detailed guidance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
