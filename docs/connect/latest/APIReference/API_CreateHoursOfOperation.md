---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateHoursOfOperation.html
---

# CreateHoursOfOperation
<a name="API_CreateHoursOfOperation"></a>

Creates hours of operation.

## Request Syntax
<a name="API_CreateHoursOfOperation_RequestSyntax"></a>

```
PUT /hours-of-operations/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "Config": [
      {
         "Day": "{{string}}",
         "EndTime": {
            "Hours": {{number}},
            "Minutes": {{number}}
         },
         "StartTime": {
            "Hours": {{number}},
            "Minutes": {{number}}
         }
      }
   ],
   "Description": "{{string}}",
   "Name": "{{string}}",
   "ParentHoursOfOperationConfigs": [
      {
         "HoursOfOperationId": "{{string}}"
      }
   ],
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TimeZone": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateHoursOfOperation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateHoursOfOperation_RequestSyntax) **   <a name="connect-CreateHoursOfOperation-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateHoursOfOperation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Config](#API_CreateHoursOfOperation_RequestSyntax) **   <a name="connect-CreateHoursOfOperation-request-Config"></a>
Configuration information for the hours of operation: day, start time, and end time.
Type: Array of [HoursOfOperationConfig](API_HoursOfOperationConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

 ** [Description](#API_CreateHoursOfOperation_RequestSyntax) **   <a name="connect-CreateHoursOfOperation-request-Description"></a>
The description of the hours of operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** [Name](#API_CreateHoursOfOperation_RequestSyntax) **   <a name="connect-CreateHoursOfOperation-request-Name"></a>
The name of the hours of operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: Yes

 ** [ParentHoursOfOperationConfigs](#API_CreateHoursOfOperation_RequestSyntax) **   <a name="connect-CreateHoursOfOperation-request-ParentHoursOfOperationConfigs"></a>
Configuration for parent hours of operations. Eg: ResourceArn.
For more information about parent hours of operations, see [Link overrides from different hours of operation](https://docs.aws.amazon.com/connect/latest/adminguide/hours-of-operation-overrides.html) in the * Administrator Guide*.
Type: Array of [ParentHoursOfOperationConfig](API_ParentHoursOfOperationConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

 ** [Tags](#API_CreateHoursOfOperation_RequestSyntax) **   <a name="connect-CreateHoursOfOperation-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [TimeZone](#API_CreateHoursOfOperation_RequestSyntax) **   <a name="connect-CreateHoursOfOperation-request-TimeZone"></a>
The time zone of the hours of operation.
Type: String
Required: Yes

## Response Syntax
<a name="API_CreateHoursOfOperation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "HoursOfOperationArn": "string",
   "HoursOfOperationId": "string"
}
```

## Response Elements
<a name="API_CreateHoursOfOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HoursOfOperationArn](#API_CreateHoursOfOperation_ResponseSyntax) **   <a name="connect-CreateHoursOfOperation-response-HoursOfOperationArn"></a>
The Amazon Resource Name (ARN) for the hours of operation.
Type: String

 ** [HoursOfOperationId](#API_CreateHoursOfOperation_ResponseSyntax) **   <a name="connect-CreateHoursOfOperation-response-HoursOfOperationId"></a>
The identifier for the hours of operation.
Type: String

## Errors
<a name="API_CreateHoursOfOperation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

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
<a name="API_CreateHoursOfOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateHoursOfOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateHoursOfOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateHoursOfOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateHoursOfOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateHoursOfOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateHoursOfOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateHoursOfOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateHoursOfOperation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateHoursOfOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateHoursOfOperation)
