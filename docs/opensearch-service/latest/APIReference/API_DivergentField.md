---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DivergentField.html
---

# DivergentField
<a name="API_DivergentField"></a>

A single field that differs between the source and target copies of an item.

## Contents
<a name="API_DivergentField_Contents"></a>

 ** Path **   <a name="opensearchservice-Type-DivergentField-Path"></a>
The location of the field within the item.
Type: String
Length Constraints: Maximum length of 512.
Required: No

 ** Policy **   <a name="opensearchservice-Type-DivergentField-Policy"></a>
How the comparison treats this field.
Type: String
Valid Values: `redacted`
Required: No

 ** SourceValue **   <a name="opensearchservice-Type-DivergentField-SourceValue"></a>
The field's value on the source domain.
Type: String
Length Constraints: Maximum length of 10240.
Required: No

 ** TargetValue **   <a name="opensearchservice-Type-DivergentField-TargetValue"></a>
The field's value on the target domain.
Type: String
Length Constraints: Maximum length of 10240.
Required: No

## See Also
<a name="API_DivergentField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DivergentField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DivergentField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DivergentField)
