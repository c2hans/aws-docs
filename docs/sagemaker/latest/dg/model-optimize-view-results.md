---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize-view-results.html
---

# View the optimization job results
<a name="model-optimize-view-results"></a>

After you've created one or more optimization jobs, you can use Studio to view a summary table of all of your jobs, and you can view the details for any individual job.

## Amazon SageMaker Studio
<a name="optimization-results-studio"></a>

**To view the optimization job summary table**
+ In the Studio navigation menu, under **Jobs**, choose **Inference optimization**.

  The **Inference optimization** page shows a table that displays the jobs that you've created. For each job, it shows the optimization configurations that you applied and the job status.

**To view the details for a job**
+ On the **Inference optimization** page, in the summary table, choose the name of the job.

  Studio shows the job details page, which shows the job status and all of the settings that you applied when you created the job. If the job completed successfully, SageMaker AI stored the optimized model artifacts in the Amazon S3 location under **Optimized model S3 URI**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
