---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteDataTableAttribute.html
---

# DeleteDataTableAttribute
<a name="API_DeleteDataTableAttribute"></a>

Deletes an attribute and all its values from a data table.

## Request Syntax
<a name="API_DeleteDataTableAttribute_RequestSyntax"></a>

```
DELETE /data-tables/{{InstanceId}}/{{DataTableId}}/attributes/{{AttributeName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDataTableAttribute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AttributeName](#API_DeleteDataTableAttribute_RequestSyntax) **   <a name="connect-DeleteDataTableAttribute-request-uri-AttributeName"></a>
The name of the attribute to delete.
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** [DataTableId](#API_DeleteDataTableAttribute_RequestSyntax) **   <a name="connect-DeleteDataTableAttribute-request-uri-DataTableId"></a>
The unique identifier for the data table.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_DeleteDataTableAttribute_RequestSyntax) **   <a name="connect-DeleteDataTableAttribute-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DeleteDataTableAttribute_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDataTableAttribute_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LockVersion": {
      "Attribute": "string",
      "DataTable": "string",
      "PrimaryValues": "string",
      "Value": "string"
   }
}
```

## Response Elements
<a name="API_DeleteDataTableAttribute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LockVersion](#API_DeleteDataTableAttribute_ResponseSyntax) **   <a name="connect-DeleteDataTableAttribute-response-LockVersion"></a>
The updated lock version of the data table.
Type: [DataTableLockVersion](API_DataTableLockVersion.md) object

## Errors
<a name="API_DeleteDataTableAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Operation cannot be performed at this time as there is a conflict with another operation or contact state.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DeleteDataTableAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DeleteDataTableAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DeleteDataTableAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DeleteDataTableAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DeleteDataTableAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DeleteDataTableAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DeleteDataTableAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DeleteDataTableAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DeleteDataTableAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DeleteDataTableAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DeleteDataTableAttribute)
