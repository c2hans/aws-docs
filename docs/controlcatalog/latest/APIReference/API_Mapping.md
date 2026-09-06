---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_Mapping.html
---

# Mapping
<a name="API_Mapping"></a>

A structure that contains the details of a mapping relationship, which can be either to a framework or to a common control.

## Contents
<a name="API_Mapping_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** CommonControl **   <a name="controlcatalog-Type-Mapping-CommonControl"></a>
The common control mapping details when the mapping type relates to a common control.
Type: [CommonControlMappingDetails](API_CommonControlMappingDetails.md) object
Required: No

 ** Framework **   <a name="controlcatalog-Type-Mapping-Framework"></a>
The framework mapping details when the mapping type relates to a compliance framework.
Type: [FrameworkMappingDetails](API_FrameworkMappingDetails.md) object
Required: No

 ** RelatedControl **   <a name="controlcatalog-Type-Mapping-RelatedControl"></a>
Returns information about controls that are related to the specified control.
Type: [RelatedControlMappingDetails](API_RelatedControlMappingDetails.md) object
Required: No

## See Also
<a name="API_Mapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/Mapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/Mapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/Mapping)
