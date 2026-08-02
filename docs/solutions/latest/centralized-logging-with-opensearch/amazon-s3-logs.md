---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/amazon-s3-logs.html
---

# Amazon S3 logs
<a name="amazon-s3-logs"></a>

 [Amazon S3 server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html) provides detailed records for the requests made to the bucket. S3 Access Logs can be enabled and saved in another S3 bucket.

You can create a log ingestion into Amazon OpenSearch Service either by using the Centralized Logging with OpenSearch console or by deploying a standalone CloudFormation stack.

**Important**
The S3 Bucket Region must be the same as the Centralized Logging with OpenSearch solution Region.
The Amazon OpenSearch Service index is rotated on a daily basis by default, and you can adjust the index in the Additional Settings.

## Create log ingestion (OpenSearch Engine)
<a name="create-log-ingestion-opensearch-engine-1"></a>

### Using the Centralized Logging with OpenSearch Console
<a name="using-the-centralized-logging-with-opensearch-console-2"></a>

1. Sign in to the Centralized Logging with OpenSearch Console.

1. In the navigation pane, under **Log Analytics Pipelines**, choose **Service Log**.

1. Choose the Create a log ingestion button.

1. In the **AWS Services** section, choose **Amazon S3**.

1. Choose **Next**.

1. Under **Specify settings**, choose **Automatic** or **Manual** for **Amazon S3 Access Log enabling**. The automatic mode will enable the Amazon S3 Access Log and save the logs to a centralized S3 bucket if logging is not enabled yet.
   + For **Automatic mode**, choose the S3 bucket from the dropdown list.
   + For Manual mode, enter the Bucket Name and Amazon S3 Access Log location.
   + (Optional) If you are ingesting Amazon S3 logs from another account, select a [linked account](cross-account-ingestion.md#add-a-member-account) from the **Account** dropdown list first.

1. Choose **Next**.

1. In the Specify OpenSearch domain section, select an imported domain for the Amazon OpenSearch Service domain.

1. Choose **Yes** for **Sample dashboard** if you want to ingest an associated built-in Amazon OpenSearch Service dashboard.

1. You can change the **Index Prefix** of the target Amazon OpenSearch Service index if needed. The default prefix is your bucket name.

1. In the **Log Lifecycle** section, enter the number of days to manage the Amazon OpenSearch Service index lifecycle. The Centralized Logging with OpenSearch will create the associated [Index State Management (ISM)](https://opensearch.org/docs/latest/im-plugin/ism/index/) policy automatically for this pipeline.

1. Choose **Next**.

1. Add tags if needed.

1. Choose **Create**.

### Using the CloudFormation Stack
<a name="using-the-cloudformation-stack-2"></a>

This automated AWS CloudFormation template deploys the *Centralized Logging with OpenSearch - Amazon S3 Access Log Ingestion* solution in the AWS Cloud.

|  | Launch in AWS Management Console | Download Template |
| --- | --- | --- |
| AWS Regions |  [https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/S3AccessLog.template](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/S3AccessLog.template)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/S3AccessLog.template)  |
| AWS China Regions |  ![Launch solution](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image17.png)  |  [Template](https://solutions-reference.s3.amazonaws.com/centralized-logging-with-opensearch/latest/S3AccessLog.template)  |

1. Log in to the AWS Management Console and select the preceding button to launch the AWS CloudFormation template. You can also download the template as a starting point for your own implementation.

1. To launch the stack in a different AWS Region, use the Region selector in the console navigation bar.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following parameters.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/amazon-s3-logs.html)

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Check the box acknowledging that the template creates AWS Identity and Access Management (IAM) resources.

1. Choose **Submit** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 10 minutes.

### View dashboard
<a name="view-dashboard-2"></a>

The dashboard includes the following visualizations.

| Visualization Name | Source Field | Description |
| --- | --- | --- |
| Total Requests | \* log event | A visualization showing the total number of requests made to the Amazon S3 bucket, including all types of operations (for example, GET, PUT, DELETE). |
| Unique Visitors | \* log event | This visualization displays the count of unique visitors accessing the Amazon S3 bucket, identified by their IP addresses. |
| Access History | \* log event | Provides a chronological log of all access events made to the Amazon S3 bucket, including details about the operations and their outcomes. |
| Request By Operation | \* operation | This visualization categorizes and shows the distribution of requests based on different operations (for example, GET, PUT, DELETE). |
| Status Code | \* http\_status | Displays the count of requests made to the Amazon S3 bucket, grouped by HTTP status codes returned by the server (for example, 200, 404, 403). |
| Status Code History | \* http\_status | Shows the historical trend of HTTP status codes returned by the Amazon S3 server over a specific period of time. |
| Status Code Pie | \* http\_status | Represents the distribution of requests based on different HTTP status codes using a pie chart. |
| Average Time | \* total\_time | This visualization calculates and presents the average time taken for various operations in the Amazon S3 bucket (for example, average time for GET, PUT requests). |
| Average Turn Around Time | \* turn\_around\_time | Shows the average turnaround time for different operations, which is the time between receiving a request and sending the response back to the client. |
| Data Transfer | \* bytes\_sent \* object\_size \* operation | Provides insights into data transfer activities, including the total bytes transferred, object sizes, and different operations involved. |
| Top Client IPs | \* remote\_ip | Displays the top client IP addresses with the highest number of requests made to the Amazon S3 bucket. |
| Top Request Keys | \* key \* object\_size | Shows the top requested keys in the Amazon S3 bucket along with the corresponding object sizes. |
| Delete Events | \* operation \* key \* version\_id \* object\_size \* remote\_ip \* http\_status \* error\_code | Focuses on delete events, including the operation, key, version ID, object size, client IP, HTTP status, and error code associated with the delete requests. |
| Access Failures | \* operation \* key \* version\_id \* object\_size \* remote\_ip \* http\_status \* error\_code | Highlights access failures, showing the details of the failed requests, including operation, key, version ID, object size, client IP, HTTP status, and error code. |

You can access the built-in dashboard in Amazon OpenSearch Service to view log data. For more information, see the [Access Dashboard](getting-started.md#step-4-access-the-dashboard).

 **Amazon S3 logs sample dashboard.**

![image34](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image34.png)
