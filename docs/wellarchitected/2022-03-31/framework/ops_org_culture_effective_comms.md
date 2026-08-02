---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_org_culture_effective_comms.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS03-BP04 Communications are timely, clear, and actionable
<a name="ops_org_culture_effective_comms"></a>

 Mechanisms exist and are used to provide timely notice to team members of known risks and planned events. Necessary context, details, and time (when possible) are provided to support determining if action is necessary, what action is required, and to take action in a timely manner. For example, providing notice of software vulnerabilities so that patching can be expedited, or providing notice of planned sales promotions so that a change freeze can be implemented to avoid the risk of service disruption.

 Planned events can be recorded in a change calendar or maintenance schedule so that team members can identify what activities are pending.

 On AWS, [AWS Systems Manager Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar.html) can be used to record these details. It supports programmatic checks of calendar status to determine if the calendar is open or closed to activity at a particular point of time. Operations activities can be planned around specific *approved* windows of time that are reserved for potentially disruptive activities. AWS Systems Manager Maintenance Windows allows you to schedule activities against instances and other [supported resources](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html#supported-resources-console) to automate the activities and make those activities discoverable.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Communications are timely, clear, and actionable: Mechanisms are in place to provide notification of risks or planned events in a clear and actionable way with enough notice to allow appropriate responses.
  +  Document planned activities on a change calendar and provide notifications: Provide an accessible source of information where planned events can be discovered. Provide notifications of planned events from the same system.
  +  Track events and activity that may have an impact on your workload: Monitoring vulnerability notifications and patch information to understand vulnerabilities in the wild and potential risks associated to your workload components. Provide notification to team members so that they can take action.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Systems Manager Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar.html)
+  [AWS Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html)
