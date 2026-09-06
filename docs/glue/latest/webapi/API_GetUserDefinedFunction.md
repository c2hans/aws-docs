---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetUserDefinedFunction.html
---

# GetUserDefinedFunction
<a name="API_GetUserDefinedFunction"></a>

Retrieves a specified function definition from the Data Catalog.

## Request Syntax
<a name="API_GetUserDefinedFunction_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "FunctionName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetUserDefinedFunction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetUserDefinedFunction_RequestSyntax) **   <a name="Glue-GetUserDefinedFunction-request-CatalogId"></a>
The ID of the Data Catalog where the function to be retrieved is located. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_GetUserDefinedFunction_RequestSyntax) **   <a name="Glue-GetUserDefinedFunction-request-DatabaseName"></a>
The name of the catalog database where the function is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [FunctionName](#API_GetUserDefinedFunction_RequestSyntax) **   <a name="Glue-GetUserDefinedFunction-request-FunctionName"></a>
The name of the function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetUserDefinedFunction_ResponseSyntax"></a>

```
{
   "UserDefinedFunction": {
      "CatalogId": "string",
      "ClassName": "string",
      "CreateTime": number,
      "DatabaseName": "string",
      "FunctionName": "string",
      "FunctionType": "string",
      "OwnerName": "string",
      "OwnerType": "string",
      "ResourceUris": [
         {
            "ResourceType": "string",
            "Uri": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetUserDefinedFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserDefinedFunction](#API_GetUserDefinedFunction_ResponseSyntax) **   <a name="Glue-GetUserDefinedFunction-response-UserDefinedFunction"></a>
The requested function definition.
Type: [UserDefinedFunction](API_UserDefinedFunction.md) object

## Errors
<a name="API_GetUserDefinedFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** GlueEncryptionException **
An encryption operation failed.
 ** Message **
The message describing the problem.
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
<a name="API_GetUserDefinedFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetUserDefinedFunction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetUserDefinedFunction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetUserDefinedFunction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetUserDefinedFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetUserDefinedFunction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetUserDefinedFunction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetUserDefinedFunction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetUserDefinedFunction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetUserDefinedFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetUserDefinedFunction)
