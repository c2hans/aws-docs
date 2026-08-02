---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetCustomEntityType.html
---

# GetCustomEntityType
<a name="API_GetCustomEntityType"></a>

Retrieves the details of a custom pattern by specifying its name.

## Request Syntax
<a name="API_GetCustomEntityType_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCustomEntityType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_GetCustomEntityType_RequestSyntax) **   <a name="Glue-GetCustomEntityType-request-Name"></a>
The name of the custom pattern that you want to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetCustomEntityType_ResponseSyntax"></a>

```
{
   "ContextWords": [ "string" ],
   "Name": "string",
   "RegexString": "string"
}
```

## Response Elements
<a name="API_GetCustomEntityType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContextWords](#API_GetCustomEntityType_ResponseSyntax) **   <a name="Glue-GetCustomEntityType-response-ContextWords"></a>
A list of context words if specified when you created the custom pattern. If none of these context words are found within the vicinity of the regular expression the data will not be detected as sensitive data.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [Name](#API_GetCustomEntityType_ResponseSyntax) **   <a name="Glue-GetCustomEntityType-response-Name"></a>
The name of the custom pattern that you retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [RegexString](#API_GetCustomEntityType_ResponseSyntax) **   <a name="Glue-GetCustomEntityType-response-RegexString"></a>
A regular expression string that is used for detecting sensitive data in a custom pattern.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_GetCustomEntityType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetCustomEntityType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetCustomEntityType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetCustomEntityType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetCustomEntityType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetCustomEntityType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetCustomEntityType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetCustomEntityType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetCustomEntityType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetCustomEntityType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetCustomEntityType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetCustomEntityType)
