---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_CreateEventRule.html
---

# CreateEventRule
<a name="API_CreateEventRule"></a>

Creates an [`EventRule`](https://docs.aws.amazon.com/notifications/latest/userguide/glossary.html) that is associated with a specified `NotificationConfiguration`.

## Request Syntax
<a name="API_CreateEventRule_RequestSyntax"></a>

```
POST /event-rules HTTP/1.1
Content-type: application/json

{
   "eventPattern": "{{string}}",
   "eventType": "{{string}}",
   "notificationConfigurationArn": "{{string}}",
   "regions": [ "{{string}}" ],
   "source": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateEventRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEventRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [eventPattern](#API_CreateEventRule_RequestSyntax) **   <a name="Notifications-CreateEventRule-request-eventPattern"></a>
An additional event pattern used to further filter the events this `EventRule` receives.
For more information, see [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *Amazon EventBridge User Guide.*
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [eventType](#API_CreateEventRule_RequestSyntax) **   <a name="Notifications-CreateEventRule-request-eventType"></a>
The event type to match.
Must match one of the valid Amazon EventBridge event types. For example, EC2 Instance State-change Notification and Amazon CloudWatch Alarm State Change. For more information, see [Event delivery from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([a-zA-Z0-9 \-\(\)])+`
Required: Yes

 ** [notificationConfigurationArn](#API_CreateEventRule_RequestSyntax) **   <a name="Notifications-CreateEventRule-request-notificationConfigurationArn"></a>
The Amazon Resource Name (ARN) of the `NotificationConfiguration` associated with this `EventRule`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`
Required: Yes

 ** [regions](#API_CreateEventRule_RequestSyntax) **   <a name="Notifications-CreateEventRule-request-regions"></a>
A list of AWS Regions that send events to this `EventRule`.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`
Required: Yes

 ** [source](#API_CreateEventRule_RequestSyntax) **   <a name="Notifications-CreateEventRule-request-source"></a>
The matched event source.
Must match one of the valid EventBridge sources. Only AWS service sourced events are supported. For example, `aws.ec2` and `aws.cloudwatch`. For more information, see [Event delivery from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `aws.([a-z0-9\-])+`
Required: Yes

## Response Syntax
<a name="API_CreateEventRule_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "notificationConfigurationArn": "string",
   "statusSummaryByRegion": {
      "string" : {
         "reason": "string",
         "status": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateEventRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateEventRule_ResponseSyntax) **   <a name="Notifications-CreateEventRule-response-arn"></a>
The ARN of the resource.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}/rule/[a-z0-9]{27}`

 ** [notificationConfigurationArn](#API_CreateEventRule_ResponseSyntax) **   <a name="Notifications-CreateEventRule-response-notificationConfigurationArn"></a>
The ARN of a `NotificationConfiguration`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`

 ** [statusSummaryByRegion](#API_CreateEventRule_ResponseSyntax) **   <a name="Notifications-CreateEventRule-response-statusSummaryByRegion"></a>
A list of an `EventRule`'s status by Region. Regions are mapped to `EventRuleStatusSummary`.
Type: String to [EventRuleStatusSummary](API_EventRuleStatusSummary.md) object map
Key Length Constraints: Minimum length of 2. Maximum length of 25.
Key Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`

## Errors
<a name="API_CreateEventRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** resourceId **
The resource ID that prompted the conflict error.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The ID of the resource that wasn't found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
 ** quotaCode **
The code for the service quota in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
 ** resourceId **
The ID of the resource that exceeds the service quota.
 ** resourceType **
The type of the resource that exceeds the service quota.
 ** serviceCode **
The code for the service quota exceeded in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
HTTP Status Code: 402

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
<a name="API_CreateEventRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/CreateEventRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/CreateEventRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/CreateEventRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/CreateEventRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/CreateEventRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/CreateEventRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/CreateEventRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/CreateEventRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/CreateEventRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/CreateEventRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
