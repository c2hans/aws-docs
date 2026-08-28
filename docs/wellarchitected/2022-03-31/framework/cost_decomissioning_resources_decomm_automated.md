---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_decomissioning_resources_decomm_automated.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST04-BP04 Decommission resources automatically
<a name="cost_decomissioning_resources_decomm_automated"></a>

 Design your workload to gracefully handle resource termination as you identify and decommission non-critical resources, resources that are not required, or resources with low utilization.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

Use automation to reduce or remove the associated costs of the decommissioning process. Designing your workload to perform automated decommissioning will reduce the overall workload costs during its lifetime. You can use [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) or [Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide) to perform the decommissioning process. You can also implement custom code using the [API or SDK](https://aws.amazon.com/developer/tools/) to decommission workload resources automatically.

**Implementation steps**
+ ** Implement Amazon EC2 Auto Scaling or Application Auto Scaling:** For resources that are supported, configure them with Amazon EC2 Auto Scaling or Application Auto Scaling.
+ ** Configure CloudWatch to terminate instances:** Instances can be configured to terminate using CloudWatch alarms. Using the metrics from the decommissioning process, implement an alarm with an Amazon Elastic Compute Cloud (Amazon EC2) action. Verify the operation in a non-production environment before rolling out.
+  **Implement code within the workload:** You can use the AWS SDK or AWS CLI to decommission workload resources. Implement code within the application that integrates with AWS and terminates or removes resources that are no longer used.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/)
+  [Getting Started with Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/GettingStartedTutorial.html)
+  [Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide)
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/)
+  [Create Alarms to Stop, Terminate, Reboot, or Recover an Instance](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingAlarmActions.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
