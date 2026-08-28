---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/security-findings-data.html
---

# Security findings data
<a name="security-findings-data"></a>

 Security Incident Response continuously ingests security findings metadata from Amazon GuardDuty and AWS Security Hub CSPM across all supported AWS Regions where you have enabled these services. This findings data includes resource identifiers, finding types, severity levels, affected resources, and detection timestamps. Unlike case investigation data, findings data is ingested automatically and continuously to enable Security Incident Response to correlate threats across your entire AWS environment.

 The findings data does not include the detailed logs or raw data that generated the findings—only the metadata about what was detected, where it was detected, and the severity of the detection. This metadata enables Security Incident Response to identify patterns, correlate related security events across Regions, and provide comprehensive threat analysis.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
