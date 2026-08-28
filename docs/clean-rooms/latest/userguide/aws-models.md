---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/aws-models.html
---

# AWS models in Clean Rooms ML
<a name="aws-models"></a>

AWS Clean Rooms ML provides a privacy-preserving method for two parties to identify similar users in their data without the need to share their data with each other. The first party brings the training data to AWS Clean Rooms so that they can create and configure a lookalike model and associate it with a collaboration. Then, seed data is brought to the collaboration to create a lookalike segment that resembles the training data.

For a more detailed explanation of how this works, see [Cross-account jobs](ml-behaviors.md#ml-behaviors-cross-account-jobs).

The following topics provide information on how to create and configure a AWS models in Clean Rooms ML.

**Topics**
+ [Privacy protections of AWS Clean Rooms ML](ml-privacy.md)
+ [Training data requirements for Clean Rooms ML](ml-training-data-requirements.md)
+ [Seed data requirements for Clean Rooms ML](ml-seed-data-requirements.md)
+ [AWS Clean Rooms ML model evaluation metrics](ml-metrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
