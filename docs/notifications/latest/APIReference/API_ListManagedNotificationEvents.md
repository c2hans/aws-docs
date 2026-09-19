---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListManagedNotificationEvents.html
---

# ListManagedNotificationEvents
<a name="API_ListManagedNotificationEvents"></a>

Returns a list of Managed Notification Events according to specified filters, ordered by creation time in reverse chronological order (newest first).

## Request Syntax
<a name="API_ListManagedNotificationEvents_RequestSyntax"></a>

```
GET /managed-notification-events?endTime={{endTime}}&includeSensitiveEvents={{includeSensitiveEvents}}&locale={{locale}}&maxResults={{maxResults}}&nextToken={{nextToken}}&organizationalUnitId={{organizationalUnitId}}&relatedAccount={{relatedAccount}}&source={{source}}&startTime={{startTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListManagedNotificationEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endTime](#API_ListManagedNotificationEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationEvents-request-uri-endTime"></a>
Latest time of events to return from this call.

 ** [includeSensitiveEvents](#API_ListManagedNotificationEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationEvents-request-uri-includeSensitiveEvents"></a>
Specifies whether to include sensitive events in the result. By default, only non-sensitive events are returned. The `notifications:AccessSensitiveEvents` permission controls access to sensitive events.

 ** [locale](#API_ListManagedNotificationEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationEvents-request-uri-locale"></a>
The locale code of the language used for the retrieved NotificationEvent. The default locale is English (en\_US).
Valid Values: `de_DE | en_CA | en_US | en_UK | es_ES | fr_CA | fr_FR | id_ID | it_IT | ja_JP | ko_KR | pt_BR | tr_TR | zh_CN | zh_TW`

 ** [maxResults](#API_ListManagedNotificationEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationEvents-request-uri-maxResults"></a>
The maximum number of results to be returned in this call. Defaults to 20.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListManagedNotificationEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationEvents-request-uri-nextToken"></a>
The start token for paginated calls. Retrieved from the response of a previous `ListManagedNotificationChannelAssociations` call. Next token uses Base64 encoding.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

 ** [organizationalUnitId](#API_ListManagedNotificationEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationEvents-request-uri-organizationalUnitId"></a>
The Organizational Unit Id that an AWS account belongs to.
Pattern: `(Root|r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`

 ** [relatedAccount](#API_ListManagedNotificationEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationEvents-request-uri-relatedAccount"></a>
The AWS account ID associated with the Managed Notification Events.
Pattern: `\d{12}`

 ** [source](#API_ListManagedNotificationEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationEvents-request-uri-source"></a>
The AWS service the event originates from. For example aws.cloudwatch.
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `aws.([a-z0-9\-])+`

 ** [startTime](#API_ListManagedNotificationEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationEvents-request-uri-startTime"></a>
The earliest time of events to return from this call.

## Request Body
<a name="API_ListManagedNotificationEvents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListManagedNotificationEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "managedNotificationEvents": [
      {
         "aggregatedNotificationRegions": [ "string" ],
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
         "managedNotificationConfigurationArn": "string",
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListManagedNotificationEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [managedNotificationEvents](#API_ListManagedNotificationEvents_ResponseSyntax) **   <a name="Notifications-ListManagedNotificationEvents-response-managedNotificationEvents"></a>
A list of Managed Notification Events matching the request criteria.
Type: Array of [ManagedNotificationEventOverview](API_ManagedNotificationEventOverview.md) objects

 ** [nextToken](#API_ListManagedNotificationEvents_ResponseSyntax) **   <a name="Notifications-ListManagedNotificationEvents-response-nextToken"></a>
A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

## Errors
<a name="API_ListManagedNotificationEvents_Errors"></a>

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
<a name="API_ListManagedNotificationEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/ListManagedNotificationEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/ListManagedNotificationEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ListManagedNotificationEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/ListManagedNotificationEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ListManagedNotificationEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/ListManagedNotificationEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/ListManagedNotificationEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/ListManagedNotificationEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/ListManagedNotificationEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ListManagedNotificationEvents)
