---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ResourceTagParameter.html
---

# ResourceTagParameter
<a name="API_ResourceTagParameter"></a>

The resource tag parameter of the project profile.

## Contents
<a name="API_ResourceTagParameter_Contents"></a>

 ** isValueEditable **   <a name="datazone-Type-ResourceTagParameter-isValueEditable"></a>
Specifies whether the value of the resource tag parameter of the project profile is editable at the project level.
Type: Boolean
Required: Yes

 ** key **   <a name="datazone-Type-ResourceTagParameter-key"></a>
The key of the resource tag parameter of the project profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w \.:/=+@-]+`
Required: Yes

 ** value **   <a name="datazone-Type-ResourceTagParameter-value"></a>
The value of the resource tag parameter key of the project profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\w \.:/=+@-]*`
Required: Yes

## See Also
<a name="API_ResourceTagParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ResourceTagParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ResourceTagParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ResourceTagParameter)
