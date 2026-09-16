---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchDeleteConnection.html
---

# BatchDeleteConnection
<a name="API_BatchDeleteConnection"></a>

Deletes a list of connection definitions from the Data Catalog.

## Request Syntax
<a name="API_BatchDeleteConnection_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "ConnectionNameList": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchDeleteConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_BatchDeleteConnection_RequestSyntax) **   <a name="Glue-BatchDeleteConnection-request-CatalogId"></a>
The ID of the Data Catalog in which the connections reside. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [ConnectionNameList](#API_BatchDeleteConnection_RequestSyntax) **   <a name="Glue-BatchDeleteConnection-request-ConnectionNameList"></a>
A list of names of the connections to delete.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_BatchDeleteConnection_ResponseSyntax"></a>

```
{
   "Errors": {
      "string" : {
         "ErrorCode": "string",
         "ErrorMessage": "string"
      }
   },
   "Succeeded": [ "string" ]
}
```

## Response Elements
<a name="API_BatchDeleteConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchDeleteConnection_ResponseSyntax) **   <a name="Glue-BatchDeleteConnection-response-Errors"></a>
A map of the names of connections that were not successfully deleted to error details.
Type: String to [ErrorDetail](API_ErrorDetail.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [Succeeded](#API_BatchDeleteConnection_ResponseSyntax) **   <a name="Glue-BatchDeleteConnection-response-Succeeded"></a>
A list of names of the connection definitions that were successfully deleted.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_BatchDeleteConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_BatchDeleteConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchDeleteConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchDeleteConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchDeleteConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchDeleteConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchDeleteConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchDeleteConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchDeleteConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchDeleteConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchDeleteConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchDeleteConnection)
