---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-application-activity-by-using-cloudwatch-logs-insights.html
---

# Monitor application activity by using CloudWatch Logs Insights
<a name="monitor-application-activity-by-using-cloudwatch-logs-insights"></a>

*Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="monitor-application-activity-by-using-cloudwatch-logs-insights-summary"></a>

This pattern provides a solution for automatically detecting and alerting on application exceptions by using Amazon CloudWatch Logs Insights. By implementing automated log analysis and alerting, you can quickly identify and respond to application issues in your production environment.

Logs play a crucial role in monitoring system behavior, identifying issues, and ensuring optimal performance. During a migration process, log files are invaluable for validating the system's functioning in the new environment, detecting compatibility problems, and identifying any unexpected behaviors. Issues could be related to operations or security. For security-related issues, enabling the detection of unauthorized access attempts or suspicious activities early is essential for maintaining security and regulatory compliance. This capability is especially important when dealing with sensitive data or critical systems.

This pattern is particularly valuable for teams that need to do the following:
+ Maintain high application availability.
+ Respond to production issues quickly.
+ Analyze application-specific errors not captured by AWS service logs.
+ Perform on-demand log analysis without pre-built infrastructure.

CloudWatch Logs Insights is optimal for analyzing application-generated logs where the error context exists only within your application code. CloudWatch Logs Insights excels at the following tasks:
+ Query unstructured or semi-structured log data.
+ Perform on-demand analysis during incident response.
+ Correlate events across multiple log groups.
+ Create quick visualizations without external tools.

## Prerequisites and limitations
<a name="monitor-application-activity-by-using-cloudwatch-logs-insights-prereqs"></a>

**Prerequisites**
+ A production application deployed in active AWS account
+ Basic understanding of the production application's logging format and exception patterns
+ Application logs configured to stream to Amazon CloudWatch Logs

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="monitor-application-activity-by-using-cloudwatch-logs-insights-architecture"></a>

The following diagram shows how CloudWatch Logs Insights evaluates resource logs and sends a relevant data visualization to a CloudWatch dashboard.

![CloudWatch Logs Insights evaluates resource logs and sends data visualization to dashboard.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/082ff4b6-9303-42e6-bc62-263e2254f232/images/b1cbb699-07cd-45e6-ac06-839159bafa6b.png)

The diagram shows the following workflow:

1. The resources publish logs to CloudWatch Logs. Resources can include AWS resources such as Amazon Elastic Compute Cloud (Amazon EC2) instances or Amazon Simple Storage Service (Amazon S3) buckets. Another example includes on-premises systems with CloudWatch Agent installed that can publish logs to CloudWatch.

1. CloudWatch Logs Insights filters for the relevant pattern string. Examples of search pattern strings include "error", "exception", or a specific regular expression.

1. Typically, the production support team or developers add the pattern visualization to the CloudWatch dashboard.

**Automation and scale**

Developers can automate this pattern’s solution by using the AWS Cloud Development Kit (AWS CDK), AWS CloudFormation, or AWS SDKs to handle multiple string patterns. Teams can incorporate this automation into their continuous integration and deployment (CI/CD) DevOps processes.

## Tools
<a name="monitor-application-activity-by-using-cloudwatch-logs-insights-tools"></a>

**AWS services**
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.

## Best practices
<a name="monitor-application-activity-by-using-cloudwatch-logs-insights-best-practices"></a>

**Query efficiency**
+ Define and configure [log groups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) to analyze relevant log data.
+ Use field explorers to understand the structure and fields available in your log data.
+ Write efficient queries by using [CloudWatch Logs Insights query syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_LogsInsights.html).
+ Adapt [sample queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html) to your specific requirements for quicker analysis.
+ Limit query time ranges to reduce data scanned and improve performance.
+ [Save queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_Insights-Saving-Queries.html) for future use to save time and ensure consistent analysis.

**Security**
+ Apply appropriate IAM[ policies](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html) to CloudWatch Logs Insights and log groups. Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.
+ Enable [log data encryption using AWS KMS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Encrypt.html) for sensitive log data.

**Cost optimization**
+ CloudWatch Logs Insights charges per GB of data scanned per query. Narrow time ranges and target specific log groups to reduce costs.
+ Configure appropriate log retention policies to manage storage costs.
+ For frequent analysis of large historical datasets, consider exporting logs to Amazon S3 and using Amazon Athena.
+ Review [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/) to understand cost implications for your use case.

## Epics
<a name="monitor-application-activity-by-using-cloudwatch-logs-insights-epics"></a>

