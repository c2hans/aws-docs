---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/Dates.html
---

# Dates
<a name="Dates"></a>

To convert dates to strings, we recommend following the ISO 8601 format, which supports lexicographical order comparisons.

The following table describes formats for representing date-time values with differing degrees of granularity. You must use components exactly as they are shown here and with exactly this punctuation. Note that the "T" appears literally in the string, to indicate the beginning of the time element, as is specified in ISO 8601.

| Granularity | String |
| --- | --- |
| Year | YYYY <br />(e.g., 1997) |
| Year and month | YYYY-MM <br />(e.g., 1997-07) |
| Complete date | YYYY-MM-DD<br />(e.g., 1997-07-16) |
| Complete date plus hours and minutes | YYYY-MM-DDThh:mmTZD <br />(e.g., 1997-07-16T19:20\+01:00) |
| Complete date plus hours, minutes and seconds | YYYY-MM-DDThh:mm:ssTZD <br />(e.g., 1997-07-16T19:20:30\+01:00) |
| Complete date plus hours, minutes, seconds and a decimal fraction of a second | YYYY-MM-DDThh:mm:ss.sTZD <br />(e.g., 1997-07-16T19:20:30.45\+01:00) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
