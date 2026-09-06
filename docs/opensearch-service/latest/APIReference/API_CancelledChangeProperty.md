---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CancelledChangeProperty.html
---

# CancelledChangeProperty
<a name="API_CancelledChangeProperty"></a>

A property change that was cancelled for an Amazon OpenSearch Service domain.

## Contents
<a name="API_CancelledChangeProperty_Contents"></a>

 ** ActiveValue **   <a name="opensearchservice-Type-CancelledChangeProperty-ActiveValue"></a>
The current value of the property, after the change was cancelled.
Type: String
Required: No

 ** CancelledValue **   <a name="opensearchservice-Type-CancelledChangeProperty-CancelledValue"></a>
The pending value of the property that was cancelled. This would have been the eventual value of the property if the chance had not been cancelled.
Type: String
Required: No

 ** PropertyName **   <a name="opensearchservice-Type-CancelledChangeProperty-PropertyName"></a>
The name of the property whose change was cancelled.
Type: String
Required: No

## See Also
<a name="API_CancelledChangeProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CancelledChangeProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CancelledChangeProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CancelledChangeProperty)
