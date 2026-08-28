---
source_url: https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-alarm-review.html
---

# Alarm review and feedback
<a name="idr-gs-alarm-review"></a>

AWS Incident Detection and Response conduct comprehensive reviews of your alarms prior to onboarding them for monitoring. Alarms are evaluated against a technical acceptance criteria including configuration parameters, data quality and alert effectiveness.

Based on this review, two types of feedback are provided:
+ Mandatory configuration requirements - these changes must be implemented for alarm acceptance.
+ Optional improvement recommendations - these changes enhance alarm effectiveness but are not mandatory for alarm acceptance.

Following alarm review completion, alarms suitable for onboarding to AWS Incident Detection and Response are onboarded for your workload's go-live.

For alarms requiring modifications, address the feedback provided and submit a [change request](idr-workloads-change-request.md) to initiate onboarding of those remaining alarms. Attach any relevant documents related to the requested updates.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Incident Detection Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IDR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
