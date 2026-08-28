---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-auto.html
---

# Automatic model evaluation
<a name="clarify-foundation-model-evaluate-auto"></a>

You can create an automatic model evaluation in Studio or by using the `fmeval` library inside your own code. Studio uses a wizard to create the model evaluation job. The `fmeval` library provides tools to customize your work flow further.

Both types of automatic model evaluation jobs support the use of publicly available JumpStart models, and JumpStart models that you previously deployed to an endpoint. If you use a JumpStart that has *not* been previously deployed, SageMaker AI will handle creating the necessary resource, and shutting them down once the model evaluation job has finished.

To use text based LLMs from other AWS service or a model hosted outside of AWS, you must use the `fmeval` library.

When your jobs are completed the results are saved in the Amazon S3 bucket specified when the job was created. To learn how to interpret your results, see [Understand the results of your model evaluation job](clarify-foundation-model-evaluate-results.md).

**Topics**
+ [Create an automatic model evaluation job in Studio](clarify-foundation-model-evaluate-auto-ui.md)
+ [Use the `fmeval` library to run an automatic evaluation](clarify-foundation-model-evaluate-auto-lib.md)
+ [Model evaluation results](clarify-foundation-model-reports.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
