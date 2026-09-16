---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutSegmentSubscription.html
---

# PutSegmentSubscription
<a name="API_connect-customer-profiles_PutSegmentSubscription"></a>

Creates or updates a segment subscription for membership events. When a subscription is created, an initial snapshot is taken and the system begins monitoring for membership changes.

You can optionally set a schedule configuration interval to control how often membership snapshots are run. The interval can be from 1 to 24 hours. If not set, the interval defaults to 24 hours. Scheduled snapshots run on a best-effort basis. If a scheduled snapshot takes longer than the configured interval, the next scheduled run does not start until the in-progress snapshot completes, so a run might be delayed or skipped and is not guaranteed to occur at exactly the requested time.

For Classic segments, membership events are generated from these scheduled snapshots and also in near real-time as profile attribute changes occur. For SQL segments, membership events are generated only from the scheduled snapshots.

## Request Syntax
<a name="API_connect-customer-profiles_PutSegmentSubscription_RequestSyntax"></a>

```
PUT /domains/{{DomainName}}/segment-definitions/{{SegmentDefinitionName}}/subscriptions HTTP/1.1
Content-type: application/json

{
   "ScheduleConfiguration": {
      "Interval": {{number}},
      "Unit": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_PutSegmentSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_PutSegmentSubscription_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutSegmentSubscription-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [SegmentDefinitionName](#API_connect-customer-profiles_PutSegmentSubscription_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutSegmentSubscription-request-uri-SegmentDefinitionName"></a>
The unique name of the segment definition.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_PutSegmentSubscription_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ScheduleConfiguration](#API_connect-customer-profiles_PutSegmentSubscription_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutSegmentSubscription-request-ScheduleConfiguration"></a>
The optional schedule configuration that controls how often membership snapshots are run. If not provided, the subscription defaults to a 24-hour interval.
Type: [ScheduleConfiguration](API_connect-customer-profiles_ScheduleConfiguration.md) object
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_PutSegmentSubscription_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ScheduleConfiguration": {
      "Interval": number,
      "Unit": "string"
   },
   "StartedAt": number,
   "Status": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_PutSegmentSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ScheduleConfiguration](#API_connect-customer-profiles_PutSegmentSubscription_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutSegmentSubscription-response-ScheduleConfiguration"></a>
The schedule configuration for the subscription, if configured.
Type: [ScheduleConfiguration](API_connect-customer-profiles_ScheduleConfiguration.md) object

 ** [StartedAt](#API_connect-customer-profiles_PutSegmentSubscription_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutSegmentSubscription-response-StartedAt"></a>
The timestamp of when the subscription was started.
Type: Timestamp

 ** [Status](#API_connect-customer-profiles_PutSegmentSubscription_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutSegmentSubscription-response-Status"></a>
The current lifecycle status of the subscription. The following are valid values:
+  **STARTING**: Initial snapshot is in progress.
+  **RUNNING**: Notifications are active and running.
+  **STOPPED**: Notifications have been stopped.
+  **FAILED**: Notifications failed (for example, the Amazon Kinesis data stream became inaccessible).
Type: String
Valid Values: `STARTING | RUNNING | STOPPED | FAILED`

## Errors
<a name="API_connect-customer-profiles_PutSegmentSubscription_Errors"></a>

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
<a name="API_connect-customer-profiles_PutSegmentSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/PutSegmentSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/PutSegmentSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/PutSegmentSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/PutSegmentSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/PutSegmentSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/PutSegmentSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/PutSegmentSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/PutSegmentSubscription)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/PutSegmentSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/PutSegmentSubscription)
