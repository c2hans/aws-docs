---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-eks-observability-best-practices/logging-best-practices.html
---

# Best practices for logging in Amazon EKS
<a name="logging-best-practices"></a>

The following best practices help create a robust, scalable, and efficient logging system for your Amazon EKS environment, and provide better troubleshooting, monitoring, and overall management of your Kubernetes clusters.
+ **Centralize log collection** – Use a centralized logging solution such as CloudWatch Logs, Elasticsearch, or a third-party service to aggregate logs from all components. This provides a single point of access for log analysis and simplifies management.
+ **Implement structured logging** – Use structured log formats such as JSON so that logs can be parsed and searched more easily. Include relevant metadata such as timestamps, log levels, and source identifiers.
+ **Use log levels appropriately** – Implement proper log levels (such as `DEBUG`, `INFO`, `WARN`, and `ERROR`) in your applications. Configure production environments to log at appropriate levels to avoid excessive logging.
+ **Enable container logging** – Configure your containers to log to `stdout` and `stderr`. This allows Kubernetes to capture and forward these logs to your chosen logging solution.
+ **Enable application logging** – Configure applications to write logs to `stdout` and `stderr` instead of writing to log files. This follows the [12-factor app methodology](https://12factor.net/logs) and aligns with cloud-native best practices.
+ **Use Kubernetes DaemonSets for log collection** – Deploy log collection agents (such as Fluent Bit) as DaemonSets to ensure that they run on every node in your cluster.
+ **Implement retention policies** – Define and enforce log retention policies to comply with regulations and to manage storage costs.
+ **Secure log data** – Encrypt logs in transit and at rest. Implement access controls to restrict who can view and manage logs.
+ **Monitor log ingestion** – Set up alerts for log ingestion failures or delays to ensure continuous logging.
+ **Use Kubernetes annotations and labels** – Use Kubernetes annotations and labels to add metadata to your logs, to improve searchability and filtering.
+ **Implement distributed tracing** – Use distributed tracing tools such as [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) or Jaeger to correlate logs across microservices.
+ **Optimize log volume** – Be selective about what you log to avoid unnecessary costs and performance issues. Use sampling for high-volume, low-value logs.
+ **Implement log aggregation** – Use tools such as Logstash to aggregate logs from multiple sources before sending them to your central logging system.
+ **Use AWS services when possible** – Services such as CloudWatch Logs and Container Insights provide seamless integration with other AWS services.
+ **Implement log analysis and visualization** – Use tools such as CloudWatch Logs Insights, Elasticsearch with Kibana, or third-party solutions for log analysis and visualization.
+ **Implement automated log analysis** – Use machine learning and AI-powered tools to detect anomalies and patterns in your logs automatically.
+ **Document your logging strategy** – Maintain clear documentation of your logging architecture, practices, and tools for your team.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
