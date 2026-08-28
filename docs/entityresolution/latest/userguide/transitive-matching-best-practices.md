---
source_url: https://docs.aws.amazon.com/entityresolution/latest/userguide/transitive-matching-best-practices.html
---

# Best practices for rule ordering
<a name="transitive-matching-best-practices"></a>

When you use transitive matching, rule ordering is critical. Follow these best practices:
+ Order rules from most specific (highest confidence) to least specific.
+ For unique identifier attributes like SSN or date of birth, arrange rules in adjacent pairs – one rule that includes the attribute and the next rule without it. This allows the system to properly handle records that lack those attributes.
+ Be aware that the number of rules affects workflow latency, because records are processed across all rule levels.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
