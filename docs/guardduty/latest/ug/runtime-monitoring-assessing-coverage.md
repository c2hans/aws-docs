---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-assessing-coverage.html
---

# Reviewing runtime coverage statistics and troubleshooting issues
<a name="runtime-monitoring-assessing-coverage"></a>

After you enable Runtime Monitoring and the GuardDuty security agent gets deployed to your resource, GuardDuty provides coverage statistics for the corresponding resource type and individual coverage status for the resources that belong to your account. Coverage status is determined by making sure that you have enabled Runtime Monitoring, your Amazon VPC endpoint has been created, and the GuardDuty security agent for the corresponding resource has been deployed. A **Healthy** coverage status indicates that when there is a runtime event related to your resource, GuardDuty is able to receive the said runtime event through the Amazon VPC endpoint, and monitor the behavior. If there was an issue at the time of configuring Runtime Monitoring, creating an Amazon VPC endpoint, or deploying the GuardDuty security agent, the coverage status appears as **Unhealthy**. When the coverage status is unhealthy, GuardDuty will not be able to receive or monitor the runtime behavior of the corresponding resource, or generate any Runtime Monitoring findings.

The following topics will help you review coverage statistics, configure EventBridge notifications, and troubleshoot the coverage issues for a specific resource type.

**Topics**
+ [Runtime coverage and troubleshooting for Amazon EC2 instance](gdu-assess-coverage-ec2.md)
+ [Runtime coverage and troubleshooting for ECS-EC2 Bottlerocket](gdu-assess-coverage-bottlerocket-ecs-ec2.md)
+ [Runtime coverage and troubleshooting for Amazon ECS clusters](gdu-assess-coverage-ecs.md)
+ [Runtime coverage and troubleshooting for Amazon EKS clusters](eks-runtime-monitoring-coverage.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
