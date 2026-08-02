---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.Engines.html
---

# Amazon Aurora DB engine, Region, and instance class support for Performance Insights
<a name="USER_PerfInsights.Overview.Engines"></a>

**Important**
 AWS has announced the end-of-life date for Performance Insights: July 31, 2026. After this date, Amazon RDS will no longer support the Performance Insights console experience. The Performance Insights console will redirect to CloudWatch Database Insights. Flexible retention periods (1–24 months) and their associated pricing are preserved in Standard mode of Database Insights at the same cost as Performance Insights today. The Performance Insights API will continue to exist with no changes. Costs for the Performance Insights API will appear in your AWS bill with the cost of CloudWatch Database Insights.
 We recommend that you review your DB clusters using Performance Insights and choose the Database Insights mode that best fits your needs before July 31, 2026. For core monitoring with flexible retention, Standard mode of Database Insights preserves your existing experience and pricing. For advanced capabilities including fleet-level monitoring, lock diagnostics, and execution plan capture, see [Turning on the Advanced mode of Database Insights for Amazon Aurora](USER_DatabaseInsights.TurningOnAdvanced.md).
 If you take no action, DB clusters using Performance Insights will default to using the Standard mode of Database Insights with your existing retention period configured. Your CloudFormation templates, Terraform configurations, and deployment scripts will continue to work exactly as they do today – all Performance Insights API parameters, including retention period settings, are fully preserved. After July 31, 2026, only the Advanced mode of Database Insights will support execution plans and on-demand analysis.
 With CloudWatch Database Insights, you can monitor database load for your fleet of databases and analyze and troubleshoot performance at scale. For more information about Database Insights, see [Monitoring Amazon Aurora databases with CloudWatch Database Insights](USER_DatabaseInsights.md) or [Register for upcoming workshops](https://aws-experience.com/amer/smb/events/series/Cloud-Operations-Enablement) to learn more. For current pricing information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

The following table provides Amazon Aurora DB engines that support Performance Insights.

| Amazon Aurora DB engine | Supported engine versions and Regions | Instance class restrictions |
| --- | --- | --- |
| Amazon Aurora MySQL-Compatible Edition | For more information on version and Region availability of Performance Insights with Aurora MySQL, see [Performance Insights with Aurora MySQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.amy). | Performance Insights has the following engine class restrictions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.Engines.html) |
| Amazon Aurora PostgreSQL-Compatible Edition | For more information on version and Region availability of Performance Insights with Aurora PostgreSQL, see [Performance Insights with Aurora PostgreSQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.apg). | N/A |

## Amazon Aurora DB engine, Region, and instance class support for Performance Insights features
<a name="USER_PerfInsights.Overview.PIfeatureEngnRegSupport"></a>

The following table provides Amazon Aurora DB engines that support Performance Insights features.

| Feature | [Pricing tier](https://aws.amazon.com/rds/performance-insights/pricing/) |  [Supported regions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.RegionsAndAvailabilityZones.html#Concepts.RegionsAndAvailabilityZones.Regions)  |  Supported DB engines  |  [Supported instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html#Concepts.DBInstanceClass.Types)  |
| --- | --- | --- | --- | --- |
| [SQL statistics for Performance Insights](sql-statistics.md) | All | All | All | All |
| [Analyzing database performance for a period of time](USER_PerfInsights.UsingDashboard.AnalyzePerformanceTimePeriod.md) | Paid tier only | All | All | All except db.serverless (Aurora serverless) |
| [Viewing Performance Insights proactive recommendations](USER_PerfInsights.InsightsRecommendationViewDetails.md) | Paid tier only | [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.Engines.html)  | All | All except db.serverless (Aurora serverless) |
