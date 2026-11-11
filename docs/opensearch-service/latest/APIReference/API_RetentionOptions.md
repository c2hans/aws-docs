---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RetentionOptions.html
---

# RetentionOptions
<a name="API_RetentionOptions"></a>

Controls how long the cluster that you cut over from is kept after cutover completes. Specify exactly one of `RetentionInHours` or `RetentionAction`.

## Contents
<a name="API_RetentionOptions_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** RetentionAction **   <a name="opensearchservice-Type-RetentionOptions-RetentionAction"></a>
Ends the retention period now. Valid only after cutover completes.
Type: String
Valid Values: `RollbackToPrimaryCluster | DeletePrimaryCluster`
Required: No

 ** RetentionInHours **   <a name="opensearchservice-Type-RetentionOptions-RetentionInHours"></a>
The number of hours to keep the cluster that you cut over from. The retention period starts when cutover completes. The minimum is 1 hour. In an `UpdateClone` response after cutover completes, this value is the number of hours remaining in the retention period, rounded up.
Type: Integer
Required: No

## See Also
<a name="API_RetentionOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/RetentionOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/RetentionOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/RetentionOptions)
