---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableMaintenanceJobStatusValue.html
---

# TableMaintenanceJobStatusValue
<a name="API_s3Buckets_TableMaintenanceJobStatusValue"></a>

Details about the status of a maintenance job.

## Contents
<a name="API_s3Buckets_TableMaintenanceJobStatusValue_Contents"></a>

 ** status **   <a name="AmazonS3-Type-s3Buckets_TableMaintenanceJobStatusValue-status"></a>
The status of the job.
Type: String
Valid Values: `Not_Yet_Run | Successful | Failed | Disabled`
Required: Yes

 ** failureMessage **   <a name="AmazonS3-Type-s3Buckets_TableMaintenanceJobStatusValue-failureMessage"></a>
The failure message of a failed job.
Type: String
Required: No

 ** lastRunTimestamp **   <a name="AmazonS3-Type-s3Buckets_TableMaintenanceJobStatusValue-lastRunTimestamp"></a>
The date and time that the maintenance job was last run.
Type: Timestamp
Required: No

## See Also
<a name="API_s3Buckets_TableMaintenanceJobStatusValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/TableMaintenanceJobStatusValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/TableMaintenanceJobStatusValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/TableMaintenanceJobStatusValue)
