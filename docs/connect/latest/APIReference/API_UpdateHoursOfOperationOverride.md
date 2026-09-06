---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateHoursOfOperationOverride.html
---

# UpdateHoursOfOperationOverride
<a name="API_UpdateHoursOfOperationOverride"></a>

Update the hours of operation override.

## Request Syntax
<a name="API_UpdateHoursOfOperationOverride_RequestSyntax"></a>

```
POST /hours-of-operations/{{InstanceId}}/{{HoursOfOperationId}}/overrides/{{HoursOfOperationOverrideId}} HTTP/1.1
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
<a name="API_UpdateHoursOfOperationOverride_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HoursOfOperationId](#API_UpdateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-UpdateHoursOfOperationOverride-request-uri-HoursOfOperationId"></a>
The identifier for the hours of operation.
Required: Yes

 ** [HoursOfOperationOverrideId](#API_UpdateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-UpdateHoursOfOperationOverride-request-uri-HoursOfOperationOverrideId"></a>
The identifier for the hours of operation override.
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** [InstanceId](#API_UpdateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-UpdateHoursOfOperationOverride-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateHoursOfOperationOverride_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Config](#API_UpdateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-UpdateHoursOfOperationOverride-request-Config"></a>
Configuration information for the hours of operation override: day, start time, and end time.
Type: Array of [HoursOfOperationOverrideConfig](API_HoursOfOperationOverrideConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** [Description](#API_UpdateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-UpdateHoursOfOperationOverride-request-Description"></a>
The description of the hours of operation override.
Type: String
Pattern: `^[\P{C}\r\n\t]{1,250}$`
Required: No

 ** [EffectiveFrom](#API_UpdateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-UpdateHoursOfOperationOverride-request-EffectiveFrom"></a>
The date from when the hours of operation override would be effective.
Type: String
Pattern: `^\d{4}-\d{2}-\d{2}$`
Required: No

 ** [EffectiveTill](#API_UpdateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-UpdateHoursOfOperationOverride-request-EffectiveTill"></a>
The date until the hours of operation override is effective.
Type: String
Pattern: `^\d{4}-\d{2}-\d{2}$`
Required: No

 ** [Name](#API_UpdateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-UpdateHoursOfOperationOverride-request-Name"></a>
The name of the hours of operation override.
Type: String
Pattern: `^[\P{C}\r\n\t]{1,127}$`
Required: No

 ** [OverrideType](#API_UpdateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-UpdateHoursOfOperationOverride-request-OverrideType"></a>
Whether the override will be defined as a *standard* or as a *recurring event*.
For more information about how override types are applied, see [Build your list of overrides](https://docs.aws.amazon.com/connect/latest/adminguide/hours-of-operation-overrides.html) in the * Administrator Guide*.
Type: String
Valid Values: `STANDARD | OPEN | CLOSED`
Required: No

 ** [RecurrenceConfig](#API_UpdateHoursOfOperationOverride_RequestSyntax) **   <a name="connect-UpdateHoursOfOperationOverride-request-RecurrenceConfig"></a>
Configuration for a recurring event.
Type: [RecurrenceConfig](API_RecurrenceConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateHoursOfOperationOverride_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateHoursOfOperationOverride_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateHoursOfOperationOverride_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConditionalOperationFailedException **
Request processing failed because dependent condition failed.
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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateHoursOfOperationOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateHoursOfOperationOverride)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateHoursOfOperationOverride)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateHoursOfOperationOverride)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateHoursOfOperationOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateHoursOfOperationOverride)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateHoursOfOperationOverride)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateHoursOfOperationOverride)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateHoursOfOperationOverride)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateHoursOfOperationOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateHoursOfOperationOverride)
