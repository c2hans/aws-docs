---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/ops_event_response_process_per_alert.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS10-BP02 Have a process per alert
<a name="ops_event_response_process_per_alert"></a>

 Establishing a clear and defined process for each alert in your system is essential for effective and efficient incident management. This practice ensures that every alert leads to a specific, actionable response, improving the reliability and responsiveness of your operations.

 **Desired outcome:** Every alert initiates a specific, well-defined response plan. Where possible, responses are automated, with clear ownership and a defined escalation path. Alerts are linked to an up-to-date knowledge base so that any operator can respond consistently and effectively. Responses are quick and uniform across the board, enhancing operational efficiency and reliability.

 **Common anti-patterns:**
+  Alerts have no predefined response process, leading to makeshift and delayed resolutions.
+  Alert overload causes important alerts to be overlooked.
+  Alerts are inconsistently handled due to lack of clear ownership and responsibility.

 **Benefits of establishing this best practice:**
+  Reduced alert fatigue by only raising actionable alerts.
+  Decreased mean time to resolution (MTTR) for operational issues.
+  Decreased mean time to investigate (MTTI), which helps reduce MTTR.
+  Enhanced ability to scale operational responses.
+  Improved consistency and reliability in handling operational events.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Having a process per alert involves establishing a clear response plan for each alert, automating responses where possible, and continually refining these processes based on operational feedback and evolving requirements.

### Implementation steps
<a name="implementation-steps"></a>

 The following diagram illustrates the incident management workflow within [AWS Systems Manager Incident Manager](https://aws.amazon.com/systems-manager/features/incident-manager/). It is designed to respond swiftly to operational issues by automatically creating incidents in response to specific events from [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) or [Amazon EventBridge](https://aws.amazon.com/eventbridge/). When an incident is created, either automatically or manually, Incident Manager centralizes the management of the incident, organizes relevant AWS resource information, and initiates predefined response plans. This includes running Systems Manager Automation runbooks for immediate action, as well as creating a parent operational work item in OpsCenter to track related tasks and analyses. This streamlined process speeds up and coordinates incident response across your AWS environment.

![Flowchart depicting how Incident Manager works - Amazon Q Developer in chat applications, escalation plans and contacts, and runbooks flow into response plans, which flow into incident and analysis. Amazon CloudWatch also flows into response plans.](http://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/images/incident-manager-how-it-works.png)

1.  **Use composite alarms:** Create [composite alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.html) in CloudWatch to group related alarms, reducing noise and allowing for more meaningful responses.

1.  **Integrate Amazon CloudWatch alarms with Incident Manager** Configure CloudWatch alarms to automatically create incidents in [AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/response-plans.html).

1.  **Integrate Amazon EventBridge with Incident Manager:** Create [EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) to react to events and create incidents using defined response plans.

1.  **Prepare for incidents in Incident Manager:**
   +  Establish detailed [response plans](https://docs.aws.amazon.com/incident-manager/latest/userguide/response-plans.html) in Incident Manager for each type of alert.
   +  Establish chat channels through [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/incident-manager/latest/userguide/chat.html) connected to response plans in Incident Manager, facilitating real-time communication during incidents across platforms like Slack, Microsoft Teams, and Amazon Chime.
   +  Incorporate [Systems Manager Automation runbooks](https://docs.aws.amazon.com/incident-manager/latest/userguide/runbooks.html) within Incident Manager to drive automated responses to incidents.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS04-BP01 Identify key performance indicators](ops_observability_identify_kpis.md)
+  [OPS08-BP04 Create actionable alerts](ops_workload_observability_create_alerts.md)

 **Related documents:**
+ [AWS Cloud Adoption Framework: Operations Perspective - Incident and problem management ](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/incident-and-problem-management.html)
+ [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
+ [ Setting up AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/setting-up.html)
+ [ Preparing for incidents in Incident Manager ](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-response.html)

 **Related videos:**
+ [ Top incident response tips from AWS](https://www.youtube.com/watch?v=Cu20aOvnHwA)

 **Related examples:**
+ [AWS Workshops - AWS Systems Manager Incident Manager - Automate incident response to security events ](https://catalog.workshops.aws/automate-incident-response/en-US/settingupim/onboarding)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
