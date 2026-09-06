---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetWorkflow.html
---

# GetWorkflow
<a name="API_GetWorkflow"></a>

Retrieves resource metadata for a workflow.

## Request Syntax
<a name="API_GetWorkflow_RequestSyntax"></a>

```
{
   "IncludeGraph": {{boolean}},
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetWorkflow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IncludeGraph](#API_GetWorkflow_RequestSyntax) **   <a name="Glue-GetWorkflow-request-IncludeGraph"></a>
Specifies whether to include a graph when returning the workflow resource metadata.
Type: Boolean
Required: No

 ** [Name](#API_GetWorkflow_RequestSyntax) **   <a name="Glue-GetWorkflow-request-Name"></a>
The name of the workflow to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetWorkflow_ResponseSyntax"></a>

```
{
   "Workflow": {
      "BlueprintDetails": {
         "BlueprintName": "string",
         "RunId": "string"
      },
      "CreatedOn": number,
      "DefaultRunProperties": {
         "string" : "string"
      },
      "Description": "string",
      "Graph": {
         "Edges": [
            {
               "DestinationId": "string",
               "SourceId": "string"
            }
         ],
         "Nodes": [
            {
               "CrawlerDetails": {
                  "Crawls": [
                     {
                        "CompletedOn": number,
                        "ErrorMessage": "string",
                        "LogGroup": "string",
                        "LogStream": "string",
                        "StartedOn": number,
                        "State": "string"
                     }
                  ]
               },
               "JobDetails": {
                  "JobRuns": [
                     {
                        "AllocatedCapacity": number,
                        "Arguments": {
                           "string" : "string"
                        },
                        "Attempt": number,
                        "CompletedOn": number,
                        "DPUSeconds": number,
                        "ErrorMessage": "string",
                        "ExecutionClass": "string",
                        "ExecutionRoleSessionPolicy": "string",
                        "ExecutionTime": number,
                        "GlueVersion": "string",
                        "Id": "string",
                        "JobMode": "string",
                        "JobName": "string",
                        "JobRunQueuingEnabled": boolean,
                        "JobRunState": "string",
                        "LastModifiedOn": number,
                        "LogGroupName": "string",
                        "MaintenanceWindow": "string",
                        "MaxCapacity": number,
                        "NotificationProperty": {
                           "NotifyDelayAfter": number
                        },
                        "NumberOfWorkers": number,
                        "PredecessorRuns": [
                           {
                              "JobName": "string",
                              "RunId": "string"
                           }
                        ],
                        "PreviousRunId": "string",
                        "ProfileName": "string",
                        "SecurityConfiguration": "string",
                        "StartedOn": number,
                        "StateDetail": "string",
                        "Timeout": number,
                        "TriggerName": "string",
                        "WorkerType": "string"
                     }
                  ]
               },
               "Name": "string",
               "TriggerDetails": {
                  "Trigger": {
                     "Actions": [
                        {
                           "Arguments": {
                              "string" : "string"
                           },
                           "CrawlerName": "string",
                           "JobName": "string",
                           "NotificationProperty": {
                              "NotifyDelayAfter": number
                           },
                           "SecurityConfiguration": "string",
                           "Timeout": number
                        }
                     ],
                     "Description": "string",
                     "EventBatchingCondition": {
                        "BatchSize": number,
                        "BatchWindow": number
                     },
                     "Id": "string",
                     "Name": "string",
                     "Predicate": {
                        "Conditions": [
                           {
                              "CrawlerName": "string",
                              "CrawlState": "string",
                              "JobName": "string",
                              "LogicalOperator": "string",
                              "State": "string"
                           }
                        ],
                        "Logical": "string"
                     },
                     "Schedule": "string",
                     "State": "string",
                     "Type": "string",
                     "WorkflowName": "string"
                  }
               },
               "Type": "string",
               "UniqueId": "string"
            }
         ]
      },
      "LastModifiedOn": number,
      "LastRun": {
         "CompletedOn": number,
         "ErrorMessage": "string",
         "Graph": {
            "Edges": [
               {
                  "DestinationId": "string",
                  "SourceId": "string"
               }
            ],
            "Nodes": [
               {
                  "CrawlerDetails": {
                     "Crawls": [
                        {
                           "CompletedOn": number,
                           "ErrorMessage": "string",
                           "LogGroup": "string",
                           "LogStream": "string",
                           "StartedOn": number,
                           "State": "string"
                        }
                     ]
                  },
                  "JobDetails": {
                     "JobRuns": [
                        {
                           "AllocatedCapacity": number,
                           "Arguments": {
                              "string" : "string"
                           },
                           "Attempt": number,
                           "CompletedOn": number,
                           "DPUSeconds": number,
                           "ErrorMessage": "string",
                           "ExecutionClass": "string",
                           "ExecutionRoleSessionPolicy": "string",
                           "ExecutionTime": number,
                           "GlueVersion": "string",
                           "Id": "string",
                           "JobMode": "string",
                           "JobName": "string",
                           "JobRunQueuingEnabled": boolean,
                           "JobRunState": "string",
                           "LastModifiedOn": number,
                           "LogGroupName": "string",
                           "MaintenanceWindow": "string",
                           "MaxCapacity": number,
                           "NotificationProperty": {
                              "NotifyDelayAfter": number
                           },
                           "NumberOfWorkers": number,
                           "PredecessorRuns": [
                              {
                                 "JobName": "string",
                                 "RunId": "string"
                              }
                           ],
                           "PreviousRunId": "string",
                           "ProfileName": "string",
                           "SecurityConfiguration": "string",
                           "StartedOn": number,
                           "StateDetail": "string",
                           "Timeout": number,
                           "TriggerName": "string",
                           "WorkerType": "string"
                        }
                     ]
                  },
                  "Name": "string",
                  "TriggerDetails": {
                     "Trigger": {
                        "Actions": [
                           {
                              "Arguments": {
                                 "string" : "string"
                              },
                              "CrawlerName": "string",
                              "JobName": "string",
                              "NotificationProperty": {
                                 "NotifyDelayAfter": number
                              },
                              "SecurityConfiguration": "string",
                              "Timeout": number
                           }
                        ],
                        "Description": "string",
                        "EventBatchingCondition": {
                           "BatchSize": number,
                           "BatchWindow": number
                        },
                        "Id": "string",
                        "Name": "string",
                        "Predicate": {
                           "Conditions": [
                              {
                                 "CrawlerName": "string",
                                 "CrawlState": "string",
                                 "JobName": "string",
                                 "LogicalOperator": "string",
                                 "State": "string"
                              }
                           ],
                           "Logical": "string"
                        },
                        "Schedule": "string",
                        "State": "string",
                        "Type": "string",
                        "WorkflowName": "string"
                     }
                  },
                  "Type": "string",
                  "UniqueId": "string"
               }
            ]
         },
         "Name": "string",
         "PreviousRunId": "string",
         "StartedOn": number,
         "StartingEventBatchCondition": {
            "BatchSize": number,
            "BatchWindow": number
         },
         "Statistics": {
            "ErroredActions": number,
            "FailedActions": number,
            "RunningActions": number,
            "StoppedActions": number,
            "SucceededActions": number,
            "TimeoutActions": number,
            "TotalActions": number,
            "WaitingActions": number
         },
         "Status": "string",
         "WorkflowRunId": "string",
         "WorkflowRunProperties": {
            "string" : "string"
         }
      },
      "MaxConcurrentRuns": number,
      "Name": "string"
   }
}
```

## Response Elements
<a name="API_GetWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Workflow](#API_GetWorkflow_ResponseSyntax) **   <a name="Glue-GetWorkflow-response-Workflow"></a>
The resource metadata for the workflow.
Type: [Workflow](API_Workflow.md) object

## Errors
<a name="API_GetWorkflow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetWorkflow)
