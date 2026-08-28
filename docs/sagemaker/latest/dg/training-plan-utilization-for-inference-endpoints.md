---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/training-plan-utilization-for-inference-endpoints.html
---

# Using training plans for SageMaker inference endpoints
<a name="training-plan-utilization-for-inference-endpoints"></a>

You can use a SageMaker training plans to deploy inference endpoints with predictable access to GPU capacity. When you create a training plan, set the target resource to "endpoint". This secures compute instances specifically for inference workloads.

**Note**
The training plan must be in the `Active` status to be used by an inference endpoint. The endpoint only functions during the reservation window specified in the training plan.

**Important**
When the training plan reservation expires, endpoint behavior depends on the `CapacityReservationPreference` setting. If you set this to `capacity-reservations-only`, the endpoint stops serving traffic and invocations fail with a capacity error. To resume service, you must either create a new training plan reservation and update the endpoint configuration, or update the endpoint to use on-demand capacity.

**Topics**
+ [Deploy an inference endpoint using the API, AWS CLI](use-training-plan-for-inference-endpoints-using-api-cli-sdk.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
