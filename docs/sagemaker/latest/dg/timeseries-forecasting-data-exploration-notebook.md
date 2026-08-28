---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/timeseries-forecasting-data-exploration-notebook.html
---

# Amazon SageMaker Autopilot data exploration notebook
<a name="timeseries-forecasting-data-exploration-notebook"></a>

Amazon SageMaker Autopilot cleans and pre-processes your dataset automatically. To help users understand their data, uncover patterns, relationships, and anomalies about the time-series, Amazon SageMaker Autopilot generates a **data exploration** static report in the form of a notebook for users to reference.

The data exploration notebook is generated for every Autopilot job. The report is stored in an Amazon S3 bucket and can be accessed from the job output path.

You can find the Amazon S3 prefix to the data exploration notebook in the response to `[DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html)` at `[AutoMLJobArtifacts.DataExplorationNotebookLocation](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html#sagemaker-DescribeAutoMLJobV2-response-AutoMLJobArtifacts)`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
