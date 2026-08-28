---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/evaluate-and-release.html
---

# Evaluate and release
<a name="evaluate-and-release"></a>

 The evaluate and release focus area provides best practices for making a responsible release decision, given the release criteria from [Release criteria](release-criteria.md), the evaluation datasets from [Dataset planning](dataset-planning.md), and the AI system design from [System planning](system-planning.md). The release decision is a binary (yes or no) decision that aggregates the results of testing the AI system against each individual release criterion. A well-designed decision factors in the compounded uncertainty in the individual criterion decisions, that is have we met each criterion with the required confidence (for example, are we at least 95% confident that the release criteria have been satisfied?). If a specific release criterion is not met, release may still be possible if the residual risk is disclosed through Monitoring transparency mechanisms. Otherwise, you should return to [System planning](system-planning.md) to review options for baking and filtering mitigations.

**Topics**
+ [System evaluation](raier01.md)
+ [Aggregate results](raier02.md)
+ [Address unmet release criteria](raier03.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
