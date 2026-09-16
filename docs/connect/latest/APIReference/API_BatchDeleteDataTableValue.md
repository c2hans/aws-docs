---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_BatchDeleteDataTableValue.html
---

# BatchDeleteDataTableValue
<a name="API_BatchDeleteDataTableValue"></a>

Deletes multiple values from a data table. API users may delete values at any time. When deletion is requested from the admin website, a warning is shown alerting the user of the most recent time the attribute and its values were accessed. System managed values are not deletable by customers.

## Request Syntax
<a name="API_BatchDeleteDataTableValue_RequestSyntax"></a>

```
POST /data-tables/{{InstanceId}}/{{DataTableId}}/values/delete HTTP/1.1
Content-type: application/json

{
   "Values": [
      {
         "AttributeName": "{{string}}",
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
         ]
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchDeleteDataTableValue_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataTableId](#API_BatchDeleteDataTableValue_RequestSyntax) **   <a name="connect-BatchDeleteDataTableValue-request-uri-DataTableId"></a>
The unique identifier for the data table. Must also accept the table ARN with or without a version alias.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_BatchDeleteDataTableValue_RequestSyntax) **   <a name="connect-BatchDeleteDataTableValue-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_BatchDeleteDataTableValue_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Values](#API_BatchDeleteDataTableValue_RequestSyntax) **   <a name="connect-BatchDeleteDataTableValue-request-Values"></a>
A list of value identifiers to delete, each specifying primary values, attribute name, and lock version information.
Type: Array of [DataTableDeleteValueIdentifier](API_DataTableDeleteValueIdentifier.md) objects
Required: Yes

## Response Syntax
<a name="API_BatchDeleteDataTableValue_ResponseSyntax"></a>

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
<a name="API_BatchDeleteDataTableValue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_BatchDeleteDataTableValue_ResponseSyntax) **   <a name="connect-BatchDeleteDataTableValue-response-Failed"></a>
A list of values that failed to be deleted with error messages explaining the failure reason.
Type: Array of [BatchDeleteDataTableValueFailureResult](API_BatchDeleteDataTableValueFailureResult.md) objects

 ** [Successful](#API_BatchDeleteDataTableValue_ResponseSyntax) **   <a name="connect-BatchDeleteDataTableValue-response-Successful"></a>
A list of successfully deleted values with their identifiers and updated lock versions.
Type: Array of [BatchDeleteDataTableValueSuccessResult](API_BatchDeleteDataTableValueSuccessResult.md) objects

## Errors
<a name="API_BatchDeleteDataTableValue_Errors"></a>

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
<a name="API_BatchDeleteDataTableValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/BatchDeleteDataTableValue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/BatchDeleteDataTableValue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/BatchDeleteDataTableValue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/BatchDeleteDataTableValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/BatchDeleteDataTableValue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/BatchDeleteDataTableValue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/BatchDeleteDataTableValue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/BatchDeleteDataTableValue)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/BatchDeleteDataTableValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/BatchDeleteDataTableValue)
