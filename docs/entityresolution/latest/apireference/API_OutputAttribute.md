---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_OutputAttribute.html
---

# OutputAttribute
<a name="API_OutputAttribute"></a>

A list of `OutputAttribute` objects, each of which have the fields `Name` and `Hashed`. Each of these objects selects a column to be included in the output table, and whether the values of the column should be hashed.

## Contents
<a name="API_OutputAttribute_Contents"></a>

 ** name **   <a name="API-Type-OutputAttribute-name"></a>
A name of a column to be written to the output. This must be an `InputField` name in the schema mapping.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z_0-9- ]*`
Required: Yes

 ** hashed **   <a name="API-Type-OutputAttribute-hashed"></a>
Enables the ability to hash the column values in the output.
Type: Boolean
Required: No

## See Also
<a name="API_OutputAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/OutputAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/OutputAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/OutputAttribute)
