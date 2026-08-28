---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex-bucket.html
---

# Use an Amazon S3 bucket for input and output
<a name="automatic-model-tuning-ex-bucket"></a>

Set up a S3 bucket to upload training datasets and save training output data for your hyperparameter tuning job.

**To use a default S3 bucket**

Use the following code to specify the default S3 bucket allocated for your SageMaker AI session. `prefix` is the path within the bucket where SageMaker AI stores the data for the current training job.

```
sess = sagemaker.Session()
bucket = sess.default_bucket() # Set a default S3 bucket
prefix = 'DEMO-automatic-model-tuning-xgboost-dm'
```

**To use a specific S3 bucket (Optional)**

If you want to use a specific S3 bucket, use the following code and replace the strings to the exact name of the S3 bucket. The name of the bucket must contain **sagemaker**, and be globally unique. The bucket must be in the same AWS Region as the notebook instance that you use for this example.

```
bucket = "{{sagemaker-your-preferred-s3-bucket}}"

sess = sagemaker.Session(
    default_bucket = bucket
)
```

**Note**
The name of the bucket doesn't need to contain **sagemaker** if the IAM role that you use to run the hyperparameter tuning job has a policy that gives the `S3FullAccess` permission.

## Next Step
<a name="automatic-model-tuning-ex-next-data"></a>

[Download, Prepare, and Upload Training Data](automatic-model-tuning-ex-data.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
