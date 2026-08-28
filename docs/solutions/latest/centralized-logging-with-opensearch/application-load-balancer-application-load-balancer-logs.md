---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/application-load-balancer-application-load-balancer-logs.html
---

# Application Load Balancer logs
<a name="application-load-balancer-application-load-balancer-logs"></a>

 [Application Load Balancer access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html) capture detailed information about requests sent to your load balancer. Application Load Balancer publishes a log file for each load balancer node every 5 minutes.

You can create a log ingestion into Amazon OpenSearch Service either by using the Centralized Logging with OpenSearch console or by deploying a standalone CloudFormation stack.

**Important**
The Elastic Load Balancing logging bucket must be the same as the Centralized Logging with OpenSearch solution.
The Amazon OpenSearch Service index is rotated on a daily basis by default, and you can adjust the index in the Additional Settings.

## Create log ingestion (OpenSearch Engine)
<a name="create-log-ingestion-opensearch-engine-5"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-8"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the AWS Services section, choose **Elastic Load Balancer**.

1. Choose **Next**.

1. Under Specify settings, choose Automatic or Manual.
   + For **Automatic** mode, choose an Application Load Balancer in the dropdown list. (If the selected Application Load Balancer access log is not enabled, choose **Enable** to enable the Application Load Balancer access log.)
   + For Manual mode, enter the Application Load Balancer identifier and Log location.
   + (Optional) If you are ingesting logs from another account, select a [linked account](cross-account-ingestion.md#add-a-member-account) from the **Account** dropdown first.

1. Choose **Next**.

1. In the Specify OpenSearch domain section, select an imported domain for the Amazon OpenSearch Service domain.

1. Choose **Yes** for **Sample dashboard** if you want to ingest an associated templated Amazon OpenSearch Service dashboard.

1. You can change the **Index Prefix** of the target Amazon OpenSearch Service index if needed. The default prefix is the Load Balancer Name.

1. In the **Log Lifecycle** section, input the number of days to manage the Amazon OpenSearch Service index lifecycle. The Centralized Logging with OpenSearch will create the associated [Index State Management (ISM)](https://opensearch.org/docs/latest/im-plugin/ism/index/) policy automatically for this pipeline.

1. In the **Log Lifecycle** section, enter the number of days to manage the Amazon OpenSearch Service index lifecycle. Centralized Logging with OpenSearch will create the associated [Index State Management (ISM)](https://opensearch.org/docs/latest/im-plugin/ism/index/) policy automatically for this pipeline.

1. In the **Select log processor** section, choose the log processor.

   1. When selecting Lambda as a log processor, you can configure the Lambda concurrency if needed.

   1. (Optional) OSI as log processor is now supported in these [Regions](https://aws.amazon.com/about-aws/whats-new/2023/04/amazon-opensearch-service-ingestion/). When OSI is selected, type in the minimum and maximum number of OCU. See more information [here](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ingestion.html#ingestion-scaling).

1. Choose **Next**.

1. Add tags if needed.

1. Choose **Create**.

### Using the CloudFormation Stack
<a name="using-the-cloudformation-stack-8"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - ELB Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions |  [![Launch solution](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/ELBLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/ELBLog.template)  |
| AWS China Regions |  [![Launch solution](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/ELBLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/ELBLog.template)  |

1. Log in to the AWS Management Console and select the preceding button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the stack in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/application-load-balancer-application-load-balancer-logs.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-8"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Total Requests | \* log event | Displays aggregated events based on a specified time interval. |
| Request History | \* log event | Presents a bar chart that displays the distribution of events over time. |
| Request By Target | \* log event \* target\_ip | Presents a bar chart that displays the distribution of events over time and IP. |
| Unique Visitors | \* client\_ip | Displays unique visitors identified by client IP address. |
| Status Code | \* elb\_status\_code | Displays the count of requests made to the Application Load Balancer, grouped by HTTP status codes (for example, 200, 404, 403). |
| Status History | \* elb\_status\_code | Shows the historical trend of HTTP status codes returned by the Application Load Balancer over a specific period of time. |
| Status Code Pipe | \* elb\_status\_code | Represents the distribution of requests based on different HTTP status codes using a pie chart. |
| Average Processing Time | \* request\_processing\_time \* response\_processing\_time \* target\_processing\_time | This visualization calculates and presents the average time taken for various operations in the Application Load Balancer. |
| Avg. Processing Time History | \* request\_processing\_time \* response\_processing\_time \* target\_processing\_time | Displays the historical trend of the average time-consuming of each operation returned by the Application Load Balancer within a specific period of time. |
| Request Verb | \* request\_verb | Displays the count of requests made to the Application Load Balancer using a pie chart, grouped by HTTP request method names (for example, POST, GET, HEAD). |
| Total Bytes | \* received\_bytes \* sent\_bytes | Provides insights into data transfer activities, including the total bytes transferred. |
| Sent and Received Bytes History | \* received\_bytes \* sent\_bytes | Displays the historical trend of the received bytes, send bytes |
| SSL Protocol | \* ssl\_protocol | Displays the count of requests made to the Application Load Balancer, grouped by SSL Protocol |
| Top Request URLs | \* request\_url | The web requests view enables you to analyze the top web requests. |
| Top Client IPs | \* client\_ip | Provides the top 10 IP address accessing your Application Load Balancer. |
| Top User Agents | \* user\_agent | Provides the top 10 user agents accessing your Application Load Balancer. |
| Target Status | \* target\_ip \* target\_status\_code | Displays the HTTP status code request count for targets in the Application Load Balancer target group. |
| Abnormal Requests | \* @timestamp \* client\_ip \* target\_ip \* elb\_status\_code \* error\_reason \* request\_verb \* target\_status\_code \* target\_status\_code\_list \* request\_url \* request\_proto \* trace\_id | Provides a detailed list of log events, including timestamps, client ip, and target ip. |
| Requests by OS | \* ua\_os | Displays the count of requests made to the Application Load Balancer, grouped by user agent OS |
| Request by Device | \* ua\_device | Displays the count of requests made to the Application Load Balancer, grouped by user agent device. |
| Request by Browser | \* ua\_browser | Displays the count of requests made to the Application Load Balancer, grouped by user agent browser. |
| Request by Category | \* ua\_category | Displays the count of categories made to the Application Load Balancer, grouped by user agent category (for example, PC, Mobile, Tablet). |
| Requests by Countries or Regions | \* geo\_iso\_code | Displays the count of requests made to the Application Load Balancer (grouped by the corresponding country or Region resolved by the client IP). |
| Top Countries or Regions | \* geo\_country | Top 10 countries with the Application Load Balancer Access. |
| Top Cities | \* geo\_city | Top 10 cities with Application Load Balancer Access |

You can access the built-in dashboard in Amazon OpenSearch Service to view log data. For more information, see the [Access Dashboard](getting-started.md#step-4-access-the-dashboard).

 **Application Load Balancer logs sample dashboard.**

![image40](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image40.png)

## Create log ingestion (Light Engine)
<a name="create-log-ingestion-light-engine-3"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-9"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the AWS Services section, choose **Elastic Load Balancer**.

1. Choose **Next**.

1. Under **Specify settings**, choose **Automatic** or **Manual** for **CloudFront logs enabling**. The automatic mode will detect the CloudFront log location automatically.
   + For **Automatic** mode, choose an Application Load Balancer in the dropdown list. (If the selected Application Load Balancer access log is not enabled, choose **Enable** to enable the Application Load Balancer access log.)
   + For Manual mode, enter the Application Load Balancer identifier and Log location.
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
<a name="using-the-cloudformation-stack-9"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - ELB Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions |  [![Launch solution](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesAlbPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesAlbPipeline.template)  |
| AWS China Regions |  [![Launch solution](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesAlbPipeline.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/MicroBatchAwsServicesAlbPipeline.template)  |

1. Log in to the AWS Management Console and select the preceding button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the stack in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.

   1. Parameters for **Pipeline settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/application-load-balancer-application-load-balancer-logs.html)

   1. Parameters for **Destination settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/application-load-balancer-application-load-balancer-logs.html)

   1. Parameters for **Scheduler settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/application-load-balancer-application-load-balancer-logs.html)

   1. Parameters for **Notification settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/application-load-balancer-application-load-balancer-logs.html)

   1. Parameters for **Dashboard settings**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/application-load-balancer-application-load-balancer-logs.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-9"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Filters | Filters | The following data can be filtered by query filter conditions. |
| Total Requests | log event | Displays aggregated events based on a specified time interval. |
| Unique Visitors | client\_ip | Displays unique visitors identified by client IP address. |
| Requests History | log event | Presents a bar chart that displays the distribution of events over time. |
| Request By Target | log event target\_ip | Presents a bar chart that displays the distribution of events over time and IP. |
| HTTP Status Code | elb\_status\_code | Displays the count of requests made to the Application Load Balancer, grouped by HTTP status codes (for example, 200, 404, 403). |
| Status Code History | elb\_status\_code | Shows the historical trend of HTTP status codes returned by the Application Load Balancer over a specific period of time. |
| Status Code Pie | elb\_status\_code | Represents the distribution of requests based on different HTTP status codes using a pie chart. |
| Average Processing Time | request\_processing\_time response\_processing\_time target\_processing\_time | This visualization calculates and presents the average time taken for various operations in the Application Load Balancer. |
| Avg. Processing Time History | request\_processing\_time response\_processing\_time target\_processing\_time | Displays the historical trend of the average time-consuming of each operation returned by the Application Load Balancer within a specific period of time. |
| HTTP Method | request\_verb | Displays the count of requests made to the Application Load Balancer using a pie chart, grouped by HTTP request method names (for example, POST, GET, HEAD). |
| Total Bytes | received\_bytes sent\_bytes | Provides insights into data transfer activities, including the total bytes transferred. |
| Sent and Received Bytes History | received\_bytes sent\_bytes | Displays the historical trend of the received bytes, send bytes. |
| SSL Protocol | ssl\_protocol | Displays the count of requests made to the Application Load Balancer, grouped by SSL Protocol. |
| Top Request URLs | request\_url | The web requests view enables you to analyze the top web requests. |
| Top Client IPs | client\_ip | Provides the top 10 IP addresses accessing your Application Load Balancer. |
| Bad Requests | type client\_ip target\_group\_arn target\_ip elb\_status\_code request\_verb request\_url ssl\_protocol received\_bytes sent\_bytes | Provides a detailed list of log events, including timestamps, client IP, and target IP. |
| Requests by OS | ua\_os | Displays the count of requests made to the Application Load Balancer, grouped by user agent OS. |
| Requests by Device | ua\_device | Displays the count of requests made to the Application Load Balancer, grouped by user agent device. |
| Requests by Browser | ua\_browser | Displays the count of requests made to the Application Load Balancer, grouped by user agent browser. |
| Requests by Category | ua\_category | Displays the count of categories made to the Application Load Balancer, grouped by user agent category (for example, PC, Mobile, Tablet). |
| Requests by Countries or Regions | geo\_iso\_code | Displays the count of requests made to the Application Load Balancer (grouped by the corresponding country or Region resolved by the client IP). |
| Top Countries or Regions | geo\_country | Top 10 countries with the Application Load Balancer Access. |

 **Application Load Balancer logs sample dashboard.**

![image41](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image41.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Logging with OpenSearch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
