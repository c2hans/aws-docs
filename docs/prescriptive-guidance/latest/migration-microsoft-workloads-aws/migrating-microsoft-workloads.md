---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-microsoft-workloads-aws/migrating-microsoft-workloads.html
---

# Monitoring Microsoft workloads
<a name="migrating-microsoft-workloads"></a>

Microsoft workloads typically use SQL Server in the backend to retrieve and persist data. Often in the journey to the cloud, a rehost decision is made for such a solution by using a simple lift-and-shift approach. When such applications are hosted on a Windows on Amazon EC2 platform, you can use native Windows-based tools to monitor the health of these applications at the server level. However, getting a holistic view across the different components and servers deployed as part of the solution is a challenge, but this pain point can be addressed by [Amazon CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html).

CloudWatch Application Insights is a cloud-native monitoring service that can help you set up and monitor application resources for your AWS workloads. Enterprise customers deal with a variety of workloads and require a monitoring service that can correlate telemetric data from different sources. If you're an enterprise customer, then CloudWatch Application Insights can help you avoid the complexity in setting up monitoring by automating resource discovery and helping create the application from a variety of resources.

## Assess
<a name="migrating-microsoft-workloads-assess"></a>

Tracking an application's performance and backend health is essential for most organizations. You need to know when and where along the journey an abnormality was found and why it happened. You also need to monitor your systems and reduce maintenance costs.

CloudWatch can help you with your monitoring needs, and CloudWatch Application Insights uses CloudWatch metrics, alarms, and events. You can use CloudWatch to set up monitoring and management of metrics, telemetry, and logs for many AWS resources. [Amazon CloudWatch ServiceLens](https://aws.amazon.com/blogs/aws/visualize-and-monitor-highly-distributed-applications-with-amazon-cloudwatch-servicelens/) provides a combination of services to give you everything you need for monitoring the health of your applications.

## Mobilize
<a name="migrating-microsoft-workloads-mobilize"></a>

CloudWatch Application Insights provides a low-click user interface that you can use to quickly and easily set up the optimal telemetry metrics and logs for your applications. CloudWatch Application Insights tailors its monitors to your specific workload so you can continuously analyze signs of problems for your specific applications. It also delivers auto-configuration and analysis of recommended workload telemetry. Some examples include .NET CLR, requests per second for application/web server technologies, identifying common issues related to .NET garbage collection, and SQL Server failed backups.

When you're looking to onboard a monitoring solution, you typically must understand and configure CPU, memory, and other threshold requirements. However, CloudWatch Application Insights automatically detects these resources and relevant metrics. When you add your applications to CloudWatch Application Insights, it scans the resources, and recommends and configures metrics and logs on CloudWatch for application components. Example application components include SQL Server backend databases and Microsoft IIS/web tiers.

Based on the resource group selected, CloudWatch Application Insights automatically sets up monitoring for each component. In the case of account-based application monitoring, all of the resources discovered in your account are added automatically. You can also benefit from the resource detection capabilities of CloudWatch Application Insights.

CloudWatch Application Insights analyzes metric patterns using historical data to detect anomalies, and continuously detects errors and exceptions from the application, operating system, and infrastructure logs. It correlates these observations using a combination of classification algorithms and built-in rules. Then, it automatically creates dashboards that show the relevant observations and problem severity information to help you prioritize your actions. For common problems in .NET and SQL application stacks, such as application latency, SQL Server failed backups, memory leaks, large and invalid HTTP requests, and canceled I/O operations, CloudWatch Application Insights provides additional insights that point to a possible root cause and steps for resolution.

Built-in integration with [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) allows you to resolve issues by running the relevant AWS Systems Manager Automation document. CloudWatch Application Insights passes the severity level for each problem to AWS Systems Manager OpsCenter, which further helps the you prioritize and assign tasks within your support teams.

## Migrate
<a name="migrating-microsoft-workloads-migrate"></a>

CloudWatch Application Insights is part of the Windows on Amazon EC2 ecosystem. Using CloudWatch Application Insights for monitoring is an essential part of this offering. After you start the migration of workloads into AWS, you can depend on CloudWatch Application Insights to monitor your Microsoft workloads. Additionally, CloudWatch Application Insights provides support beyond Microsoft workloads, including support for SAP, Java, Oracle, MySQL, PostgreSQL, and other AWS resources (including support for serverless applications). To get started with CloudWatch Application Insights, see [Getting set up](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html) in the CloudWatch documentation.
