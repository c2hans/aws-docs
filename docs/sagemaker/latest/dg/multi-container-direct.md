---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-direct.html
---

# Invoke a multi-container endpoint with direct invocation
<a name="multi-container-direct"></a>

SageMaker AI multi-container endpoints enable customers to deploy multiple containers to deploy different models on a SageMaker AI endpoint. You can host up to 15 different inference containers on a single endpoint. By using direct invocation, you can send a request to a specific inference container hosted on a multi-container endpoint.

 To invoke a multi-container endpoint with direct invocation, call [invoke\_endpoint](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.invoke_endpoint) as you would invoke any other endpoint, and specify which container you want to invoke by using the `TargetContainerHostname` parameter.

 The following example directly invokes the `secondContainer` of a multi-container endpoint to get a prediction.

```
import boto3
runtime_sm_client = boto3.Session().client('sagemaker-runtime')

response = runtime_sm_client.invoke_endpoint(
   EndpointName ='my-endpoint',
   ContentType = 'text/csv',
   TargetContainerHostname='secondContainer',
   Body = body)
```

 For each direct invocation request to a multi-container endpoint, only the container with the `TargetContainerHostname` processes the invocation request. You will get validation errors if you do any of the following:
+ Specify a `TargetContainerHostname` that does not exist in the endpoint
+ Do not specify a value for `TargetContainerHostname` in a request to an endpoint configured for direct invocation
+ Specify a value for `TargetContainerHostname` in a request to an endpoint that is not configured for direct invocation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
