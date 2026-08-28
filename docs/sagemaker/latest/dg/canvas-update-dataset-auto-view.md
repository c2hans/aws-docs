---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-update-dataset-auto-view.html
---

# View your automatic dataset update jobs
<a name="canvas-update-dataset-auto-view"></a>

To view the job history for your automatic dataset updates in Amazon SageMaker Canvas, on your dataset details page, choose the **Auto updates** tab.

Each automatic update to a dataset shows as a job in the **Auto updates** tab under the **Job history** section. For each job, you can see the following:
+ **Job created** – The timestamp for when Canvas started updating the dataset.
+ **Files** – The number of files in the dataset.
+ **Cells (Columns x Rows)** – The number of columns and rows in the dataset.
+ **Status** – The status of the dataset after the update. If the job was successful, the status is **Ready**. If the job failed for any reason, the status is **Failed**, and you can hover over the status for more details.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
