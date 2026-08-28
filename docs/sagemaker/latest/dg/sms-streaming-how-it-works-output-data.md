---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-how-it-works-output-data.html
---

# Receive output data from a streaming labeling job
<a name="sms-streaming-how-it-works-output-data"></a>

**Note**
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

Your Amazon S3 output bucket is periodically updated with new output data from your streaming labeling job. Optionally, you can specify an Amazon SNS output topic. Each time a worker submits a labeled object, a notification with the output data is sent to that topic. You can subscribe an endpoint to your SNS output topic to receive notifications or trigger events when you receive output data from a labeling task. Use an Amazon SNS output topic if you want to do real time chaining to another streaming job and receive an Amazon SNS notifications each time a data object is submitted by a worker.

To learn more, see [Subscribe an Endpoint to Your Amazon SNS Output Topic](sms-create-sns-input-topic.md#sms-streaming-subscribe-output-topic).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
