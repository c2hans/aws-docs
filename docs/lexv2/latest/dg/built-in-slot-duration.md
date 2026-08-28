---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-duration.html
---

# AMAZON.Duration
<a name="built-in-slot-duration"></a>

Converts words that indicate durations into a numeric duration.

The duration is resolved to a format based on the [ISO-8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations), `PnYnMnWnDTnHnMnS`. The `P` indicates that this is a duration, the `n` is a numeric value, and the capital letter following the `n` is the specific date or time element. For example, `P3D` means 3 days. A `T` is used to indicate that the remaining values represent time elements rather than date elements.

Examples:
+ "ten minutes": `PT10M`
+ "five hours": `PT5H`
+ "three days": `P3D`
+ "forty five seconds": `PT45S`
+ "eight weeks": `P8W`
+ "seven years": `P7Y`
+ "five hours ten minutes": `PT5H10M`
+ "two years three hours ten minutes": `P2YT3H10M`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
