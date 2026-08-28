---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/how-the-solution-works.html
---

# Guidance components
<a name="how-the-solution-works"></a>

 The Clickstream Analytics on AWS guidance has four components: a web console, Analytics Studio, SDKs, and the data pipeline.

## Web console
<a name="web-console"></a>

 This guidance provides a simple web console which allows you to create and manage projects with their data pipeline to ingest, process, analyze and visualize the Clickstream data.

## Analytics Studio
<a name="analytics-studio-1"></a>

 Analytics Studio is a unified web interface for business analysts or data analysts to view and create dashboards, query and explore clickstream data, and manage metadata. It supports the following features:
+ provide a pre-canned user lifecycle dashboard
+ provide an explorative analytics model to query and analyze clickstream data
+ support creating custom analysis and visualization in a drag-and-drop manner
+ auto-generate metadata for clickstream data, and support metadata management

## SDKs
<a name="sdks"></a>

 This guidance provides native SDKs to help you easily collect and report in-app events from your applications to your Clickstream pipelines.
+  [Android SDK](android-sdk.md#introduction)
+  [Swift SDK](swift-sdk.md#introduction-1)
+  [Web SDK](web-sdk.md#introduction-2)
+  [Flutter SDK](flutter-sdk.md#introduction-3)

## Data pipeline
<a name="data-pipeline-1"></a>

 This guidance uses the web console to manage the project and its data pipeline. The data pipeline consists of four modules.

### Ingestion module
<a name="ingestion-module-1"></a>

 The ingestion module serves as web server for ingesting the Clickstream data. It supports the following features:
+  Specify the auto scaling group capability
+  Specify warm pool size to scale out faster and save costs
+  Support authenticate with OIDC
+  Support SSL
+  Support enabling AWS Global Accelerator for ELB
+  Support different sink buffer, S3, KDS and MSK

### Data processing module
<a name="data-processing-module-1"></a>

 The data processing module transforms and enriches the ingested data to guidance's data model by the Apache Spark application running in EMR serverless. It supports the following features:
+  Specify the batch interval of data processing
+  Specify the data refreshness age
+  Provider out-of-the-box enrichment plug-ins
  +  UA enrichment to parse OS, device, browser information from User Agent string of the HTTP request header
  +  IP enrichment to mapping device location information (for example, city, country, region) based on the request source IP
+  Support third-party transformer plug-ins
+  Support third-party enrichment plug-ins

### Data modeling module
<a name="data-modeling-module-1"></a>

 The data modeling module loads the processed data into lake house. It supports the following features:
+  Support both provisioned Redshift and Redshift Serverless as data warehouse
  +  Users can specify the time range for storing data in Redshift
  +  Users can specify the interval to update user dimension table
+  Support use Athena to query the data in data lake

### Reporting module
<a name="reporting-module-1"></a>

 The reporting module creates a secure connection to the data warehouse and provisions the out-of-the-box dashboards in business intelligence Amazon QuickSight.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
