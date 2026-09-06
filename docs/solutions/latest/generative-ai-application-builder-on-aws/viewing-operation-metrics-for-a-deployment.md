---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/viewing-operation-metrics-for-a-deployment.html
---

# Viewing operation metrics for a deployment
<a name="viewing-operation-metrics-for-a-deployment"></a>

The Deployment dashboard and use case stacks each come with their own CloudWatch dashboard tracking various operational metrics of the solution. You can use these CloudWatch dashboards to help compare different deployments. To access the dashboards:

1. Navigate to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. Search for the pre-built dashboards either by looking up the stack name, or universally unique identifier (UUID).

For example, the Text use case comes with graphs tracking the number of WebSocket connections, the number of user sign ins and sign ups, the amount of time the LLM took to process a completion, and so on. Customers can use these graphs to compare various \_quantitative \_metrics of a deployment.

**Example**
It is difficult to compare the *qualitative* results of various models applied to different use cases. Use the [Clone feature](use-the-solution.md#how-to-clone-a-deployment) to spin up multiple deployments quickly so that you can compare the outputs side by side.
