---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_monitor_aws_resources_automate_response_monitor.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL06-BP04 Automate responses (Real-time processing and alarming)
<a name="rel_monitor_aws_resources_automate_response_monitor"></a>

 Use automation to take action when an event is detected, for example, to replace failed components.

 Alerts can invoke AWS Auto Scaling events, so that clusters react to changes in demand. Alerts can be sent to Amazon Simple Queue Service (Amazon SQS), which can serve as an integration point for third-party ticket systems. AWS Lambda can also subscribe to alerts, providing users an asynchronous serverless model that reacts to change dynamically. AWS Config continually monitors and records your AWS resource configurations, and can invoke [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) to remediate issues.

 Amazon DevOps Guru can automatically monitor application resources for anomalous behavior and deliver targeted recommendations to speed up problem identification and remediation times.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use Amazon DevOps Guru to perform automated actions. Amazon DevOps Guru can automatically monitor application resources for anomalous behavior and deliver targeted recommendations to speed up problem identification and remediation times.
  +  [What is Amazon DevOps Guru?](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html)
+  Use AWS Systems Manager to perform automated actions. AWS Config continually monitors and records your AWS resource configurations, and can invoke AWS Systems Manager Automation to remediate issues.
  +  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
    +  Create and use Systems Manager Automation documents. These define the actions that Systems Manager performs on your managed instances and other AWS resources when an automation process runs.
    +  [Working with Automation Documents (Playbooks)](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html)
+  Amazon CloudWatch sends alarm state change events to Amazon EventBridge. Create EventBridge rules to automate responses.
  +  [Creating an EventBridge Rule That Triggers on an Event from an AWS Resource](https://docs.aws.amazon.com/eventbridge/latest/userguide/create-eventbridge-rule.html)
+  Create and run a plan to automate responses.
  +  Inventory all your alert response procedures. You must plan your alert responses before you rank the tasks.
  +  Inventory all the tasks with specific actions that must be taken. Most of these actions are documented in runbooks. You must also have playbooks for alerts of unexpected events.
  +  Examine the runbooks and playbooks for all automatable actions. In general, if an action can be defined, it most likely can be automated.
  +  Rank the error-prone or time-consuming activities first. It is most beneficial to remove sources of errors and reduce time to resolution.
  +  Establish a plan to complete automation. Maintain an active plan to automate and update the automation.
  +  Examine manual requirements for opportunities for automation. Challenge your manual process for opportunities to automate.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
+  [Creating an EventBridge Rule That Triggers on an Event from an AWS Resource](https://docs.aws.amazon.com/eventbridge/latest/userguide/create-eventbridge-rule.html)
+  [One Observability Workshop](https://observability.workshop.aws/)
+  [The Amazon Builders' Library: Instrumenting distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/)
+  [What is Amazon DevOps Guru?](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html)
+  [Working with Automation Documents (Playbooks)](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html)
