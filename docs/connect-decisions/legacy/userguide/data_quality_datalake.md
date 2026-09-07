---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/data_quality_datalake.html
---

# Data quality
<a name="data_quality_datalake"></a>

Any identified data quality errors are displayed on the web application under Module errors. You can view the dataset that has errors and the impacted AWS Supply Chain module. Additionally, you can download the data quality report from your Amazon S3 bucket. The report provides detailed information on the dataset errors in the ingested data.

## Viewing data quality reports
<a name="data_qual"></a>

To view the AWS Supply Chain module errors, complete the following steps:

**Note**
For information on required and optional data entities for each AWS Supply Chain module, see the Demand Planning, Insights, and Work Order Insights sections under [Data entities and columns used in AWS Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model.html).

1. On the AWS Supply Chain dashboard, on the left navigation pane, choose **Data Lake** and then choose the **Data Quality** tab.

1. Choose the **Module Errors** tab. You can view the data ingestion errors for the AWS Supply Chain modules.
**Note**
You can also view the dataset errors and the affected modules after the first ingestion is complete and the destination flows are successful. If the destination flows are unsuccessful, you can view the data quality errors under the **Detail** column of the **Destination Flows** tab.

   You can filter the errors using the following filters in the **Module** dropdown box:
   + All
   + Multiple Applications
   + Demand Planning
   + Insights
   + Order Insights
![Module filters dropdown box.](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/module_filters.png)

1. View the data quality errors under the **Impacted Module** and **Status Message** columns.

   The **Impacted Module** column displays the AWS Supply Chain application and the related feature that was impacted.

   The **Status Message** column displays the product entity and the number of errors under each product entity. For example, the "The field "channel\_id" has null or empty value..." error means that the "channel\_id" column in the ingested outbound\_order\_line file is missing data.
![Impacted Module and Status Message columns.](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/data_quality_columns.png)

## Downloading data quality reports
<a name="data_qual_reports"></a>

To download the data quality report, complete the following steps:

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/) and sign in.

1. Navigate to the **aws-supply-chain-data** instance ID folder, then **data-quality-report**.

1. Select the folder for the data entity you want to view.

   Individual folders for each data ingestion will appear.
![Product data entity folder with data ingestion folders within.](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/data_entity_folder.png)

1. Select the folder for the data ingestion you want to view.

   The data quality report will appear.
![Data quality report json file.](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/data_quality_report.png)

1. Select the file and choose **Download** to download the data quality report in json format.
