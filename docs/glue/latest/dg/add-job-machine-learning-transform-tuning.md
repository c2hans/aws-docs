---
source_url: https://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform-tuning.html
---

# Tuning machine learning transforms in AWS Glue
<a name="add-job-machine-learning-transform-tuning"></a>

You can tune your machine learning transforms in AWS Glue to improve the results of your data-cleansing jobs to meet your objectives. To improve your transform, you can teach it by generating a labeling set, adding labels, and then repeating these steps several times until you get your desired results. You can also tune by changing some machine learning parameters.

For more information about machine learning transforms, see [Record matching with AWS Lake Formation FindMatches](machine-learning.md).

**Topics**
+ [Machine learning measurements](machine-learning-terminology.md)
+ [Deciding between precision and recall](machine-learning-precision-recall-tradeoff.md)
+ [Deciding Between accuracy and cost](machine-learning-accuracy-cost-tradeoff.md)
+ [Estimating the quality of matches using match confidence scores](match-scoring.md)
+ [Teaching the Find Matches transform](machine-learning-teaching.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
