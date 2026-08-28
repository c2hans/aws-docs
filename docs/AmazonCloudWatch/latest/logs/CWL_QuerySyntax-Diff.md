---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Diff.html
---

# diff
<a name="CWL_QuerySyntax-Diff"></a>

Compares the log events found in your requested time period with the log events from a previous time period of equal length. This way, you can look for trends and find whether specific log events are new.

Add a modifier to the `diff` command to specify the time period that you want to compare with:
+ `diff` compares the log events in the currently selected time range to the log events of the immediately preceding time range.
+ `diff previousDay` compares the log events in the currently selected time range to the log events from the same time the preceding day.
+ `diff previousWeek` compares the log events in the currently selected time range to the log events from the same time the preceding week.
+ `diff previousMonth` compares the log events in the currently selected time range to the log events from the same time the preceding month.

For more information, see [Compare (diff) with previous time ranges](CWL_AnalyzeLogData_Compare.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
