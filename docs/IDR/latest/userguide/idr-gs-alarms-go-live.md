---
source_url: https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-alarms-go-live.html
---

# Alarms go live
<a name="idr-gs-alarms-go-live"></a>

After alarm ingestion completes, AWS Incident Detection and Response enables monitoring for your workload. From this point forward, your onboarded alarms are actively monitored and AWS Incident Detection and Response engages you per the workload's runbook when your onboarded alarms enter the **ALARM** state.

**Key outputs**
+ Your workload is confirmed as live and monitored by AWS Incident Detection and Response.

**Next steps**
+ To validate that your onboarded alarms engage AWS Incident Detection and Response as expected, see [Test onboarded workloads in Incident Detection and Response](idr-workloads-testing.md).
+ To make changes to your onboarded alarms, runbook, or workload information, see [Request changes to an onboarded workload in Incident Detection and Response](idr-workloads-change-request.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Incident Detection Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IDR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
