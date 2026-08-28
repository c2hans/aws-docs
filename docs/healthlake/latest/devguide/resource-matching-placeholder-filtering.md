---
source_url: https://docs.aws.amazon.com/healthlake/latest/devguide/resource-matching-placeholder-filtering.html
---

# Placeholder value filtering
<a name="resource-matching-placeholder-filtering"></a>

Resource matching automatically ignores identifier values that are:
+ all zeros (for example, `0`, `000000000`, `00-000-0000`);
+ common placeholders, case-insensitive (`unknown`, `n/a`, `na`, `none`, `null`, `unassigned`, `pending`, `temp`, `test`);
+ fewer than three characters; or
+ empty or whitespace only.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
