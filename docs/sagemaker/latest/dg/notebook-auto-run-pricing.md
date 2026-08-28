---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-auto-run-pricing.html
---

# Pricing for SageMaker Notebook Jobs
<a name="notebook-auto-run-pricing"></a>

When you schedule notebook jobs, your Jupyter notebooks run on SageMaker training instances. After you select an **Image** and **Kernel** in your **Create Job** form, the form provides a list of available compute types. You are charged for the compute type you choose, based on the combined duration of use for all notebook jobs that run from the job definition. If you don’t specify a compute type, SageMaker AI assigns you a default Amazon EC2 instance type of `ml.m5.large`. For a breakdown of SageMaker AI pricing by compute type, see [Amazon SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
