---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-templates.html
---

# Workflow monitor groups and templates
<a name="monitor-with-workflow-monitor-configure-templates"></a>

Before you can deploy workflow monitoring to a signal map, you must create the groups and templates for CloudWatch alarms and EventBridge notifications. The CloudWatch templates define what scenarios and thresholds will be used to trigger the alarms. The EventBridge templates will determine how these alarms are reported to you.

If you only want mappings of your connected resources and do not want to use the monitoring template capabilities of workflow monitor, signal maps can be used without CloudWatch and EventBridge templates. For more information about using signal maps, see: [Signal maps ](monitor-with-workflow-monitor-configure-signal-maps.md)

**Topics**
+ [CloudWatch alarm groups and templates for monitoring your AWS media workflow](monitor-with-workflow-monitor-configure-alarms.md)
+ [EventBridge rule groups and templates for monitoring your AWS media workflow](monitor-with-workflow-monitor-configure-notifications.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
