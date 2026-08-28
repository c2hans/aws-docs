---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-percent.html
---

# AMAZON.Percentage
<a name="built-in-slot-percent"></a>

Converts words and symbols that represent a percentage into a numeric value with a percent sign (%).

If the user enters a number without a percent sign or the word "percent," the slot value is set to the number. The following table shows how the `AMAZON.Percentage` slot type captures percentages.

| Input | Response |
| --- | --- |
| 50 percent | 50% |
| 0.4 percent | 0.4% |
| 23.5% | 23.5% |
| twenty five percent | 25% |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
