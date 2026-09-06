---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/pipeline-artifact-amazon-s3-buckets.html
---

# Pipeline artifact Amazon S3 buckets
<a name="pipeline-artifact-amazon-s3-buckets"></a>

Two Amazon S3 buckets are created with the solution by default. These buckets are used to host artifacts for the CodePipeline pipelines. If desired, you can delete artifacts after the pipeline invocations have completed. However, don’t delete the buckets themselves because this breaks the functionality of the pipelines. For more information, refer to [Input and output artifacts](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome-introducing-artifacts.html) in the *AWS CodePipeline User Guide*.
