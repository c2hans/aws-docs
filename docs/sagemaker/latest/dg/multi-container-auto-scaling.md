---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-auto-scaling.html
---

# Autoscale multi-container endpoints
<a name="multi-container-auto-scaling"></a>

If you want to configure automatic scaling for a multi-container endpoint using the `InvocationsPerInstance` metric, we recommend that the model in each container exhibits similar CPU utilization and latency on each inference request. This is recommended because if traffic to the multi-container endpoint shifts from a low CPU utilization model to a high CPU utilization model, but the overall call volume remains the same, the endpoint does not scale out and there may not be enough instances to handle all the requests to the high CPU utilization model. For information about automatically scaling endpoints, see [Automatic scaling of Amazon SageMaker AI models](endpoint-auto-scaling.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
