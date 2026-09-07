---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/manually-uploading-data.html
---

# Uploading data to an Amazon S3 bucket
<a name="manually-uploading-data"></a>

**Note**
Follow this procedure for the SAP ERP Component Central (ECC) connector, and the EDI connector to manually ingest data in the S3 bucket associated with the AWS Supply Chain instance. If you're using the Amazon S3 API to upload data, see [Connecting to SAP ECC 6.0](connecting-sap-ecc.md), or [Connecting to an EDI](connecting-edi.md).

To upload data to an Amazon S3 bucket associated with the AWS Supply Chain instance follow the following procedure.

1. On the AWS Supply Chain dashboard, on the left navigation bar, choose **Open Connections**.

1. Select the required connection.

1. On the **Connection Details** page, note down the Amazon S3 path or choose **Copy** to copy the Amazon S3 path.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/) and sign in.

1. Under **Buckets**, select the name of the bucket (the first name in the Amazon S3 path) that you want to upload your folders or files to.

1. Navigate to the Amazon S3 path that you copied from the AWS Supply Chain dashboard.

1. Choose **Upload**.
![Uploading data to an Amazon S3 bucket](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/S3_console.png)
