---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetSegmentSubscription.html
---

# GetSegmentSubscription
<a name="API_connect-customer-profiles_GetSegmentSubscription"></a>

Returns the current subscription configuration, execution schedule, and status for segment membership events.

## Request Syntax
<a name="API_connect-customer-profiles_GetSegmentSubscription_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/segment-definitions/{{SegmentDefinitionName}}/subscriptions HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetSegmentSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetSegmentSubscription_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSubscription-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [SegmentDefinitionName](#API_connect-customer-profiles_GetSegmentSubscription_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSubscription-request-uri-SegmentDefinitionName"></a>
The unique name of the segment definition.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetSegmentSubscription_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetSegmentSubscription_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LastUpdatedAt": number,
   "Message": "string",
   "ScheduleConfiguration": {
      "Interval": number,
      "Unit": "string"
   },
   "ScheduledExecutions": {
      "LastExecutedAt": number,
      "NextExecutedAt": number
   },
   "StartedAt": number,
   "Status": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetSegmentSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LastUpdatedAt](#API_connect-customer-profiles_GetSegmentSubscription_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSubscription-response-LastUpdatedAt"></a>
The timestamp of the most recent configuration change.
Type: Timestamp

 ** [Message](#API_connect-customer-profiles_GetSegmentSubscription_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSubscription-response-Message"></a>
A status message providing additional context, such as a failure reason.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [ScheduleConfiguration](#API_connect-customer-profiles_GetSegmentSubscription_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSubscription-response-ScheduleConfiguration"></a>
The schedule configuration for periodic membership event notifications.
Type: [ScheduleConfiguration](API_connect-customer-profiles_ScheduleConfiguration.md) object

 ** [ScheduledExecutions](#API_connect-customer-profiles_GetSegmentSubscription_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSubscription-response-ScheduledExecutions"></a>
Information about scheduled execution timestamps.
Type: [ScheduledExecutions](API_connect-customer-profiles_ScheduledExecutions.md) object

 ** [StartedAt](#API_connect-customer-profiles_GetSegmentSubscription_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSubscription-response-StartedAt"></a>
The timestamp of when the subscription was first started.
Type: Timestamp

 ** [Status](#API_connect-customer-profiles_GetSegmentSubscription_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentSubscription-response-Status"></a>
The current lifecycle status of the subscription. The following are valid values:
+  **STARTING**: Initial snapshot is in progress.
+  **RUNNING**: Notifications are active and running.
+  **STOPPED**: Notifications have been stopped.
+  **FAILED**: Notifications failed (for example, the Amazon Kinesis data stream became inaccessible).
Type: String
Valid Values: `STARTING | RUNNING | STOPPED | FAILED`

## Errors
<a name="API_connect-customer-profiles_GetSegmentSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_GetSegmentSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetSegmentSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetSegmentSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetSegmentSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetSegmentSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetSegmentSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetSegmentSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetSegmentSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetSegmentSubscription)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetSegmentSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetSegmentSubscription)
