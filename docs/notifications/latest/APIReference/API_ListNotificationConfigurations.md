---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListNotificationConfigurations.html
---

# ListNotificationConfigurations
<a name="API_ListNotificationConfigurations"></a>

Returns a list of abbreviated `NotificationConfigurations` according to specified filters, in reverse chronological order (newest first).

## Request Syntax
<a name="API_ListNotificationConfigurations_RequestSyntax"></a>

```
GET /notification-configurations?channelArn={{channelArn}}&eventRuleSource={{eventRuleSource}}&maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}}&subtype={{subtype}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNotificationConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_ListNotificationConfigurations_RequestSyntax) **   <a name="Notifications-ListNotificationConfigurations-request-uri-channelArn"></a>
The Amazon Resource Name (ARN) of the Channel to match.
Pattern: `arn:[a-z-]{3,10}:(chatbot|consoleapp|notifications-contacts):[a-zA-Z0-9-]*:[0-9]{12}:[a-zA-Z0-9-_.@]+/[a-zA-Z0-9/_.@:-]+`

 ** [eventRuleSource](#API_ListNotificationConfigurations_RequestSyntax) **   <a name="Notifications-ListNotificationConfigurations-request-uri-eventRuleSource"></a>
The matched event source.
Must match one of the valid EventBridge sources. Only AWS service sourced events are supported. For example, `aws.ec2` and `aws.cloudwatch`. For more information, see [Event delivery from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the *Amazon EventBridge User Guide*.
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `aws.([a-z0-9\-])+`

 ** [maxResults](#API_ListNotificationConfigurations_RequestSyntax) **   <a name="Notifications-ListNotificationConfigurations-request-uri-maxResults"></a>
The maximum number of results to be returned in this call. Defaults to 20.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListNotificationConfigurations_RequestSyntax) **   <a name="Notifications-ListNotificationConfigurations-request-uri-nextToken"></a>
The start token for paginated calls. Retrieved from the response of a previous `ListEventRules` call. Next token uses Base64 encoding.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

 ** [status](#API_ListNotificationConfigurations_RequestSyntax) **   <a name="Notifications-ListNotificationConfigurations-request-uri-status"></a>
The `NotificationConfiguration` status to match.
+ Values:
  +  `ACTIVE`
    + All `EventRules` are `ACTIVE` and any call can be run.
  +  `PARTIALLY_ACTIVE`
    + Some `EventRules` are `ACTIVE` and some are `INACTIVE`. Any call can be run.
    + Any call can be run.
  +  `INACTIVE`
    + All `EventRules` are `INACTIVE` and any call can be run.
  +  `DELETING`
    + This `NotificationConfiguration` is being deleted.
    + Only `GET` and `LIST` calls can be run.
Valid Values: `ACTIVE | PARTIALLY_ACTIVE | INACTIVE | DELETING`

 ** [subtype](#API_ListNotificationConfigurations_RequestSyntax) **   <a name="Notifications-ListNotificationConfigurations-request-uri-subtype"></a>
The subtype used to filter the notification configurations in the request.
Valid Values: `ACCOUNT | ADMIN_MANAGED`

## Request Body
<a name="API_ListNotificationConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNotificationConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "notificationConfigurations": [
      {
         "aggregationDuration": "string",
         "arn": "string",
         "creationTime": "string",
         "description": "string",
         "name": "string",
         "status": "string",
         "subtype": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNotificationConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListNotificationConfigurations_ResponseSyntax) **   <a name="Notifications-ListNotificationConfigurations-response-nextToken"></a>
A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\w+-/=]+`

 ** [notificationConfigurations](#API_ListNotificationConfigurations_ResponseSyntax) **   <a name="Notifications-ListNotificationConfigurations-response-notificationConfigurations"></a>
The `NotificationConfigurations` in the account.
Type: Array of [NotificationConfigurationStructure](API_NotificationConfigurationStructure.md) objects

## Errors
<a name="API_ListNotificationConfigurations_Errors"></a>

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
<a name="API_ListNotificationConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/ListNotificationConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/ListNotificationConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ListNotificationConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/ListNotificationConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ListNotificationConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/ListNotificationConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/ListNotificationConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/ListNotificationConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/ListNotificationConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ListNotificationConfigurations)
