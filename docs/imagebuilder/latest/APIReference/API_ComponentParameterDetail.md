---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ComponentParameterDetail.html
---

# ComponentParameterDetail
<a name="API_ComponentParameterDetail"></a>

Defines a parameter that is used to provide configuration details for the component.

## Contents
<a name="API_ComponentParameterDetail_Contents"></a>

 ** name **   <a name="imagebuilder-Type-ComponentParameterDetail-name"></a>
The name of this input parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\x00]+`
Required: Yes

 ** type **   <a name="imagebuilder-Type-ComponentParameterDetail-type"></a>
The type of input this parameter provides. The currently supported value is "string".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^String|Integer|Boolean|StringList$`
Required: Yes

 ** defaultValue **   <a name="imagebuilder-Type-ComponentParameterDetail-defaultValue"></a>
The default value of this parameter if no input is provided.
Type: Array of strings
Length Constraints: Minimum length of 0.
Pattern: `[^\x00]*`
Required: No

 ** description **   <a name="imagebuilder-Type-ComponentParameterDetail-description"></a>
Describes this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[^\x00]+`
Required: No

## See Also
<a name="API_ComponentParameterDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ComponentParameterDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ComponentParameterDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ComponentParameterDetail)
