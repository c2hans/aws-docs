---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_org_culture_effective_comms.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS03-BP04 Communications are timely, clear, and actionable
<a name="ops_org_culture_effective_comms"></a>

 Mechanisms exist and are used to provide timely notice to team members of known risks and planned events. Necessary context, details, and time (when possible) are provided to support determining if action is necessary, what action is required, and to take action in a timely manner. For example, providing notice of software vulnerabilities so that patching can be expedited, or providing notice of planned sales promotions so that a change freeze can be implemented to avoid the risk of service disruption. Planned events can be recorded in a change calendar or maintenance schedule so that team members can identify what activities are pending.

 **Desired outcome:**
+  Communications provide context, details, and time expectations.
+  Team members have a clear understanding of when and how to act in response to communications.
+  Leverage change calendars to provide notice of expected changes.

 **Common anti-patterns:**
+  An alert happens several times per week that is a false positive. You mute the notification each time it happens.
+  You are asked to make a change to your security groups but are not given an expectation of when it should happen.
+  You receive constant notifications in chat when systems scale up but no action is necessary. You avoid the chat channel and miss an important notification.
+  A change is made to production without informing the operations team. The change creates an alert and the on-call team is activated.

 **Benefits of establishing this best practice:**
+  Your organization avoids alert fatigue.
+  Team members can act with the necessary context and expectations.
+  Changes can be made during change windows, reducing risk.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 To implement this best practice, you must work with stakeholders across your organization to agree to communication standards. Publicize those standards to your organization. Identify and remove alerts that are false-positive or always on. Utilize change calendars so team members know when actions can be taken and what activities are pending. Verify that communications lead to clear actions with necessary context.

 **Customer example**

 AnyCompany Retail uses chat as their main communication medium. Alerts and other information populate specific channels. When someone must act, the desired outcome is clearly stated, and in many cases, they are given a runbook or playbook to use. They use a change calendar to schedule major changes to production systems.

 **Implementation steps**

1.  Analyze your alerts for false-positives or alerts that are constantly created. Remove or change them so that they start when human intervention is required. If an alert is initiated, provide a runbook or playbook.

   1.  You can use [AWS Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html) to build playbooks and runbooks for alerts.

1.  Mechanisms are in place to provide notification of risks or planned events in a clear and actionable way with enough notice to allow appropriate responses. Use email lists or chat channels to send notifications ahead of planned events.

   1.  [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) can be used to send alerts and respond to events within your organizations messaging platform.

1.  Provide an accessible source of information where planned events can be discovered. Provide notifications of planned events from the same system.

   1.  [AWS Systems Manager Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar.html) can be used to create change windows when changes can occur. This provides team members notice when they can make changes safely.

1.  Monitor vulnerability notifications and patch information to understand vulnerabilities in the wild and potential risks associated to your workload components. Provide notification to team members so that they can act.

   1.  You can subscribe to [AWS Security Bulletins](https://aws.amazon.com/security/security-bulletins/) to receive notifications of vulnerabilities on AWS.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS07-BP03 Use runbooks to perform procedures](ops_ready_to_support_use_runbooks.md) - Make communications actionable by supplying a runbook when the outcome is known.
+  [OPS07-BP04 Use playbooks to investigate issues](ops_ready_to_support_use_playbooks.md) - In the case where the outcome is unknown, playbooks can make communications actionable.

 **Related documents:**
+ [AWS Security Bulletins ](https://aws.amazon.com/security/security-bulletins)
+ [ Open CVE ](https://www.opencve.io/welcome)

 **Related examples:**
+ [ Well-Architected Labs: Inventory and Patch Management (Level 100) ](https://wellarchitectedlabs.com/operational-excellence/100_labs/100_inventory_patch_management/)

 **Related services:**
+ [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html)
+ [AWS Systems Manager Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar.html)
+ [AWS Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html)
