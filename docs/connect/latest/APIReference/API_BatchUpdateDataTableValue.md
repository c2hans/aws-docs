---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_BatchUpdateDataTableValue.html
---

# BatchUpdateDataTableValue
<a name="API_BatchUpdateDataTableValue"></a>

Updates multiple data table values using all properties from BatchCreateDataTableValue. System managed values are not modifiable by customers. The operation requires proper lock versions to prevent concurrent modification conflicts.

## Request Syntax
<a name="API_BatchUpdateDataTableValue_RequestSyntax"></a>

```
POST /data-tables/{{InstanceId}}/{{DataTableId}}/values/update HTTP/1.1
Content-type: application/json

{
   "Values": [
      {
         "AttributeName": "{{string}}",
         "LastModifiedRegion": "{{string}}",
         "LastModifiedTime": {{number}},
         "LockVersion": {
            "Attribute": "{{string}}",
            "DataTable": "{{string}}",
            "PrimaryValues": "{{string}}",
            "Value": "{{string}}"
         },
         "PrimaryValues": [
            {
               "AttributeName": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchUpdateDataTableValue_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataTableId](#API_BatchUpdateDataTableValue_RequestSyntax) **   <a name="connect-BatchUpdateDataTableValue-request-uri-DataTableId"></a>
The unique identifier for the data table. Must also accept the table ARN with or without a version alias.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_BatchUpdateDataTableValue_RequestSyntax) **   <a name="connect-BatchUpdateDataTableValue-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_BatchUpdateDataTableValue_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Values](#API_BatchUpdateDataTableValue_RequestSyntax) **   <a name="connect-BatchUpdateDataTableValue-request-Values"></a>
A list of values to update, each including the current lock version to ensure optimistic locking.
Type: Array of [DataTableValue](API_DataTableValue.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## Response Syntax
<a name="API_BatchUpdateDataTableValue_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Failed": [
      {
         "AttributeName": "string",
         "Message": "string",
         "PrimaryValues": [
            {
               "AttributeName": "string",
               "Value": "string"
            }
         ]
      }
   ],
   "Successful": [
      {
         "AttributeName": "string",
         "LockVersion": {
            "Attribute": "string",
            "DataTable": "string",
            "PrimaryValues": "string",
            "Value": "string"
         },
         "PrimaryValues": [
            {
               "AttributeName": "string",
               "Value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_BatchUpdateDataTableValue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_BatchUpdateDataTableValue_ResponseSyntax) **   <a name="connect-BatchUpdateDataTableValue-response-Failed"></a>
A list of values that failed to be updated with error messages explaining the failure reason.
Type: Array of [BatchUpdateDataTableValueFailureResult](API_BatchUpdateDataTableValueFailureResult.md) objects

 ** [Successful](#API_BatchUpdateDataTableValue_ResponseSyntax) **   <a name="connect-BatchUpdateDataTableValue-response-Successful"></a>
A list of successfully updated values with their new lock versions and identifiers.
Type: Array of [BatchUpdateDataTableValueSuccessResult](API_BatchUpdateDataTableValueSuccessResult.md) objects

## Errors
<a name="API_BatchUpdateDataTableValue_Errors"></a>

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
<a name="API_BatchUpdateDataTableValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/BatchUpdateDataTableValue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/BatchUpdateDataTableValue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/BatchUpdateDataTableValue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/BatchUpdateDataTableValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/BatchUpdateDataTableValue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/BatchUpdateDataTableValue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/BatchUpdateDataTableValue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/BatchUpdateDataTableValue)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/BatchUpdateDataTableValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/BatchUpdateDataTableValue)
