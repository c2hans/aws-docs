---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/databrew.html
---

# AWS Glue DataBrew
<a name="databrew"></a>

AWS Glue DataBrew is a fully managed visual data preparation service for cleaning, normalizing, and transforming data. It differs from AWS Glue ETL in that you don't have write code to work with it. DataBrew provides more than 250 built-in transformations, with a visual point-and-click interface for creating and managing data transformation jobs.

DataBrew is available in a separate console view from AWS Glue. It is natively integrated with several AWS services and supports many different file formats. For more information, see [Product and service integrations](https://docs.aws.amazon.com/databrew/latest/dg/databrew-integrations.html).

DataBrew is based on the following six core concepts:
+ **Project** – The entire data preparation workspace in DataBrew
+ **Dataset** – A collection of structured or semi-structured data
+ **Recipe** – A set of data transformation steps; each step can contain many actions
+ **Job** – A set of instructions to run a recipe or a data profile job
+ **Data lineage** – The tracking of data in a visual interface to identify its origin
+ **Data profile** – A summary view of the shape of your data

[AWS Glue DataBrew is integrated with AWS Glue Studio](https://aws.amazon.com/blogs/big-data/use-aws-glue-databrew-recipes-in-your-aws-glue-studio-visual-etl-jobs/), so you can orchestrate DataBrew recipes within your AWS Glue ETL jobs and workflows. DataBrew recipes can also take advantage of AWS Glue features such as job bookmarks, automatic retries, and automatic scaling. To get started with DataBrew, use the [AWS Glue DataBrew sample project](https://aws.amazon.com/blogs/big-data/use-aws-glue-databrew-recipes-in-your-aws-glue-studio-visual-etl-jobs/) tutorial.
