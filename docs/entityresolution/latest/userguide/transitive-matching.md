---
source_url: https://docs.aws.amazon.com/entityresolution/latest/userguide/transitive-matching.html
---

# Using transitive matching
<a name="transitive-matching"></a>

By default, AWS Entity Resolution uses a waterfall matching approach where records that match at a higher rule level are excluded from subsequent rules. This means that only unmatched records are evaluated by the next rule. While this approach works well for single-source matching, it can cause problems when you have multiple data sources with different attributes.

With the waterfall approach, you might need to combine all matching logic into a single overly permissive rule to match records across sources. This can lead to overmatching, where records that are not true matches are incorrectly grouped together.

Transitive matching solves this problem by processing all records across all rule levels. Once a record matches a rule, its match ID is fixed, but the record can still act as a link to connect unmatched records from later rules to match groups from earlier rules. This feature is currently available through the API only.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
