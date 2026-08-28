---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-date.html
---

# AMAZON.Date
<a name="built-in-slot-date"></a>

Converts words that represent dates into a date format.

The date is provided to your intent in ISO-8601 date format. The date that your intent receives in the slot can vary depending on the specific phrase uttered by the user.
+ Utterances that map to a specific date, such as "today," "now," or "November twenty-fifth," convert to a complete date: `2020-11-25`. This defaults to dates *on or after* the current date.
+ Utterances that map to a future week, such as "next week," convert to the date of the last day of the current week. In ISO-8601 format, the week starts on Monday and ends on Sunday. For example, if today is 2020-11-25, "next week" converts to `2020-11-29`. Dates that map to the current or previous week convert to the first day of the week. For example, if today is 2020-11-25, "last week" converts to `2020-11-16`.
+ Utterances that map to a future month, but not a specific day, such as "next month," convert to the last day of the month. For example, if today is 2020-11-25, "next month" converts to `2020-12-31`. For dates that map to the current or previous month convert to the first day of the month. For example, if today is 2020-11-25, "this month" maps to `2020-11-01`.
+ Utterances that map to a future year, but not a specific month or day, such as "next year," convert to the last day of the following year. For example, if today is 2020-11-25, "next year" converts to `2021-12-31`. For dates that map to the current or previous year convert to the first day of the year. For example, if today is 2020-11-25, "last year" converts to `2019-01-01`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
