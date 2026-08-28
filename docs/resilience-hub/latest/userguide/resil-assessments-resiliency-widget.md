---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/resil-assessments-resiliency-widget.html
---

# Running and managing resiliency assessments from Resiliency widget
<a name="resil-assessments-resiliency-widget"></a>

AWS Resilience Hub enables you to run assessments for applications created and managed in myApplications in Resiliency widget. Whenever you make modifications to an application, it is recommended to run a resiliency assessment from Resiliency widget or from AWS Resilience Hub console. During this assessment, the configuration of each Application Component is evaluated against established policies and best practices. Based on this evaluation, the assessment generates recommendations for setting up alarms, creating Standard Operating Procedures (SOPs), and implementing testing strategies. Implementing these configuration recommendations can enhance the speed and efficiency of your recovery procedures, ensuring faster incident response and minimizing potential downtime.

Alarm recommendations help you set alarms that detect outages. SOP recommendations provide scripts that manage common recovery processes, such as recovery from a backup. Test recommendations offer suggestions to verify your configurations work properly. For example, you can test whether an application recovers during automatic recovery processes, such as automatic scaling or load balancing because of network issues. You can test whether application alarms are triggered when resources reach their limits. You can also test how well SOPs work under the conditions that you indicate.

**Topics**
+ [Running resiliency assessments from Resiliency widget](run-assessment-resiliency-widget.md)
+ [Reviewing assessment summary in Resiliency widget](review-assessment-resliency-widget.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
