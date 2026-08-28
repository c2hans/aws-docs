---
source_url: https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-alarm-optimization.html
---

# Alarm optimization and monitoring adjustments
<a name="idr-gs-alarm-optimization"></a>

To ensure optimal incident detection accuracy, our Incident Management Engineers continuously evaluate alarm performance against your critical workloads. We provide recommended alarm configuration changes, which you are required to make, and proactively collaborate with you and your Technical Account Managers (TAMs) to refine these settings.

When monitoring data indicates that alarms may not be aligned with your business-critical operations, such as when alerts trigger without corresponding customer impact or when alarm states fluctuate frequently, we would recommend offboarding the non-critical alarms and onboarding alarms that better reflect critical workload impact. This helps maintain the overall effectiveness of your incident response coverage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Incident Detection Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IDR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
