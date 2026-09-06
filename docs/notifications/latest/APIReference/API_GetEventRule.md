---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetEventRule.html
---

# GetEventRule
<a name="API_GetEventRule"></a>

Returns a specified `EventRule`.

## Request Syntax
<a name="API_GetEventRule_RequestSyntax"></a>

```
GET /event-rules/{{arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEventRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetEventRule_RequestSyntax) **   <a name="Notifications-GetEventRule-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the `EventRule` to return.
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}/rule/[a-z0-9]{27}`
Required: Yes

## Request Body
<a name="API_GetEventRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEventRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationTime": "string",
   "eventPattern": "string",
   "eventType": "string",
   "managedRules": [ "string" ],
   "notificationConfigurationArn": "string",
   "regions": [ "string" ],
   "source": "string",
   "statusSummaryByRegion": {
      "string" : {
         "reason": "string",
         "status": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetEventRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetEventRule_ResponseSyntax) **   <a name="Notifications-GetEventRule-response-arn"></a>
The ARN of the resource.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}/rule/[a-z0-9]{27}`

 ** [creationTime](#API_GetEventRule_ResponseSyntax) **   <a name="Notifications-GetEventRule-response-creationTime"></a>
The date when the `EventRule` was created.
Type: Timestamp

 ** [eventPattern](#API_GetEventRule_ResponseSyntax) **   <a name="Notifications-GetEventRule-response-eventPattern"></a>
An additional event pattern used to further filter the events this `EventRule` receives.
For more information, see [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *Amazon EventBridge User Guide.*
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [eventType](#API_GetEventRule_ResponseSyntax) **   <a name="Notifications-GetEventRule-response-eventType"></a>
The event type to match.
Must match one of the valid Amazon EventBridge event types. For example, EC2 Instance State-change Notification and Amazon CloudWatch Alarm State Change. For more information, see [Event delivery from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([a-zA-Z0-9 \-\(\)])+`

 ** [managedRules](#API_GetEventRule_ResponseSyntax) **   <a name="Notifications-GetEventRule-response-managedRules"></a>
A list of managed rules from EventBridge that are associated with this `EventRule`.
These are created by AWS User Notifications within your account so this `EventRule` functions.
Type: Array of strings
Pattern: `arn:[a-z-]{3,10}:events:[a-z-\d]{2,25}:\d{12}:rule\/[a-zA-Z-\d]{1,1024}`

 ** [notificationConfigurationArn](#API_GetEventRule_ResponseSyntax) **   <a name="Notifications-GetEventRule-response-notificationConfigurationArn"></a>
The ARN of a `NotificationConfiguration`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`

 ** [regions](#API_GetEventRule_ResponseSyntax) **   <a name="Notifications-GetEventRule-response-regions"></a>
A list of AWS Regions that send events to this `EventRule`.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`

 ** [source](#API_GetEventRule_ResponseSyntax) **   <a name="Notifications-GetEventRule-response-source"></a>
The matched event source.
Must match one of the valid EventBridge sources. Only AWS service sourced events are supported. For example, `aws.ec2` and `aws.cloudwatch`. For more information, see [Event delivery from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `aws.([a-z0-9\-])+`

 ** [statusSummaryByRegion](#API_GetEventRule_ResponseSyntax) **   <a name="Notifications-GetEventRule-response-statusSummaryByRegion"></a>
A list of an `EventRule`'s status by Region. Regions are mapped to `EventRuleStatusSummary`.
Type: String to [EventRuleStatusSummary](API_EventRuleStatusSummary.md) object map
Key Length Constraints: Minimum length of 2. Maximum length of 25.
Key Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`

## Errors
<a name="API_GetEventRule_Errors"></a>

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
<a name="API_GetEventRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/GetEventRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/GetEventRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/GetEventRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/GetEventRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/GetEventRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/GetEventRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/GetEventRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/GetEventRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/GetEventRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/GetEventRule)
