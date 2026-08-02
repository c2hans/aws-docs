---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/ingesting-data.html
---

# Ingesting data for existing connections
<a name="ingesting-data"></a>

The following are the ingestion options if you're using Amazon S3:
+ **Append** – To append the ingestion data or for incremental ingestion, all files from the source path are combined into a single dataset before being ingested into data lake. This method ensures completeness of data for files spanning multiple days. When you remove files from the source path in your S3 bucket, files that are only available in the source path are ingested into data lake.

   The *Append* option make sure that your files in Amazon S3 are replicated and synchronized in data lake.
+ **Overwrite** – During replace, data files are ingested into data lake as they're updated in the source path. Each new file replaces the dataset entirely.
**Note**
You can delete source flows and corresponding data in both the *Append* and *Overwrite* options.

The following are the ingestion operation options for *EDI*, *SAP S/4 HANA*, and *SAP ECC*:
+ **Update** – Updates existing rows of data using the same fields that are used in the recipe.
+ **Replace** – Deletes existing, uploaded data and replaces it with the new, incoming data.
+ **Delete** – Deletes one or more rows of data by using the primary IDs.

**To start data ingestion, follow the procedure below.**

1. On the AWS Supply Chain dashboard, on the left navigation pane, choose **Data Lake**.

1. On the **Data Ingestion** tab, choose **Connections**.

1. Select the connection to ingest data and choose **Data Ingestion**.

   The **Data Ingestion Configuration** page appears.

1. Choose **Get started**.

1. On the **Data Ingestion Details** page, select if you would like to *Update*, *Replace*, or *Delete* the data. Copy the Amazon S3 path by choosing **Copy**.
