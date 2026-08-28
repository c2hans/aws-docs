---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.blocked-windows.html
---

# Blocked windows and allowed windows (in UTC)
<a name="arc-zonal-autoshift.how-it-works.blocked-windows"></a>

You have the option to *block* or *allow* practice runs for specific calendar dates, or for specific time windows, that is, days and times, specified in UTC.

For example, if you have an application update scheduled to launch on May 1, 2024, and you don't want practice runs to shift traffic away at that time, you could set a blocked date for `2024-05-01`.

Or, say you run business report summaries three days a week. For this scenario, you could set the following recurring days and times as blocked windows, for example, in UTC: `MON-20:30-21:30 WED-20:30-21:30 FRI-20:30-21:30`.

Alternatively, you might decide that Wednesdays and Fridays from noon to 5:00 are the best times for ARC to start practice runs, to test your setup. For this scenario, you could set the following recurring days and times as allowed windows, for example, in UTC: `WED-12:00-17:00 FRI-12:00-17:00`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
