---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-eks-observability-best-practices/alerting-tools.html
---

# Alerting tools for Amazon EKS
<a name="alerting-tools"></a>

Amazon EKS supports several AWS and third-party options for implementing alerting. When you choose a tool for Amazon EKS alerting, consider factors such as integration capabilities, scalability, ease of use, cost, and specific features that align with your monitoring and alerting requirements. Many organizations use a combination of these tools to create a comprehensive monitoring and alerting solution for their Amazon EKS environments.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html):** **AWS service for monitoring and observability

  CloudWatch provides metrics, logs, and alarms for EKS clusters, and integrates well with other AWS services.
+ [Prometheus](https://docs.aws.amazon.com/eks/latest/userguide/deploy-prometheus.html): Open source monitoring and alerting tool for Kubernetes

  Prometheus provides a powerful query language (PromQL) for defining alert conditions.
+ [Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/): Companion to Prometheus for handling alerts

  Alertmanager provides deduplication, grouping, and routing of alerts. It supports various notification channels, including email, Slack, and PagerDuty.
+ [Grafana](https://aws.amazon.com/grafana/): Open source platform for monitoring and observability

  Grafana provides visualization and alerting capabilities. It can integrate with various data sources, including Prometheus and CloudWatch.
+ [Elastic Stack (ELK Stack)](https://aws.amazon.com/what-is/elk-stack/): Combination of Elasticsearch, Logstash, and Kibana

  This tool is useful for log aggregation, analysis, and alerting. It can be extended with Elastic's observability features.
+ Third-party solutions

  There are many tools available on the market, including  Datadog, New Relic, Sysdig, Dynatrace, Zabbix, Nagios, Splunk, IBM Instana, and AppDynamics.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
