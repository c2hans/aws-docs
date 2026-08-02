---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/gdu-assess-coverage-bottlerocket-ecs-ec2.html
---

# Runtime coverage and troubleshooting for ECS-EC2 Bottlerocket
<a name="gdu-assess-coverage-bottlerocket-ecs-ec2"></a>

For Bottlerocket Amazon EC2 instances in Amazon ECS clusters, GuardDuty evaluates runtime coverage at the instance level. The GuardDuty security agent runs as a host container on Bottlerocket, rather than as an installed RPM or Debian package.

Bottlerocket Amazon EC2 instances appear under the **EC2 instance runtime coverage** tab. To review coverage statistics for your Bottlerocket instances, open the GuardDuty console, choose **Runtime Monitoring** in the navigation pane, and then choose the **Runtime coverage** tab. Under **EC2 instance runtime coverage**, you can view the coverage status of each instance and filter by account ID, agent version, or coverage status. For more information, see [Reviewing coverage statistics](gdu-assess-coverage-ec2.md#review-coverage-statistics-ec2-runtime-monitoring).

## Troubleshooting Bottlerocket ECS-EC2 runtime coverage issues
<a name="bottlerocket-ecs-ec2-coverage-issues-troubleshoot"></a>

If the coverage status of your Bottlerocket Amazon EC2 instance is **Unhealthy**, you can view the reason under the **Issue** column.

The following table lists the issue types and the corresponding troubleshooting steps.

| Issue type | Issue message | Troubleshooting steps |
| --- | --- | --- |
| No Agent Reporting | Waiting for SSM notification | Receiving the SSM notification might take a few minutes.<br />Make sure that your Bottlerocket instance is SSM managed. The SSM agent runs in the Bottlerocket control container by default. Verify that the instance profile includes the `AmazonSSMManagedInstanceCore` and `AmazonEC2ContainerRegistryReadOnly` managed policies. |
| No Agent Reporting | Not applicable | Verify that the agent host container is enabled and running:[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/gdu-assess-coverage-bottlerocket-ecs-ec2.html) |
| No Agent Reporting | Not applicable | Validate that the instance has network connectivity to the Amazon ECR endpoint and the GuardDuty VPC endpoint. If your instance runs in a private subnet, make sure you have configured VPC endpoints for both Amazon ECR and GuardDuty. |
| No Agent Reporting | Not applicable | If your organization has a service control policy (SCP), confirm that the permissions boundary allows the `guardduty:SendSecurityTelemetry` permission. |
| SSM Association Creation Failed | GuardDuty SSM association already exists in your account. |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/gdu-assess-coverage-bottlerocket-ecs-ec2.html)  |
| SSM Association Creation Failed | Your account has too many SSM associations. | Choose **one** of the following two options:[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/gdu-assess-coverage-bottlerocket-ecs-ec2.html) |
| SSM Association Update Failed | GuardDuty SSM association does not exist in your account. | GuardDuty SSM association is not present in your account. Disable and then re-enable Runtime Monitoring. |
| SSM Association Deletion Failed | GuardDuty SSM association does not exist in your account. | The SSM association is not present in your account. If the SSM association was deleted intentionally, then no action is needed. |
| SSM Instance Association Execution Failed | Architectural requirements or other prerequisites are not met. | For information about verified requirements, see [Prerequisites for ECS-EC2 Bottlerocket support](prereq-runtime-monitoring-ecs-ec2-bottlerocket-support.md).<br />If you still experience this issue, check the SSM State Manager execution history:[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/gdu-assess-coverage-bottlerocket-ecs-ec2.html) |
| Agent disconnected | Not applicable |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/gdu-assess-coverage-bottlerocket-ecs-ec2.html)  |
| Agent Not Provisioned | Instances with exclusion tags are excluded from Runtime Monitoring. | GuardDuty doesn't receive runtime events from Amazon EC2 instances that are launched with the exclusion tag `GuardDutyManaged`:`false`.<br />To receive runtime events from this instance, remove the exclusion tag. |
| Agent Not Provisioned | Kernel version is lower than the supported version. | Update to the latest Bottlerocket ECS-2 or ECS-3 optimized AMI `v1.62.1` or later for automated agent configuration. |
| ECR Image Pull Failed | The agent container image could not be pulled from Amazon ECR. |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/gdu-assess-coverage-bottlerocket-ecs-ec2.html)  |
