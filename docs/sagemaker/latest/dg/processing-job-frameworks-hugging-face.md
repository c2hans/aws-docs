---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job-frameworks-hugging-face.html
---

# Code example using HuggingFaceProcessor in the Amazon SageMaker Python SDK
<a name="processing-job-frameworks-hugging-face"></a>

Hugging Face is an open-source provider of natural language processing (NLP) models. The `HuggingFaceProcessor` in the Amazon SageMaker Python SDK provides you with the ability to run processing jobs with Hugging Face scripts. When you use the `HuggingFaceProcessor`, you can leverage an Amazon-built Docker container with a managed Hugging Face environment so that you don't need to bring your own container.

The following code example shows how you can run your Processing job using a Docker image provided and maintained by SageMaker AI. Note that when you run the job, you can specify a directory containing your scripts and dependencies in the `source_dir` argument, and you can have a `requirements.txt` file located inside your `source_dir` directory that specifies the dependencies for your processing script(s). SageMaker Processing installs the dependencies in `requirements.txt` in the container for you.

```
from sagemaker.core.resources import ProcessingJob
from sagemaker.core.helper.session_helper import get_execution_role

# Create a processing job with a Hugging Face container
processing_job = ProcessingJob.create(
    processing_job_name='frameworkprocessor-hf',
    role_arn=get_execution_role(),
    app_specification={
        "image_uri": "{{huggingface-processing-image-uri}}",
        "container_entrypoint": ["python3", "/opt/ml/processing/input/code/{{processing-script.py}}"]
    },
    processing_resources={
        "cluster_config": {
            "instance_count": 1,
            "instance_type": "ml.g4dn.xlarge",
            "volume_size_in_gb": 30
        }
    },
    processing_inputs=[
        {
            "input_name": "data",
            "s3_input": {
                "s3_uri": f"{{s3://{{BUCKET}}/{{S3_INPUT_PATH}}}}",
                "local_path": "/opt/ml/processing/input/data/",
                "s3_data_type": "S3Prefix",
                "s3_input_mode": "File"
            }
        },
        {
            "input_name": "code",
            "s3_input": {
                "s3_uri": "{{s3://path/to/scripts/}}",
                "local_path": "/opt/ml/processing/input/code",
                "s3_data_type": "S3Prefix",
                "s3_input_mode": "File"
            }
        }
    ],
    processing_output_config={
        "outputs": [
            {"output_name": "train", "s3_output": {"s3_uri": f"{{s3://{{BUCKET}}/{{S3_OUTPUT_PATH}}}}", "local_path": "/opt/ml/processing/output/train/", "s3_upload_mode": "EndOfJob"}},
            {"output_name": "test", "s3_output": {"s3_uri": f"{{s3://{{BUCKET}}/{{S3_OUTPUT_PATH}}}}", "local_path": "/opt/ml/processing/output/test/", "s3_upload_mode": "EndOfJob"}},
            {"output_name": "val", "s3_output": {"s3_uri": f"{{s3://{{BUCKET}}/{{S3_OUTPUT_PATH}}}}", "local_path": "/opt/ml/processing/output/val/", "s3_upload_mode": "EndOfJob"}}
        ]
    }
)
```

If you have a `requirements.txt` file, it should be a list of libraries you want to install in the container. The path for `source_dir` can be a relative, absolute, or Amazon S3 URI path. However, if you use an Amazon S3 URI, then it must point to a tar.gz file. You can have multiple scripts in the directory you specify for `source_dir`. To learn more about the `HuggingFaceProcessor` class, see [Hugging Face Estimator](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) in the *Amazon SageMaker AI Python SDK*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
