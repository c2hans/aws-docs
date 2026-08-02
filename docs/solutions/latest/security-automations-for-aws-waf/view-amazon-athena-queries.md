---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/view-amazon-athena-queries.html
---

# View Amazon Athena queries
<a name="view-amazon-athena-queries"></a>

If you selected `Yes - Amazon Athena log parser` for the **Activate HTTP Flood Protection** or **Activate Scanner & Probe Protection** template parameters, this solution creates and runs Athena queries for CloudFront or ALB (`ScannersProbesLogParser`) or AWS WAF logs (`HTTPFloodLogParser`), parses the output, and updates AWS WAF accordingly.

To improve performance and keep costs low, the solution partitions logs based on timestamps in the file names. The solution dynamically generates Athena queries to use partition keys (year, month, day, and hour). By default, queries run every five minutes. You can configure their run schedules by changing the value of the **Athena Query Run Time Schedule (Minute)** template parameter. Each query run scans the last four to five hours of data by default. You can configure the amount of data that a query scans by changing the value of the **WAF Block Period** template parameter. The solution also places queries in separate workgroups to manage query access and costs.

**Note**
Verify that Athena is configured to access the AWS Glue Data Catalog. This solution creates the access logs data catalog in AWS Glue and configures an Athena query to process the data. If Athena isn’t configured correctly, the query doesn’t run. For more information, refer to [Upgrading to the latest AWSAWS Glue Data Catalog step-by-step](https://docs.aws.amazon.com/athena/latest/ug/glue-upgrade.html).

Use the following procedure to view these queries:

## View WAF log queries
<a name="view-waf-log-queries"></a>

1. Sign in to the [Amazon Athena console](https://console.aws.amazon.com/athena/).

1. Choose **Launch query editor**.

1. Select the database for this solution.

1. Select **WAFLogAthenaQueryWorkGroup** from the dropdown list.
**Note**
This workgroup exists only if you selected `Yes - Amazon Athena log parser` for the **Activate HTTP Flood Protection** template parameter.

1. Choose **Switch** to switch the workgroup.

 **Screenshot of Athena query editor showing no queries**

![athena query editor](http://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/images/athena-query-editor.png)

1. Select the **History** tab.

1. Select and open `SELECT` queries from the list.

## View application access log queries
<a name="view-application-access-log-queries"></a>

1. Sign in to the [Amazon Athena console](https://console.aws.amazon.com/athena/).

1. Select the **Workgroup** tab.

1. Select **WAFAppAccessLogAthenaQueryWorkGroup** from the list.
**Note**
This workgroup exists only if you selected `Yes - Amazon Athena log parser` for the **Activate Scanner & Probe Protection** template parameter.

1. Choose **Switch workgroup**.

1. Select the **Recent queries** tab.

1. Select and open `SELECT` queries from the list.

## View adding Athena partition queries
<a name="view-adding-athena-partition-queries"></a>

1. Sign in to the [Amazon Athena console](https://console.aws.amazon.com/athena/).

1. Select the **Workgroup** tab.

1. Select **WAFAddPartitionAthenaQueryWorkGroup** from the list.
**Note**
This workgroup exists only if you selected `Yes - Amazon Athena log parser` for the **Activate HTTP Flood Protection** and/or **Activate Scanner & Probe Protection** template parameter.

1. Select **Switch workgroup**.

1. Select the **History** tab.

1. Select and open `ALTER TABLE` queries from the list. These queries run every hour to add a new hourly partition to the Athena table.
