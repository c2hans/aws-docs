---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_CreateScheduleGroup.html
---

# CreateScheduleGroup
<a name="API_CreateScheduleGroup"></a>

Creates the specified schedule group.

## Request Syntax
<a name="API_CreateScheduleGroup_RequestSyntax"></a>

```
POST /schedule-groups/{{Name}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateScheduleGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_CreateScheduleGroup_RequestSyntax) **   <a name="scheduler-CreateScheduleGroup-request-uri-Name"></a>
The name of the schedule group that you are creating.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`
Required: Yes

## Request Body
<a name="API_CreateScheduleGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateScheduleGroup_RequestSyntax) **   <a name="scheduler-CreateScheduleGroup-request-ClientToken"></a>
 Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** [Tags](#API_CreateScheduleGroup_RequestSyntax) **   <a name="scheduler-CreateScheduleGroup-request-Tags"></a>
The list of tags to associate with the schedule group.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateScheduleGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ScheduleGroupArn": "string"
}
```

## Response Elements
<a name="API_CreateScheduleGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ScheduleGroupArn](#API_CreateScheduleGroup_ResponseSyntax) **   <a name="scheduler-CreateScheduleGroup-response-ScheduleGroupArn"></a>
The Amazon Resource Name (ARN) of the schedule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]+)?:scheduler:[a-z0-9\-]+:\d{12}:schedule-group\/[0-9a-zA-Z-_.]+`

## Errors
<a name="API_CreateScheduleGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting the resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error encountered while processing the request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateScheduleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/scheduler-2021-06-30/CreateScheduleGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/scheduler-2021-06-30/CreateScheduleGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/CreateScheduleGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/scheduler-2021-06-30/CreateScheduleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/CreateScheduleGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/scheduler-2021-06-30/CreateScheduleGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/scheduler-2021-06-30/CreateScheduleGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/scheduler-2021-06-30/CreateScheduleGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/scheduler-2021-06-30/CreateScheduleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/CreateScheduleGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EventBridge Scheduler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query scheduler` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
