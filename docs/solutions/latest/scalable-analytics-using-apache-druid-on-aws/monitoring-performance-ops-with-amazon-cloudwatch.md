---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/monitoring-performance-ops-with-amazon-cloudwatch.html
---

# Monitoring performance and operations with Amazon CloudWatch
<a name="monitoring-performance-ops-with-amazon-cloudwatch"></a>

The guidance captures all the Druid data logs in Amazon CloudWatch for monitoring purposes. This includes alarms, logs and a dashboard for reporting purposes.

 **Amazon CloudWatch** gives you an application-level view into this guidance and its resources so that you can:
+ Monitor alarms, logs for your deployed clusters, and metrics associated with this guidance from a central location.
+ View operations data for the guidance’s AWS resources (such as deployment status, Amazon CloudWatch alarms, resource configurations, and operational issues) in the context of an application.

Sign in to the [AWS Management Console](https://console.aws.amazon.com/), and navigate to **CloudWatch**. Use the left hand navigation to view this data for your Druid deployment.

**Note**
You must activate the CloudWatch Application Insights before you can use CloudWatch to monitor any alarms, logs, or dashboards for the guidance. For more information, refer to the [Activate CloudWatch Application Insights](activate-cloudwatch-application-insights.md) section.

## Dashboard
<a name="dashboard"></a>

1. From the left, select **CloudWatch > Dashboards**.

1. On the **Custom Dashboards** tab, click to select the dashboard you want to view. For example, `druid-ec2-custom-name-ops` -dashboard.

 **CloudWatch dashboard for Scalable Analytics using Apache Druid on AWS.**

![image4](http://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/images/image4.png)

The dashboard provides the following information for your Druid deployment.

| Item | Description |
| --- | --- |
| Canary status | Displays the availability and latency of your web services and allows you to discover and troubleshoot any issues. |
| Application Load Balancer (ALB) - Key Performance Indicators | Provides the following data in relation to your ALB application:<br />\* Request Count \* Target Response Time \* HTTP Connection Count \* Response Code Count |
| Druid - Key Performance Indicators | Provides the following data in relation to Druid core parameters:<br />\* Deep Storage \* Ingestion Count \* Query Count \* Query Time |
| Druid ZooKeeper - Key Performance Indicators | Displays the following data in relation to the Zookeeper cluster state management:<br />\* CPU Utilization (%) \* Network In/Out (bytes) \* Memory Utilization (%) \* Disk Utilization (%) |
| Druid data | Displays the following data in relation to the Druid ingestion jobs and queryable data:<br />\* CPU Utilization (%) \* Network In/Out (bytes) \* Memory Utilization (%) \* Disk Utilization (%) |
| Druid query | Displays the following data in relation to the Druid queries:<br />\* CPU Utilization (%) \* Network In/Out (bytes) \* Memory Utilization (%) \* Disk Utilization (%) |
| Druid master | Displays the following data in relation to the Druid data ingestion and availability:<br />\* CPU Utilization (%) \* Network In/Out (bytes) \* Memory Utilization (%) \* Disk Utilization (%) |
| Aurora Cluster | Provides the following data in relation to the Druid databases:<br />\* CPU Utilization (%) \* Database connections \* Throughput \* Free Memory |

## Alarms
<a name="alarms"></a>

Amazon CloudWatch provides detailed alarms for your Druid deployment, and displays the different states, conditions, and relevant actions associated with these alarms. To view the **Alarms** page, from the left, select **CloudWatch > Alarms**.

For more information about alarms, alarm states, actions, and configuring alarms, refer to the [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) page.

## Logs
<a name="logs"></a>

You can use Amazon CloudWatch Logs to monitor, store, and access your log files from Amazon Elastic Compute Cloud (Amazon EC2) instances, and other sources. CloudWatch Logs allow you to centralize the logs from all of your Druid guidance components, applications, and AWS services, in a single, highly scalable service.

To view logs for the Druid deployment, from the left, select **CloudWatch > logs > Log groups**.

For more information about working with log groups and log streams, refer to the [AWS CloudWatch logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) page.

## Metrics
<a name="metrics"></a>

In addition to logs and alarms, CloudWatch allows to view, and analyze data about the performance of your Druid deployment via custom namespaces.

To view metrics for the Druid deployment:

1. From the left, select **CloudWatch > Metrics > All metrics**.

1. On the Metrics page, under Custom namespaces, select `AWSSolutions/Druid`. This will display all metrics for the Druid deployment.

    **Screenshot of metrics for Scalable Analytics using Apache Druid on AWS in CloudWatch.**
![image5](http://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/images/image5.png)

1. Choose to select a relevant dimension to view additional information. The dimensions page provides a breakdown of individual Druid services, source, query, and other metrics.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Scalable Analytics Using Apache Druid on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
