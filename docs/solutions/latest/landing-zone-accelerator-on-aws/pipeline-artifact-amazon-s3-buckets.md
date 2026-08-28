---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/pipeline-artifact-amazon-s3-buckets.html
---

# Pipeline artifact Amazon S3 buckets
<a name="pipeline-artifact-amazon-s3-buckets"></a>

Two Amazon S3 buckets are created with the solution by default. These buckets are used to host artifacts for the CodePipeline pipelines. If desired, you can delete artifacts after the pipeline invocations have completed. However, don’t delete the buckets themselves because this breaks the functionality of the pipelines. For more information, refer to [Input and output artifacts](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome-introducing-artifacts.html) in the *AWS CodePipeline User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
