---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-after-configuration.html
---

# After you enable Runtime Monitoring
<a name="runtime-monitoring-after-configuration"></a>

After you enable Runtime Monitoring and install GuardDuty security agent in your standalone account or multiple member accounts, you can take the following steps to ensure that the protection plan setting is working as expected, and monitor how much memory and CPU does GuardDuty security agent uses.

**Assess runtime coverage**
GuardDuty recommends you to continuously assess the coverage status of the resource where you have deployed the security agent. The coverage status could be either **Healthy** or **Unhealthy**. A **Healthy** coverage status indicates that GuardDuty is receiving the runtime events from the corresponding resource when there is an operating system-level activity.
When the coverage status becomes **Healthy** for the resource, GuardDuty is able to receive the runtime events and analyze them for threat detection. When GuardDuty detects a potential security threat in the tasks or applications running in your container workloads and instances, GuardDuty generates [GuardDuty Runtime Monitoring finding types](findings-runtime-monitoring.md).
You can also configure an Amazon EventBridge (EventBridge) to receive a notification when the coverage status changes from **Unhealthy** to **Healthy** and otherwise. For more information, see [Reviewing runtime coverage statistics and troubleshooting issues](runtime-monitoring-assessing-coverage.md).

**Set up CPU and memory monitoring for GuardDuty security agent**
After you have assessed that the coverage status shows as **Healthy**, you can evaluate the performance of the security agent for your resource type. For Amazon EKS clusters that have the security agent release v1.5 or above, GuardDuty supports configuring the parameters of the (add-on) security agent. For more information, see [Setting up CPU and memory monitoring](runtime-monitoring-setting-cpu-mem-monitoring.md).

**GuardDuty detects potential threats**
As GuardDuty starts to receive the runtime events for your resource, it starts analyzing those events. When GuardDuty detects a potential security threat in any of your Amazon EC2 instances, Amazon ECS clusters, or Amazon EKS clusters, it generates one or more [GuardDuty Runtime Monitoring finding types](findings-runtime-monitoring.md). You can access the finding details to view the impacted resource details.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
