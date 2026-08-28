---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/neo-requests-cli.html
---

# Request Inferences from a Deployed Service (AWS CLI)
<a name="neo-requests-cli"></a>

Inference requests can be made with the [`sagemaker-runtime invoke-endpoint`](https://docs.aws.amazon.com/cli/latest/reference/sagemaker-runtime/invoke-endpoint.html) once you have an Amazon SageMaker AI endpoint `InService`. You can make inference requests with the AWS Command Line Interface (AWS CLI). The following example shows how to send an image for inference:

```
aws sagemaker-runtime invoke-endpoint --endpoint-name {{'insert name of your endpoint here'}} --body fileb://image.jpg --content-type=application/x-image output_file.txt
```

An `output_file.txt` with information about your inference requests is made if the inference was successful.

 For TensorFlow submit an input with `application/json` as the content type.

```
aws sagemaker-runtime invoke-endpoint --endpoint-name {{'insert name of your endpoint here'}} --body fileb://input.json --content-type=application/json output_file.txt
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
