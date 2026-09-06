---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UserDefinedFunctionInput.html
---

# UserDefinedFunctionInput
<a name="API_UserDefinedFunctionInput"></a>

A structure used to create or update a user-defined function.

## Contents
<a name="API_UserDefinedFunctionInput_Contents"></a>

 ** ClassName **   <a name="Glue-Type-UserDefinedFunctionInput-ClassName"></a>
The Java class that contains the function code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** FunctionName **   <a name="Glue-Type-UserDefinedFunctionInput-FunctionName"></a>
The name of the function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** FunctionType **   <a name="Glue-Type-UserDefinedFunctionInput-FunctionType"></a>
The type of the function.
Type: String
Valid Values: `REGULAR_FUNCTION | AGGREGATE_FUNCTION | STORED_PROCEDURE`
Required: No

 ** OwnerName **   <a name="Glue-Type-UserDefinedFunctionInput-OwnerName"></a>
The owner of the function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** OwnerType **   <a name="Glue-Type-UserDefinedFunctionInput-OwnerType"></a>
The owner type.
Type: String
Valid Values: `USER | ROLE | GROUP`
Required: No

 ** ResourceUris **   <a name="Glue-Type-UserDefinedFunctionInput-ResourceUris"></a>
The resource URIs for the function.
Type: Array of [ResourceUri](API_ResourceUri.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: No

## See Also
<a name="API_UserDefinedFunctionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UserDefinedFunctionInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UserDefinedFunctionInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UserDefinedFunctionInput)
