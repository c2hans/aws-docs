---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/contacts-in-queue-on-specific-date.html
---

# Determine the number of contacts in a queue on a specific date
<a name="contacts-in-queue-on-specific-date"></a>

The historical metrics reports don't provide a way for you to determine how many contacts were in queue on a specific date, at a specific time.

To get this information in a historical report, you need the help of a developer. The developer uses the [GetCurrentMetricData](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetCurrentMetricData.html) API to store the data so you can look it up later.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
