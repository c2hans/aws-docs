---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateHoursOfOperation.html
---

# UpdateHoursOfOperation
<a name="API_UpdateHoursOfOperation"></a>

Updates the hours of operation.

## Request Syntax
<a name="API_UpdateHoursOfOperation_RequestSyntax"></a>

```
POST /hours-of-operations/{{InstanceId}}/{{HoursOfOperationId}} HTTP/1.1
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
   "TimeZone": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateHoursOfOperation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HoursOfOperationId](#API_UpdateHoursOfOperation_RequestSyntax) **   <a name="connect-UpdateHoursOfOperation-request-uri-HoursOfOperationId"></a>
The identifier of the hours of operation.
Required: Yes

 ** [InstanceId](#API_UpdateHoursOfOperation_RequestSyntax) **   <a name="connect-UpdateHoursOfOperation-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateHoursOfOperation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Config](#API_UpdateHoursOfOperation_RequestSyntax) **   <a name="connect-UpdateHoursOfOperation-request-Config"></a>
Configuration information of the hours of operation.
Type: Array of [HoursOfOperationConfig](API_HoursOfOperationConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [Description](#API_UpdateHoursOfOperation_RequestSyntax) **   <a name="connect-UpdateHoursOfOperation-request-Description"></a>
The description of the hours of operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Required: No

 ** [Name](#API_UpdateHoursOfOperation_RequestSyntax) **   <a name="connect-UpdateHoursOfOperation-request-Name"></a>
The name of the hours of operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** [TimeZone](#API_UpdateHoursOfOperation_RequestSyntax) **   <a name="connect-UpdateHoursOfOperation-request-TimeZone"></a>
The time zone of the hours of operation.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateHoursOfOperation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateHoursOfOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateHoursOfOperation_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateHoursOfOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateHoursOfOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateHoursOfOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateHoursOfOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateHoursOfOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateHoursOfOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateHoursOfOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateHoursOfOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateHoursOfOperation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateHoursOfOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateHoursOfOperation)
