---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_PollForDecisionTask.html
---

# PollForDecisionTask
<a name="API_PollForDecisionTask"></a>

Used by deciders to get a [DecisionTask](API_DecisionTask.md) from the specified decision `taskList`. A decision task may be returned for any open workflow execution that is using the specified task list. The task includes a paginated view of the history of the workflow execution. The decider should use the workflow type and the history to determine how to properly handle the task.

This action initiates a long poll, where the service holds the HTTP connection open and responds as soon a task becomes available. If no decision task is available in the specified task list before the timeout of 60 seconds expires, an empty result is returned. An empty result, in this context, means that a DecisionTask is returned, but that the value of taskToken is an empty string.

**Important**
Deciders should set their client side socket timeout to at least 70 seconds (10 seconds higher than the timeout).

**Important**
Because the number of workflow history events for a single workflow execution might be very large, the result returned might be split up across a number of pages. To retrieve subsequent pages, make additional calls to `PollForDecisionTask` using the `nextPageToken` returned by the initial call. Note that you do *not* call `GetWorkflowExecutionHistory` with this `nextPageToken`. Instead, call `PollForDecisionTask` again.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ Constrain the `taskList.name` parameter by using a `Condition` element with the `swf:taskList.name` key to allow the action to access only certain task lists.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_PollForDecisionTask_RequestSyntax"></a>

