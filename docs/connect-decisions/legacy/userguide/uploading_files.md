---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/uploading_files.html
---

# Uploading files for the first time
<a name="uploading_files"></a>

You can use the AWS Supply Chain Auto-association feature to upload your raw data and automatically associate your raw data with AWS Supply Chain data model. You can also view the *required* columns and tables for each AWS Supply Chain module within the AWS Supply Chain web application.

For a brief demonstration of how auto-association works, watch the following video:

**Note**
You can only upload CSV files to Amazon S3 when you are using Auto-association.

After the source columns from your dataset are associated with the destination columns, AWS Supply Chain will automatically generate the SQL recipe.

**Note**
AWS Supply Chain uses Amazon Bedrock for Auto-association, which it's not supported in all the &AWS Regions that AWS Supply Chain is available in. Hence, AWS Supply Chain will call Amazon Bedrock endpoint from the closest available region, Europe (Ireland) Region – Europe (Frankfurt) and Asia Pacific (Sydney) Region – US West (Oregon).

**Note**
Auto-association using the Large Language Models (LLM) is only supported when data is ingested through Amazon S3.

1. On the AWS Supply Chain dashboard, on the left navigation pane, choose **Data Lake** and then choose the **Data Ingestion** tab.

   The **Data Ingestion** page appears.

1. Choose **Add New Source**.

   The **Select your data source** page appears.

1. On the **Select your data source** page, choose **Upload files**.

1. Choose **Continue**.
![Uploading your source files](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/data_lake.png)

1. On the **Which capabilities do you want to run** page, choose the AWS Supply Chain modules that you want to use. You can choose more than one module.

1. Under **Upload your source files** section, add a suffix to the **Source system name**. For example, oracle\_test.

1. To upload your source dataset, choose **files** or drag and drop files.

   The source tables with the name and status are displayed.

1. Choose **Upload to S3**. The *upload status* will change to display the status.

1. Under **Review data requirements**, review all the required data entities and columns for the selected AWS Supply Chain feature. All of the required primary and foreign keys are displayed.

1. Choose **Continue**.

1. Under **Manage your source tables**, the following source tables and the columns listed will be auto associated and imported into data lake.

   Choose **Delete table** to delete any of the source tables before importing into data lake.
![Managing your source files](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/data_lake1.png)

1. Choose **Accept all and Continue**.

   A message on auto-associating your tables to AWS Supply Chain data lake is displayed.
![Managing destination flows](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/data_lake3.png)

1. Under **Manage Destination Flows**, you can review each auto-associated table.

   By default, **Auto-Association** is enabled and the source columns are auto-associated with the destination columns. To update the auto-associated columns, you can update the SQL recipe to create your custom recipe.

1. Under **Source Columns**, all of the unassociated source columns are listed. Drag and drop the unassociated columns to the **Destination Columns** on the right.

1. Follow the preceding step for each auto-associated table.

1. Choose **Submit**.

1. Choose **Exit and Review Destination Flows**.
