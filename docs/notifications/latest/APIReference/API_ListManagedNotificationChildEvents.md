---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListManagedNotificationChildEvents.html
---

# ListManagedNotificationChildEvents
<a name="API_ListManagedNotificationChildEvents"></a>

Returns a list of `ManagedNotificationChildEvents` for a specified aggregate `ManagedNotificationEvent`, ordered by creation time in reverse chronological order (newest first).

## Request Syntax
<a name="API_ListManagedNotificationChildEvents_RequestSyntax"></a>

```
GET /list-managed-notification-child-events/{{aggregateManagedNotificationEventArn}}?endTime={{endTime}}&locale={{locale}}&maxResults={{maxResults}}&nextToken={{nextToken}}&organizationalUnitId={{organizationalUnitId}}&relatedAccount={{relatedAccount}}&startTime={{startTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListManagedNotificationChildEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [aggregateManagedNotificationEventArn](#API_ListManagedNotificationChildEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationChildEvents-request-uri-aggregateManagedNotificationEventArn"></a>
The Amazon Resource Name (ARN) of the `ManagedNotificationEvent`.
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}/event/[a-z0-9]{27}`
Required: Yes

 ** [endTime](#API_ListManagedNotificationChildEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationChildEvents-request-uri-endTime"></a>
Latest time of events to return from this call.

 ** [locale](#API_ListManagedNotificationChildEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationChildEvents-request-uri-locale"></a>
The locale code of the language used for the retrieved `NotificationEvent`. The default locale is English.`en_US`.
Valid Values: `de_DE | en_CA | en_US | en_UK | es_ES | fr_CA | fr_FR | id_ID | it_IT | ja_JP | ko_KR | pt_BR | tr_TR | zh_CN | zh_TW`

 ** [maxResults](#API_ListManagedNotificationChildEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationChildEvents-request-uri-maxResults"></a>
The maximum number of results to be returned in this call. Defaults to 20.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListManagedNotificationChildEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationChildEvents-request-uri-nextToken"></a>
The start token for paginated calls. Retrieved from the response of a previous ListManagedNotificationChannelAssociations call. Next token uses Base64 encoding.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

 ** [organizationalUnitId](#API_ListManagedNotificationChildEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationChildEvents-request-uri-organizationalUnitId"></a>
The identifier of the AWS Organizations organizational unit (OU) associated with the Managed Notification Child Events.
Pattern: `(Root|r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`

 ** [relatedAccount](#API_ListManagedNotificationChildEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationChildEvents-request-uri-relatedAccount"></a>
The AWS account ID associated with the Managed Notification Child Events.
Pattern: `\d{12}`

 ** [startTime](#API_ListManagedNotificationChildEvents_RequestSyntax) **   <a name="Notifications-ListManagedNotificationChildEvents-request-uri-startTime"></a>
The earliest time of events to return from this call.

## Request Body
<a name="API_ListManagedNotificationChildEvents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListManagedNotificationChildEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "managedNotificationChildEvents": [
      {
         "aggregateManagedNotificationEventArn": "string",
         "arn": "string",
         "childEvent": {
            "aggregationDetail": {
               "summarizationDimensions": [
                  {
                     "name": "string",
                     "value": "string"
                  }
               ]
            },
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
         "creationTime": "string",
         "managedNotificationConfigurationArn": "string",
         "organizationalUnitId": "string",
         "relatedAccount": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListManagedNotificationChildEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [managedNotificationChildEvents](#API_ListManagedNotificationChildEvents_ResponseSyntax) **   <a name="Notifications-ListManagedNotificationChildEvents-response-managedNotificationChildEvents"></a>
A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.
Type: Array of [ManagedNotificationChildEventOverview](API_ManagedNotificationChildEventOverview.md) objects

 ** [nextToken](#API_ListManagedNotificationChildEvents_ResponseSyntax) **   <a name="Notifications-ListManagedNotificationChildEvents-response-nextToken"></a>
A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

## Errors
<a name="API_ListManagedNotificationChildEvents_Errors"></a>

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
<a name="API_ListManagedNotificationChildEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/ListManagedNotificationChildEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/ListManagedNotificationChildEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ListManagedNotificationChildEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/ListManagedNotificationChildEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ListManagedNotificationChildEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/ListManagedNotificationChildEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/ListManagedNotificationChildEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/ListManagedNotificationChildEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/ListManagedNotificationChildEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ListManagedNotificationChildEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
