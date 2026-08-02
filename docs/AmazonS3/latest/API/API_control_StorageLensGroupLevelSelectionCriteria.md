---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensGroupLevelSelectionCriteria.html
---

# StorageLensGroupLevelSelectionCriteria
<a name="API_control_StorageLensGroupLevelSelectionCriteria"></a>

 Indicates which Storage Lens group ARNs to include or exclude in the Storage Lens group aggregation. You can only attach Storage Lens groups to your Storage Lens dashboard if they're included in your Storage Lens group aggregation. If this value is left null, then all Storage Lens groups are selected.

## Contents
<a name="API_control_StorageLensGroupLevelSelectionCriteria_Contents"></a>

 ** Exclude **   <a name="AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Exclude"></a>
 Indicates which Storage Lens group ARNs to exclude from the Storage Lens group aggregation.
Type: Array of strings
Length Constraints: Minimum length of 4. Maximum length of 1024.
Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:storage\-lens\-group\/.*`
Required: No

 ** Include **   <a name="AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Include"></a>
 Indicates which Storage Lens group ARNs to include in the Storage Lens group aggregation.
Type: Array of strings
Length Constraints: Minimum length of 4. Maximum length of 1024.
Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:storage\-lens\-group\/.*`
Required: No

## See Also
<a name="API_control_StorageLensGroupLevelSelectionCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/StorageLensGroupLevelSelectionCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/StorageLensGroupLevelSelectionCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/StorageLensGroupLevelSelectionCriteria)
