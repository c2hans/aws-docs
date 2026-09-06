---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ViewRepresentationInput.html
---

# ViewRepresentationInput
<a name="API_ViewRepresentationInput"></a>

A structure containing details of a representation to update or create a Lake Formation view.

## Contents
<a name="API_ViewRepresentationInput_Contents"></a>

 ** Dialect **   <a name="Glue-Type-ViewRepresentationInput-Dialect"></a>
A parameter that specifies the engine type of a specific representation.
Type: String
Valid Values: `REDSHIFT | ATHENA | SPARK`
Required: No

 ** DialectVersion **   <a name="Glue-Type-ViewRepresentationInput-DialectVersion"></a>
A parameter that specifies the version of the engine of a specific representation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ValidationConnection **   <a name="Glue-Type-ViewRepresentationInput-ValidationConnection"></a>
The name of the connection to be used to validate the specific representation of the view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ViewExpandedText **   <a name="Glue-Type-ViewRepresentationInput-ViewExpandedText"></a>
A string that represents the SQL query that describes the view with expanded resource ARNs
Type: String
Length Constraints: Maximum length of 409600.
Required: No

 ** ViewOriginalText **   <a name="Glue-Type-ViewRepresentationInput-ViewOriginalText"></a>
A string that represents the original SQL query that describes the view.
Type: String
Length Constraints: Maximum length of 409600.
Required: No

## See Also
<a name="API_ViewRepresentationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ViewRepresentationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ViewRepresentationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ViewRepresentationInput)
