---
source_url: https://docs.aws.amazon.com/machine-learning/latest/dg/retrieving-object-descriptions.html
---

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Retrieving Object Descriptions
<a name="retrieving-object-descriptions"></a>

You can view detailed descriptions of any object through the console or through the API.

## Detailed Descriptions in the Console
<a name="detailed-descriptions-in-the-console"></a>

To see descriptions on the console, navigate to a list for a specific type of object (datasource, ML model, evaluation, or batch prediction). Next, locate the row in the table that corresponds to the object, either by browsing through the list or by searching for its name or ID.

## Detailed Descriptions from the API
<a name="detailed-descriptions-from-the-api"></a>

Each object type has an operation that retrieves the full details of an Amazon ML object:
+ GetDataSource
+ GetMLModel
+ GetEvaluation
+ GetBatchPrediction

Each operation takes exactly two parameters: the object ID and a Boolean flag called Verbose. Calls with Verbose set to true will include extra details about the object, resulting in higher latencies and larger responses. To learn which fields are included by setting the Verbose flag, see the [Amazon ML API Reference](https://docs.aws.amazon.com/machine-learning/latest/APIReference/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Machine Learning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
