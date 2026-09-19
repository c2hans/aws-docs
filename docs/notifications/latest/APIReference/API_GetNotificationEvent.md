---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetNotificationEvent.html
---

# GetNotificationEvent
<a name="API_GetNotificationEvent"></a>

Returns a specified `NotificationEvent`.

**Important**
User Notifications stores notifications in the individual Regions you register as notification hubs and the Region of the source event rule. `GetNotificationEvent` only returns notifications stored in the same Region in which the action is called. User Notifications doesn't backfill notifications to new Regions selected as notification hubs. For this reason, we recommend that you make calls in your oldest registered notification hub. For more information, see [Notification hubs](https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html) in the * AWS User Notifications User Guide*.

## Request Syntax
<a name="API_GetNotificationEvent_RequestSyntax"></a>

```
GET /notification-events/{{arn}}?locale={{locale}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetNotificationEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetNotificationEvent_RequestSyntax) **   <a name="Notifications-GetNotificationEvent-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the `NotificationEvent` to return.
Pattern: `arn:[a-z-]{3,10}:notifications:[-.a-z0-9]{1,63}:[0-9]{12}:configuration/[a-z0-9]{27}/event/[a-z0-9]{27}`
Required: Yes

 ** [locale](#API_GetNotificationEvent_RequestSyntax) **   <a name="Notifications-GetNotificationEvent-request-uri-locale"></a>
The locale code of the language used for the retrieved `NotificationEvent`. The default locale is English `en_US`.
Valid Values: `de_DE | en_CA | en_US | en_UK | es_ES | fr_CA | fr_FR | id_ID | it_IT | ja_JP | ko_KR | pt_BR | tr_TR | zh_CN | zh_TW`

## Request Body
<a name="API_GetNotificationEvent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetNotificationEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "content": {
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
      "endTime": "string",
      "eventStatus": "string",
      "id": "string",
      "media": [
         {
            "caption": "string",
            "mediaId": "string",
            "type": "string",
            "url": "string"
         }
      ],
      "messageComponents": {
         "completeDescription": "string",
         "dimensions": [
            {
               "name": "string",
               "value": "string"
            }
         ],
         "headline": "string",
         "markupDescription": "string",
         "paragraphSummary": "string"
      },
      "notificationType": "string",
      "organizationalUnitId": "string",
      "schemaVersion": "string",
      "sourceEventDetailUrl": "string",
      "sourceEventDetailUrlDisplayText": "string",
      "sourceEventMetadata": {
         "eventOccurrenceTime": "string",
         "eventOriginRegion": "string",
         "eventType": "string",
         "eventTypeVersion": "string",
         "relatedAccount": "string",
         "relatedResources": [
            {
               "arn": "string",
               "detailUrl": "string",
               "id": "string",
               "tags": [ "string" ]
            }
         ],
         "source": "string",
         "sourceEventId": "string"
      },
      "startTime": "string",
      "textParts": {
         "string" : {
            "displayText": "string",
            "textByLocale": {
               "string" : "string"
            },
            "type": "string",
            "url": "string"
         }
      }
   },
   "creationTime": "string",
   "notificationConfigurationArn": "string"
}
```

## Response Elements
<a name="API_GetNotificationEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetNotificationEvent_ResponseSyntax) **   <a name="Notifications-GetNotificationEvent-response-arn"></a>
The ARN of the resource.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications:[-.a-z0-9]{1,63}:[0-9]{12}:configuration/[a-z0-9]{27}/event/[a-z0-9]{27}`

 ** [content](#API_GetNotificationEvent_ResponseSyntax) **   <a name="Notifications-GetNotificationEvent-response-content"></a>
The content of the `NotificationEvent`.
Type: [NotificationEvent](API_NotificationEvent.md) object

 ** [creationTime](#API_GetNotificationEvent_ResponseSyntax) **   <a name="Notifications-GetNotificationEvent-response-creationTime"></a>
The creation time of the `NotificationEvent`.
Type: Timestamp

 ** [notificationConfigurationArn](#API_GetNotificationEvent_ResponseSyntax) **   <a name="Notifications-GetNotificationEvent-response-notificationConfigurationArn"></a>
The ARN of the `NotificationConfiguration`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`

## Errors
<a name="API_GetNotificationEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The ID of the resource that wasn't found.
HTTP Status Code: 404

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
<a name="API_GetNotificationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/GetNotificationEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/GetNotificationEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/GetNotificationEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/GetNotificationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/GetNotificationEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/GetNotificationEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/GetNotificationEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/GetNotificationEvent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/GetNotificationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/GetNotificationEvent)
