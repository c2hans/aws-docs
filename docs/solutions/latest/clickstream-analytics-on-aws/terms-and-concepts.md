---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/terms-and-concepts.html
---

# Terms and concepts
<a name="terms-and-concepts"></a>

This section describes key concepts and defines terminology specific to this guidance:

 **Project**

A project in this solution is the top-level entity, like a container, that groups your apps and data pipeline for collecting and processing clickstream data. One project contains one data pipeline, and can have one or more apps registered to it.

 **Data pipeline**

A data pipeline is deployed into one AWS region, which means all the underlining resources are created in one AWS region. A data pipeline in this solution contains four modules:
+ **Ingestion server**: a web service that provides an endpoint to collect data through HTTP requests, and sink the data in streaming services or S3.
+ **Data processing**: a module that transforms raw data to the solution schema and enriches data with additional dimensions.
+ **Data modeling**: a module that aggregates data to calculate metrics for business analytics.
+ **Reporting**: a module that creates metrics and out-of-the-box visualizations in QuickSight.

 **App**

An app in this guidance can represent an application in your business, which might be built on one or multiple platforms (for example, Android, iOS, and Web).

 **Analytics Studio**

Analytics Studio is a web console for business or data analysts to view dashboards, query, and manage clickstream data.

Below is a diagram to help you better understand those concepts and their relationship with each other in the AWS context.

![](https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/concepts.png)

For a general reference of AWS terms, see the [AWS glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html) in the *AWS General Reference*.
