---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-get-feature-monitoring-onboarding.html
---

# Onboarding Accelerate monitoring
<a name="acc-get-feature-monitoring-onboarding"></a>

Monitoring is enabled by default for all new resources except Amazon EC2 instances. You can start monitoring your Amazon EC2 instances by tagging your instances.

To onboard monitoring, first make sure that your configuration monitors the resources that you want AMS to monitor, and ignores the resources that you want it to ignore.

You can use the following CloudWatch dashboards to explore how many of your resources are targeted by AMS monitoring and tagging, and how many are not. In your account, navigate to the CloudWatch dashboards console, and select one of the following:
+ AMS-Alarm-Manager-Reporting-Dashboard
+ AMS-Resource-Tagger-Reporting-Dashboard

For a complete description of the dashboard metrics, see:
+ [Viewing the number of resources managed by Resource Tagger](acc-rt-using.md#acc-rt-number-of-resources)

## Onboarding resources to be monitored in Accelerate
<a name="acc-get-feature-monitoring-onboarding-resources"></a>

To override the default behavior, for example, to disable default monitoring for non-EC2 resources, you need to untag those resources using a custom configuration profile. For more information about tagging for monitoring, see [Monitoring in Accelerate](acc-tag-req-mon.md).

Monitoring is disabled for EC2 instances until you onboard your instances, which includes tagging your instances using a custom configuration profile. The next section describes EC2 instance onboarding.

## Creating a monitoring configuration profile in Accelerate
<a name="acc-get-feature-monitoring-onboarding-profile"></a>
+ For information about using the default configuration, see [Accelerate Alarm Manager](acc-mem-tag-alarms.md).
+ For information about using a custom configuration, see [Modifying the Accelerate alarm default configuration](acc-mem-modify-default.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
