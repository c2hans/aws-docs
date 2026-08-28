---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html
---

# StartWorkflowExecution
<a name="API_StartWorkflowExecution"></a>

Starts an execution of the workflow type in the specified domain using the provided `workflowId` and input data.

This action returns the newly started workflow execution.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ Constrain the following parameters by using a `Condition` element with the appropriate keys.
  +  `tagList.member.0`: The key is `swf:tagList.member.0`.
  +  `tagList.member.1`: The key is `swf:tagList.member.1`.
  +  `tagList.member.2`: The key is `swf:tagList.member.2`.
  +  `tagList.member.3`: The key is `swf:tagList.member.3`.
  +  `tagList.member.4`: The key is `swf:tagList.member.4`.
  +  `taskList`: String constraint. The key is `swf:taskList.name`.
  +  `workflowType.name`: String constraint. The key is `swf:workflowType.name`.
  +  `workflowType.version`: String constraint. The key is `swf:workflowType.version`.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_StartWorkflowExecution_RequestSyntax"></a>

```
{
   "childPolicy": "{{string}}",
   "domain": "{{string}}",
   "executionStartToCloseTimeout": "{{string}}",
   "input": "{{string}}",
   "lambdaRole": "{{string}}",
   "tagList": [ "{{string}}" ],
   "taskList": {
      "name": "{{string}}"
   },
   "taskPriority": "{{string}}",
   "taskStartToCloseTimeout": "{{string}}",
   "workflowId": "{{string}}",
   "workflowType": {
      "name": "{{string}}",
      "version": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_StartWorkflowExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [childPolicy](#API_StartWorkflowExecution_RequestSyntax) **   <a name="SWF-StartWorkflowExecution-request-childPolicy"></a>
If set, specifies the policy to use for the child workflow executions of this workflow execution if it is terminated, by calling the [TerminateWorkflowExecution](API_TerminateWorkflowExecution.md) action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using [RegisterWorkflowType](API_RegisterWorkflowType.md).
The supported child policies are:
+  `TERMINATE` – The child executions are terminated.
+  `REQUEST_CANCEL` – A request to cancel is attempted for each child execution by recording a `WorkflowExecutionCancelRequested` event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.
+  `ABANDON` – No action is taken. The child executions continue to run.
A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.
Type: String
Valid Values: `TERMINATE | REQUEST_CANCEL | ABANDON`
Required: No

 ** [domain](#API_StartWorkflowExecution_RequestSyntax) **   <a name="SWF-StartWorkflowExecution-request-domain"></a>
The name of the domain in which the workflow execution is created.
The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` \| `\u007f-\u009f`). Also, it must *not* be the literal string `arn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [executionStartToCloseTimeout](#API_StartWorkflowExecution_RequestSyntax) **   <a name="SWF-StartWorkflowExecution-request-executionStartToCloseTimeout"></a>
The total duration for this workflow execution. This overrides the defaultExecutionStartToCloseTimeout specified when registering the workflow type.
The duration is specified in seconds; an integer greater than or equal to `0`. Exceeding this limit causes the workflow execution to time out. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of "NONE" for this timeout; there is a one-year max limit on the time that a workflow execution can run.
An execution start-to-close timeout must be specified either through this parameter or as a default when the workflow type is registered. If neither this parameter nor a default execution start-to-close timeout is specified, a fault is returned.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** [input](#API_StartWorkflowExecution_RequestSyntax) **   <a name="SWF-StartWorkflowExecution-request-input"></a>
The input for the workflow execution. This is a free form string which should be meaningful to the workflow you are starting. This `input` is made available to the new workflow execution in the `WorkflowExecutionStarted` history event.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** [lambdaRole](#API_StartWorkflowExecution_RequestSyntax) **   <a name="SWF-StartWorkflowExecution-request-lambdaRole"></a>
The IAM role to attach to this workflow execution.
Executions of this workflow type need IAM roles to invoke Lambda functions. If you don't attach an IAM role, any attempt to schedule a Lambda task fails. This results in a `ScheduleLambdaFunctionFailed` history event. For more information, see [https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html](https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html) in the *Amazon SWF Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** [tagList](#API_StartWorkflowExecution_RequestSyntax) **   <a name="SWF-StartWorkflowExecution-request-tagList"></a>
The list of tags to associate with the workflow execution. You can specify a maximum of 5 tags. You can list workflow executions with a specific tag by calling [ListOpenWorkflowExecutions](API_ListOpenWorkflowExecutions.md) or [ListClosedWorkflowExecutions](API_ListClosedWorkflowExecutions.md) and specifying a [TagFilter](API_TagFilter.md).
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [taskList](#API_StartWorkflowExecution_RequestSyntax) **   <a name="SWF-StartWorkflowExecution-request-taskList"></a>
The task list to use for the decision tasks generated for this workflow execution. This overrides the `defaultTaskList` specified when registering the workflow type.
A task list for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task list was specified at registration time then a fault is returned.
The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` \| `\u007f-\u009f`). Also, it must *not* be the literal string `arn`.
Type: [TaskList](API_TaskList.md) object
Required: No

 ** [taskPriority](#API_StartWorkflowExecution_RequestSyntax) **   <a name="SWF-StartWorkflowExecution-request-taskPriority"></a>
The task priority to use for this workflow execution. This overrides any default priority that was assigned when the workflow type was registered. If not set, then the default task priority for the workflow type is used. Valid values are integers that range from Java's `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.
For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide*.
Type: String
Required: No

 ** [taskStartToCloseTimeout](#API_StartWorkflowExecution_RequestSyntax) **   <a name="SWF-StartWorkflowExecution-request-taskStartToCloseTimeout"></a>
Specifies the maximum duration of decision tasks for this workflow execution. This parameter overrides the `defaultTaskStartToCloseTimout` specified when registering the workflow type using [RegisterWorkflowType](API_RegisterWorkflowType.md).
The duration is specified in seconds, an integer greater than or equal to `0`. You can use `NONE` to specify unlimited duration.
A task start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault is returned.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** [workflowId](#API_StartWorkflowExecution_RequestSyntax) **   <a name="SWF-StartWorkflowExecution-request-workflowId"></a>
The user defined identifier associated with the workflow execution. You can use this to associate a custom identifier with the workflow execution. You may specify the same identifier if a workflow execution is logically a *restart* of a previous execution. You cannot have two open workflow executions with the same `workflowId` at the same time within the same domain.
The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` \| `\u007f-\u009f`). Also, it must *not* be the literal string `arn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [workflowType](#API_StartWorkflowExecution_RequestSyntax) **   <a name="SWF-StartWorkflowExecution-request-workflowType"></a>
The type of the workflow to start.
Type: [WorkflowType](API_WorkflowType.md) object
Required: Yes

## Response Syntax
<a name="API_StartWorkflowExecution_ResponseSyntax"></a>

```
{
   "runId": "string"
}
```

## Response Elements
<a name="API_StartWorkflowExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [runId](#API_StartWorkflowExecution_ResponseSyntax) **   <a name="SWF-StartWorkflowExecution-response-runId"></a>
The `runId` of a workflow execution. This ID is generated by the service and can be used to uniquely identify the workflow execution within a domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

## Errors
<a name="API_StartWorkflowExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DefaultUndefinedFault **
The `StartWorkflowExecution` API action was called without the required parameters set.
Some workflow execution parameters, such as the decision `taskList`, must be set to start the execution. However, these parameters might have been set as defaults when the workflow type was registered. In this case, you can omit these parameters from the `StartWorkflowExecution` call and Amazon SWF uses the values defined in the workflow type.
If these parameters aren't set and no default parameters were defined in the workflow type, this error is displayed.
HTTP Status Code: 400

 ** LimitExceededFault **
Returned by any operation if a system imposed limitation has been reached. To address this fault you should either clean up unused resources or increase the limit by contacting AWS.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** OperationNotPermittedFault **
Returned when the caller doesn't have sufficient permissions to invoke the action.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** TypeDeprecatedFault **
Returned when the specified activity or workflow type was already deprecated.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** UnknownResourceFault **
Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** WorkflowExecutionAlreadyStartedFault **
Returned by [StartWorkflowExecution](#API_StartWorkflowExecution) when an open execution with the same workflowId is already running in the specified domain.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

## Examples
<a name="API_StartWorkflowExecution_Examples"></a>

### StartWorkflowExecution Example
<a name="API_StartWorkflowExecution_Example_1"></a>

This example illustrates one usage of StartWorkflowExecution.

#### Sample Request
<a name="API_StartWorkflowExecution_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: swf.us-east-1.amazonaws.com
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.25) Gecko/20111212 Firefox/3.6.25 ( .NET CLR 3.5.30729; .NET4.0E)
Accept: application/json, text/javascript, */*
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive
Content-Type: application/x-amz-json-1.0
X-Requested-With: XMLHttpRequest
X-Amz-Date: Sat, 14 Jan 2012 22:45:13 GMT
X-Amz-Target: SimpleWorkflowService.StartWorkflowExecution
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=aYxuqLX+TO91kPVg+jh+aA8PWxQazQRN2+SZUGdOgU0=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 417
Pragma: no-cache
Cache-Control: no-cache

{
  "domain": "867530901",
  "taskList": {
  "name": "specialTaskList"
  },
  "taskPriority": "100",
  "taskStartToCloseTimeout": "600",
  "workflowId": "20110927-T-1",
  "childPolicy": "TERMINATE",
  "executionStartToCloseTimeout": "1800",
  "input": "arbitrary-string-that-is-meaningful-to-the-workflow",
  "workflowType": {
  "version": "1.0",
  "name": "customerOrderWorkflow"
  },
  "tagList": [
  "music purchase",
  "digital",
  "ricoh-the-dog"
  ]
}
```

#### Sample Response
<a name="API_StartWorkflowExecution_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 48
Content-Type: application/json
x-amzn-RequestId: 6c25f6e6-3f01-11e1-9a27-0760db01a4a8

{
  "runId": "1e536162-f1ea-48b0-85f3-aade88eef2f7"
}
```

## See Also
<a name="API_StartWorkflowExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/StartWorkflowExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/StartWorkflowExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/StartWorkflowExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/StartWorkflowExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/StartWorkflowExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/StartWorkflowExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/StartWorkflowExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/StartWorkflowExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/StartWorkflowExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/StartWorkflowExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
