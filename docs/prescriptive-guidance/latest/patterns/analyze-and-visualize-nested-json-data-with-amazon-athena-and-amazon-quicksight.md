---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/analyze-and-visualize-nested-json-data-with-amazon-athena-and-amazon-quicksight.html
---

# Analyze and visualize nested JSON data with Amazon Athena and Amazon Quick Sight
<a name="analyze-and-visualize-nested-json-data-with-amazon-athena-and-amazon-quicksight"></a>

*Anoop Singh, Amazon Web Services*

## Summary
<a name="analyze-and-visualize-nested-json-data-with-amazon-athena-and-amazon-quicksight-summary"></a>

This pattern explains how to translate a nested, JSON-formatted data structure into a tabular view by using Amazon Athena, and then visualize the data in Amazon Quick Sight.

You can use JSON-formatted data for API-powered data feeds from operational systems to create data products. This data can also help you understand your customers and their interactions with your products better, so you can tailor user experiences and predict outcomes.

## Prerequisites and limitations
<a name="analyze-and-visualize-nested-json-data-with-amazon-athena-and-amazon-quicksight-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A JSON file that represents a nested data structure (this pattern provides a sample file)

**Limitations:**
+ JSON features integrate well with existing SQL-oriented functions in Athena. However, they aren’t ANSI SQL compatible, and the JSON file is expected to carry each record on a separate line. You might need to use the `ignore.malformed.json` property in Athena to indicate if malformed JSON records should be turned into null characters or generate errors. For more information, see [Best practices for reading JSON data](https://docs.aws.amazon.com/athena/latest/ug/parsing-JSON.html) in the Athena documentation.
+ This pattern considers only simple and small amounts of JSON-formatted data. If you want to use these concepts at scale, consider applying data partitioning and consolidate your data into larger files.

## Architecture
<a name="analyze-and-visualize-nested-json-data-with-amazon-athena-and-amazon-quicksight-architecture"></a>

The following diagram shows the architecture and workflow for this pattern. The nested data structures are stored in Amazon Simple Storage Service (Amazon S3) in JSON format. In Athena, the JSON data is mapped to an Athena data structure. You then create a view to analyze the data, and visualize the data structure in Quick Sight.

![Analyzing and visualizing nested JSON data on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e9ad39a1-e0a4-4429-bdc0-594b68707761/images/474e8747-626f-468c-9c27-c007af79bf2d.png)

## Tools
<a name="analyze-and-visualize-nested-json-data-with-amazon-athena-and-amazon-quicksight-tools"></a>

**AWS services**
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data. This pattern uses Amazon S3 to store the JSON file.
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon S3 by using standard SQL. This pattern uses Athena to query and transform the JSON data. With a few actions in the AWS Management Console, you can point Athena at your data in Amazon S3 and use standard SQL to run one-time queries. Athena is serverless, so there is no infrastructure to set up or manage, and you pay only for the queries that you run. Athena scales automatically and runs queries in parallel, so results are fast, even with large datasets and complex queries.
+ [Amazon Quick Sight](https://docs.aws.amazon.com/quicksuite/latest/userguide/quick-bi.html) is a cloud-scale business intelligence (BI) service that helps you visualize, analyze, and report your data on a single dashboard. Quick Sight lets you easily create and publish interactive dashboards that include machine learning (ML) insights. You can access these dashboards from any device, and embed them into your applications, portals, and websites.

**Example code **

The following JSON file provides a nested data structure that you can use in this pattern.

```
{
  "symbol": "AAPL",
  "financials": [
    {
      "reportDate": "2017-03-31",
      "grossProfit": 20591000000,
      "costOfRevenue": 32305000000,
      "operatingRevenue": 52896000000,
      "totalRevenue": 52896000000,
      "operatingIncome": 14097000000,
      "netIncome": 11029000000,
      "researchAndDevelopment": 2776000000,
      "operatingExpense": 6494000000,
      "currentAssets": 101990000000,
      "totalAssets": 334532000000,
      "totalLiabilities": 200450000000,
      "currentCash": 15157000000,
      "currentDebt": 13991000000,
      "totalCash": 67101000000,
      "totalDebt": 98522000000,
      "shareholderEquity": 134082000000,
      "cashChange": -1214000000,
      "cashFlow": 12523000000,
      "operatingGainsLosses": null
    }
  ]
}
```

## Epics
<a name="analyze-and-visualize-nested-json-data-with-amazon-athena-and-amazon-quicksight-epics"></a>

### Set up an S3 bucket
<a name="set-up-an-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket. | To create a bucket to store the JSON file, sign in to the AWS Management Console, open the [Amazon S3 console](https://console.aws.amazon.com/s3/), and then choose **Create bucket**. For more information, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon S3 documentation.  | Systems administrator |
| Add the nested JSON data. | Upload your JSON file to the S3 bucket. For a sample JSON file, see the previous section. For instructions, see [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the Amazon S3 documentation. | Systems administrator |

### Analyze data in Athena
<a name="analyze-data-in-ate"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a table for mapping the JSON data. | 1. Open the [Athena console](https://console.aws.amazon.com/athena/).<br />2. Create a database by following the instructions in the [Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/creating-databases.html).<br />3. From the **Database** menu, choose the database that you created.<br />4. In the query editor, enter a `CREATE TABLE` statement such as the following:<pre>CREATE EXTERNAL TABLE financials_json (<br />    symbol string,<br />    financials array<<br />        struct<reportdate: string,<br />             grossprofit: bigint,<br />             totalrevenue: bigint,<br />             totalcash: bigint,<br />             totaldebt: bigint, <br />             researchanddevelopment: bigint>><br />)<br />ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe' LOCATION 's3://s3bucket-for-athena/'</pre><br />where `LOCATION` specifies the location of the S3 bucket that contains the JSON file.<br />5. Choose **Run** to create the table.For more information about creating tables, see the [Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/creating-tables.html). | Developer |
| Create a view for data analysis. | 1. Open the [Athena console](https://console.aws.amazon.com/athena/).<br />2. Create a database by following the instructions in the [Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/creating-databases.html).<br />3. From the **Database** menu, choose the database that you created.<br />4. In the query editor, enter a `CREATE VIEW` statement such as the following:<pre>CREATE OR REPLACE VIEW financial_json_view AS <br />  SELECT <br />  symbol, <br />  financials[1].reportdate one_report_date, -- indexes start with 1 <br />  financials[1].totalrevenue one_total_revenue, <br />  financials[1].reportdate another_report_date,<br />  financials[1].totalrevenue another_total_revenue <br />FROM financials_json where symbol='AAPL' <br />ORDER BY <br />  1</pre><br />5. Choose **Run** to create the view.For more information about creating views, see the [Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/create-view.html). | Developer |
| Analyze and validate the data. | 1. Open the [Athena console](https://console.aws.amazon.com/athena/).<br />2. In the query editor, run queries by using the view that you created in the previous step.<br />3. Validate the data against the JSON file, to confirm that column names and data types are mapped correctly. | Developer |

### Visualize data in Quick Sight
<a name="visualize-data-in-qsight"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Athena as a data source in Quick Sight. | 1. Open the [Quick console](https://quicksight.aws.amazon.com/).<br />2. Choose **Datasets**, **New dataset**.<br />3. Choose Athena as a data source.<br />4. Choose the database that includes the view that you created.<br />5. Choose the view that you want to create a dataset for.<br />6. On the **Finish data set creation** page, choose **Directly query your data**.<br />7. Choose **Visualize**. | Systems administrator |
| Visualize data in Quick Sight. | 1. After you visualize the dataset, choose the visuals from the left pane, and choose fields for the dataset. For more information, see the [tutorial](https://docs.aws.amazon.com/quicksight/latest/user/example-create-an-analysis.html) in the Quick documentation.<br />2. Save the changes to the analysis.<br />3. Choose **Publish dashboard** to publish the visuals that you created. | Data analyst |

## Related resources
<a name="analyze-and-visualize-nested-json-data-with-amazon-athena-and-amazon-quicksight-resources"></a>
+ [Amazon Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html)
+ [Amazon Quick Sight tutorials](https://docs.aws.amazon.com/quicksuite/latest/userguide/example-analysis.html)
+ [Working with nested JSON ](https://aws.amazon.com/blogs/big-data/create-tables-in-amazon-athena-from-nested-json-and-mappings-using-jsonserde/)(blog post)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
