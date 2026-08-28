---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hyperscale-aurora-mysql/tuning-query-workload.html
---

# Tuning your query workload
<a name="tuning-query-workload"></a>

A well-tuned workload will take you a long way in achieving a stable solution for hypergrowth. If your workload is not well tuned, no matter the power of the Amazon Aurora cluster that you use, you will encounter bottlenecks that will degrade performance and impact the user experience of your application. The best practice is to have a process in place from the start that helps you identify and tune problematic queries in your system.

## Tracking and tuning problematic queries in your workload
<a name="track-tune"></a>

When encountering hypergrowth, having a well-tuned work load is half the battle won. To understand the nature of real-time workloads and performance issues your Aurora cluster is facing, ensure that your team gathers problematic queries from both your writer and your reader instances. These problematic queries need to be tuned for your workload to run at an optimal state. Amazon Aurora MySQL-Compatible Edition provides you with two ways to accomplish this:
+ Performance Insights
+ Slow query logs

### Using Performance Insights
<a name="using-performance-insights.942ca63d-e5a2-5f56-9e82-c79ee92bc69c"></a>

Performance Insights tracks the load on the Aurora writer or reader instance based on the average active sessions (AAS). The AAS value is calculated by using sampling and the number of active sessions that are waiting for a CPU to pick up their query workload and process it. Performance Insights provides a graphical interface where you can check the SQL statements that are causing the highest load by waits for active sessions.

![Performance Insights graphs and charts.](http://docs.aws.amazon.com/prescriptive-guidance/latest/hyperscale-aurora-mysql/images/guide-img/49d4e249-129b-4485-8b88-a230c0a689ca/images/99907e19-80ff-461f-899e-eb2566c029ac.png)

In the previous screenshot, the call to the stored procedure `my_sqrt` is causing an average of 13.03 sessions to wait for their loads to be processed. The logical next step is to tune this procedure. You should identify SQL statements in your readers and writers that are causing load on their respective instance and tune them to improve the performance until the AAS values drop and stay below the Max vCPU dotted line in Performance Insights. If you have hit a ceiling with your tuning efforts and still see the AAS over the Max vCPU line, you can opt for a larger instance class to handle your workload. Do not opt for a larger instance without first trying to tune your query workload, because growing traffic will start exposing the fault lines created by bad queries in your workload.

### Using slow query logs and publishing them to CloudWatch
<a name="using-slow-query-logs-and-publishing-them-to-cloudwatch.f8684ad4-baff-530c-8290-db2aac7e4eae"></a>

The slow query log is a native MySQL feature and is complementary to Performance Insights. The best practice is to use both these methods to stay ahead of problematic queries that can cause havoc on your instances. The slow query log logs any query that slower than the dynamic variable `long_query_time`. This variable can be set up without any restart to your cluster instances.

To provide flexibility and isolation in the tuning exercise, use separate parameter groups for your writer and reader instances. This is especially important if you use read-write split. Set up a comfortable limit for `long_query_time` in your cluster instances based on your need. As you tune your load, you can aim for aggressive values in the `long_query_time` variable, because you can set the threshold at the millisecond level. With high concurrency and a well-tuned workload, almost all your queries should run in milliseconds.

When you set Amazon Aurora MySQL-Compatible Edition to log slow queries to a file, Aurora MySQL-Compatible will write the slow query logs to the Aurora MySQL-Compatible file system and retain them for 24 hours. To retain the slow query logs for a longer period for analysis, publish them to Amazon CloudWatch. You can also build a CloudWatch Dashboard to monitor your slow queries. For more information, see the blog post [Creating an Amazon CloudWatch dashboard to monitor Amazon RDS and Amazon Aurora MySQL](https://aws.amazon.com/blogs/database/creating-an-amazon-cloudwatch-dashboard-to-monitor-amazon-rds-and-amazon-aurora-mysql/). In addition to analyzing your slow queries on Amazon CloudWatch, you can profile slow query logs by using pt-query-digest, a tool in [Percona Toolkit](https://www.percona.com/doc/percona-toolkit/LATEST/pt-query-digest.html).

You can also choose to automate this process of downloading and profiling queries for higher efficiency in your team. Your team should check for queries that run frequently and for longer intervals, and prioritize tuning them. Aim for a state where very few queries are logged in your slow query log, and you can reduce the `long_query_time` to get more aggressive as you understand and tune your workload.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
