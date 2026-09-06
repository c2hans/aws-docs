---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_GetWorkflowExecutionHistory.html
---

# GetWorkflowExecutionHistory
<a name="API_GetWorkflowExecutionHistory"></a>

Returns the history of the specified workflow execution. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the `nextPageToken` returned by the initial call.

**Note**
This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.

 **Access Control**

You can use IAM policies to control this action's access to Amazon SWF resources as follows:
+ Use a `Resource` element with the domain name to limit the action to only specified domains.
+ Use an `Action` element to allow or deny permission to call this action.
+ You cannot use an IAM policy to constrain this action's parameters.

If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's `cause` parameter is set to `OPERATION_NOT_PERMITTED`. For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide*.

## Request Syntax
<a name="API_GetWorkflowExecutionHistory_RequestSyntax"></a>

```
{
   "domain": "{{string}}",
   "execution": {
      "runId": "{{string}}",
      "workflowId": "{{string}}"
   },
   "maximumPageSize": {{number}},
   "nextPageToken": "{{string}}",
   "reverseOrder": {{boolean}}
}
```

## Request Parameters
<a name="API_GetWorkflowExecutionHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [domain](#API_GetWorkflowExecutionHistory_RequestSyntax) **   <a name="SWF-GetWorkflowExecutionHistory-request-domain"></a>
The name of the domain containing the workflow execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [execution](#API_GetWorkflowExecutionHistory_RequestSyntax) **   <a name="SWF-GetWorkflowExecutionHistory-request-execution"></a>
Specifies the workflow execution for which to return the history.
Type: [WorkflowExecution](API_WorkflowExecution.md) object
Required: Yes

 ** [maximumPageSize](#API_GetWorkflowExecutionHistory_RequestSyntax) **   <a name="SWF-GetWorkflowExecutionHistory-request-maximumPageSize"></a>
The maximum number of results that are returned per call. Use `nextPageToken` to obtain further pages of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextPageToken](#API_GetWorkflowExecutionHistory_RequestSyntax) **   <a name="SWF-GetWorkflowExecutionHistory-request-nextPageToken"></a>
If `NextPageToken` is returned there are more results available. The value of `NextPageToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a `400` error: "`Specified token has exceeded its maximum lifetime`".
The configured `maximumPageSize` determines how many results can be returned in a single call.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [reverseOrder](#API_GetWorkflowExecutionHistory_RequestSyntax) **   <a name="SWF-GetWorkflowExecutionHistory-request-reverseOrder"></a>
When set to `true`, returns the events in reverse order. By default the results are returned in ascending order of the `eventTimeStamp` of the events.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetWorkflowExecutionHistory_ResponseSyntax"></a>

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
   "nextPageToken": "string"
}
```

## Response Elements
<a name="API_GetWorkflowExecutionHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_GetWorkflowExecutionHistory_ResponseSyntax) **   <a name="SWF-GetWorkflowExecutionHistory-response-events"></a>
The list of history events.
Type: Array of [HistoryEvent](API_HistoryEvent.md) objects

 ** [nextPageToken](#API_GetWorkflowExecutionHistory_ResponseSyntax) **   <a name="SWF-GetWorkflowExecutionHistory-response-nextPageToken"></a>
If a `NextPageToken` was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in `nextPageToken`. Keep all other arguments unchanged.
The configured `maximumPageSize` determines how many results can be returned in a single call.
Type: String
Length Constraints: Maximum length of 2048.

## Errors
<a name="API_GetWorkflowExecutionHistory_Errors"></a>

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
<a name="API_GetWorkflowExecutionHistory_Examples"></a>

### GetWorkflowExecutionHistory Example
<a name="API_GetWorkflowExecutionHistory_Example_1"></a>

This example illustrates one usage of GetWorkflowExecutionHistory.

#### Sample Request
<a name="API_GetWorkflowExecutionHistory_Example_1_Request"></a>

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
X-Amz-Date: Mon, 16 Jan 2012 03:44:00 GMT
X-Amz-Target: SimpleWorkflowService.GetWorkflowExecutionHistory
Content-Encoding: amz-1.0
X-Amzn-Authorization: AWS3 AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE,Algorithm=HmacSHA256,SignedHeaders=Host;X-Amz-Date;X-Amz-Target;Content-Encoding,Signature=90GENeUWJbEAMWuVI0dcWatHjltMWddXfLjl0MbNOzM=
Referer: http://swf.us-east-1.amazonaws.com/explorer/index.html
Content-Length: 175
Pragma: no-cache
Cache-Control: no-cache

{
  "maximumPageSize": 10,
  "domain": "867530901",
  "execution": {
  "workflowId": "20110927-T-1",
  "runId": "d29e60b5-fa71-4276-a4be-948b0adcd20b"
  },
  "reverseOrder": true
}
```

#### Sample Response
<a name="API_GetWorkflowExecutionHistory_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Length: 2942
Content-Type: application/json
x-amzn-RequestId: 5385723f-3ff4-11e1-b118-3bfa5e8e7fc3

{
  "nextPageToken": "AAAAKgAAAAEAAAAAAAAAATeTvAyvqlQz34ctbGhM5nglWmjzk0hGuHf0g4EO4CblQFku70ukjPgrAHy7Tnp7FaZ0okP8EEWnkfg8gi3Fqy/WVrXyxQaa525D31cIq1owXK21CKR6SQ0Job87G8SHvvqvP7yjLGHlHrRGZUCbJgeEuV4Rp/yW+vKhc8dJ54x7wvpQMwZ+ssG6stTyX26vu1gIDuspk13UrDZa4TbLOFdM0aAocHe3xklKMtD/B4ithem6BWm6CBl/UF7lMfNccwUYEityp1Kht/YrcD9zbJkt1FSt4Y6pgt0njAh4FKRO9nyRyvLmbvgtQXEIQz8hdbjwj3xE1+9ocYwXOCAhVkRsh3OD6F8KHilKfdwg4Xz1jtLXOh4lsCecNb8dS7J9hbRErRbw3rh1Sv415U2Ye23OEfF4Jv7JznpmEyzuq8d2bMyOLjAInQVFK4t1tPo5FAhzdICCXBhRq6Wkt++W9sRQXqqX/HTX5kNomHySZloylPuY5gL5zRj39frInfZk4EXWHwrI+18+erGIHO4nBQpMzO64dMP+A/KtVGCn59rAMmilD6wEE9rH8RuZ03Wkvm9yrJvjrI8/6358n8TMB8OcHoqILkMCAXYiIppnFlm+NWXVqxalHLKOrrNzEZM6qsz3Qj3HV1cpy9P7fnS9QAxrgsAYBoDmdOaFkS3ktAkRa0Sle8STfHi4zKbfIGS7rg==",
  "events": [
  {
    "eventId": 11,
    "eventType": "WorkflowExecutionTimedOut",
    "eventTimestamp": 1326671603.102,
    "workflowExecutionTimedOutEventAttributes": {
    "timeoutType": "START_TO_CLOSE",
    "childPolicy": "TERMINATE"
    }
  },
  {
    "eventId": 10,
    "eventType": "DecisionTaskScheduled",
    "decisionTaskScheduledEventAttributes": {
    "startToCloseTimeout": "600",
    "taskList": {
      "name": "specialTaskList"
    }
    },
    "eventTimestamp": 1326670566.124
  },
  {
    "eventId": 9,
    "eventType": "ActivityTaskTimedOut",
    "activityTaskTimedOutEventAttributes": {
    "startedEventId": 0,
    "scheduledEventId": 8,
    "timeoutType": "SCHEDULE_TO_START",
    },
    "eventTimestamp": 1326670566.124
  },
  {
    "activityTaskScheduledEventAttributes": {
    "activityId": "verification-27",
    "activityType": {
      "version": "1.0",
      "name": "activityVerify"
    },
    "control": "digital music",
    "decisionTaskCompletedEventId": 7,
    "heartbeatTimeout": "120",
    "input": "5634-0056-4367-0923,12/12,437",
    "scheduleToStartTimeout": "300",
    "scheduleToCloseTimeout": "900",
    "startToCloseTimeout": "600",
    "taskList": {
      "name": "specialTaskList"
    },
    "taskPriority": "50"
    },
    "eventId": 8,
    "eventTimestamp": 1326670266.115,
    "eventType": "ActivityTaskScheduled"
  },
  {
    "eventId": 7,
    "eventType": "DecisionTaskCompleted",
    "decisionTaskCompletedEventAttributes": {
    "startedEventId": 6,
    "executionContext": "Black Friday",
    "scheduledEventId": 5
    },
    "eventTimestamp": 1326670266.103
  },
  {
    "eventId": 6,
    "decisionTaskStartedEventAttributes": {
    "scheduledEventId": 5,
    "identity": "Decider01"
    },
    "eventTimestamp": 1326670161.497,
    "eventType": "DecisionTaskStarted"
  },
  {
    "eventId": 5,
    "eventType": "DecisionTaskScheduled",
    "decisionTaskScheduledEventAttributes": {
    "startToCloseTimeout": "600",
    "taskList": {
      "name": "specialTaskList"
    }
    },
    "eventTimestamp": 1326668752.66
  },
  {
    "eventId": 4,
    "eventType": "DecisionTaskTimedOut",
    "eventTimestamp": 1326668752.66,
    "decisionTaskTimedOutEventAttributes": {
    "startedEventId": 3,
    "timeoutType": "START_TO_CLOSE",
    "scheduledEventId": 2
    }
  },
  {
    "eventId": 3,
    "decisionTaskStartedEventAttributes": {
    "scheduledEventId": 2,
    "identity": "Decider01"
    },
    "eventTimestamp": 1326668152.648,
    "eventType": "DecisionTaskStarted"
  },
  {
    "eventId": 2,
    "eventType": "DecisionTaskScheduled",
    "decisionTaskScheduledEventAttributes": {
    "startToCloseTimeout": "600",
    "taskList": {
      "name": "specialTaskList"
    }
    },
    "eventTimestamp": 1326668003.094
  }
  ]
}
```

## See Also
<a name="API_GetWorkflowExecutionHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/swf-2012-01-25/GetWorkflowExecutionHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/swf-2012-01-25/GetWorkflowExecutionHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/GetWorkflowExecutionHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/swf-2012-01-25/GetWorkflowExecutionHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/GetWorkflowExecutionHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/swf-2012-01-25/GetWorkflowExecutionHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/swf-2012-01-25/GetWorkflowExecutionHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/swf-2012-01-25/GetWorkflowExecutionHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/swf-2012-01-25/GetWorkflowExecutionHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/GetWorkflowExecutionHistory)
