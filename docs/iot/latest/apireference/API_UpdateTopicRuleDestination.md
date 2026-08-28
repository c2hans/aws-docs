---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateTopicRuleDestination.html
---

# UpdateTopicRuleDestination
<a name="API_UpdateTopicRuleDestination"></a>

Updates a topic rule destination. You use this to change the status, endpoint URL, or confirmation URL of the destination.

Requires permission to access the [UpdateTopicRuleDestination](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateTopicRuleDestination_RequestSyntax"></a>

```
PATCH /destinations HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateTopicRuleDestination_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateTopicRuleDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_UpdateTopicRuleDestination_RequestSyntax) **   <a name="iot-UpdateTopicRuleDestination-request-arn"></a>
The ARN of the topic rule destination.
Type: String
Required: Yes

 ** [status](#API_UpdateTopicRuleDestination_RequestSyntax) **   <a name="iot-UpdateTopicRuleDestination-request-status"></a>
The status of the topic rule destination. Valid values are:
IN\_PROGRESS
A topic rule destination was created but has not been confirmed. You can set `status` to `IN_PROGRESS` by calling `UpdateTopicRuleDestination`. Calling `UpdateTopicRuleDestination` causes a new confirmation challenge to be sent to your confirmation endpoint.
ENABLED
Confirmation was completed, and traffic to this destination is allowed. You can set `status` to `DISABLED` by calling `UpdateTopicRuleDestination`.
DISABLED
Confirmation was completed, and traffic to this destination is not allowed. You can set `status` to `ENABLED` by calling `UpdateTopicRuleDestination`.
ERROR
Confirmation could not be completed, for example if the confirmation timed out. You can call `GetTopicRuleDestination` for details about the error. You can set `status` to `IN_PROGRESS` by calling `UpdateTopicRuleDestination`. Calling `UpdateTopicRuleDestination` causes a new confirmation challenge to be sent to your confirmation endpoint.
Type: String
Valid Values: `ENABLED | IN_PROGRESS | DISABLED | ERROR | DELETING`
Required: Yes

## Response Syntax
<a name="API_UpdateTopicRuleDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateTopicRuleDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateTopicRuleDestination_Errors"></a>

 ** ConflictingResourceUpdateException **
A conflicting resource update exception. This exception is thrown when two pending updates cause a conflict.
 ** message **
The message for the exception.
HTTP Status Code: 409

 ** InternalException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_UpdateTopicRuleDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateTopicRuleDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateTopicRuleDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateTopicRuleDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateTopicRuleDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateTopicRuleDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateTopicRuleDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateTopicRuleDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateTopicRuleDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateTopicRuleDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateTopicRuleDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
