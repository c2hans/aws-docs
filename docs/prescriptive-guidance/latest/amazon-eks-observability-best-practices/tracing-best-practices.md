---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-eks-observability-best-practices/tracing-best-practices.html
---

# Best practices for tracing in Amazon EKS
<a name="tracing-best-practices"></a>

This section provides a comprehensive list of best practices and techniques for creating an effective tracing system that enhances observability and troubleshooting for your Kubernetes-based applications in Amazon EKS.
+ **Strategic sampling**: Configure different sampling rates based on your application's traffic patterns and the importance of the services you're using. Implement higher sampling rates for critical paths while reducing sampling for high-volume, less critical routes to optimize costs. For guidance, see [Configuring sampling rules](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-sampling.html) in the AWS X-Ray documentation.
+ **Instrumentation setup**: Use automatic instrumentation tools such as the X-Ray SDK or AWS Distro for OpenTelemetry collectors to minimize the manual instrumentation effort. Maintain consistent naming conventions and context propagation across services for better trace correlation. For more information, see the [Distro for OpenTelemetry collector documentation](https://aws-otel.github.io/docs/getting-started/collector).
+ **Data management**: Implement appropriate retention periods and compression strategies to balance storage costs with your observability needs. Establish clear data privacy controls and backup procedures to protect sensitive trace data. For more information, see [Change log data retention in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SttingLogRetention) in the CloudWatch Logs documentation.
+ **Performance optimization**: Monitor and optimize tracing overhead to minimize impact on application performance. Use efficient buffering and asynchronous processing to reduce latency impact. For more information, see [Configuring the AWS X-Ray daemon](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-configuration.html) in the X-Ray documentation.
+ **Security controls**: Implement proper access controls and data protection measures by using IAM roles and policies. Regular security audits and compliance reviews help ensure that trace data remains secure. For more information, see[ Security in AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/security.html) in the X-Ray documentation.
+ **Monitoring and alerts**: Set up comprehensive monitoring for trace collection health and configure alerts for collection issues. Track sampling rates and system performance metrics to ensure optimal operation. For more information, see [Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html) in the CloudWatch documentation.
+ **High availability**: Deploy redundant collectors across Availability Zones and configure proper failover mechanisms. Regular testing of high availability setup ensures reliable trace collection. For more information, see [Using AWS Distro for OpenTelemetry as a collector](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ingest-with-adot.html) in the Amazon Managed Service for Prometheus documentation.

By following these best practices, you can create a robust, efficient, and effective tracing system for your Amazon EKS environment. This will help ensure comprehensive observability, efficient troubleshooting, and optimal performance of your Kubernetes-based applications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
