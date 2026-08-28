---
source_url: https://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/derive-insights-with-inside-out-data-movement.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Derive insights with inside-out data movement
<a name="derive-insights-with-inside-out-data-movement"></a>

 To get the most from your data lakes and these purpose-built stores, you need to move data between these systems easily. For example, clickstream data from web applications can be collected directly in a data lake and a portion of that data can be moved out to a data warehouse for daily reporting. We think of this concept as *inside-out data movement*.

![Diagram showing inside-out data movement](http://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/images/inside-out-data-movement.png)

## Derive real time event-based visualization insights from your Lake house with Amazon Redshift and Amazon Quick
<a name="derive-real-time-event-based-visualization-insights-from-your-lake-house-with-amazon-redshift-and-amazon-quicksight"></a>

 Customers often want to analyze their data visually as soon as data is ingested into their data lake, to make decisions with speed and agility for downstream business value.

 The following diagram illustrates the Modern Data inside-out data movement with Amazon Redshift and [Amazon Quick](https://aws.amazon.com/quicksight/) to perform data visualization insights.

![Reference architecture diagram showing deriving real time event-based visualization insights with Amazon Redshift and Amazon Quick.](http://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/images/data-visualization.png)

 The steps that data follows through the architecture are as follows:

1.  **Data ingestion** — A new data file is uploaded in Amazon S3. An S3 event triggers an [AWS Lambda](https://aws.amazon.com/lambda/) function.

1.  **Event trigger** —Lambda triggers an AWS Glue workflow to start processing the file. Lambda updates [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) with metadata changes.

1.  **Data processing** — Load transformed data into target data stores like S3 and Amazon Redshift. AWS Glue jobs push logs and notifications to Amazon CloudWatch. CloudWatch triggers a Lambda function upon AWS Glue job completion.

1.  **Data analytics** — Analyze the data in Amazon Redshift and the data lake (S3). Lambda calls the QuickSight ingestion API to refresh the [SPICE](https://docs.aws.amazon.com/quicksight/latest/user/spice.html) dataset.

1.  **Data visualizations** — New data is reflected in QuickSight visuals. QuickSight can create a data set by combining data in Amazon Redshift and Athena. Output is stored in SPICE for fast analytics.

## Derive persona-centric insights from your Modern Data with AWS Glue DataBrew, Amazon Athena, Amazon Redshift, and Amazon Quick
<a name="derive-persona-centric-insights-from-your-modern-data-with-aws-glue-databrew-amazon-athena-amazon-redshift-and-amazon-quicksight"></a>

 Many organizations want to get insights from exponentially growing data volumes to help them make decisions with speed and agility. They need to embrace data gravity by using both a central data lake, and a ring of purpose-built data services and data warehouses based on persona or job function.

 The following diagram illustrates the Modern Data inside-out data movement with AWS [Glue DataBrew](https://aws.amazon.com/glue/features/databrew/), Amazon Athena, Amazon Redshift, and Amazon Quick to perform persona-centric data analytics.

![Diagram showing how to derive persona-centric insights from your Modern Data with AWS Glue DataBrew, Amazon Athena, Amazon Redshift, and Amazon Quick](http://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/images/persona-centric-insights.png)

 The steps that data follows through the architecture are as follows:

1.  **Data ingestion** — Data is ingested into Amazon S3 from different sources.

1.  **Ad-hoc data processing** — Data curators and data scientists use Data Brew to validate, clean, and enrich the data. Amazon Athena is also used to run ad-hoc queries to analyze the data in the lake. The transformation is shared with data engineers to set up batch processing.

1.  **Batch data processing** — Data engineers or developers set up batch jobs in AWS Glue and AWS Glue DataBrew. Jobs can be event-triggered, or can be scheduled to run periodically.

1.  **Data analytics** — Data and business analysts can now analyze prepared datasets in Amazon Redshift, or in S3 using Athena.

1.  **Data visualizations** — Business analysts can create visuals in QuickSight. Data curators can enrich data from multiple sources. Administrators can enforce security and data governance. Developers can embed the QuickSight dashboard in applications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
