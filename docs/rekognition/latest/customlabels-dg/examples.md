---
source_url: https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/examples.html
---

# Custom Labels Examples
<a name="examples"></a>

This section contains examples that show you how you make use Amazon Rekognition Custom Labels's capabilities.

| Example | Description |
| --- | --- |
| [Improving a model with Model feedback](ex-feedback.md) | Shows how to improve a model using human verification to create a new training dataset. |
| [Amazon Rekognition Custom Labels demonstration](ex-custom-labels-demo.md) | Demonstration of a user interface that displays the results of a call to `DetectCustomLabels`. |
| [Detecting Custom Labels in videos](ex-video-extraction.md) | Shows how you can use `DetectCustomLabels` with frames extracted from a video. |
| [Analyzing images with an AWS Lambda function](ex-lambda.md) | Shows how you can use `DetectCustomLabels` with a Lambda function. |
| [Creating a manifest file from a CSV file](ex-csv-manifest.md) | Shows how to use a CSV file to create a manifest file suitable for finding [objects, scenes, and concepts](understanding-custom-labels.md#tm-classification) associated with an entire image (classification). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
