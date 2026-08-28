---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-update-endpoint.html
---

# Update an Asynchronous Endpoint
<a name="async-inference-update-endpoint"></a>

Update an asynchronous endpoint with the [`UpdateEndpoint`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) API. When you update an endpoint, SageMaker AI first provisions and switches to the new endpoint configuration you specify before it deletes the resources that were provisioned in the previous endpoint configuration. Do not delete an `EndpointConfig` with an endpoint that is live or while the `UpdateEndpoint` or `CreateEndpoint` operations are being performed on the endpoint.

```
# The name of the endpoint. The name must be unique within an AWS Region in your AWS account.
endpoint_name={{'<endpoint-name>'}}

# The name of the endpoint configuration associated with this endpoint.
endpoint_config_name={{'<endpoint-config-name>'}}

sagemaker_client.update_endpoint(
                                EndpointConfigName=endpoint_config_name,
                                EndpointName=endpoint_name
                                )
```

When Amazon SageMaker AI receives the request, it sets the endpoint status to **Updating**. After updating the asynchronous endpoint, it sets the status to **InService**. To check the status of an endpoint, use the [`DescribeEndpoint`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html) API. For a full list of parameters you can specify when updating an endpoint, see the [`UpdateEndpoint`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html) API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
