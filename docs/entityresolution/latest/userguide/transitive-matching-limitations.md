---
source_url: https://docs.aws.amazon.com/entityresolution/latest/userguide/transitive-matching-limitations.html
---

# Limitations
<a name="transitive-matching-limitations"></a>

Transitive matching has the following limitations:
+ Available for Advanced Matching workflows only. Not available for Simple rule type or machine learning-based matching workflows.
+ The **EmptyValues=Ignore** modifier is not supported when transitive matching is enabled. Transitive matching includes built-in handling for empty values that prevents overmatching.
+ Workflow runtime increases proportionally with the number of rules defined, because records are processed across all rule levels.
+ The `enableTransitiveMatching` setting can only be configured during workflow creation. To use transitive matching, you must create a new workflow.
+ You are responsible for ordering rules correctly. Rules with more attributes must come before rules with fewer attributes. Incorrect ordering can cause records with different values for unique fields (such as date of birth or SSN) to be incorrectly grouped together.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
