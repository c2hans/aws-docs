---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/introduction.html
---

# Designing and implementing logging and monitoring with Amazon CloudWatch
<a name="introduction"></a>

*Khurram Nizami, Amazon Web Services*

This guide helps you design and implement logging and monitoring with [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) and related Amazon Web Services (AWS) management and governance services for workloads that use [Amazon Elastic Compute Cloud (Amazon EC2) instances](https://docs.aws.amazon.com/ec2/index.html), [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html), [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), and on-premises servers. The guide is intended for operations teams, DevOps engineers, and application engineers that manage workloads on the AWS Cloud.

Your logging and monitoring approach should be based on the [five pillars](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc) of the AWS Well-Architected Framework. These pillars are [operational excellence](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html), [security](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html), [reliability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html), [performance efficiency](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html), and [cost optimization](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html). A well-architected monitoring and alarming solution improves reliability and performance by helping you proactively analyze and adjust your infrastructure.

This guide doesn't extensively discuss logging and monitoring for security or cost-optimization because these are topics that require in-depth evaluation. There are many AWS services that support security logging and monitoring, including [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_introduction.html), [Amazon Detective](https://docs.aws.amazon.com/detective/latest/userguide/detective-investigation-about.html), [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html), [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html), and [AWS Security Hub](https://docs.aws.amazon.com/securityhub/). You can also use [AWS Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-what-is.html), [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), and [CloudWatch billing metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/gs_monitor_estimated_charges_with_cloudwatch.html) for cost optimization.

The following table outlines the six areas that your logging and monitoring solution should address.

|  |
| --- |
| Capturing and ingesting log files and metrics | Identify, configure, and send system and application logs and metrics to AWS services from different sources. |
| --- |--- |
| **Searching and analyzing logs** | Search and analyze logs for operations management, problem identification, troubleshooting, and applications analysis. |
| **Monitoring metrics and alarming** | Identify and act on observations and trends in your workloads. |
| **Monitoring application and service availability** | Reduce downtime and improve your ability to meet service level targets by continuously monitoring service availability. |
| **Tracing applications** | Trace application requests in systems and external dependencies to fine-tune performance, perform root cause analysis, and troubleshoot issues. |
| **Creating dashboards and visualizations** | Create dashboards that focus on relevant metrics and observations for your systems and workloads, which helps continuous improvement and proactive discovery of issues. |

CloudWatch can meet most logging and monitoring requirements, and provides a reliable, scalable, and flexible solution. Many AWS services automatically provide CloudWatch metrics, in addition to CloudWatch logging integration for monitoring and analysis. CloudWatch also provides agents and log drivers to support a variety of compute options such as servers (both in the cloud and on premises), containers, and serverless computing. This guide also covers the following AWS services that are used with logging and monitoring:
+ [AWS Systems Manager Distributor,](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html)[ Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html), and [Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)

[Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) to automate, configure, and update the CloudWatch agent for your EC2 instances and onpremises servers
+ [Amazon Elasticsearch Service (Amazon ES)](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/what-is-amazon-elasticsearch-service.html) for advanced log aggregation, search, and analysis
+ [Amazon Route 53 health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html) and [CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) to monitor application and service availability
+ [Amazon Managed Service for Prometheus (AMP)](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html) for monitoring containerized applications at scale
+ [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) for application tracing and runtime analysis
+ [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html) to visualize and analyze data from multiple sources (for example, CloudWatch, Amazon ES, and [Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html))

The AWS compute services that you choose also affect the implementation and configuration of your logging and monitoring solution. For example, CloudWatch's implementation and configuration is different for Amazon EC2, Amazon ECS, Amazon EKS, and Lambda.

Application and workload owners can often forget about logging and monitoring or inconsistently configure and implement it. This means that workloads enter production with limited observability, which causes delays in identifying issues and increases the time taken to troubleshoot and resolve them. At a minimum, your logging and monitoring solution must address the systems layer for the operating system (OS)-level logs and metrics, in addition to the application layer for application logs and metrics. The guide provides a recommended approach for addressing these two layers across different compute types, including the three compute types outlined in the following table.

|  |
| --- |
| Long-running and immutable EC2 instances | System and application logs and metrics across multiple operating systems (OSs) in multiple AWS Regions or accounts. |
| --- |--- |
| **Containers** | System and application logs and metrics for your Amazon ECS and Amazon EKS clusters, including examples for different configurations. |
| **Serverless** | System and application logs and metrics for your Lambda functions and considerations for customization. |

This guide provides a logging and monitoring solution that addresses CloudWatch and related AWS services in the following areas:
+ Planning your CloudWatch deployment  – Considerations for planning your CloudWatch deployment and guidance on centralizing your CloudWatch configuration.
+ Configuring the CloudWatch agent for EC2 instances and on-premises servers – CloudWatch configuration details for system-level and application-level logging and metrics.
+ CloudWatch agent installation approaches for Amazon EC2 and on-premises servers – Approaches for installing the CloudWatch agent, including automated deployment using Systems Manager across multiple Regions and accounts.
+ Logging and monitoring on Amazon ECS – Guidance for configuring CloudWatch for clusterlevel and application-level logging and metrics in Amazon ECS.
+ Logging and monitoring on Amazon EKS   – Guidance for configuring CloudWatch for clusterlevel and application-level logging and metrics in Amazon EKS.
+ Prometheus monitoring on Amazon EKS  – Introduces and compares Amazon Managed Service for Prometheus (AMP) with CloudWatch Container Insights monitoring for Prometheus.
+ Logging and metrics for AWS Lambda  – Guidance for configuring CloudWatch for your Lambda functions.
+ Searching and analyzing logs in CloudWatch  – Methods to analyze your logs using Amazon CloudWatch Application Insights, CloudWatch Logs Insights, and extending log analysis to Amazon ES.
+ Alarming options with CloudWatch – Introduces CloudWatch Alarms and CloudWatch Anomaly Detection and provides guidance on alarm creation and setup.
+ Monitoring application and service availability – Introduces and compares CloudWatch Synthetics and Route 53 health checks for automated availability monitoring.
+ Tracing applications with AWS X-Ray  – Introduction and setup for application tracing using X-Ray for Amazon EC2, Amazon ECS, Amazon EKS, and Lambda
+ Dashboards and visualizations with CloudWatch  – Introduction to CloudWatch Dashboards for improved observability across AWS workloads.
+ CloudWatch integration with AWS services – Explains how CloudWatch integrates with various AWS services.
+ Amazon Managed Grafana for dashboarding and visualization – Introduces and compares AMG with CloudWatch for dashboarding and visualization.

Implementation examples are used throughout this guide across these areas and are also available from the [AWS Samples GitHub repository](https://github.com/aws-samples/logging-monitoring-apg-guide-examples)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
