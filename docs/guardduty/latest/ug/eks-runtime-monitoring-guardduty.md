---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-monitoring-guardduty.html
---

# EKS Runtime Monitoring in GuardDuty
<a name="eks-runtime-monitoring-guardduty"></a>

EKS Runtime Monitoring provides runtime threat detection coverage for Amazon Elastic Kubernetes Service (Amazon EKS) nodes and containers within your AWS environment. EKS Runtime Monitoring uses a GuardDuty security agent that adds runtime visibility into individual EKS workloads, for example, file access, process execution, and network connections. The GuardDuty security agent helps GuardDuty identify specific containers within your EKS clusters that are potentially compromised. It can also detect attempts to escalate privileges from an individual container to the underlying EC2 host, and the broader AWS environment.

With the availability of Runtime Monitoring, GuardDuty has consolidated the console experience for EKS Runtime Monitoring into Runtime Monitoring. GuardDuty will not migrate your EKS Runtime Monitoring settings on your behalf automatically. This requires an action at your end. If you want to continue using only EKS Runtime Monitoring, you can use the APIs or AWS CLI to check and update the existing configuration status for EKS Runtime Monitoring. However, GuardDuty recommends [Migrating from EKS Runtime Monitoring to Runtime Monitoring](migrating-from-eksrunmon-to-runtime-monitoring.md) and using Runtime Monitoring to monitor your Amazon EKS clusters.

**Topics**
+ [Configuring EKS Runtime Monitoring for multiple-account environments (API)](eks-runtime-monitoring-configuration-multiple-accounts.md)
+ [Configuring EKS Runtime Monitoring for a standalone account (API)](eks-runtime-monitoring-configuration-standalone-acc.md)
+ [Migrating from EKS Runtime Monitoring to Runtime Monitoring](migrating-from-eksrunmon-to-runtime-monitoring.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
