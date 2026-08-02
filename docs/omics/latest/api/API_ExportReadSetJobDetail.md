---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ExportReadSetJobDetail.html
---

# ExportReadSetJobDetail
<a name="API_ExportReadSetJobDetail"></a>

Details about a read set export job.

## Contents
<a name="API_ExportReadSetJobDetail_Contents"></a>

 ** creationTime **   <a name="omics-Type-ExportReadSetJobDetail-creationTime"></a>
When the job was created.
Type: Timestamp
Required: Yes

 ** destination **   <a name="omics-Type-ExportReadSetJobDetail-destination"></a>
The job's destination in Amazon S3.
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/?((.{1,1024})/)?`
Required: Yes

 ** id **   <a name="omics-Type-ExportReadSetJobDetail-id"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** sequenceStoreId **   <a name="omics-Type-ExportReadSetJobDetail-sequenceStoreId"></a>
The job's sequence store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** status **   <a name="omics-Type-ExportReadSetJobDetail-status"></a>
The job's status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELLING | CANCELLED | FAILED | COMPLETED | COMPLETED_WITH_FAILURES`
Required: Yes

 ** completionTime **   <a name="omics-Type-ExportReadSetJobDetail-completionTime"></a>
When the job completed.
Type: Timestamp
Required: No

## See Also
<a name="API_ExportReadSetJobDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ExportReadSetJobDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ExportReadSetJobDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ExportReadSetJobDetail)
