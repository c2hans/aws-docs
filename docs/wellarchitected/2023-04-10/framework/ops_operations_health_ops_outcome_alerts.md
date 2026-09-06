---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_operations_health_ops_outcome_alerts.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS09-BP06 Alert when operations outcomes are at risk
<a name="ops_operations_health_ops_outcome_alerts"></a>

 Whenever operations outcomes are at risk, an alert must be raised and acted upon. Operations outcomes are any activity that supports a workload in production. This includes everything from deploying new versions of applications to recovering from an outage. Operations outcomes must be treated with the same importance as business outcomes.

Software teams should identify key operations metrics and activities and build alerts for them. Alerts must be timely and actionable. If an alert is raised, a reference to a corresponding runbook or playbook should be included. Alerts without a corresponding action can lead to alert fatigue.

 **Desired outcome:** When operations activities are at risk, alerts are sent to drive action. The alerts contain context on why an alert is being raised and point to a playbook to investigate or a runbook to mitigate. Where possible, runbooks are automated and notifications are sent.

 **Common anti-patterns:**
+ You are investigating an incident and support cases are being filed. The support cases are breaching the service level agreement (SLA) but no alerts are being raised.
+ A deployment to production scheduled for midnight is delayed due to last-minute code changes. No alert is raised and the deployment hangs.
+ A production outage occurs but no alerts are sent.
+  Your deployment time consistently runs behind estimates. No action is taken to investigate.

 **Benefits of establishing this best practice:**
+  Alerting when operations outcomes are at risk boosts your ability to support your workload by staying ahead of issues.
+  Business outcomes are improved due to healthy operations outcomes.
+  Detection and remediation of operations issues are improved.
+  Overall operational health is increased.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Operations outcomes must be defined before you can alert on them. Start by defining what operations activities are most important to your organization. Is it deploying to production in under two hours or responding to a support case within a set amount of time? Your organization must define key operations activities and how they are measured so that they can be monitored, improved, and alerted on. You need a central location where workload and operations telemetry is stored and analyzed. The same mechanism should be able to raise an alert when an operations outcome is at risk.

 **Customer example**

 A CloudWatch alarm was initiated during a routine deployment at AnyCompany Retail. The lead time for deployment was breached. Amazon EventBridge created an OpsItem in AWS Systems Manager OpsCenter. The Cloud Operations team used a playbook to investigate the issue and identified that a schema change was taking longer than expected. They alerted the on-call developer and continued monitoring the deployment. Once the deployment was complete, the Cloud Operations team resolved the OpsItem. The team will analyze the incident during a postmortem.

## Implementation steps
<a name="implementation-steps"></a>

1. If you have not identified operations KPIs, metrics, and activities, work on implementing the preceding best practices to this question (OPS09-BP01 to OPS09-BP05).
   +  Support customers with [Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/) can request the [Operations KPI Workshop](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/#Operational_Workshops_and_Deep_Dives) from their Technical Account Manager. This collaborative workshop helps you define operations KPIs and metrics aligned to business goals, provided at no additional cost. Contact your Technical Account Manager to learn more.

1.  Once you have operations activities, KPIs, and metrics established, configure alerts in your observability platform. Alerts should have an action associated to them, like a playbook or runbook. Alerts without an action should be avoided.

1.  Over time, you should evaluate your operations metrics, KPIs, and activities to identify areas of improvement. Capture feedback in runbooks and playbooks from operators to identify areas for improvement in responding to alerts.

1.  Alerts should include a mechanism to flag them as a false-positive. This should lead to a review of the metric thresholds.

 **Level of effort for the implementation plan:** Medium. There are several best practices that must be in place before implementing this best practice. Once operations activities have been identified and operations KPIs established, alerts should be established.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS02-BP03 Operations activities have identified owners responsible for their performance](ops_ops_model_def_activity_owners.md): Every operation activity and outcome should have an identified owner that's responsible. This is who should be alerted when outcomes are at risk.
+  [OPS03-BP02 Team members are empowered to take action when outcomes are at risk](ops_org_culture_team_emp_take_action.md): When alerts are raised, your team should have agency to act to remedy the issue.
+  [OPS09-BP01 Identify key performance indicators](ops_operations_health_define_ops_kpis.md): Alerting on operations outcomes starts with identify operations KPIs.
+  [OPS09-BP02 Define operations metrics](ops_operations_health_design_ops_metrics.md): Establish this best practice before you start generating alerts.
+  [OPS09-BP03 Collect and analyze operations metrics](ops_operations_health_collect_analyze_ops_metrics.md): Centrally collecting operations metrics is required to build alerts.
+  [OPS09-BP04 Establish operations metrics baselines](ops_operations_health_ops_metric_baselines.md): Operations metrics baselines provide the ability to tune alerts and avoid alert fatigue.
+  [OPS09-BP05 Learn the expected patterns of activity for operations](ops_operations_health_learn_ops_usage_patterns.md): You can improve the accuracy of your alerts by understanding the activity patterns for operations events.
+  [OPS09-BP08 Validate the achievement of outcomes and the effectiveness of KPIs and metrics](ops_operations_health_biz_level_view_ops.md): Evaluate the achievement of operations outcomes to ensure that your KPIs and metrics are valid.
+  [OPS10-BP02 Have a process per alert](ops_event_response_process_per_alert.md): Every alert should have an associated runbook or playbook and provide context for the person being alerted.
+  [OPS11-BP02 Perform post-incident analysis](ops_evolve_ops_perform_rca_process.md): Conduct a post-incident analysis after the alert to identify areas for improvement.

 **Related documents:**
+  [AWS Deployment Pipelines Reference Architecture: Application Pipeline Architecture](https://pipelines.devops.aws.dev/application-pipeline/)
+  [GitLab: Getting Started with Agile / DevOps Metrics](https://about.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/devops-metrics/)

 **Related videos:**
+  [Aggregate and Resolve Operational Issues Using AWS Systems Manager OpsCenter](https://www.youtube.com/watch?v=r6ilQdxLcqY)
+  [Integrate AWS Systems Manager OpsCenter with Amazon CloudWatch Alarms](https://www.youtube.com/watch?v=Gpc7a5kVakI)
+  [Integrate Your Data Sources into AWS Systems Manager OpsCenter Using Amazon EventBridge](https://www.youtube.com/watch?v=Xmmu5mMsq3c)

 **Related examples:**
+  [Automate remediation actions for Amazon EC2 notifications and beyond using Amazon EC2 Systems Manager Automation and AWS Health](https://aws.amazon.com/blogs/mt/automate-remediation-actions-for-amazon-ec2-notifications-and-beyond-using-ec2-systems-manager-automation-and-aws-health/)
+  [AWS Management and Governance Tools Workshop - Operations 2022](https://mng.workshop.aws/operations-2022.html)
+  [Ingesting, analyzing, and visualizing metrics with DevOps Monitoring Dashboard on AWS](https://docs.aws.amazon.com/solutions/latest/devops-monitoring-dashboard-on-aws/welcome.html)

 **Related services:**
+  [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
+  [Support Proactive Services - Operations KPI Workshop](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/#Operational_Workshops_and_Deep_Dives)
+  [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html)
+  [CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)
