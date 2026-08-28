---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints-resume.html
---

# Resume training from a checkpoint
<a name="model-checkpoints-resume"></a>

To resume a training job from a checkpoint, run a new estimator with the same `checkpoint_s3_uri` that you created in the [Enable checkpointing](model-checkpoints-enable.md) section. Once the training has resumed, the checkpoints from this S3 bucket are restored to `checkpoint_local_path` in each instance of the new training job. Ensure that the S3 bucket is in the same Region as that of the current SageMaker AI session.

![Architecture diagram of syncing checkpoints to resume training.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/checkpoints_resume.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
