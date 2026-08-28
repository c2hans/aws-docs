---
source_url: https://docs.aws.amazon.com/IDR/latest/userguide/suppress-alarms-at-source-wcr.html
---

# Submit a workload change request to suppress alarms
<a name="suppress-alarms-at-source-wcr"></a>

If you can’t suppress alarms at the source as described in the previous section, then submit a Workload Change Request to instruct Incident Detection and Response to manually suppress monitoring of some or all of your workload’s alarms.

For detailed instructions on how to create a Workload Change Request, see [Request changes to an onboarded workload in Incident Detection and Response](https://docs.aws.amazon.com/IDR/latest/userguide/idr-workloads-change-request.html). When raising a Workload Change Request to request suppression of your alarms, make sure that you provide the following required information
+ **Workload name:** Your workload name.
+ **Account ID(s):** ID1, ID2, ID3, and so on.
+ **Change details:** Alarm Suppression
+ **Suppression start time:** Date, time, and time zone.
+ **Suppression end time:** Date, time, and time zone.
+ **Alarms to suppress:** A list of CloudWatch alarm ARNs or third party APM event identifiers to suppress.

After you create the alarm suppression Workload Change Request, you receive the following notifications from Incident Detection and Response:
+ Acknowledgement of your Workload Change Request.
+ Notification when alarms are suppressed.
+ Notification when alarms are re-enabled for monitoring.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Incident Detection Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IDR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
