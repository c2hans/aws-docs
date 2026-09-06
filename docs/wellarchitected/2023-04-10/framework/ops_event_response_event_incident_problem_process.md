---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_event_response_event_incident_problem_process.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS10-BP01 Use a process for event, incident, and problem management
<a name="ops_event_response_event_incident_problem_process"></a>

Your organization has processes to handle events, incidents, and problems. *Events* are things that occur in your workload but may not need intervention. *Incidents* are events that require intervention. *Problems* are recurring events that require intervention or cannot be resolved. You need processes to mitigate the impact of these events on your business and make sure that you respond appropriately.

When incidents and problems happen to your workload, you need processes to handle them. How will you communicate the status of the event with stakeholders? Who oversees leading the response? What are the tools that you use to mitigate the event? These are examples of some of the questions you need answer to have a solid response process.

Processes must be documented in a central location and available to anyone involved in your workload. If you don’t have a central wiki or document store, a version control repository can be used. You’ll keep these plans up to date as your processes evolve.

Problems are candidates for automation. These events take time away from your ability to innovate. Start with building a repeatable process to mitigate the problem. Over time, focus on automating the mitigation or fixing the underlying issue. This frees up time to devote to making improvements in your workload.

**Desired outcome:** Your organization has a process to handle events, incidents, and problems. These processes are documented and stored in a central location. They are updated as processes change.

**Common anti-patterns:**
+  An incident happens on the weekend and the on-call engineer doesn’t know what to do.
+  A customer sends you an email that the application is down. You reboot the server to fix it. This happens frequently.
+  There is an incident with multiple teams working independently to try to solve it.
+  Deployments happen in your workload without being recorded.

 **Benefits of establishing this best practice:**
+  You have an audit trail of events in your workload.
+  Your time to recover from an incident is decreased.
+  Team members can resolve incidents and problems in a consistent manner.
+  There is a more consolidated effort when investigating an incident.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Implementing this best practice means you are tracking workload events. You have processes to handle incidents and problems. The processes are documented, shared, and updated frequently. Problems are identified, prioritized, and fixed.

 **Customer example**

AnyCompany Retail has a portion of their internal wiki devoted to processes for event, incident, and problem management. All events are sent to [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html). Problems are identified as OpsItems in [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) and prioritized to fix, reducing undifferentiated labor. As processes change, they’re updated in their internal wiki. They use [AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html) to manage incidents and coordinate mitigation efforts.

## Implementation steps
<a name="implementation-steps"></a>

1.  Events
   +  Track events that happen in your workload, even if no human intervention is required.
   +  Work with workload stakeholders to develop a list of events that should be tracked. Some examples are completed deployments or successful patching.
   +  You can use services like [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) or [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) to generate custom events for tracking.

1.  Incidents
   +  Start by defining the communication plan for incidents. What stakeholders must be informed? How will you keep them in the loop? Who oversees coordinating efforts? We recommend standing up an internal chat channel for communication and coordination.
   +  Define escalation paths for the teams that support your workload, especially if the team doesn’t have an on-call rotation. Based on your support level, you can also file a case with Support.
   +  Create a playbook to investigate the incident. This should include the communication plan and detailed investigation steps. Include checking the [AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) in your investigation.
   +  Document your incident response plan. Communicate the incident management plan so internal and external customers understand the rules of engagement and what is expected of them. Train your team members on how to use it.
   +  Customers can use [Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html) to set up and manage their incident response plan.
   +  Enterprise Support customers can request the [Incident Management Workshop](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/#Operational_Workshops_and_Deep_Dives) from their Technical Account Manager. This guided workshop tests your existing incident response plan and helps you identify areas for improvement.

1.  Problems
   +  Problems must be identified and tracked in your ITSM system.
   +  Identify all known problems and prioritize them by effort to fix and impact to workload.
![Action priority matrix for prioritizing problems.](http://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/images/impact-effort-chart.png)
   +  Solve problems that are high impact and low effort first. Once those are solved, move on to problems to that fall into the low impact low effort quadrant.
   +  You can use [Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) to identify these problems, attach runbooks to them, and track them.

**Level of effort for the implementation plan:** Medium. You need both a process and tools to implement this best practice. Document your processes and make them available to anyone associated with the workload. Update them frequently. You have a process for managing problems and mitigating them or fixing them.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS07-BP03 Use runbooks to perform procedures](ops_ready_to_support_use_runbooks.md): Known problems need an associated runbook so that mitigation efforts are consistent.
+  [OPS07-BP04 Use playbooks to investigate issues](ops_ready_to_support_use_playbooks.md): Incidents must be investigated using playbooks.
+  [OPS11-BP02 Perform post-incident analysis](ops_evolve_ops_perform_rca_process.md): Always conduct a postmortem after you recover from an incident.

 **Related documents:**
+  [Atlassian - Incident management in the age of DevOps](https://www.atlassian.com/incident-management/devops)
+  [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html)
+  [Incident Management in the Age of DevOps and SRE](https://www.infoq.com/presentations/incident-management-devops-sre/)
+  [PagerDuty - What is Incident Management?](https://www.pagerduty.com/resources/learn/what-is-incident-management/)

 **Related videos:**
+  [AWS re:Invent 2020: Incident management in a distributed organization](https://www.youtube.com/watch?v=tyS1YDhMVos)
+  [AWS re:Invent 2021 - Building next-gen applications with event-driven architectures](https://www.youtube.com/watch?v=U5GZNt0iMZY)
+  [AWS Supports You \| Exploring the Incident Management Tabletop Exercise](https://www.youtube.com/watch?v=0m8sGDx-pRM)
+  [AWS Systems Manager Incident Manager - AWS Virtual Workshops](https://www.youtube.com/watch?v=KNOc0DxuBSY)
+  [AWS What's Next ft. Incident Manager \| AWS Events](https://www.youtube.com/watch?v=uZL-z7cII3k)

 **Related examples:**
+  [AWS Management and Governance Tools Workshop - OpsCenter](https://mng.workshop.aws/ssm/capability_hands-on_labs/opscenter.html)
+  [AWS Proactive Services – Incident Management Workshop](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/#Operational_Workshops_and_Deep_Dives)
+  [Building an event-driven application with Amazon EventBridge](https://aws.amazon.com/blogs/compute/building-an-event-driven-application-with-amazon-eventbridge/)
+  [Building event-driven architectures on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/63320e83-6abc-493d-83d8-f822584fb3cb/en-US/)

 **Related services:**
+  [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
+  [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
+  [AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html)
+  [AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html)
+  [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html)
