---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/performance-monitoring.html
---

# Performance monitoring
<a name="performance-monitoring"></a>

AWS provides a number of features and services to monitor the performance of Oracle database instances. They cover a variety of aspects from the hypervisor level, to the operating system, to inside the database.

## Automatic monitoring
<a name="auto-monitor"></a>

Amazon RDS for Oracle and Amazon RDS Custom for Oracle both provide automatic monitoring at the hypervisor level. By default, Amazon RDS automatically sends metrics data to Amazon CloudWatch in 60-second periods. Data points are available for 15 days.

## Enhanced Monitoring
<a name="enhanced-monitoring"></a>

Enhanced Monitoring for Amazon RDS provides deeper visibility into operating system metrics and process information. You can configure it to collect at an interval of 1, 5, 10, 15, 30, or 60 seconds. The information can be visualized on the AWS Management Console, and you can customize the metrics and dashboard specifically to your business needs. For more information, see [OS metrics in Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring-Available-OS-Metrics.html) and [Amazon RDS FAQs for Enhanced Monitoring](https://aws.amazon.com/rds/faqs/#Enhanced_Monitoring).

Enhanced Monitoring is currently not supported on Amazon RDS Custom for Oracle.

## Performance Insights
<a name="performance-insights"></a>

Performance Insights expands Amazon RDS monitoring features even further inside the database instance to help you analyze your database performance. With the Performance Insights dashboard, you can visualize the Oracle database load and filter by waits, SQL statements, hosts, or users. For more information, see [Monitoring DB load with Performance Insights on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html).

Amazon RDS Custom for Oracle does not support Performance Insights.

## Oracle Enterprise Manager
<a name="oracle-enterprise-mgr"></a>

Oracle Enterprise Manager (OEM) is the Oracle native monitoring solution. It uses Management Agent running on the database host to push database monitoring and performance metrics data to a centralized Oracle Manager Server (OMS). It's your responsibility to install, configure, and manage the entire OEM system.

Both Amazon RDS for Oracle and Amazon RDS Custom for Oracle support installing OEM Management Agent.

## Performance monitoring options
<a name="perf-option-table"></a>

The following table compares performance monitoring options for Amazon RDS for Oracle and Amazon RDS Custom for Oracle.

|  |  |  |
| --- |--- |--- |
| Performance monitoring option | Amazon RDS for Oracle | Amazon RDS Custom for Oracle |
| Automatic monitoring | Yes | Yes |
| Enhanced Monitoring | Yes | No |
| Performance Insights | Yes | No |
| OEM Management Agent | Yes | Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
