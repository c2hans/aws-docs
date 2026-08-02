---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ReportDeliveryChannel.html
---

# ReportDeliveryChannel
<a name="API_ReportDeliveryChannel"></a>

Contains information from your report plan about where to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.

## Contents
<a name="API_ReportDeliveryChannel_Contents"></a>

 ** S3BucketName **   <a name="Backup-Type-ReportDeliveryChannel-S3BucketName"></a>
The unique name of the S3 bucket that receives your reports.
Type: String
Required: Yes

 ** Formats **   <a name="Backup-Type-ReportDeliveryChannel-Formats"></a>
The format of your reports: `CSV`, `JSON`, or both. If not specified, the default format is `CSV`.
Type: Array of strings
Required: No

 ** S3KeyPrefix **   <a name="Backup-Type-ReportDeliveryChannel-S3KeyPrefix"></a>
The prefix for where AWS Backup Audit Manager delivers your reports to Amazon S3. The prefix is this part of the following path: s3://your-bucket-name/`prefix`/Backup/us-west-2/year/month/day/report-name. If not specified, there is no prefix.
Type: String
Required: No

## See Also
<a name="API_ReportDeliveryChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ReportDeliveryChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ReportDeliveryChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ReportDeliveryChannel)
