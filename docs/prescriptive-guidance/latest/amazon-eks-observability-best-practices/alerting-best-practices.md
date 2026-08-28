---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-eks-observability-best-practices/alerting-best-practices.html
---

# Best practices for alerting in Amazon EKS
<a name="alerting-best-practices"></a>

This section describes the best practices for creating a robust alerting system that enhances the reliability and performance of your Kubernetes-based applications in Amazon EKS.

Define clear alert thresholds:
+ Set meaningful thresholds based on historical data and business requirements.
+ Use dynamic thresholds where appropriate to account for varying workloads.

Implement alert prioritization:
+ Categorize alerts by severity (for example, critical, high, medium, low).
+ Align alert priorities with business impact.

Avoid alert fatigue:
+ Reduce noise by eliminating redundant or low-value alerts.
+ Correlate alerts to group related issues.

Use multi-stage alerting:
+ Implement warning thresholds before critical levels are reached.
+ Use different notification channels for different alert severities.

Implement proper alert routing:
+ Make sure that alerts are sent to the right teams or individuals.
+ Use on-call schedules and rotations for all day, every day coverage.

Leverage Kubernetes-native metrics:
+ Monitor core Kubernetes components (nodes, pods, services).
+ Use [kube-state-metrics (KSM)](https://github.com/kubernetes/kube-state-metrics) for additional Kubernetes object metrics.

Monitor both infrastructure and applications:
+ Set up alerts for cluster health, node status, and resource utilization.
+ Implement application-specific alerts such as error rates and latency.

Use Prometheus and Alertmanager:
+ Use Prometheus for metric collection and PromQL to define alert conditions.
+ Use Alertmanager for alert routing and deduplication.

Integrate with Amazon CloudWatch:
+ Use [CloudWatch Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html) for Amazon EKS-specific metrics.
+ Set up [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) for critical AWS resource metrics.

Implement context-rich alerts:
+ Include relevant information in alert messages, such as cluster name, namespace, and pod details.
+ Provide links to relevant dashboards or runbooks in alerts.

Use anomaly detection:
+ Implement machine learning-based anomaly detection for complex patterns.
+ Use services such as CloudWatch anomaly detection or third-party tools.

Implement alert suppression and silencing:
+ Allow temporary suppression of known issues.
+ Implement maintenance windows to reduce noise during planned downtimes.

Monitor alert performance:
+ Track metrics such as alert frequency, resolution time, and false positive rates.
+ Regularly review and refine alert rules based on these metrics.

Implement escalation procedures:
+ Define clear escalation paths for unresolved alerts.
+ Use tools such as PagerDuty or Opsgenie for automated escalations.

Test alert systems regularly:
+ Conduct periodic tests of your alerting pipeline.
+ Include alert testing in disaster recovery drills.

  Use templates for alert consistency:
+ Create standardized alert templates for common scenarios.
+ Ensure consistent formatting and information across all alerts.

Implement rate limiting:
+ Prevent alert storms by implementing rate limiting on frequently triggered alerts.

Use custom metrics:
+ Implement custom metrics for application-specific monitoring.
+ Use the Kubernetes custom metrics API for automatic scaling based on these metrics.

Implement logging integration:
+ Correlate alerts with relevant logs for faster troubleshooting.
+ Use tools such as Grafana Loki or the ELK Stack in conjunction with your alerting system.

Consider cost alerts:
+ Set up alerts for unexpected spikes in resource usage or costs.
+ Use [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) or third-party cost management tools.

Use distributed tracing:
+ Integrate distributed tracing tools such as Jaeger or [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html).
+ Set up alerts for abnormal trace patterns or latencies.

Document alert runbooks:
+ Create clear, actionable runbooks for each alert type.
+ Include troubleshooting steps and escalation procedures in runbooks.

By following these best practices, you can create a robust, efficient, and effective alerting system for your Amazon EKS environment. This will help ensure high availability, quick issue resolution, and optimal performance of your Kubernetes-based applications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
