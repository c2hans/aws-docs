---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/monitoring-the-solution.html
---

# Monitoring the solution
<a name="monitoring-the-solution"></a>

## Overview
<a name="monitoring-overview"></a>

The Innovation Sandbox solution includes observability tools for monitoring the solution resources.

## Amazon CloudWatch Application Insights
<a name="cloudwatch-application-insights"></a>

Innovation Sandbox on AWS includes access to [Amazon CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html) to provide automatic detection and alerting for any errors raised by the solution. When a recurring error is detected within the solution, Application Insights will raise an alarm indicating the potential problem.

Currently, active alarms are displayed in the [AWS Cloudwatch Console Dashboard](https://console.aws.amazon.com/cloudwatch/home). You can also view an overview of all current and previously detected issues for the solution using the CloudFormation Application Insights console.

CloudWatch Application Insights helps you monitor your applications by identifying and setting up key metrics, logs, and alarms across your [application resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-what-is.html#appinsights-components) and your technology stack. It continuously monitors metrics and logs to detect and correlate anomalies and errors. To assist with troubleshooting, it creates automated dashboards for detected problems, which include correlated metric anomalies and log errors, along with additional insights to identify a potential root cause.

To view the CloudWatch AppInsights dashboard for Innovation Sandbox:

1. Sign in to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. From the left sidebar, under **Insights**, choose **Application Insights**.

1. Select the **Applications** tab.

1. In the *Find applications* search box, type the solution name to find the dashboard.

1. Select the dashboard, and the application.

The dashboard displays various metrics and logs for your solution.

## Cloudwatch log queries
<a name="cloudwatch-log-queries"></a>

**Note**
Innovation Sandbox implements a multi-tier log retention strategy optimized for both cost efficiency and audit compliance:

 **Retention Tiers**
CloudWatch Logs
90 days (default)
S3 Standard Storage
1 year (default)
S3 Glacier Storage
6 additional years (default)
Total Retention
7 years

 **Automatic Archiving**
Logs are automatically exported from CloudWatch to S3 every 7 days, ensuring long-term audit trail availability while minimizing CloudWatch storage costs.

 **Operational Benefits**
The 90-day CloudWatch retention provides sufficient time for operational troubleshooting, while the S3/Glacier archiving ensures compliance with typical audit and regulatory requirements.

Innovation Sandbox provides several pre-populated AWS CloudWatch log insights queries that allow you to troubleshoot issues.

To access log insights queries:

1. Sign in to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1. From the left sidebar, under **Logs**, choose **Logs Insights**.

1. On the Logs Insights tab, select **Saved and sample queries**.

1. From the Sample queries, run one of these queries:
   +  **LogQuery** — search for all logs related to a specific account, lease, leaseTemplate, or user.
   +  **ErrorLogs** — view all recent errors.
   +  **AccountCleanupLogs** — view the logs from a specific cleanup execution.

The logs section will display the compute logs for the solution.

## AWS X-Ray
<a name="aws-x-ray"></a>

Innovation Sandbox includes access to [AWS X-Ray](https://aws.amazon.com/xray/) for all critical execution paths. This allows you to troubleshoot any failing workflows and identify where the errors are occurring.
