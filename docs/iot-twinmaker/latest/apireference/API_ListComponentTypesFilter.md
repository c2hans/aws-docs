---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListComponentTypesFilter.html
---

# ListComponentTypesFilter
<a name="API_ListComponentTypesFilter"></a>

An object that filters items in a list of component types.

**Note**
Only one object is accepted as a valid input.

## Contents
<a name="API_ListComponentTypesFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** extendsFrom **   <a name="tm-Type-ListComponentTypesFilter-extendsFrom"></a>
The component type that the component types in the list extend.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z_\.\-0-9:]+`
Required: No

 ** isAbstract **   <a name="tm-Type-ListComponentTypesFilter-isAbstract"></a>
A Boolean value that specifies whether the component types in the list are abstract.
Type: Boolean
Required: No

 ** namespace **   <a name="tm-Type-ListComponentTypesFilter-namespace"></a>
The namespace to which the component types in the list belong.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

## See Also
<a name="API_ListComponentTypesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ListComponentTypesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ListComponentTypesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ListComponentTypesFilter)
