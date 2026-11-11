---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ClonedBlueGreenOptions.html
---

# ClonedBlueGreenOptions
<a name="API_ClonedBlueGreenOptions"></a>

Options for a cloned blue/green upgrade.

## Contents
<a name="API_ClonedBlueGreenOptions_Contents"></a>

 ** RetentionOptions **   <a name="opensearchservice-Type-ClonedBlueGreenOptions-RetentionOptions"></a>
How long to keep the cluster that you cut over from after cutover completes. When you start the upgrade, only `RetentionInHours` is accepted.
Type: [RetentionOptions](API_RetentionOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ClonedBlueGreenOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ClonedBlueGreenOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ClonedBlueGreenOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ClonedBlueGreenOptions)
