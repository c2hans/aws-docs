---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/design-considerations.html
---

# Design considerations
<a name="design-considerations"></a>

## Event-driven vs. continuous polling
<a name="event-driven-vs.-continuous-polling"></a>

 This solution needs to resolve all objects for all the rules in the referenced group, which is not an incremental process. To resolve all objects for all the rules, introducing an event-driven mechanism would mean having to handle a race condition making the solution more complex, and the resolution less reliable. This would cause a high error rate on rule resolution. Therefore, the solution uses continuous polling as the main mechanism to resolve objects and rules.

## Regional deployments
<a name="regional-deployments"></a>

 This solution uses the AWS Network Firewall service which is not currently available in all AWS Regions. You must launch this solution in an AWS Region where AWS Config and AWS Network Firewall is available. For the most current availability by Region, refer to the [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) List.

 As of June 2022, this solution is supported in the following Regions:

|  **Region ID**  |  **Region name**  |
| --- | --- |
| us-east-1  | US East (N. Virginia)  |
| us-west-2  | US West (Oregon)  |
| eu-west-2  | Europe (London)  |
| ap-south-1 | Asia Pacific (Mumbai) |
| ap-southeast-1 | Asia Pacific (Singapore)  |
| ap-southeast-2  | Asia Pacific (Sydney) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Object and Rule Extensions for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
