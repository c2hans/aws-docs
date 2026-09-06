---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/planning-your-cloud-watch-deployment.html
---

# Planning your CloudWatch deployment
<a name="planning-your-cloud-watch-deployment"></a>

The complexity and scope of a logging and monitoring solution depends on several factors, including:
+ How many environments, Regions, and accounts are used and how this number might increase.
+ The variety and types of your existing workloads and architectures.
+ The compute types and OSs that must be logged and monitored.
+ Whether there are both on-premises locations and AWS infrastructure.
+ The aggregation and analytic requirements of multiple systems and applications.
+ Security requirements that prevent unauthorized exposure of logs and metrics.
+ Products and solutions that must integrate with your logging and monitoring solution to support operational processes.

You must regularly review and update your logging and monitoring solution with new or updated workload deployments. Updates to your logging, monitoring, and alarming should be identified and applied when issues are observed. These issues can then be proactively identified and prevented in the future.

You must make sure that you consistently install and configure software and services for capturing and ingesting logs and metrics. An established logging and monitoring approach uses multiple AWS or independent software vendor (ISV) services and solutions for different domains (for example, security, performance, networking, or analytics). Each domain has its own deployment and configuration requirements.

We recommend using CloudWatch to capture and ingest logs and metrics for multiple OSs and compute types. Many AWS services use CloudWatch to log, monitor, and publish logs and metrics, without requiring further configuration. CloudWatch provides a [software agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) that can be installed and configured for different OSs and environments. The following sections outline how to deploy, install, and configure the CloudWatch agent for multiple accounts, Regions, and configurations:

**Topics**
+ Using CloudWatch in centralized or distributed accounts
+ Creating and storing standard CloudWatch agent configuration files