```
{
   "domain": "{{string}}",
   "identity": "{{string}}",
   "maximumPageSize": {{number}},
   "nextPageToken": "{{string}}",
   "reverseOrder": {{boolean}},
   "startAtPreviousStartedEvent": {{boolean}},
   "taskList": {
      "name": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_PollForDecisionTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [domain](#API_PollForDecisionTask_RequestSyntax) **   <a name="SWF-PollForDecisionTask-request-domain"></a>
The name of the domain containing the task lists to poll.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [identity](#API_PollForDecisionTask_RequestSyntax) **   <a name="SWF-PollForDecisionTask-request-identity"></a>
Identity of the decider making the request, which is recorded in the DecisionTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [maximumPageSize](#API_PollForDecisionTask_RequestSyntax) **   <a name="SWF-PollForDecisionTask-request-maximumPageSize"></a>
The maximum number of results that are returned per call. Use `nextPageToken` to obtain further pages of results.
This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextPageToken](#API_PollForDecisionTask_RequestSyntax) **   <a name="SWF-PollForDecisionTask-request-nextPageToken"></a>
If `NextPageToken` is returned there are more results available. The value of `NextPageToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a `400` error: "`Specified token has exceeded its maximum lifetime`".
The configured `maximumPageSize` determines how many results can be returned in a single call.
The `nextPageToken` returned by this action cannot be used with [GetWorkflowExecutionHistory](API_GetWorkflowExecutionHistory.md) to get the next page. You must call [PollForDecisionTask](#API_PollForDecisionTask) again (with the `nextPageToken`) to retrieve the next page of history records. Calling [PollForDecisionTask](#API_PollForDecisionTask) with a `nextPageToken` doesn't return a new decision task.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [reverseOrder](#API_PollForDecisionTask_RequestSyntax) **   <a name="SWF-PollForDecisionTask-request-reverseOrder"></a>
When set to `true`, returns the events in reverse order. By default the results are returned in ascending order of the `eventTimestamp` of the events.
Type: Boolean
Required: No

 ** [startAtPreviousStartedEvent](#API_PollForDecisionTask_RequestSyntax) **   <a name="SWF-PollForDecisionTask-request-startAtPreviousStartedEvent"></a>
When set to `true`, returns the events with `eventTimestamp` greater than or equal to `eventTimestamp` of the most recent `DecisionTaskStarted` event. By default, this parameter is set to `false`.
Type: Boolean
Required: No

 ** [taskList](#API_PollForDecisionTask_RequestSyntax) **   <a name="SWF-PollForDecisionTask-request-taskList"></a>
Specifies the task list to poll for decision tasks.
The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` \| `\u007f-\u009f`). Also, it must *not* be the literal string `arn`.
Type: [TaskList](API_TaskList.md) object
Required: Yes

## Response Syntax
<a name="API_PollForDecisionTask_ResponseSyntax"></a>

```
{
   "events": [
      {
         "activityTaskCanceledEventAttributes": {
            "details": "string",
            "latestCancelRequestedEventId": number,
            "scheduledEventId": number,
            "startedEventId": number
         },
         "activityTaskCancelRequestedEventAttributes": {
            "activityId": "string",
            "decisionTaskCompletedEventId": number
         },
         "activityTaskCompletedEventAttributes": {
            "result": "string",
            "scheduledEventId": number,
            "startedEventId": number
         },
         "activityTaskFailedEventAttributes": {
            "details": "string",
            "reason": "string",
            "scheduledEventId": number,
            "startedEventId": number
         },
         "activityTaskScheduledEventAttributes": {
            "activityId": "string",
            "activityType": {
               "name": "string",
               "version": "string"
            },
            "control": "string",
            "decisionTaskCompletedEventId": number,
            "heartbeatTimeout": "string",
            "input": "string",
            "scheduleToCloseTimeout": "string",
            "scheduleToStartTimeout": "string",
            "startToCloseTimeout": "string",
            "taskList": {
               "name": "string"
            },
            "taskPriority": "string"
         },
         "activityTaskStartedEventAttributes": {
            "identity": "string",
            "scheduledEventId": number
         },
         "activityTaskTimedOutEventAttributes": {
            "details": "string",
            "scheduledEventId": number,
            "startedEventId": number,
            "timeoutType": "string"
         },
         "cancelTimerFailedEventAttributes": {
            "cause": "string",
            "decisionTaskCompletedEventId": number,
            "timerId": "string"
         },
         "cancelWorkflowExecutionFailedEventAttributes": {
            "cause": "string",
            "decisionTaskCompletedEventId": number
         },
         "childWorkflowExecutionCanceledEventAttributes": {
            "details": "string",
            "initiatedEventId": number,
            "startedEventId": number,
            "workflowExecution": {
               "runId": "string",
               "workflowId": "string"
            },
            "workflowType": {
               "name": "string",
               "version": "string"
            }
         },
         "childWorkflowExecutionCompletedEventAttributes": {
            "initiatedEventId": number,
            "result": "string",
            "startedEventId": number,
            "workflowExecution": {
               "runId": "string",
               "workflowId": "string"
            },
            "workflowType": {
               "name": "string",
               "version": "string"
            }
         },
         "childWorkflowExecutionFailedEventAttributes": {
            "details": "string",
            "initiatedEventId": number,
            "reason": "string",
            "startedEventId": number,
            "workflowExecution": {
               "runId": "string",
               "workflowId": "string"
            },
            "workflowType": {
               "name": "string",
               "version": "string"
            }
         },
         "childWorkflowExecutionStartedEventAttributes": {
            "initiatedEventId": number,
            "workflowExecution": {
               "runId": "string",
               "workflowId": "string"
            },
            "workflowType": {
               "name": "string",
               "version": "string"
            }
         },
         "childWorkflowExecutionTerminatedEventAttributes": {
            "initiatedEventId": number,
            "startedEventId": number,
            "workflowExecution": {
               "runId": "string",
               "workflowId": "string"
            },
            "workflowType": {
               "name": "string",
               "version": "string"
            }
         },
         "childWorkflowExecutionTimedOutEventAttributes": {
            "initiatedEventId": number,
            "startedEventId": number,
            "timeoutType": "string",
            "workflowExecution": {
               "runId": "string",
               "workflowId": "string"
            },
            "workflowType": {
               "name": "string",
               "version": "string"
            }
         },
         "completeWorkflowExecutionFailedEventAttributes": {
            "cause": "string",
            "decisionTaskCompletedEventId": number
         },
         "continueAsNewWorkflowExecutionFailedEventAttributes": {
            "cause": "string",
            "decisionTaskCompletedEventId": number
         },
         "decisionTaskCompletedEventAttributes": {
            "executionContext": "string",
            "scheduledEventId": number,
            "startedEventId": number,
            "taskList": {
               "name": "string"
            },
            "taskListScheduleToStartTimeout": "string"
         },
         "decisionTaskScheduledEventAttributes": {
            "scheduleToStartTimeout": "string",
            "startToCloseTimeout": "string",
            "taskList": {
               "name": "string"
            },
            "taskPriority": "string"
         },
         "decisionTaskStartedEventAttributes": {
            "identity": "string",
            "scheduledEventId": number
         },
         "decisionTaskTimedOutEventAttributes": {
            "scheduledEventId": number,
            "startedEventId": number,
            "timeoutType": "string"
         },
         "eventId": number,
         "eventTimestamp": number,
         "eventType": "string",
         "externalWorkflowExecutionCancelRequestedEventAttributes": {
            "initiatedEventId": number,
            "workflowExecution": {
               "runId": "string",
               "workflowId": "string"
            }
         },
         "externalWorkflowExecutionSignaledEventAttributes": {
            "initiatedEventId": number,
            "workflowExecution": {
               "runId": "string",
               "workflowId": "string"
            }
         },
         "failWorkflowExecutionFailedEventAttributes": {
            "cause": "string",
            "decisionTaskCompletedEventId": number
         },
         "lambdaFunctionCompletedEventAttributes": {
            "result": "string",
            "scheduledEventId": number,
            "startedEventId": number
         },
         "lambdaFunctionFailedEventAttributes": {
            "details": "string",
            "reason": "string",
            "scheduledEventId": number,
            "startedEventId": number
         },
         "lambdaFunctionScheduledEventAttributes": {
            "control": "string",
            "decisionTaskCompletedEventId": number,
            "id": "string",
            "input": "string",
            "name": "string",
            "startToCloseTimeout": "string"
         },
         "lambdaFunctionStartedEventAttributes": {
            "scheduledEventId": number
         },
         "lambdaFunctionTimedOutEventAttributes": {
            "scheduledEventId": number,
            "startedEventId": number,
            "timeoutType": "string"
         },
         "markerRecordedEventAttributes": {
            "decisionTaskCompletedEventId": number,
            "details": "string",
            "markerName": "string"
         },
         "recordMarkerFailedEventAttributes": {
            "cause": "string",
            "decisionTaskCompletedEventId": number,
            "markerName": "string"
         },
         "requestCancelActivityTaskFailedEventAttributes": {
            "activityId": "string",
            "cause": "string",
            "decisionTaskCompletedEventId": number
         },
         "requestCancelExternalWorkflowExecutionFailedEventAttributes": {
            "cause": "string",
            "control": "string",
            "decisionTaskCompletedEventId": number,
            "initiatedEventId": number,
            "runId": "string",
            "workflowId": "string"
         },
         "requestCancelExternalWorkflowExecutionInitiatedEventAttributes": {
            "control": "string",
            "decisionTaskCompletedEventId": number,
            "runId": "string",
            "workflowId": "string"
         },
         "scheduleActivityTaskFailedEventAttributes": {
            "activityId": "string",
            "activityType": {
               "name": "string",
               "version": "string"
            },
            "cause": "string",
            "decisionTaskCompletedEventId": number
         },
         "scheduleLambdaFunctionFailedEventAttributes": {
            "cause": "string",
            "decisionTaskCompletedEventId": number,
            "id": "string",
            "name": "string"
         },
         "signalExternalWorkflowExecutionFailedEventAttributes": {
            "cause": "string",
            "control": "string",
            "decisionTaskCompletedEventId": number,
            "initiatedEventId": number,
            "runId": "string",
            "workflowId": "string"
         },
         "signalExternalWorkflowExecutionInitiatedEventAttributes": {
            "control": "string",
            "decisionTaskCompletedEventId": number,
            "input": "string",
            "runId": "string",
            "signalName": "string",
            "workflowId": "string"
         },
         "startChildWorkflowExecutionFailedEventAttributes": {
            "cause": "string",
            "control": "string",
            "decisionTaskCompletedEventId": number,
            "initiatedEventId": number,
            "workflowId": "string",
            "workflowType": {
               "name": "string",
               "version": "string"
            }
         },
         "startChildWorkflowExecutionInitiatedEventAttributes": {
            "childPolicy": "string",
            "control": "string",
            "decisionTaskCompletedEventId": number,
            "executionStartToCloseTimeout": "string",
            "input": "string",
            "lambdaRole": "string",
            "tagList": [ "string" ],
            "taskList": {
               "name": "string"
            },
            "taskPriority": "string",
            "taskStartToCloseTimeout": "string",
            "workflowId": "string",
            "workflowType": {
               "name": "string",
               "version": "string"
            }
         },
         "startLambdaFunctionFailedEventAttributes": {
            "cause": "string",
            "message": "string",
            "scheduledEventId": number
         },
         "startTimerFailedEventAttributes": {
            "cause": "string",
            "decisionTaskCompletedEventId": number,
            "timerId": "string"
         },
         "timerCanceledEventAttributes": {
            "decisionTaskCompletedEventId": number,
            "startedEventId": number,
            "timerId": "string"
         },
         "timerFiredEventAttributes": {
            "startedEventId": number,
            "timerId": "string"
         },
         "timerStartedEventAttributes": {
            "control": "string",
            "decisionTaskCompletedEventId": number,
            "startToFireTimeout": "string",
            "timerId": "string"
         },
         "workflowExecutionCanceledEventAttributes": {
            "decisionTaskCompletedEventId": number,
            "details": "string"
         },
         "workflowExecutionCancelRequestedEventAttributes": {
            "cause": "string",
            "externalInitiatedEventId": number,
            "externalWorkflowExecution": {
               "runId": "string",
               "workflowId": "string"
            }
         },
         "workflowExecutionCompletedEventAttributes": {
            "decisionTaskCompletedEventId": number,
            "result": "string"
         },
         "workflowExecutionContinuedAsNewEventAttributes": {
            "childPolicy": "string",
            "decisionTaskCompletedEventId": number,
            "executionStartToCloseTimeout": "string",
            "input": "string",
            "lambdaRole": "string",
            "newExecutionRunId": "string",
            "tagList": [ "string" ],
            "taskList": {
               "name": "string"
            },
            "taskPriority": "string",
            "taskStartToCloseTimeout": "string",
            "workflowType": {
               "name": "string",
               "version": "string"
            }
         },
         "workflowExecutionFailedEventAttributes": {
            "decisionTaskCompletedEventId": number,
            "details": "string",
            "reason": "string"
         },
         "workflowExecutionSignaledEventAttributes": {
            "externalInitiatedEventId": number,
            "externalWorkflowExecution": {
               "runId": "string",
               "workflowId": "string"
            },
            "input": "string",
            "signalName": "string"
         },
         "workflowExecutionStartedEventAttributes": {
            "childPolicy": "string",
            "continuedExecutionRunId": "string",
            "executionStartToCloseTimeout": "string",
            "input": "string",
            "lambdaRole": "string",
            "parentInitiatedEventId": number,
            "parentWorkflowExecution": {
               "runId": "string",
               "workflowId": "string"
            },
            "tagList": [ "string" ],
            "taskList": {
               "name": "string"
            },
            "taskPriority": "string",
            "taskStartToCloseTimeout": "string",
            "workflowType": {
               "name": "string",
               "version": "string"
            }
         },
         "workflowExecutionTerminatedEventAttributes": {
            "cause": "string",
            "childPolicy": "string",
            "details": "string",
            "reason": "string"
         },
         "workflowExecutionTimedOutEventAttributes": {
            "childPolicy": "string",
            "timeoutType": "string"
         }
      }
   ],
   "nextPageToken": "string",
   "previousStartedEventId": number,
   "startedEventId": number,
   "taskToken": "string",
   "workflowExecution": {
      "runId": "string",
      "workflowId": "string"
   },
   "workflowType": {
      "name": "string",
      "version": "string"
   }
}
```

## Response Elements
<a name="API_PollForDecisionTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_PollForDecisionTask_ResponseSyntax) **   <a name="SWF-PollForDecisionTask-response-events"></a>
A paginated list of history events of the workflow execution. The decider uses this during the processing of the decision task.
Type: Array of [HistoryEvent](API_HistoryEvent.md) objects

 ** [nextPageToken](#API_PollForDecisionTask_ResponseSyntax) **   <a name="SWF-PollForDecisionTask-response-nextPageToken"></a>
If a `NextPageToken` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in `nextPageToken`. Keep all other arguments unchanged.
The configured `maximumPageSize` determines how many results can be returned in a single call.
Type: String
Length Constraints: Maximum length of 2048.

 ** [previousStartedEventId](#API_PollForDecisionTask_ResponseSyntax) **   <a name="SWF-PollForDecisionTask-response-previousStartedEventId"></a>
The ID of the DecisionTaskStarted event of the previous decision task of this workflow execution that was processed by the decider. This can be used to determine the events in the history new since the last decision task received by the decider.
Type: Long

 ** [startedEventId](#API_PollForDecisionTask_ResponseSyntax) **   <a name="SWF-PollForDecisionTask-response-startedEventId"></a>
The ID of the `DecisionTaskStarted` event recorded in the history.
Type: Long

 ** [taskToken](#API_PollForDecisionTask_ResponseSyntax) **   <a name="SWF-PollForDecisionTask-response-taskToken"></a>
The opaque string used as a handle on the task. This token is used by workers to communicate progress and response information back to the system about the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [workflowExecution](#API_PollForDecisionTask_ResponseSyntax) **   <a name="SWF-PollForDecisionTask-response-workflowExecution"></a>
The workflow execution for which this decision task was created.
Type: [WorkflowExecution](API_WorkflowExecution.md) object

 ** [workflowType](#API_PollForDecisionTask_ResponseSyntax) **   <a name="SWF-PollForDecisionTask-response-workflowType"></a>
The type of the workflow execution for which this decision task was created.
Type: [WorkflowType](API_WorkflowType.md) object

## Errors
<a name="API_PollForDecisionTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** UnknownResourceFault **
Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.
 ** message **
A description that may help with diagnosing the cause of the fault.
HTTP Status Code: 400

## Examples
<a name="API_PollForDecisionTask_Examples"></a>

### PollForDecisionTask Example
<a name="API_PollForDecisionTask_Example_1"></a>

This example illustrates one usage of PollForDecisionTask.

#### Sample Request
<a name="API_PollForDecisionTask_Example_1_Request"></a>

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
X-Amz-Date: Sun, 15 Jan 2012 02:09:54 GMT
X-Amz-Target: SimpleWorkflowService.PollForDecisionTask
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=R3CJ2HMLSVpc2p6eafeztZCZWcgza+h61gSUuWx15gw=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 171
Pragma: no-cache
Cache-Control: no-cache

{
  "maximumPageSize": 50,
  "domain": "867530901",
  "taskList": {
  "name": "specialTaskList"
  },
  "reverseOrder": true,
  "identity": "Decider01"
}
```

#### Sample Response
<a name="API_PollForDecisionTask_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 1639
Content-Type: application/json
x-amzn-RequestId: 03db54cf-3f1e-11e1-b118-3bfa5e8e7fc3

{
  "previousStartedEventId": 0,
  "workflowExecution": {
  "workflowId": "20110927-T-1",
  "runId": "06b8f87a-24b3-40b6-9ceb-9676f28e9493"
  },
  "startedEventId": 3,
  "workflowType": {
  "version": "1.0",
  "name": "customerOrderWorkflow"
  },
  "events": [
  {
    "eventId": 3,
    "decisionTaskStartedEventAttributes": {
    "scheduledEventId": 2,
    "identity": "Decider01"
    },
    "eventTimestamp": 1326593394.566,
    "eventType": "DecisionTaskStarted"
  },
  {
    "eventId": 2,
    "eventType": "DecisionTaskScheduled",
    "decisionTaskScheduledEventAttributes": {
    "startToCloseTimeout": "600",
    "taskList": {
      "name": "specialTaskList"
    },
    "taskPriority": "100"
    },
    "eventTimestamp": 1326592619.474
  },
  {
    "eventId": 1,
    "eventType": "WorkflowExecutionStarted",
    "workflowExecutionStartedEventAttributes": {
    "taskList": {
      "name": "specialTaskList"
    },
    "parentInitiatedEventId": 0,
    "taskStartToCloseTimeout": "600",
    "childPolicy": "TERMINATE",
    "executionStartToCloseTimeout": "3600",
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
    },
    "eventTimestamp": 1326592619.474
  }
  ],
  "taskToken": "AAAAKgAAAAEAAAAAAAAAATZDvCYwk/hP/X1ZGdJhb+T6OWzcBx2DPhsIi5HF4aGQI4OXrDE7Ny3uM+aiAhGrmeNyVAa4yNIBQuoZuJA5G+BoaB0JuHFBOynHDTnm7ayNH43KhMkfdrDG4elfHSz3m/EtbLnFGueAr7+3NKDG6x4sTKg3cZpOtSguSx05yI1X3AtscS8ATcLB2Y3Aub1YonN/i/k67voca/GFsSiwSz3AAnJj1IPvrujgIj9KUvckwRPC5ET7d33XJcRp+gHYzZsBLVBaRmV3gEYAnp2ICslFn4YSjGy+dFXCNpOa4G1O8pczCbFUGbQ3+5wf0RSaa/xMq2pfdBKnuFp0wp8kw1k+5ZsbtDZeZn8g5GyKCLiLms/xD0OxugGGUe5ZlAoHEkTWGxZj/G32P7cMoCgrcACfFPdx1LNYYEre7YiGiyjGnfW2t5mW7VK9Np28vcXVbdpH4JNEB9OuB1xqL8N8ifPVtc72uxB1i9XEdq/8rkXasSEw4TubB2FwgqnuJstmfEhpOdb5HfhR6OwmnHuk9eszO/fUkGucTUXQP2hhB+Gz"
}
```

## See Also
<a name="API_PollForDecisionTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/PollForDecisionTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/PollForDecisionTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/PollForDecisionTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/PollForDecisionTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/PollForDecisionTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/PollForDecisionTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/PollForDecisionTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/PollForDecisionTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/PollForDecisionTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/PollForDecisionTask)
