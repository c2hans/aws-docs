---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/edit-pipeline-before-execution.html
---

# Edit a pipeline
<a name="edit-pipeline-before-execution"></a>

To make changes to a pipeline before running it, do the following:

1. Open SageMaker Studio by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane of Studio, select **Pipelines**.

1. Select a pipeline name to view details about the pipeline.

1. Choose the **Executions** tab.

1. Select the name of a pipeline execution.

1. Choose **Edit** to open the Pipeline Designer.

1. Update the edges between steps or the step configuration as required and click **Save**.

   Saving a pipeline after editing automatically generates a new version number.

1. Choose **Run**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
