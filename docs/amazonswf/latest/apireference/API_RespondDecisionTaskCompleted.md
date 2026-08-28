---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondDecisionTaskCompleted.html
---

# RespondDecisionTaskCompleted
<a name="API_RespondDecisionTaskCompleted"></a>

Used by deciders to tell the service that the [DecisionTask](API_DecisionTask.md) identified by the `taskToken` has successfully completed. The `decisions` argument specifies the list of decisions made while processing the task.

A `DecisionTaskCompleted` event is added to the workflow history. The `executionContext` specified is attached to the event in the workflow execution history.

 **Access Control**

If an IAM policy grants permission to use `RespondDecisionTaskCompleted`, it can express permissions for the list of decisions in the `decisions` parameter. Each of the decisions has one or more parameters, much like a regular API call. To allow for policies to be as readable as possible, you can express permissions on decisions as if they were actual API calls, including applying conditions to some parameters. For more information, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_RespondDecisionTaskCompleted_RequestSyntax"></a>

```
{
   "decisions": [
      {
         "cancelTimerDecisionAttributes": {
            "timerId": "{{string}}"
         },
         "cancelWorkflowExecutionDecisionAttributes": {
            "details": "{{string}}"
         },
         "completeWorkflowExecutionDecisionAttributes": {
            "result": "{{string}}"
         },
         "continueAsNewWorkflowExecutionDecisionAttributes": {
            "childPolicy": "{{string}}",
            "executionStartToCloseTimeout": "{{string}}",
            "input": "{{string}}",
            "lambdaRole": "{{string}}",
            "tagList": [ "{{string}}" ],
            "taskList": {
               "name": "{{string}}"
            },
            "taskPriority": "{{string}}",
            "taskStartToCloseTimeout": "{{string}}",
            "workflowTypeVersion": "{{string}}"
         },
         "decisionType": "{{string}}",
         "failWorkflowExecutionDecisionAttributes": {
            "details": "{{string}}",
            "reason": "{{string}}"
         },
         "recordMarkerDecisionAttributes": {
            "details": "{{string}}",
            "markerName": "{{string}}"
         },
         "requestCancelActivityTaskDecisionAttributes": {
            "activityId": "{{string}}"
         },
         "requestCancelExternalWorkflowExecutionDecisionAttributes": {
            "control": "{{string}}",
            "runId": "{{string}}",
            "workflowId": "{{string}}"
         },
         "scheduleActivityTaskDecisionAttributes": {
            "activityId": "{{string}}",
            "activityType": {
               "name": "{{string}}",
               "version": "{{string}}"
            },
            "control": "{{string}}",
            "heartbeatTimeout": "{{string}}",
            "input": "{{string}}",
            "scheduleToCloseTimeout": "{{string}}",
            "scheduleToStartTimeout": "{{string}}",
            "startToCloseTimeout": "{{string}}",
            "taskList": {
               "name": "{{string}}"
            },
            "taskPriority": "{{string}}"
         },
         "scheduleLambdaFunctionDecisionAttributes": {
            "control": "{{string}}",
            "id": "{{string}}",
            "input": "{{string}}",
            "name": "{{string}}",
            "startToCloseTimeout": "{{string}}"
         },
         "signalExternalWorkflowExecutionDecisionAttributes": {
            "control": "{{string}}",
            "input": "{{string}}",
            "runId": "{{string}}",
            "signalName": "{{string}}",
            "workflowId": "{{string}}"
         },
         "startChildWorkflowExecutionDecisionAttributes": {
            "childPolicy": "{{string}}",
            "control": "{{string}}",
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
         },
         "startTimerDecisionAttributes": {
            "control": "{{string}}",
            "startToFireTimeout": "{{string}}",
            "timerId": "{{string}}"
         }
      }
   ],
   "executionContext": "{{string}}",
   "taskList": {
      "name": "{{string}}"
   },
   "taskListScheduleToStartTimeout": "{{string}}",
   "taskToken": "{{string}}"
}
```

