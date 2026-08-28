---
source_url: https://docs.aws.amazon.com/entityresolution/latest/userguide/transitive-matching-how-it-works.html
---

# How transitive matching works
<a name="transitive-matching-how-it-works"></a>

Transitive matching uses the following match ID resolution process for each match group on the current rule:
+ The system checks if any record in the group already has a match ID from an earlier rule level.
+ If a match ID exists, the entire group inherits that earlier match ID.
+ If multiple candidates exist, the smallest match ID from the earliest rule level is selected.
+ If no prior match exists, the group is assigned a new match ID.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
