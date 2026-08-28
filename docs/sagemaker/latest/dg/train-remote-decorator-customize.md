---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-decorator-customize.html
---

# Customize your runtime environment
<a name="train-remote-decorator-customize"></a>

You can customize your runtime environment to use your preferred local integrated development environments (IDEs), SageMaker notebooks, or SageMaker Studio Classic notebooks to write your ML code. SageMaker AI will help package and submit your functions and its dependencies as a SageMaker training job. This allows you to access the capacity of the SageMaker training server to run your training jobs.

Both the remote decorator and the `RemoteExecutor` methods to invoke a function allow users to define and customize their runtime environment. You can use either a `requirements.txt` file or a conda environment YAML file.

To customize a runtime environment using both a conda environment YAML file and a `requirements.txt` file, refer to the following code example.

```
# specify a conda environment inside a yaml file
@remote(instance_type="{{ml.m5.large}}",
        image_uri = "{{my_base_python:latest}}",
        dependencies = "./environment.yml{{}}")
def matrix_multiply(a, b):
    return np.matmul(a, b)

# use a requirements.txt file to import dependencies
@remote(instance_type="{{ml.m5.large}}",
        image_uri = "{{my_base_python:latest}}",
        dependencies = '{{./requirements.txt}}')
def matrix_multiply(a, b):
    return np.matmul(a, b)
```

Alternatively, you can set `dependencies` to `auto_capture` to let the SageMaker Python SDK capture the installed dependencies in the active conda environment. The following are required for `auto_capture` to work reliably:
+ You must have an active conda environment. We recommend not using the `base` conda environment for remote jobs so that you can reduce potential dependency conflicts. Not using the `base` conda environment also allows for faster environment setup in the remote job.
+ You must not have any dependencies installed using pip with a value for the parameter `--extra-index-url`.
+ You must not have any dependency conflicts between packages installed with conda and packages installed with pip in the local development environment.
+ Your local development environment must not contain operating system-specific dependencies that are not compatible with Linux.

In case `auto_capture` does not work, we recommend that you pass in your dependencies as a requirement.txt or conda environment.yaml file, as described in the first coding example in this section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
