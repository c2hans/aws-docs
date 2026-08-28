---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/welcome.html
---

# Solution to specify elastic and dynamic cloud resources as objects that can be easily referenced within AWS Network Firewall rules
<a name="welcome"></a>

Publication date: *March 2022 ([last update](revisions.md): June 2023)*

 Traditionally, firewall products are not cloud aware, and addresses allocated to dynamic instances in the cloud cannot be predetermined. As a result, customers must create rules based on ranges covering entire AWS accounts, Amazon Virtual Private Clouds (Amazon VPCs), or subnets, at odds with the security principle of least-privilege (PoLP). Such rigid dependence on hard-coded entities detracts from the dynamic, flexible, and elastic nature of the cloud infrastructure. Moreover, the challenge of keeping firewall configurations up to date when referenced endpoints are modified or removed, necessitates a high-touch process between application teams and security operations staff.

 The Dynamic Object and Rule Extensions for AWS Network Firewall solution provides an object abstraction around elastic and dynamic groups of AWS resources, so that these resources can be referenced within AWS Network Firewall (ANFW) rules, and continually and automatically synchronized as these resources scale in or out.

 This implementation guide describes architectural considerations and configuration steps for deploying Dynamic Object and Rule Extensions for AWS Network Firewall in the Amazon Web Services (AWS) Cloud. It includes links to an [AWS CloudFormation](https://aws.amazon.com/cloudformation/) template that launches and configures the AWS services required to deploy this solution using AWS best practices for security and availability.

 The guide is intended for IT architects, developers, DevOps, data analysts, and marketing technology professionals who have practical experience architecting in the AWS Cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Object and Rule Extensions for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
