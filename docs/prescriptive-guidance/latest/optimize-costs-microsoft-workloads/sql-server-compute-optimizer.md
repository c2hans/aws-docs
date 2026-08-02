---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-compute-optimizer.html
---

# Optimize SQL Server licensing by using Compute Optimizer
<a name="sql-server-compute-optimizer"></a>

Guidance on how to optimize licenses for SQL Server by using AWS Compute Optimizer.

## Overview
<a name="sql-server-compute-optimizer-overview"></a>

[AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) can recommend licensing optimization opportunities for Microsoft SQL Server workloads on Amazon Elastic Compute Cloud (Amazon EC2). Compute Optimizer can provide automated recommendations to reduce licensing costs. The recommendations from Compute Optimizer are listed next to each of your EC2 instances with Microsoft SQL Server licenses. The information that's provided includes recommended saving opportunities, EC2 instance On-Demand prices, and hourly bring your own license (BYOL) prices. This information can help you decide if you should downgrade your license edition.

Compute Optimizer automatically discovers your SQL Server instances on Amazon EC2 by inferred workload type. To view the licensing recommendations, you can select the SQL Server instances in Compute Optimizer and then authenticate with [Amazon CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html) by using your read-only database credentials. Compute Optimizer analyzes if you are using any SQL Server Enterprise edition features. If no Enterprise edition features are being used, Compute Optimizer recommends that you downgrade to Standard edition to reduce licensing costs.

You can also use Compute Optimizer to make sizing recommendations for your Amazon EC2 instances that run SQL Server workloads. For more information, see [Optimize SQL Server sizing by using Compute Optimizer](sql-server-sizing-compute-optimizer.md) in this guide.

## Cost optimization recommendations
<a name="sql-server-compute-optimizer-recommendations"></a>

The license recommendations in Compute Optimizer can help you evaluate the features you are using in Microsoft SQL Server and choose the most cost-effective edition for your workloads. SQL Server Enterprise edition is significantly more expensive than Standard edition. For more information, see [Compare SQL Server editions](sql-server-editions.md) in this guide and see [SQL Server 2022 pricing](https://www.microsoft.com/en-us/sql-server/sql-server-2022-pricing) on the Microsoft website. Investing the time to configure Compute Optimizer to evaluate your SQL Server fleet and provide recommendations can dramatically reduce your licensing costs.

The **License details** page provides the following information:
+ Use the table to compare your current license settings (such as edition, model, and number of instance cores) with Compute Optimizer recommendations.
+ Use the utilization graphs to review the number of Enterprise edition features that were used during the analysis period.

For more information, see [Viewing details of a commercial software license recommendation](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-license-recommendations.html#license-viewing-details) in the Compute Optimizer documentation.

## Configure Compute Optimizer
<a name="sql-server-compute-optimizer-configuration"></a>

Compute Optimizer analyzes commercial software licenses by using the `mssql_enterprise_features_used` metric. For more information about this metric, see [Metrics for commercial software licenses](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#license-metrics-analyzed).

1. Make sure that you have the appropriate permissions to opt in to Compute Optimizer. For more information, see the following:
   + [Policy to opt in to Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#opting-in-access)
   + [Policies to grant access to Compute Optimizer for standalone AWS accounts](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#standalone-account-access)
   + [Policies to grant access to Compute Optimizer for a management account of an organization](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#organization-account-access)

1. Attach the required instance roles and policy for CloudWatch Application Insights. For instructions, see [Policies to enable commercial software license recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#license-access).

1. Enable CloudWatch Application Insights by using your Microsoft SQL Server database credentials. For instructions, see [Set up application for monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-setting-up.html) in the CloudWatch documentation.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-compute-optimizer.html)

1. Use the following SQL query to configure least-privilege access for CloudWatch Application Insights.

   ```
   GRANT VIEW SERVER STATE TO [LOGIN];
   GRANT VIEW ANY DEFINITION TO [LOGIN];
   ```

   This enables a new service, PrometheusSqlExporterSQL.

1. From the target AWS account or organization management account, opt in to Compute Optimizer. For instructions, see [Opting in your account](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html#account-opt-in).
[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-compute-optimizer.html)

1. In the [Compute Optimizer console](https://console.aws.amazon.com/compute-optimizer/), choose **Licenses** in the navigation pane.

1. In the **Findings** column, search for any instances that have the **Insufficient metrics** finding. Compute Optimizer returns this finding if it detects that CloudWatch Application Insights isn't enabled or has insufficient permissions. For more information, see [Finding reasons](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-license-recommendations.html#license-finding-reasons). Do the following to resolve these findings:

   1. Choose the instance.

   1. Add a secret.

   1. Confirm the instance role and policy are attached.

   1. Choose **Enable license recommendations**.

1. In the **Findings** column, search for any instances that have the **Not optimized** finding. Compute Optimizer returns this finding if it detects that your Amazon EC2 infrastructure isn't using any of the Microsoft SQL Server license features that you're paying for. For more information, see [Finding reasons](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-license-recommendations.html#license-finding-reasons). Do the following to resolve these findings:

   1. Choose the instance.

   1. Compare the current license edition with the recommended edition.

   1. Review the current license utilization graph.

   1. If you want to downgrade the license, choose **Implement recommendation**.

   1. Review the requirements and follow the instructions to downgrade the license. If you want to automate the process, see [Downgrade SQL Server Enterprise edition using AWS Systems Manager Document to reduce cost](https://aws.amazon.com/blogs/mt/downgrade-sql-server-enterprise-edition-using-aws-systems-manager-document-to-reduce-cost/) (AWS Blog).

## Additional resources
<a name="sql-server-compute-optimizer-resources"></a>
+ [Reduce Microsoft SQL Server licensing costs with AWS Compute Optimizer](https://aws.amazon.com/blogs/modernizing-with-aws/reduce-microsoft-sql-server-licensing-costs-with-aws-compute-optimizer/) (AWS Blog)
+ [What is AWS Compute Optimizer?](https://docs.aws.amazon.com/compute-optimizer/index.html) (AWS documentation)
+ [Viewing commercial software license recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-license-recommendations.html) (AWS documentation)
+ [Downgrade your Microsoft SQL Server edition](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/downgrade-sql-server-on-ec2.html) (AWS documentation)
+ [Microsoft SQL Server on AWS](https://aws.amazon.com/sql/) (AWS)
+ [Microsoft Licensing on AWS](https://aws.amazon.com/windows/resources/licensing/) (AWS)
+ [Microsoft SQL Server 2019 Pricing](https://www.microsoft.com/en-us/sql-server/sql-server-2019-pricing) (Microsoft)
+ [Microsoft SQL Server 2022 Pricing](https://www.microsoft.com/en-us/sql-server/sql-server-2022-pricing) (Microsoft)
