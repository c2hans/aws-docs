---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateUserDefinedFunction.html
---

# CreateUserDefinedFunction
<a name="API_CreateUserDefinedFunction"></a>

Creates a new function definition in the Data Catalog.

## Request Syntax
<a name="API_CreateUserDefinedFunction_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "FunctionInput": {
      "ClassName": "{{string}}",
      "FunctionName": "{{string}}",
      "FunctionType": "{{string}}",
      "OwnerName": "{{string}}",
      "OwnerType": "{{string}}",
      "ResourceUris": [
         {
            "ResourceType": "{{string}}",
            "Uri": "{{string}}"
         }
      ]
   }
}
```

## Request Parameters
<a name="API_CreateUserDefinedFunction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_CreateUserDefinedFunction_RequestSyntax) **   <a name="Glue-CreateUserDefinedFunction-request-CatalogId"></a>
The ID of the Data Catalog in which to create the function. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_CreateUserDefinedFunction_RequestSyntax) **   <a name="Glue-CreateUserDefinedFunction-request-DatabaseName"></a>
The name of the catalog database in which to create the function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [FunctionInput](#API_CreateUserDefinedFunction_RequestSyntax) **   <a name="Glue-CreateUserDefinedFunction-request-FunctionInput"></a>
A `FunctionInput` object that defines the function to create in the Data Catalog.
Type: [UserDefinedFunctionInput](API_UserDefinedFunctionInput.md) object
Required: Yes

## Response Elements
<a name="API_CreateUserDefinedFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateUserDefinedFunction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
A resource to be created or added already exists.
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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateUserDefinedFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateUserDefinedFunction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateUserDefinedFunction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateUserDefinedFunction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateUserDefinedFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateUserDefinedFunction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateUserDefinedFunction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateUserDefinedFunction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateUserDefinedFunction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateUserDefinedFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateUserDefinedFunction)
