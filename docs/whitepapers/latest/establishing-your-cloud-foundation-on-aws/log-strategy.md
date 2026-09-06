---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/log-strategy.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Log strategy
<a name="log-strategy"></a>

Each type of log that is being collected may require a different log storage strategy. The strategy will vary depending on the type of log, frequency, retention, size, quantity, compliance, and access that may be required. Some examples of common log types are: network logs, access logs, financial logs, DNS logs, inventory records, and change management records. A common lifecycle pattern for logs is keeping them for a period of time in: standard storage, cold storage option, archival storage, and then deleted.

## Audit logs
<a name="audit-logs"></a>

We recommend that you protect your organization with a wide array of preventative controls to help you inhibit non-compliant changes. However, given the degree of self-service and agility often required by modern business, you need to ensure full transparency of changes made to at least production aspects of your environment, workloads, and data so that detective and corrective controls can be employed.

A secure, centralized repository of logs should represent the single source of truth and be tamper resistant because centralizing your audit logs provides you a clear view of what has occurred in your environment and when it happened. For example, this would be help you facilitate access to a trail during forensic investigations.

## Auditors use of audit logs
<a name="auditors-use-of-logs"></a>

If you work in a regulated industry, you will be engaging the services of an external auditing company in order to periodically assert your compliance with relevant standards. Your auditor will most likely have their own accounts as part of their own organization. They will need to analyze your log data as part of their audit process to determine whether you have remained in compliance since their last audit. It’s a benefit to both you and the auditor to grant an account they nominate in their organization read-only access to your log archive bucket(s). This will enable your auditor to proactively access and analyze your logs in their environment before they need to engage in other audit activities, such as reviewing documentation and interviewing operations staff.

As part of the audit process, your internal security team might need to have a security assurance function. This would involve conducting internal dry-runs of external audits to minimize the risk of the external audit not proceeding smoothly. This process can be conducted by your security team, though they may wish to separate security assurance-specific activities into their own account for isolation from day-to-day security operations. If you have a security assurance team separate from your security team, their function should be separated into its own account in order to enforce separation of duty.

## Configuration logs
<a name="configuration-logs"></a>

Configuration logs contain detailed information about changes in your infrastructure or applications. Configuration logs also provide a current and historical view of infrastructure or application configurations. The length of time to keep configuration logs in each lifecycle phase will heavily depend on requirements, business policies, and applicable regulations.

## Networking logs
<a name="networking-logs"></a>

Networking logs give you an overview of what is happening on your network. They can help you monitor traffic in your environment and diagnose network related issues. Due to the amount and frequency that networking logs are generated, it is common to keep them in accessible storage for a much shorter time compared to other logs. A best practice is to define the lifecycle strategy to keep your networking logs based on technical requirements, cost considerations, and the criticality of the infrastructure.
