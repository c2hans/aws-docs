---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/edge-device-fleet-about.html
---

# The Edge Manager Agent
<a name="edge-device-fleet-about"></a>

The Edge Manager agent is an inference engine for your edge devices. Use the agent to make predictions with models loaded onto your edge devices. The agent also collects model metrics and captures data at specific intervals. Sample data is stored in your Amazon S3 bucket.

There are two methods of installing and deploying the Edge Manager agent onto your edge devices:

1. Download the agent as a binary from the Amazon S3 release bucket. For more information, see [Download and Set Up the Edge Manager Agent Manually](edge-device-fleet-manual.md).

1. Use the AWS IoT Greengrass V2 console or the AWS CLI to deploy `aws.greengrass.SageMakerEdgeManager`. See [Create the AWS IoT Greengrass V2 Components](edge-greengrass-custom-component.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
