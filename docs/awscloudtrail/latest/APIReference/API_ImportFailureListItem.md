---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ImportFailureListItem.html
---

# ImportFailureListItem
<a name="API_ImportFailureListItem"></a>

 Provides information about an import failure.

## Contents
<a name="API_ImportFailureListItem_Contents"></a>

 ** ErrorMessage **   <a name="awscloudtrail-Type-ImportFailureListItem-ErrorMessage"></a>
 Provides the reason the import failed.
Type: String
Required: No

 ** ErrorType **   <a name="awscloudtrail-Type-ImportFailureListItem-ErrorType"></a>
 The type of import error.
Type: String
Required: No

 ** LastUpdatedTime **   <a name="awscloudtrail-Type-ImportFailureListItem-LastUpdatedTime"></a>
 When the import was last updated.
Type: Timestamp
Required: No

 ** Location **   <a name="awscloudtrail-Type-ImportFailureListItem-Location"></a>
 The location of the failure in the S3 bucket.
Type: String
Required: No

 ** Status **   <a name="awscloudtrail-Type-ImportFailureListItem-Status"></a>
 The status of the import.
Type: String
Valid Values: `FAILED | RETRY | SUCCEEDED`
Required: No

## See Also
<a name="API_ImportFailureListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ImportFailureListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ImportFailureListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ImportFailureListItem)
