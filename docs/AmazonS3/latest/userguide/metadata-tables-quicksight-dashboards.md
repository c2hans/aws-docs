---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/metadata-tables-quicksight-dashboards.html
---

# Visualizing metadata table data with Amazon Quick
<a name="metadata-tables-quicksight-dashboards"></a>

With Amazon Quick, you can create interactive dashboards to analyze and visualize SQL query results about your S3 managed metadata tables. Quick dashboards can help you monitor statistics, track changes, and get operational insights about your metadata tables.

A dashboard about your journal table might show you:
+ What's the percentage of object uploads compared to deletions?
+ Which objects were deleted by S3 Lifecycle in the past 24 hours?
+ Which IP addresses did the most recent `PUT` requests come from?

A dashboard about your inventory table might show you:
+ How many objects are in different storage classes?
+ What percentage of your storage data is small objects compared to large objects?
+ What types of objects are in my bucket?

After you [integrate your S3 table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html) with AWS analytics services, you can create datasets from your metadata tables and work with them in Amazon Quick using SPICE or direct SQL queries from your query engine. Quick supports Amazon Athena and Amazon Redshift as data sources.

For more information, see [Visualizing table data with Amazon Quick](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-quicksight.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
