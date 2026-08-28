---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/findings-data-storage-and-movement.html
---

# Security findings data storage and movement
<a name="findings-data-storage-and-movement"></a>

 Security findings metadata traverses Regions regardless of where the findings originate. Security Incident Response ingests findings from Amazon GuardDuty andAWS Security Hub CSPM across all Regions where you have enabled these services and correlates this metadata across Regions to identify distributed threats and attack patterns.

 For standard AWS Regions, findings metadata from all Regions is accessible for correlation and analysis. This cross-Region movement enables Security Incident Response to detect threats that span multiple Regions, such as an attacker moving laterally across your infrastructure.

 For AWS opt-in Regions, findings metadata follows the same replication pattern as case investigation data. Findings from opt-in Regions replicate to commercial AWS Regions (Regions other than the AWS GovCloud (US) Regions and the China Regions) for centralized analysis alongside findings from other Regions.

 The findings metadata includes only resource identifiers, finding types, and severity information—not the detailed logs or raw data that generated the findings. This metadata enables threat correlation while minimizing the volume of data that crosses Region boundaries.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
