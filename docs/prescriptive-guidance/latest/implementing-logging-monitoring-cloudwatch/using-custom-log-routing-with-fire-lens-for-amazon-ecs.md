---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/using-custom-log-routing-with-fire-lens-for-amazon-ecs.html
---

# Using custom log routing with FireLens for Amazon ECS
<a name="using-custom-log-routing-with-fire-lens-for-amazon-ecs"></a>

FireLens for Amazon ECS helps you route logs to [Fluentd](https://www.fluentd.org/) or [Fluent Bit](https://docs.fluentbit.io/manual) so that you can directly send container logs to AWS services and AWS Partner Network (APN) destinations as well as support log shipping to CloudWatch Logs.

AWS provides a [Docker image for Fluent Bit ](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/firelens-using-fluentbit.html)with pre-installed plugins for Amazon Kinesis Data Streams, Amazon Data Firehose, and CloudWatch Logs. You can use the FireLens log driver instead of the awslogs log driver for more customization and control over logs sent to CloudWatch Logs.

For example, you can use the FireLens log driver to control the log format output. This means that an Amazon ECS container's CloudWatch logs are automatically formatted as JSON objects and include JSON-formatted properties for ecs\_cluster,ecs\_task\_arn, ecs\_task\_definition, container\_id, container\_name, and ec2\_instance\_id. The fluent host is exposed to your container through the FLUENT\_HOST and FLUENT\_PORT environment variables when you specify the awsfirelens driver. This means that you can directly log to the log router from your code by using fluent logger libraries. For example, your application might include the fluent-logger-python library to log to Fluent Bit by using the values available from the environment variables.

If you choose to use FireLens for Amazon ECS, you can configure the same settings as the awslogs log driver [and use other settings as well](https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit). For example, you can use the [ecs-task-nginx-firelense.json](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/examples/ecs/ecs-task-nginx-firelense.json) Amazon ECS task definition that launches an NGINX server configured to use FireLens for logging to CloudWatch. It also launches a FireLens Fluent Bit container as a sidecar for logging.
