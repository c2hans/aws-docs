---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_StartAuditMitigationActionsTask.html
---

# StartAuditMitigationActionsTask
<a name="API_StartAuditMitigationActionsTask"></a>

Starts a task that applies a set of mitigation actions to the specified target.

Requires permission to access the [StartAuditMitigationActionsTask](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_StartAuditMitigationActionsTask_RequestSyntax"></a>

```
POST /audit/mitigationactions/tasks/{{taskId}} HTTP/1.1
Content-type: application/json

{
   "auditCheckToActionsMapping": {
      "{{string}}" : [ "{{string}}" ]
   },
   "clientRequestToken": "{{string}}",
   "target": {
      "auditCheckToReasonCodeFilter": {
         "{{string}}" : [ "{{string}}" ]
      },
      "auditTaskId": "{{string}}",
      "findingIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_StartAuditMitigationActionsTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [taskId](#API_StartAuditMitigationActionsTask_RequestSyntax) **   <a name="iot-StartAuditMitigationActionsTask-request-uri-taskId"></a>
A unique identifier for the task. You can use this identifier to check the status of the task or to cancel it.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_StartAuditMitigationActionsTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [auditCheckToActionsMapping](#API_StartAuditMitigationActionsTask_RequestSyntax) **   <a name="iot-StartAuditMitigationActionsTask-request-auditCheckToActionsMapping"></a>
For an audit check, specifies which mitigation actions to apply. Those actions must be defined in your AWS accounts.
Type: String to array of strings map
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [clientRequestToken](#API_StartAuditMitigationActionsTask_RequestSyntax) **   <a name="iot-StartAuditMitigationActionsTask-request-clientRequestToken"></a>
Each audit mitigation task must have a unique client request token. If you try to start a new task with the same token as a task that already exists, an exception occurs. If you omit this value, a unique client request token is generated automatically.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: Yes

 ** [target](#API_StartAuditMitigationActionsTask_RequestSyntax) **   <a name="iot-StartAuditMitigationActionsTask-request-target"></a>
Specifies the audit findings to which the mitigation actions are applied. You can apply them to a type of audit check, to all findings from an audit, or to a specific set of findings.
Type: [AuditMitigationActionsTaskTarget](API_AuditMitigationActionsTaskTarget.md) object
Required: Yes

## Response Syntax
<a name="API_StartAuditMitigationActionsTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "taskId": "string"
}
```

## Response Elements
<a name="API_StartAuditMitigationActionsTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [taskId](#API_StartAuditMitigationActionsTask_ResponseSyntax) **   <a name="iot-StartAuditMitigationActionsTask-response-taskId"></a>
The unique identifier for the audit mitigation task. This matches the `taskId` that you specified in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_StartAuditMitigationActionsTask_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** TaskAlreadyExistsException **
 This exception occurs if you attempt to start a task with the same task-id as an existing task but with a different clientRequestToken.
HTTP Status Code: 400

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_StartAuditMitigationActionsTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/StartAuditMitigationActionsTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/StartAuditMitigationActionsTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/StartAuditMitigationActionsTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/StartAuditMitigationActionsTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/StartAuditMitigationActionsTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/StartAuditMitigationActionsTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/StartAuditMitigationActionsTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/StartAuditMitigationActionsTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/StartAuditMitigationActionsTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/StartAuditMitigationActionsTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
