---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_dev_a4.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS06-BP03 Increase utilization of build environments
<a name="sus_sus_dev_a4"></a>

 Use automation and infrastructure-as-code to bring pre-production environments up when needed and take them down when not used. A common pattern is to schedule periods of availability that coincide with the working hours of your development team members. Hibernation is a useful tool to preserve the state and rapidly bring instances online only when needed. Use instance types with burst capacity, Spot Instances, elastic database services, containers, and other technologies to align development and test capacity with use.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use automation to maximize utilization of your development and test environments.
+  Use automation to manage the lifecycle of your development and test environments.
+  Use minimum viable representative environments to develop and test potential improvements.
+  Use On-Demand Instances to supplement your developer devices.
+  Use automation to maximize the efficiency of your build resources.
+  Use instance types with burst capacity, Spot Instances, and other technologies to align build capacity with use.
+  Adopt native cloud services for secure instance shell access rather than deploying fleets of bastion hosts.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
+  [Amazon EC2 Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html)
+  [What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
