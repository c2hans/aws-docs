---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/cost.html
---

# Cost
<a name="cost"></a>

You’re responsible for the cost of the AWS services used while running the Security Automations for AWS WAF solution. The total cost for running this solution depends on the protection activated and the amount of data ingested, stored, and processed.

We recommend creating a [budget](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. For full details, refer to the pricing webpage for each AWS service you used in this solution.

The following tables are example cost breakdowns for running this solution in the US East (N. Virginia) Region (excludes AWS Free Tier). Prices are subject to change.

 **Example 1: Activate Reputation List Protection, Bad Bot Protection, AWS Lambda Log Parser for HTTP Flood Protection, and Scanner & Probe Protection**

| AWS service | Dimensions/Month | Cost [USD] |
| --- | --- | --- |
| Amazon Data Firehose | 100 GB | \~$2.90 |
| Amazon S3 | 100 GB | \~$2.30 |
| AWS Lambda | 128 MB: 3 functions, 1M invocations, and average 500 millisecond duration per Lambda run<br />512 MB: 2 functions, 1M invocations, and average 500 millisecond duration per Lambda run | \~$5.40 |
| AWS WAF web ACL | 1 | $5.00 |
| AWS WAF rule | 4 | $4.00 |
| AWS WAF request | 1M | $0.60 |
|  **Total**  |  |  **\~$20.60 per month**  |

 **Example 2: Activate Reputation List Protection, Bad Bot Protection, Amazon Athena Log Parser for HTTP Flood Protection, and Scanner & Probe Protection**

| AWS service | Dimensions/Month | Cost [USD] |
| --- | --- | --- |
| Amazon Data Firehose | 100 GB | \~$2.90 |
| Amazon S3 | 100 GB | \~$2.30 |
| AWS Lambda | 128 MB: 3 functions, 1M invocations ,and average 500 millisecond duration per Lambda run<br />512 MB: 2 functions, 7560 invocations, and average 500 millisecond duration per Lambda run | \~$1.26 |
| Amazon Athena | 1.2M CloudFront objects hits or 1.2M ALB requests per day that generates a \~500 byte log record per hit or request | \~$4.32 |
| AWS WAF web ACL | 1 | $5.00 |
| AWS WAF rule | 4 | $4.00 |
| AWS WAF request | 1M | $0.60 |
|  **Total**  |  |  **\~$20.38** **per month**  |

 **Example 3: Activate IP Retention for Allowed and Denied IP Sets**

| AWS service | Dimensions/Month | Cost [USD] |
| --- | --- | --- |
| Amazon DynamoDB | 1K writes and 1 MB data storage | \~$0.00 |
| AWS Lambda | 128 MB: 1 function, 2K invocations, and average 500 millisecond duration per Lambda run<br />512 MB: 1 function, 2K invocations, and average 500 millisecond duration per Lambda run | \~$0.01 |
| Amazon CloudWatch | 2K events | \~$0.00 |
| AWS WAF Web ACL | 1 | $5.00 |
| AWS WAF Rule | 2 | $2.00 |
| WAS WAF request | 1M | $0.60 |
|  **Total**  |  |  **\~$7.61** **per month**  |

## Cost estimate of CloudWatch logs
<a name="cost-estimate-of-cloudwatch-logs"></a>

Some AWS services used in this solution, such as Lambda, generate CloudWatch logs. These logs incur [charges](https://aws.amazon.com/cloudwatch/pricing/). We recommend deleting or archiving logs to reduce the cost. For log archive detail, refer to [Exporting log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html) in the *Amazon CloudWatch Logs User Guide*.

If you choose to use the Athena log parser on installation, this solution schedules a query to run against the AWS WAF or application access logs in your Amazon S3 bucket(s) as configured. You’re charged based on the amount of data scanned by each query. The solution applies partitioning to logs and queries to minimize costs. By default, the solution moves application access logs from their original Amazon S3 location to a partitioned folder structure. You can also retain original, but you will be charged for duplicated log storage. This solution uses [workgroups](https://docs.aws.amazon.com/athena/latest/ug/manage-queries-control-costs-with-workgroups.html) to segment workloads, and you can configure both to manage query access and costs. Refer to [Cost estimate of Athena](#cost-estimate-of-athena) for a sample cost estimate calculation. For more information, refer to [Amazon Athena Pricing](https://aws.amazon.com/athena/pricing/).

## Cost estimate of Athena
<a name="cost-estimate-of-athena"></a>

If you use the Athena log parser option while running the **HTTP Flood Protection**, **Scanner & Probe Protection** or **Bad Bot Protection** rules, you will be charged for Athena usage. By default, each Athena query runs every five minutes and scans the past four hours of data. The solution applies partitioning to logs and Athena queries to minimize costs. You can configure the number of hours of data that a query scans by changing the value for the **WAF Block Period** template parameter. However, increasing the amount of data scanned will likely increase the Athena cost.

**Tip**
The following is an example CloudFront logs cost calculation:
On average, each CloudFront hit might generate around 500 bytes of data.
If there are 1.2M CloudFront objects hit per day, then there will be 200K (1.2M/6) hits per four hours, assuming that data is ingested at a consistent rate. Consider your actual traffic patterns when calculate your cost.
 `[500 bytes of data] * [200K hits per four hours] = [an average 100 MB (0.0001TB) data scanned per query]`
Athena charges $5.00 per TB of data scanned.
 `[0.0001 TB] * [$5] = [$0.0005 per query scan]`
The Athena query runs every five minutes, which is 12 runs per hour.
 `[12 runs] * [24 hours] = [288 runs per day]`
 `[$0.0005 per query scan] * [288 runs per day] * [30 days] = [$4.32 per month]`
Actual costs vary depending on your application’s traffic patterns. For more information, refer to [Amazon Athena Pricing](https://aws.amazon.com/athena/pricing/).
