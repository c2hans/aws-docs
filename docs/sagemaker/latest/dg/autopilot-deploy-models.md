---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-deploy-models.html
---

# Autopilot model deployment and prediction
<a name="autopilot-deploy-models"></a>

This Amazon SageMaker Autopilot guide includes steps for model deployment, setting up real-time inference, and running inference with batch jobs.

After you train your Autopilot models, you can deploy them to get predictions in one of two ways:

1. Use [Deploy models for real-time inference](autopilot-deploy-models-realtime.md) to set up an endpoint and obtain predictions interactively. Real-time inference is ideal for inference workloads where you have real-time, interactive, low latency requirements.

1. Use [Run batch inference jobs](autopilot-deploy-models-batch.md) to make predictions in parallel on batches of observations on an entire dataset. Batch inference is a good option for large datasets or if you don't need an immediate response to a model prediction request.

**Note**
To avoid incurring unnecessary charges: After the endpoints and resources that were created from model deployment are no longer needed, you can delete them. For information about pricing of instances by Region, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
