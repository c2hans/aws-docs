---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-waf-logs.html
---

# AWS WAF logs
<a name="aws-waf-logs"></a>

 [AWS WAF Access Logs](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html) provide detailed information about traffic that is analyzed by your web ACL. Logged information includes the time that AWS WAF received a web request from your AWS resource, detailed information about the request, and details about the rules that the request matched.

You can create a log ingestion into Amazon OpenSearch Service either by using the Centralized Logging with OpenSearch console or by deploying a standalone CloudFormation stack.

**Important**
Deploy Centralized Logging with OpenSearch solution in the same Region as your Web ACLs, or you will not be able to create a AWS WAF pipeline. For example:
If your Web ACL is associated with Global CloudFront, you must deploy the solution in us-east-1.
If your Web ACL is associated with other resources in Regions like Ohio, your Centralized Logging with OpenSearch stack must also be deployed in that Region.
The AWS WAF logging bucket must be the same as the Centralized Logging with OpenSearch solution.
 [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) logs are not supported in Centralized Logging with OpenSearch. Learn more about [migrating rules from AWS WAF Classic to the new AWS WAF](https://aws.amazon.com/blogs/security/migrating-rules-from-aws-waf-classic-to-new-aws-waf/).
The Amazon OpenSearch Service index is rotated on a daily basis by default, and you can adjust the index in the Additional Settings.

## Create log ingestion (OpenSearch Engine)
<a name="create-log-ingestion-opensearch-engine-6"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-10"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the **AWS Services** section, choose **AWS WAF**.

1. Choose **Next**.

1. Under Specify settings, choose Automatic or Manual.
   + For **Automatic** mode, choose a Web ACL in the dropdown list.
   + For **Manual** mode, enter the **Web ACL name**.
   + (Optional) If you are ingesting AWS WAF logs from another account, select a [linked account](cross-account-ingestion.md#add-a-member-account) from the **Account** dropdown list first.

1. Specify an Ingest Options. Choose between Sampled Request or Full Request.
   + For **Sampled Request**, enter how often you want to ingest sample requests in minutes.
   + For **Full Request**, if the Web ACL log is not enabled, choose **Enable** to enable the access log, or enter **Log location** in Manual mode. Note that Centralized Logging with OpenSearch will automatically enable logging with a Firehose stream as destination for your AWS WAF.

1. Choose **Next**.

1. In the Specify OpenSearch domain section, select an imported domain for the Amazon OpenSearch Service domain.

1. Choose **Yes** for **Sample dashboard** if you want to ingest an associated templated Amazon OpenSearch Service dashboard.

1. You can change the **Index Prefix** of the target Amazon OpenSearch Service index if needed. The default prefix is the Web ACL Name.

1. In the **Log Lifecycle** section, enter the number of days to manage the Amazon OpenSearch Service index lifecycle. The Centralized Logging with OpenSearch will create the associated [Index State Management (ISM)](https://opensearch.org/docs/latest/im-plugin/ism/index/) policy automatically for this pipeline.

1. In the **Select log processor** section, choose the log processor.

   1. When selecting Lambda as a log processor, you can configure the Lambda concurrency if needed.

   1. (Optional) OSI as log processor is now supported in these [Regions](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-opensearch-service-ingestion/). When OSI is selected, type in the minimum and maximum number of OCU. See more information [here](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html#ingestion-scaling).

1. Choose **Next**.

1. Add tags if needed.

1. Choose **Create**.

### Using the CloudFormation Stack
<a name="using-the-cloudformation-stack-10"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - AWS WAF Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions (Full Request) |  [https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFLog.template](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFLog.template)  |
| AWS China Regions (Full Request) |  [https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFLog.template](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFLog.template)  |
| AWS Regions (Sampled Request) |  [https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFSampledLog.template](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFSampledLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFSampledLog.template)  |
| AWS China Regions (Sampled Request) |  [https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFSampledLog.template](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFSampledLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/WAFSampledLog.template)  |

1. Log in to the AWS Management Console and select the button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the stack in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.
   + Parameters for **Full Request** only
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-waf-logs.html)
   + Parameters for **Sampled Request** only
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-waf-logs.html)
   + Common parameters
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-waf-logs.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-10"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Filters | \* Filters | The following data can be filtered by query filter conditions. |
| Web ACLs | \* log event \* webaclName | Displays the count of requests made to the AWS WAF, grouped by Web ACL Names. |
| Total Requests | \* log event | Displays the total number of web requests. |
| Request Timeline | \* log event | Presents a bar chart that displays the distribution of events over time. |
| AWS WAF Rules | \* terminatingRuleId | Presents a pie chart that displays the distribution of events over the AWS WAF rules in the Web ACL. |
| Total Blocked Requests | \* log event | Displays the total number of blocked web requests. |
| Unique Client IPs | \* Request.ClientIP | Displays unique visitors identified by client IP. |
| Country or Region By Request | \* Request.Country | Displays the count of requests made to the Web ACL (grouped by the corresponding country or Region resolved by the client IP). |
| Http Methods | \* Request.HTTPMethod | Displays the count of requests made to the Web ACL using a pie chart, grouped by HTTP request method names (for example, POST, GET, HEAD). |
| Http Versions | \* Request.HTTPVersion | Displays the count of requests made to the Web ACL using a pie chart, grouped by HTTP protocol version (for example, HTTP/2.0, HTTP/1.1). |
| Top WebACLs | \* webaclName \* webaclId.keyword | The web requests view enables you to analyze the top web requests. |
| Top Hosts | \* host | Lists the source IP addresses associated with events, enabling you to identify and investigate potentially suspicious or unauthorized activities. |
| Top Request URIs | \* Request.URI | Top 10 request URIs. |
| Top Countries or Regions | \* Request.country | Top 10 countries with the Web ACL Access. |
| Top Rules | \* terminatingRuleId | Top 10 rules in the web ACL that matched the request. |
| Top Client IPs | \* Request.ClientIP | Provides the top 10 IP address. |
| Top User Agents | \* userAgent | Provides the top 10 user agents |
| Block Allow Host Uri | \* host \* Request.URI \* action | Provides blocked or allowed web requests. |
| Top Labels with Host, Uri | \* labels.name \* host \* Request.URI | Top 10 detailed logs by labels with host, URI |
| View by Matching Rule | \* sc-status | This visualization provides detailed logs by DQL "terminatingRuleId:\*". |
| View by httpRequest args,uri,path | \* sc-status | This visualization provides detailed logs by DQL. |

You can access the built-in dashboard in Amazon OpenSearch Service to view log data. For more information, see the [Access Dashboard](getting-started.md#step-4-access-the-dashboard).

 **AWS WAF logs sample dashboard.**

![image42](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image42.png)

## Create log ingestion (Light Engine)
<a name="create-log-ingestion-light-engine-4"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-11"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the **AWS Services** section, choose **AWS WAF**.

1. Choose **Light Engine**, choose **Next**.

1. Under Specify settings, choose Automatic or Manual.
   + For **Automatic** mode, choose a Web ACL from the dropdown list.
   + For **Manual** mode, enter the Web ACL name.
   + (Optional) If you are ingesting CloudFront logs from another account, select a [linked account](cross-account-ingestion.md#add-a-member-account) from the **Account** dropdown list first.

1. Choose **Next**.

1. Choose **Log Processing Enriched fields** if needed. The available plugins are **location** and **OS/User Agent**. Enabling rich fields increases data processing latency and processing costs. By default, it is not selected.

1. In the **Specify Light Engine Configuration** section, if you want to ingest associated templated Grafana dashboards, select **Yes** for the sample dashboard.

1. You can choose an existing Grafana, or if you must import a new one, you can go to Grafana for configuration.

1. Select an S3 bucket to store partitioned logs and define a name for the log table. We have provided a predefined table name, but you can modify it according to your business needs.

1. If needed, change the log processing frequency, which is set to **5** minutes by default, with a minimum processing frequency of **1** minute.

1. In the **Log Lifecycle** section, enter the log merge time and log archive time. We have provided default values, but you can adjust them based on your business requirements.

1. Select **Next**.

1. If desired, add tags.

1. Select **Create**.

### Using the CloudFormation Stack
<a name="using-the-cloudformation-stack-11"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - AWS WAF Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions |  [https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesWafPipeline.template](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesWafPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesWafPipeline.template)  |
| AWS China Regions |  [https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesWafPipeline.template](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesWafPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesWafPipeline.template)  |

1. Log in to the AWS Management Console and select the preceding button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the stack in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.

   1. Parameters for **Pipeline settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-waf-logs.html)

   1. Parameters for **Destination settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-waf-logs.html)

   1. Parameters for **Scheduler settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-waf-logs.html)

   1. Parameters for **Notification settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-waf-logs.html)

   1. Parameters for **Dashboard settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-waf-logs.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates IAM resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-11"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Filters | Filters | The following data can be filtered by query filter conditions. |
