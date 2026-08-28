---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_UpdateEventRule.html
---

# UpdateEventRule
<a name="API_UpdateEventRule"></a>

Updates an existing `EventRule`.

## Request Syntax
<a name="API_UpdateEventRule_RequestSyntax"></a>

```
PUT /event-rules/{{arn}} HTTP/1.1
Content-type: application/json

{
   "eventPattern": "{{string}}",
   "regions": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateEventRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_UpdateEventRule_RequestSyntax) **   <a name="Notifications-UpdateEventRule-request-uri-arn"></a>
The Amazon Resource Name (ARN) to use to update the `EventRule`.
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}/rule/[a-z0-9]{27}`
Required: Yes

## Request Body
<a name="API_UpdateEventRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [eventPattern](#API_UpdateEventRule_RequestSyntax) **   <a name="Notifications-UpdateEventRule-request-eventPattern"></a>
An additional event pattern used to further filter the events this `EventRule` receives.
For more information, see [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *Amazon EventBridge User Guide.*
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [regions](#API_UpdateEventRule_RequestSyntax) **   <a name="Notifications-UpdateEventRule-request-regions"></a>
A list of AWS Regions that sends events to this `EventRule`.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`
Required: No

## Response Syntax
<a name="API_UpdateEventRule_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateEventRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateEventRule_ResponseSyntax) **   <a name="Notifications-UpdateEventRule-response-arn"></a>
The Amazon Resource Name (ARN) to use to update the `EventRule`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}/rule/[a-z0-9]{27}`

 ** [notificationConfigurationArn](#API_UpdateEventRule_ResponseSyntax) **   <a name="Notifications-UpdateEventRule-response-notificationConfigurationArn"></a>
The ARN of the `NotificationConfiguration`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`

 ** [statusSummaryByRegion](#API_UpdateEventRule_ResponseSyntax) **   <a name="Notifications-UpdateEventRule-response-statusSummaryByRegion"></a>
The status of the action by Region.
Type: String to [EventRuleStatusSummary](API_EventRuleStatusSummary.md) object map
Key Length Constraints: Minimum length of 2. Maximum length of 25.
Key Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`

## Errors
<a name="API_UpdateEventRule_Errors"></a>

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
<a name="API_UpdateEventRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/notifications-2018-05-10/UpdateEventRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/notifications-2018-05-10/UpdateEventRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/UpdateEventRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/notifications-2018-05-10/UpdateEventRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/UpdateEventRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/notifications-2018-05-10/UpdateEventRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/notifications-2018-05-10/UpdateEventRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/notifications-2018-05-10/UpdateEventRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/notifications-2018-05-10/UpdateEventRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/UpdateEventRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
