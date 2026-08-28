---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-troubleshooting.html
---

# Troubleshooting guide
<a name="clarify-online-explainability-troubleshooting"></a>

If you encounter errors using SageMaker Clarify online explainability, consult the topics in this section.

**`InvokeEndpoint` API fails with the error "ReadTimeoutError:Read timeout on endpoint..."**

This error means that the request could not be completed within the 60-second time limit set by the [request timeout](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html).

To reduce the request latency, try the following:
+ Tune the model's performance during inference. For example, SageMaker AI [Neo](https://aws.amazon.com/sagemaker/neo/) can optimize models for inference.
+ Allow the model container to handle batch requests.
+ Use a larger `MaxRecordCount` to reduce the number of calls from the explainer to the model container. This will reduce network latency and overhead.
+ Use an instance type that has more resources allocated to it. Alternately, assign more instances to the endpoint to help balance the load.
+ Reduce the number of records inside a single `InvokeEndpoint` request.
+ Reduce the number of records in the baseline data.
+ Use a smaller `NumberOfSamples` value to reduce the size of the synthetic dataset. For more information about how the number of samples affects your synthetic dataset, see [Synthetic dataset](clarify-online-explainability-create-endpoint-synthetic.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