### Create log group and configure logs to view in dashboard.
<a name="create-log-group-and-configure-logs-to-view-in-dashboard"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure IAM permissions. | To configure IAM permissions, do the following:1. Identify the IAM roles used by your application for writing logs and by users or services that will create dashboards, queries, and alarms.<br />2. For the application role, add the following API actions and resource to a policy:<pre>{<br />         "Version": "2012-10-17",		 	 	 <br />         "Statement": [<br />             {<br />                 "Effect": "Allow",<br />                 "Action": [<br />                     "logs:CreateLogGroup",<br />                     "logs:CreateLogStream",<br />                     "logs:PutLogEvents"<br />                 ],<br />                 "Resource": [<br />                     "arn:aws:logs:*:*:*"<br />                 ]<br />             }<br />         ]<br />     }</pre><br />3. For managing CloudWatch resources, add the following to a policy:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Action": [<br />                "cloudwatch:PutDashboard",<br />                "cloudwatch:GetDashboard",<br />                "logs:StartQuery",<br />                "logs:StopQuery",<br />                "logs:GetQueryResults",<br />                "cloudwatch:PutMetricAlarm"<br />            ],<br />            "Resource": "*"<br />        }<br />    ]<br />}<br /></pre><br />For information about how to create IAM policies or to add permissions to existing policies, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) and [Edit IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html) in the *IAM User Guide*. For more information, see [Identity and access management for Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/auth-and-access-control-cwl.html) and [CloudWatch Logs permissions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html) in the *Amazon CloudWatch Logs User Guide*. | AWS administrator, AWS DevOps, AWS systems administrator, Cloud administrator, Cloud architect, DevOps engineer |
| Create a log group. | To create a log group, use any of the following options:+ Create or open a CloudFormation template file (YAML or JSON format) with a `.yaml` or `.json` extension. (The following code uses YAML format.) Add the following resource definition to the [Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html) section of your template:<pre>MyLogGroup:<br />  Type: AWS::Logs::LogGroup<br />  Properties:<br />    LogGroupName: my-log-group</pre><br />For more information, see [Quick Start: Use AWS CloudFormation to get started with CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/QuickStartCloudFormation.html) in the *Amazon CloudWatch Logs User Guide*.+ Use the CloudWatch console, as described in [Create a log group in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#Create-Log-Group) in the *Amazon CloudWatch Logs User Guide*.<br />+ Use the [CreateLogGroup](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.html) operation in the [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#Create-Log-Group) API. | AWS administrator, AWS DevOps, AWS systems administrator, Cloud administrator, Cloud architect, DevOps engineer |
| Generate a CloudWatch Logs Insights query. | To create and save a CloudWatch Logs Insights query, do the following:1. Open the CloudWatch console.<br />2. Navigate to **Logs Insights**.<br />3. Create your query by using one of the following methods:Start with a [sample query](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html) from the **Queries** section.Write a custom query.[Modify](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_Insights-Saving-Queries.html) the following example query:<pre>fields @timestamp, @message | filter @message like /(?i)exception/|stats count() by bin(30s)</pre><br />This query checks the log file, extracts the timestamp and message content, filters for the word "exception" (case-insensitive), and counts occurrences in 30-second intervals. | AWS administrator, AWS DevOps, AWS systems administrator, Cloud administrator, Cloud architect, DevOps engineer |
| Create visualization in a CloudWatch dashboard. | To use a CloudWatch dashboard to create a visualization, do the following:1. Open the CloudWatch console, and [create a CloudWatch dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html) (if you don’t have one already) or open an existing dashboard. <br />2. Add your exception monitoring visualization. Bar, line, and pie charts are available, depending on your business need. For more information, see [Using widgets on CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-and-work-with-widgets.html) in the *Amazon CloudWatch Logs User Guide*. For real-time data visualizations, you can customize a widget to meet your requirements.<br />For more information about dashboard options and capabilities, see [Using Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) and [Creating flexible CloudWatch dashboards with dashboard variables](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables.html) in the *Amazon CloudWatch Logs User Guide*. | AWS administrator, AWS DevOps, AWS systems administrator, Cloud administrator, Cloud architect, DevOps engineer |

## Troubleshooting
<a name="monitor-application-activity-by-using-cloudwatch-logs-insights-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Unable to see query results or query seems broken | Start with a working query that was modified from a [sample query](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html). Perform small incremental changes to parts of the query (such as a filter or field), and take advantage of the CloudWatch Logs [query generator feature](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Assist.html). |
| Log groups not creating log streams | In the IAM policy, make sure that the resource for the [CreateLogStream](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.html) and the [CreateLogGroup](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.html) operations is provided with a wildcard character `(*)` value. The `create `operation will not succeed without this wildcard permission. |
| Query timeout or slow performance | Reduce the time range, target specific log groups, or simplify the query. Complex regular expression (`regex`) patterns and large time ranges increase query time. |
| No data returned for valid time range | Verify log group selection and check that logs are being ingested (review log streams), and confirm the filter pattern matches your log format. |

## Related resources
<a name="monitor-application-activity-by-using-cloudwatch-logs-insights-resources"></a>
+ [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
+ [Amazon CloudWatch FAQs](https://aws.amazon.com/cloudwatch/faqs/#topic-0)
+ [Creating flexible CloudWatch dashboards with dashboard variables](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables.html)
+ [Get started with Logs Insights QL: Query tutorials](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Tutorials.html)
+ [Use natural language to generate and update CloudWatch Logs Insights queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Assist.html)
+ [Use PutDashboard with an AWS SDK or CLI](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/example_cloudwatch_PutDashboard_section.html)
+ [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)
