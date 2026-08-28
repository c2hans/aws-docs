---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/incident-and-problem-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Incident and problem management
<a name="incident-and-problem-management"></a>

 **Quickly restore service operations and minimize adverse business impact. **

 Monitored and observable workloads provide insight into system health and business function. For workloads to adhere to SLAs and maintain uptime, develop plans for identifying, responding to, and resolving incidents with workloads. AWS provides services that teams can use to manage minor and major incidents in an automated and repeatable way. This ensures MTTD and MTTR are reduced, and unplanned business disruption is kept to a minimum.

## Start
<a name="start-2"></a>

 Amazon CloudWatch metrics can be displayed on dashboards and integrated with alarms to send notifications to engineers. Workloads should have dashboards and alerts in place, with alerts notifying teams, not individuals. You can use SNS to send low-priority notifications to engineers through email and high-priority incidents through SMS. Alerts should notify before a problem affects users as this enables engineers to assess and remediate issues before they negatively impact business outcomes. Alerts should be created in response to a specific problem; this ensures that all alerts are relevant and engineers are conditioned to act on them immediately.

 When creating alerts, always ask these three questions:
+  Why am I monitoring this metric?
+  Who should be notified when the threshold is breached?
+  What is the business impact of a breach?

 Runbooks and playbooks should be used to diagnose and resolve incidents; initially, runbooks and playbooks can be stored in knowledge base systems or repository READMEs. *Runbooks* are a set of predetermined steps or pieces of code that perform actions, such as daemon restarts or scaling activities. Playbooks are orchestrated steps which should be used to perform complex procedures or fault investigation.

 Ensure all workloads have support contacts and that engineers understand when and how to engage with one another. Repeat incidents should be investigated by a problem management team who can work with stakeholders to identify why the issue has been occurring and develop a remediation plan. After major incidents, ensure stakeholders come together to discuss the incident in detail to prevent or reduce the impact of a future occurrence.

## Advance
<a name="advance-2"></a>

 Alerts should have human-readable messages with embedded diagnostic information so engineers can mitigate impact and diagnose faster, reducing MTTR. CloudWatch alarms can automatically cue [Amazon EC2 Auto Scaling actions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2autoscaling.html#amazonec2autoscaling-actions-as-permissions), [reboot EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-reboot.html), [create AWS Systems Manager OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-creating-OpsItems.html), and cue incident playbooks using [AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html).

 AWS Systems Manager enables immediate and automated resolution of issues. AWS provides over 300 [Systems Manager documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html) that automate common operational actions, such as running Ansible playbooks, modifying [Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html) parameters, performing Secure Shell Protocol (SSH) troubleshooting steps, and installing patches. Custom documents can run commands on Amazon EC2 instances or make API calls to the AWS control plane. Documents are JSON formatted, version controlled, and can be shared across AWS accounts, providing a mechanism to control runbooks centrally. Scripts and knowledge base articles can be translated into automation documents, which can be triggered in response to events to provide an immediate resolution.

 Major incidents cannot be resolved by one team, and coordinated steps often need to be taken to restore normal business operations. In these scenarios, you can use AWS Systems Manager Incident Manager to orchestrate an incident. Major incidents require planned processes regarding stakeholder management, incident communications, instant messaging, incident roles, and more. Engineers also need access to dashboards, documentation, tools, historical incident details, scaling processes, and the means to investigate the issue. With AWS Systems Manager Incident Manager, this information can be kept inside one AWS Systems Manager document.

 CloudWatch alarms can cue an Incident Manager playbook that starts an incident and begins an escalation plan to contact incident responders. All Incident Management information is visible with quick links for instant messaging groups. Incident commanders and engineers can walk through the steps in the playbook until the incident has been resolved. Teams can use an AWS provided playbook or create their own, with necessary customizations. These can be kept in version control systems to allow changes to be tracked over time and to ensure that one source of truth exists for how to manage incidents.

 Incident Manager provides a [post-incident analysis](https://docs.aws.amazon.com/incident-manager/latest/userguide/analysis.html) document that you can use after a major incident. This template contains AWS suggested best practices for post-incident analysis and can be modified as needed to suit your requirements. Processes, questions, timelines, follow-up actions, and summaries of the incident can be tracked centrally to prevent or reduce the impact of a future occurrence. After an incident you should perform a post-incident analysis to identify how you can detect and diagnose quicker, and what adjustments could be made to the metrics used for detection. Always ensure follow-up actions are tracked and completed; this can be done through tickets inside [OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html), and also synchronized with third-party tools such as Jira and ServiceNow using [AWS Service Management Connectors](https://docs.aws.amazon.com/smc/latest/ag/overview.html).

## Excel
<a name="excel-2"></a>

 Alerts and runbooks should be kept on a one-to-one mapping. Alerts should cue because of a genuine business reason and have a specific process to resolve the problem. Understanding workloads’ common incident scenarios is what drives the plan for immediate and automated remediation. A known response to a CloudWatch alarm could be for an engineer to manually run a runbook that restarts daemons or cues, scaling events. Within AWS, this is a process that could be executed immediately in response to an event using [Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html). This model has no human involvement, ensures responses are immediate, and has reduced margin for error. The configuration for the alarm, the triggering steps, and the runbooks can all be version controlled. This provides a central source of truth, a view of all configuration changes, and a repeatable pattern for other engineers to adopt.

 [AWS Fault Injection Simulator](https://aws.amazon.com/fis/) (FIS) can perform controlled chaos experiments to test workload resilience and engineers’ ability to respond to events. You can create [Fault injection templates](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html) to perform many [actions](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html), such as stopping instances, throttling API actions, or stressing CPUs. These activities provide insights into gaps associated with people, process, and tools, leading to reduced MTTR and MTTD, while also raising teams’ familiarity with incident management.

 Some customers may be constrained by skills and/or staff to provide 24x7x365 proactive monitoring and incident management for their AWS accounts and resources. AMS can provide that capability.

 To continuously respond to issues and resolve them instantly, you need to monitor the correct metrics, define relevant KPIs, understand failure scenarios, and have defined remediation runbooks. Initially, these runbooks can be run by humans, but as confidence and maturity grows, CloudWatch and Systems Manager can implement remediations automatically. Keep all runbooks, alarms, and configuration inside version control; this provides centralized sources of truth, auditable changes, and templated usage. To ensure incident response and remediation is fast, prepare for incidents in advance by creating Incident Manager playbooks with links, documentation, procedures, and contacts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
