---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_BatchCreateDataTableValue.html
---

# BatchCreateDataTableValue
<a name="API_BatchCreateDataTableValue"></a>

Creates values for attributes in a data table. The value may be a default or it may be associated with a primary value. The value must pass all customer defined validation as well as the default validation for the value type. The operation must conform to Batch Operation API Standards. Although the standard specifies that successful and failed entities are listed separately in the response, authorization fails if any primary values or attributes are unauthorized. The combination of primary values and the attribute name serve as the identifier for the individual item request.

## Request Syntax
<a name="API_BatchCreateDataTableValue_RequestSyntax"></a>

```
POST /data-tables/{{InstanceId}}/{{DataTableId}}/values/create HTTP/1.1
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
<a name="API_BatchCreateDataTableValue_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataTableId](#API_BatchCreateDataTableValue_RequestSyntax) **   <a name="connect-BatchCreateDataTableValue-request-uri-DataTableId"></a>
The unique identifier for the data table. Must also accept the table ARN with or without a version alias. If no alias is provided, the default behavior is identical to providing the $LATEST alias.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_BatchCreateDataTableValue_RequestSyntax) **   <a name="connect-BatchCreateDataTableValue-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_BatchCreateDataTableValue_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Values](#API_BatchCreateDataTableValue_RequestSyntax) **   <a name="connect-BatchCreateDataTableValue-request-Values"></a>
A list of values to create. Each value must specify the attribute name and optionally primary values if the table has primary attributes.
Type: Array of [DataTableValue](API_DataTableValue.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## Response Syntax
<a name="API_BatchCreateDataTableValue_ResponseSyntax"></a>

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
         ],
         "RecordId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchCreateDataTableValue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_BatchCreateDataTableValue_ResponseSyntax) **   <a name="connect-BatchCreateDataTableValue-response-Failed"></a>
A list of values that failed to be created with error messages explaining the failure reason.
Type: Array of [BatchCreateDataTableValueFailureResult](API_BatchCreateDataTableValueFailureResult.md) objects

 ** [Successful](#API_BatchCreateDataTableValue_ResponseSyntax) **   <a name="connect-BatchCreateDataTableValue-response-Successful"></a>
A list of successfully created values with their identifiers and lock versions.
Type: Array of [BatchCreateDataTableValueSuccessResult](API_BatchCreateDataTableValueSuccessResult.md) objects

## Errors
<a name="API_BatchCreateDataTableValue_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Operation cannot be performed at this time as there is a conflict with another operation or contact state.
HTTP Status Code: 409

 ** DuplicateResourceException **
A resource with the specified name already exists.
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

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_BatchCreateDataTableValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/BatchCreateDataTableValue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/BatchCreateDataTableValue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/BatchCreateDataTableValue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/BatchCreateDataTableValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/BatchCreateDataTableValue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/BatchCreateDataTableValue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/BatchCreateDataTableValue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/BatchCreateDataTableValue)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/BatchCreateDataTableValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/BatchCreateDataTableValue)