## Request Parameters
<a name="API_RespondDecisionTaskCompleted_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [decisions](#API_RespondDecisionTaskCompleted_RequestSyntax) **   <a name="SWF-RespondDecisionTaskCompleted-request-decisions"></a>
The list of decisions (possibly empty) made by the decider while processing this decision task. See the docs for the [Decision](API_Decision.md) structure for details.
Type: Array of [Decision](API_Decision.md) objects
Required: No

 ** [executionContext](#API_RespondDecisionTaskCompleted_RequestSyntax) **   <a name="SWF-RespondDecisionTaskCompleted-request-executionContext"></a>
User defined context to add to workflow execution.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** [taskList](#API_RespondDecisionTaskCompleted_RequestSyntax) **   <a name="SWF-RespondDecisionTaskCompleted-request-taskList"></a>
The task list to use for the future decision tasks of this workflow execution. This list overrides the original task list you specified while starting the workflow execution.
Type: [TaskList](API_TaskList.md) object
Required: No

 ** [taskListScheduleToStartTimeout](#API_RespondDecisionTaskCompleted_RequestSyntax) **   <a name="SWF-RespondDecisionTaskCompleted-request-taskListScheduleToStartTimeout"></a>
Specifies a timeout (in seconds) for the task list override. When this parameter is missing, the task list override is permanent. This parameter makes it possible to temporarily override the task list. If a decision task scheduled on the override task list is not started within the timeout, the decision task will time out. Amazon SWF will revert the override and schedule a new decision task to the original task list.
If a decision task scheduled on the override task list is started within the timeout, but not completed within the start-to-close timeout, Amazon SWF will also revert the override and schedule a new decision task to the original task list.
Type: String
Length Constraints: Maximum length of 8.
Required: No

 ** [taskToken](#API_RespondDecisionTaskCompleted_RequestSyntax) **   <a name="SWF-RespondDecisionTaskCompleted-request-taskToken"></a>
The `taskToken` from the [DecisionTask](API_DecisionTask.md).
 `taskToken` is generated by the service and should be treated as an opaque value. If the task is passed to another process, its `taskToken` must also be passed. This enables it to provide its progress and respond with results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Response Elements
<a name="API_RespondDecisionTaskCompleted_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RespondDecisionTaskCompleted_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedFault **
Returned when the caller doesn't have sufficient permissions to invoke the action.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

 ** UnknownResourceFault **
Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

## Examples
<a name="API_RespondDecisionTaskCompleted_Examples"></a>

### RespondDecisionTaskCompleted Example
<a name="API_RespondDecisionTaskCompleted_Example_1"></a>

This example illustrates one usage of RespondDecisionTaskCompleted.

#### Sample Request
<a name="API_RespondDecisionTaskCompleted_Example_1_Request"></a>

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
X-Amz-Date: Sun, 15 Jan 2012 23:31:06 GMT
X-Amz-Target: SimpleWorkflowService.RespondDecisionTaskCompleted
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=FL4ouCb8n6j5egcKOXoa+5Vctc8WmA91B2ekKnks2J8=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 1184
Pragma: no-cache
Cache-Control: no-cache

{
  "executionContext": "Black Friday",
  "decisions": [
  {
    "scheduleActivityTaskDecisionAttributes": {
    "control": "digital music",
    "taskList": {
      "name": "specialTaskList"
    },
    "scheduleToCloseTimeout": "900",
    "activityType": {
      "version": "1.0",
      "name": "activityVerify"
    },
    "heartbeatTimeout": "120",
    "activityId": "verification-27",
    "scheduleToStartTimeout": "300",
    "startToCloseTimeout": "600",
    "taskPriority": "100",
    "input": "5634-0056-4367-0923,12/12,437"
    },
    "decisionType": "ScheduleActivityTask"
  }
  ],
  "taskToken": "AAAAKgAAAAEAAAAAAAAAAQLPoqDSLcx4ksNCEQZCyEBqpKhE+FgFSOvHd9zlCROacKYHh640MkANx2y9YM3CQnec0kEb1oRvB6DxKesTY3U/UQhvBqPY7E4BYE6hkDj/NmSbt9EwEJ/a+WD+oc2sDNfeVz2x+6wjb5vQdFKwBoQ6MDWLFbAhcgK+ymoRjoBHrPsrNLX3IA6sQaPmQRZQs3FRZonoVzP6uXMCZPnCZQULFjU1kTM8VHzH7ywqWKVmmdvnqyREOCT9VqmYbhLntJXsDj+scAvuNy17MCX9M9AJ7V/5qrLCeYdWA4FBQgY4Ew6IC+dge/UZdVMmpW/uB7nvSk6owQIhapPh5pEUwwY/yNnoVLTiPOz9KzZlANyw7uDchBRLvUJORFtpP9ZQIouNP8QOvFWm7Idc50ahwGEdTCiG+KDXV8kAzx7wKHs7l1TXYkC15x0h3XPH0MdLeEjipv98EpZaMIVtgGSdRjluOjNWEL2zowZByitleI5bdvxZdgalAXXKEnbYE6/rfLGReAJKdh2n0dmTMI+tK7uuxIWX6F4ocqSI1Xb2x5zZ"
}
```

#### Sample Response
<a name="API_RespondDecisionTaskCompleted_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 0
Content-Type: application/json
x-amzn-RequestId: feef79b5-3fd0-11e1-9a27-0760db01a4a8
```

## See Also
<a name="API_RespondDecisionTaskCompleted_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/RespondDecisionTaskCompleted)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/RespondDecisionTaskCompleted)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/RespondDecisionTaskCompleted)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/RespondDecisionTaskCompleted)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/RespondDecisionTaskCompleted)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/RespondDecisionTaskCompleted)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/RespondDecisionTaskCompleted)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/RespondDecisionTaskCompleted)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/RespondDecisionTaskCompleted)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/RespondDecisionTaskCompleted)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
