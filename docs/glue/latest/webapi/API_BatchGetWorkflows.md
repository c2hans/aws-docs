---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetWorkflows.html
---

# BatchGetWorkflows
<a name="API_BatchGetWorkflows"></a>

Returns a list of resource metadata for a given list of workflow names. After calling the `ListWorkflows` operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that uses tags.

## Request Syntax
<a name="API_BatchGetWorkflows_RequestSyntax"></a>

```
{
   "IncludeGraph": {{boolean}},
   "Names": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetWorkflows_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IncludeGraph](#API_BatchGetWorkflows_RequestSyntax) **   <a name="Glue-BatchGetWorkflows-request-IncludeGraph"></a>
Specifies whether to include a graph when returning the workflow resource metadata.
Type: Boolean
Required: No

 ** [Names](#API_BatchGetWorkflows_RequestSyntax) **   <a name="Glue-BatchGetWorkflows-request-Names"></a>
A list of workflow names, which may be the names returned from the `ListWorkflows` operation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_BatchGetWorkflows_ResponseSyntax"></a>

```
{
   "MissingWorkflows": [ "string" ],
   "Workflows": [
      {
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
   ]
}
```

## Response Elements
<a name="API_BatchGetWorkflows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MissingWorkflows](#API_BatchGetWorkflows_ResponseSyntax) **   <a name="Glue-BatchGetWorkflows-response-MissingWorkflows"></a>
A list of names of workflows not found.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [Workflows](#API_BatchGetWorkflows_ResponseSyntax) **   <a name="Glue-BatchGetWorkflows-response-Workflows"></a>
A list of workflow resource metadata.
Type: Array of [Workflow](API_Workflow.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.

## Errors
<a name="API_BatchGetWorkflows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_BatchGetWorkflows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchGetWorkflows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchGetWorkflows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetWorkflows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchGetWorkflows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetWorkflows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchGetWorkflows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchGetWorkflows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchGetWorkflows)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchGetWorkflows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetWorkflows)
