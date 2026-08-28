---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableRecordExpirationJobMetrics.html
---

# TableRecordExpirationJobMetrics
<a name="API_s3Buckets_TableRecordExpirationJobMetrics"></a>

Provides metrics for the record expiration job that most recently ran for a table. The metrics provide insight into the amount of data that was removed when the job ran.

## Contents
<a name="API_s3Buckets_TableRecordExpirationJobMetrics_Contents"></a>

 ** deletedDataFiles **   <a name="AmazonS3-Type-s3Buckets_TableRecordExpirationJobMetrics-deletedDataFiles"></a>
The total number of data files that were removed when the job ran.
Type: Long
Required: No

 ** deletedRecords **   <a name="AmazonS3-Type-s3Buckets_TableRecordExpirationJobMetrics-deletedRecords"></a>
The total number of records that were removed when the job ran.
Type: Long
Required: No

 ** removedFilesSize **   <a name="AmazonS3-Type-s3Buckets_TableRecordExpirationJobMetrics-removedFilesSize"></a>
The total size (in bytes) of the data files that were removed when the job ran.
Type: Long
Required: No

## See Also
<a name="API_s3Buckets_TableRecordExpirationJobMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/TableRecordExpirationJobMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/TableRecordExpirationJobMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/TableRecordExpirationJobMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