| Total Requests | log event | Displays the total number of web requests. |
| Total Blocked Requests | log event | Displays the total number of blocked web requests. |
| Requests History | log event | Presents a bar chart that displays the distribution of events over time. |
| AWS WAF ACLs | log event webaclName | Displays the count of requests made to the AWS WAF, grouped by Web ACL Names. |
| AWS WAF Rules | terminatingRuleId | Presents a pie chart that displays the distribution of events over the AWS WAF rules in the Web ACL. |
| Sources | httpSourceId | Presents a pie chart that displays the distribution of events over the id of the associated resource. |
| HTTP Methods | httpRequest.HTTPMethod | Displays the count of requests made to the Web ACL using a pie chart, grouped by HTTP request method names (for example, POST, GET, HEAD). |
| Country or Region By Blocked Requests | HTTPRequest.Country | Displays the count of blocked web requests made to the Web ACL (grouped by the corresponding country or Region resolved by the client IP). |
| Top WebACLs | webaclName | The web requests view enables you to analyze the top web requests. |
| Top Sources | httpSourceId | Top 10 id of the associated resource. |
| Top Requests URIs | httpRequest.URI | Top 10 request URIs. |
| Top Countries or Regions | httpRequest.country | Top 10 countries with the Web ACL Access. |
| Top Rules | terminatingRuleId | Top 10 rules in the web ACL that matched the request. |
| Top Client IPs | httpRequest.ClientIP | Provides the top 10 IP addresses. |
| Top Blocked / Allowed Hosts URI | host httpRequest.URI action | Provides blocked or allowed web requests. |
| Top Labels with Host, URI | labels host httpRequest.URI | Top 10 detailed logs by labels with host, URI. |
| Metrics | webaclId webaclName terminatingRuleId terminatingRuleType httpSourceId httpRequest.HTTPMethod httpRequest.country httpRequest.ClientIP labels httpRequest.URI action | Provides a detailed list of log events, including timestamps, web ACL, and client IP. |

 **AWS WAF logs sample dashboard.**

![image43](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image43.jpeg)
