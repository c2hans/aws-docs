---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/monitoring.html
---

# Monitoring
<a name="monitoring"></a>

Effective Solr cluster monitoring combines native tools (Admin UI and health APIs), Java Management Extensions (JMX) metrics for real-time performance data, external systems such as Prometheus or Grafana for visualization, custom scripts for resource tracking, and automated alerts for critical issues. This multi-layered approach provides comprehensive visibility into cluster health, performance, and potential problems. When you use Amazon OpenSearch Service, you get access to the same functionality through the managed service.

Setting up effective monitoring is crucial for maintaining reliable and high-performing Amazon OpenSearch Service deployments. AWS provides several integrated tools that work together to create a comprehensive monitoring solution. This module outlines the key components for implementing monitoring for OpenSearch.

## CloudWatch metrics
<a name="monitoring-cloudwatch-metrics"></a>

Amazon CloudWatch serves as the primary monitoring tool for Amazon OpenSearch Service. It provides real-time visibility into your OpenSearch resources, collects metrics at 60-second intervals (with some exceptions for EBS volumes at 5-minute intervals), and retains this data for two weeks. You can use CloudWatch to create custom dashboards and set up alerts, which makes it essential for proactive monitoring.

**Note**
Basic metrics are included at no additional cost with CloudWatch, but custom dashboards and alarms incur standard CloudWatch charges. For more information, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

## CloudWatch Logs
<a name="monitoring-cloudwatch-logs"></a>

CloudWatch Logs integration enables detailed logging capabilities for Amazon OpenSearch Service. Log types include:
+ **Error logs** for troubleshooting OpenSearch service logs.
+ **Search request slow logs** for tracking the total time a search request takes. Any search that takes longer than a set time limit is logged. You can turn this feature on and adjust the time thresholds by using cluster settings. For more information, see [Setting search request slow log thresholds](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html#createdomain-configure-search-request-slow-logs) in the Amazon OpenSearch Service documentation.
+ **Shard slow** **logs** for performance monitoring. OpenSearch tracks slow operations by using two log types: search slow logs to monitor slow searches, and indexing slow logs to monitor slow indexing. It provides customizable time limits for each index to determine when an operation is considered slow. For more information, see [Setting shard slow log thresholds](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html#createdomain-configure-slow-logs-indices) in the Amazon OpenSearch Service documentation.
+ **Audit logs** for tracking user actions on your clusters, such as logins, searches, and index changes. These logs can be customized to your needs. For more information, see [Monitoring audit logs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/audit-logs.html) in the Amazon OpenSearch Service documentation.

## Advanced monitoring
<a name="monitoring-advanced"></a>

For additional monitoring features, use:
+ Amazon EventBridge to set up automatic responses. For more information, see [Monitoring OpenSearch Service events with Amazon EventBridge](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring-events.html) in the AWS documentation.
+ AWS CloudTrail to track API activity and security. For more information, see [Monitoring Amazon OpenSearch Service API calls with AWS CloudTrail](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-cloudtrailauditing.html) in the AWS documentation.

These services work together to create a customized monitoring system for OpenSearch.

For general monitoring guidelines, see [Operational best practices for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/bp.html) in the AWS documentation. By following these guidelines and regularly reviewing and adjusting your monitoring setup, you can maintain a robust and effective monitoring system for your OpenSearch Service deployment. Remember to adapt these recommendations to your specific use case and requirements while maintaining alignment with AWS best practices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
