---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListNotificationEvents.html
---

# ListNotificationEvents
<a name="API_ListNotificationEvents"></a>

Returns a list of `NotificationEvents` according to specified filters, in reverse chronological order (newest first).

**Important**
User Notifications stores notifications in the individual Regions you register as notification hubs and the Region of the source event rule. ListNotificationEvents only returns notifications stored in the same Region in which the action is called. User Notifications doesn't backfill notifications to new Regions selected as notification hubs. For this reason, we recommend that you make calls in your oldest registered notification hub. For more information, see [Notification hubs](https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html) in the * AWS User Notifications User Guide*.

## Request Syntax
<a name="API_ListNotificationEvents_RequestSyntax"></a>

```
GET /notification-events?aggregateNotificationEventArn={{aggregateNotificationEventArn}}&endTime={{endTime}}&includeChildEvents={{includeChildEvents}}&locale={{locale}}&maxResults={{maxResults}}&nextToken={{nextToken}}&organizationalUnitId={{organizationalUnitId}}&source={{source}}&startTime={{startTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNotificationEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [aggregateNotificationEventArn](#API_ListNotificationEvents_RequestSyntax) **   <a name="Notifications-ListNotificationEvents-request-uri-aggregateNotificationEventArn"></a>
The Amazon Resource Name (ARN) of the `aggregatedNotificationEventArn` to match.
Pattern: `arn:[a-z-]{3,10}:notifications:[-.a-z0-9]{1,63}:[0-9]{12}:configuration/[a-z0-9]{27}/event/[a-z0-9]{27}`

 ** [endTime](#API_ListNotificationEvents_RequestSyntax) **   <a name="Notifications-ListNotificationEvents-request-uri-endTime"></a>
Latest time of events to return from this call.

 ** [includeChildEvents](#API_ListNotificationEvents_RequestSyntax) **   <a name="Notifications-ListNotificationEvents-request-uri-includeChildEvents"></a>
Include aggregated child events in the result.

 ** [locale](#API_ListNotificationEvents_RequestSyntax) **   <a name="Notifications-ListNotificationEvents-request-uri-locale"></a>
The locale code of the language used for the retrieved `NotificationEvent`. The default locale is English `(en_US)`.
Valid Values: `de_DE | en_CA | en_US | en_UK | es_ES | fr_CA | fr_FR | id_ID | it_IT | ja_JP | ko_KR | pt_BR | tr_TR | zh_CN | zh_TW`

 ** [maxResults](#API_ListNotificationEvents_RequestSyntax) **   <a name="Notifications-ListNotificationEvents-request-uri-maxResults"></a>
The maximum number of results to be returned in this call. Defaults to 20.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListNotificationEvents_RequestSyntax) **   <a name="Notifications-ListNotificationEvents-request-uri-nextToken"></a>
The start token for paginated calls. Retrieved from the response of a previous `ListEventRules` call. Next token uses Base64 encoding.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

 ** [organizationalUnitId](#API_ListNotificationEvents_RequestSyntax) **   <a name="Notifications-ListNotificationEvents-request-uri-organizationalUnitId"></a>
The unique identifier of the organizational unit used to filter notification events.
Pattern: `(Root|r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`

 ** [source](#API_ListNotificationEvents_RequestSyntax) **   <a name="Notifications-ListNotificationEvents-request-uri-source"></a>
The matched event source.
Must match one of the valid EventBridge sources. Only AWS service sourced events are supported. For example, `aws.ec2` and `aws.cloudwatch`. For more information, see [Event delivery from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the *Amazon EventBridge User Guide*.
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `aws.([a-z0-9\-])+`

 ** [startTime](#API_ListNotificationEvents_RequestSyntax) **   <a name="Notifications-ListNotificationEvents-request-uri-startTime"></a>
The earliest time of events to return from this call.

## Request Body
<a name="API_ListNotificationEvents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNotificationEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "notificationEvents": [
      {
         "aggregateNotificationEventArn": "string",
         "aggregationEventType": "string",
         "aggregationSummary": {
            "additionalSummarizationDimensions": [
               {
                  "count": number,
                  "name": "string",
                  "sampleValues": [ "string" ]
               }
            ],
            "aggregatedAccounts": {
               "count": number,
               "name": "string",
               "sampleValues": [ "string" ]
            },
            "aggregatedBy": [
               {
                  "name": "string",
                  "value": "string"
               }
            ],
            "aggregatedOrganizationalUnits": {
               "count": number,
               "name": "string",
               "sampleValues": [ "string" ]
            },
            "aggregatedRegions": {
               "count": number,
               "name": "string",
               "sampleValues": [ "string" ]
            },
            "eventCount": number
         },
         "arn": "string",
         "creationTime": "string",
         "notificationConfigurationArn": "string",
         "notificationEvent": {
            "eventStatus": "string",
            "messageComponents": {
               "headline": "string"
            },
            "notificationType": "string",
            "schemaVersion": "string",
            "sourceEventMetadata": {
               "eventOriginRegion": "string",
               "eventType": "string",
               "source": "string"
            }
         },
         "organizationalUnitId": "string",
         "relatedAccount": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNotificationEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListNotificationEvents_ResponseSyntax) **   <a name="Notifications-ListNotificationEvents-response-nextToken"></a>
A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

 ** [notificationEvents](#API_ListNotificationEvents_ResponseSyntax) **   <a name="Notifications-ListNotificationEvents-response-notificationEvents"></a>
The list of notification events.
Type: Array of [NotificationEventOverview](API_NotificationEventOverview.md) objects

## Errors
<a name="API_ListNotificationEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service being throttled.
HTTP Status Code: 429

 ** ValidationException **
This exception is thrown when the notification event fails validation.
 ** fieldList **
The list of input fields that are invalid.
 ** reason **
The reason why your input is considered invalid.
HTTP Status Code: 400

## See Also
<a name="API_ListNotificationEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/ListNotificationEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/ListNotificationEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ListNotificationEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/ListNotificationEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ListNotificationEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/ListNotificationEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/ListNotificationEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/ListNotificationEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/ListNotificationEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ListNotificationEvents)
