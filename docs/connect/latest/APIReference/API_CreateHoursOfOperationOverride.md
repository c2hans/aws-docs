---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateHoursOfOperationOverride.html
---

# CreateHoursOfOperationOverride
<a name="API_CreateHoursOfOperationOverride"></a>

Creates an hours of operation override in an Connect Customer hours of operation resource.

## Request Syntax
<a name="API_CreateHoursOfOperationOverride_RequestSyntax"></a>

```
PUT /hours-of-operations/{{InstanceId}}/{{HoursOfOperationId}}/overrides HTTP/1.1
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
   "EffectiveFrom": "{{string}}",
   "EffectiveTill": "{{string}}",
   "Name": "{{string}}",
   "OverrideType": "{{string}}",
   "RecurrenceConfig": {
      "RecurrencePattern": {
         "ByMonth": [ {{number}} ],
         "ByMonthDay": [ {{number}} ],
         "ByWeekdayOccurrence": [ {{number}} ],
         "Frequency": "{{string}}",
         "Interval": {{number}}
      }
   }
}
```

## URI Request Parameters
<a name="API_CreateHoursOfOperationOverride_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HoursOfOperationId](#API_CreateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-CreateHoursOfOperationOverride-request-uri-HoursOfOperationId"></a>
The identifier for the hours of operation
Required: Yes

 ** [InstanceId](#API_CreateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-CreateHoursOfOperationOverride-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateHoursOfOperationOverride_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Config](#API_CreateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-CreateHoursOfOperationOverride-request-Config"></a>
Configuration information for the hours of operation override: day, start time, and end time.
Type: Array of [HoursOfOperationOverrideConfig](API_HoursOfOperationOverrideConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

 ** [Description](#API_CreateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-CreateHoursOfOperationOverride-request-Description"></a>
The description of the hours of operation override.
Type: String
Pattern: `^[\P{C}\r\n\t]{1,250}$`
Required: No

 ** [EffectiveFrom](#API_CreateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-CreateHoursOfOperationOverride-request-EffectiveFrom"></a>
The date from when the hours of operation override is effective.
Type: String
Pattern: `^\d{4}-\d{2}-\d{2}$`
Required: Yes

 ** [EffectiveTill](#API_CreateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-CreateHoursOfOperationOverride-request-EffectiveTill"></a>
The date until when the hours of operation override is effective.
Type: String
Pattern: `^\d{4}-\d{2}-\d{2}$`
Required: Yes

 ** [Name](#API_CreateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-CreateHoursOfOperationOverride-request-Name"></a>
The name of the hours of operation override.
Type: String
Pattern: `^[\P{C}\r\n\t]{1,127}$`
Required: Yes

 ** [OverrideType](#API_CreateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-CreateHoursOfOperationOverride-request-OverrideType"></a>
Whether the override will be defined as a *standard* or as a *recurring event*.
For more information about how override types are applied, see [Build your list of overrides](https://docs.aws.amazon.com/connect/latest/adminguide/hours-of-operation-overrides.html) in the * Administrator Guide*.
Type: String
Valid Values: `STANDARD | OPEN | CLOSED`
Required: No

 ** [RecurrenceConfig](#API_CreateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-CreateHoursOfOperationOverride-request-RecurrenceConfig"></a>
Configuration for a recurring event.
Type: [RecurrenceConfig](API_RecurrenceConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateHoursOfOperationOverride_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "HoursOfOperationOverrideId": "string"
}
```

## Response Elements
<a name="API_CreateHoursOfOperationOverride_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HoursOfOperationOverrideId](#API_CreateHoursOfOperationOverride_ResponseSyntax) **   <a name="connect-CreateHoursOfOperationOverride-response-HoursOfOperationOverrideId"></a>
The identifier for the hours of operation override.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.

## Errors
<a name="API_CreateHoursOfOperationOverride_Errors"></a>

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateHoursOfOperationOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateHoursOfOperationOverride)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateHoursOfOperationOverride)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateHoursOfOperationOverride)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateHoursOfOperationOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateHoursOfOperationOverride)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateHoursOfOperationOverride)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateHoursOfOperationOverride)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateHoursOfOperationOverride)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateHoursOfOperationOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateHoursOfOperationOverride)
