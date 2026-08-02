---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_MetadataModelReference.html
---

# MetadataModelReference
<a name="API_MetadataModelReference"></a>

A reference to a metadata model, including its name and selection rules for location identification.

## Contents
<a name="API_MetadataModelReference_Contents"></a>

 ** MetadataModelName **   <a name="DMS-Type-MetadataModelReference-MetadataModelName"></a>
The name of the metadata model.
Type: String
Required: No

 ** SelectionRules **   <a name="DMS-Type-MetadataModelReference-SelectionRules"></a>
A JSON string that identifies this metadata model in the metadata tree. For the selection rule format, see [Selection rules in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html).
Usage:
+ You can pass this value as the `SelectionRules` parameter to any operation that accepts selection rules, such as `DescribeMetadataModel`, `StartMetadataModelConversion`, and others.
Type: String
Required: No

## See Also
<a name="API_MetadataModelReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/MetadataModelReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/MetadataModelReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/MetadataModelReference)
