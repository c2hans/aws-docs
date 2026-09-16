---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListNotificationHubs.html
---

# ListNotificationHubs
<a name="API_ListNotificationHubs"></a>

Returns a list of `NotificationHubs`.

## Request Syntax
<a name="API_ListNotificationHubs_RequestSyntax"></a>

```
GET /notification-hubs?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNotificationHubs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListNotificationHubs_RequestSyntax) **   <a name="Notifications-ListNotificationHubs-request-uri-maxResults"></a>
The maximum number of records to list in a single response.
Valid Range: Fixed value of 3.

 ** [nextToken](#API_ListNotificationHubs_RequestSyntax) **   <a name="Notifications-ListNotificationHubs-request-uri-nextToken"></a>
A pagination token. Set to null to start listing notification hubs from the start.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

## Request Body
<a name="API_ListNotificationHubs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNotificationHubs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "notificationHubs": [
      {
         "creationTime": "string",
         "lastActivationTime": "string",
         "notificationHubRegion": "string",
         "statusSummary": {
            "reason": "string",
            "status": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListNotificationHubs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListNotificationHubs_ResponseSyntax) **   <a name="Notifications-ListNotificationHubs-response-nextToken"></a>
A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

 ** [notificationHubs](#API_ListNotificationHubs_ResponseSyntax) **   <a name="Notifications-ListNotificationHubs-response-notificationHubs"></a>
The `NotificationHubs` in the account.
Type: Array of [NotificationHubOverview](API_NotificationHubOverview.md) objects

## Errors
<a name="API_ListNotificationHubs_Errors"></a>

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
<a name="API_ListNotificationHubs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/ListNotificationHubs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/ListNotificationHubs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ListNotificationHubs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/ListNotificationHubs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ListNotificationHubs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/ListNotificationHubs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/ListNotificationHubs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/ListNotificationHubs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/ListNotificationHubs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ListNotificationHubs)
