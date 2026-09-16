---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchGetServiceLevelObjectiveBudgetReport.html
---

# BatchGetServiceLevelObjectiveBudgetReport
<a name="API_BatchGetServiceLevelObjectiveBudgetReport"></a>

Use this operation to retrieve one or more *service level objective (SLO) budget reports*.

An *error budget* is the amount of time or requests in an unhealthy state that your service can accumulate during an interval before your overall SLO budget health is breached and the SLO is considered to be unmet. For example, an SLO with a threshold of 99.95% and a monthly interval translates to an error budget of 21.9 minutes of downtime in a 30-day month.

Budget reports include a health indicator, the attainment value, and remaining budget.

For more information about SLO error budgets, see [ SLO concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html#CloudWatch-ServiceLevelObjectives-concepts).

## Request Syntax
<a name="API_BatchGetServiceLevelObjectiveBudgetReport_RequestSyntax"></a>

```
POST /budget-report HTTP/1.1
Content-type: application/json

{
   "SloIds": [ "{{string}}" ],
   "Timestamp": {{number}}
}
```

## URI Request Parameters
<a name="API_BatchGetServiceLevelObjectiveBudgetReport_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetServiceLevelObjectiveBudgetReport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SloIds](#API_BatchGetServiceLevelObjectiveBudgetReport_RequestSyntax) **   <a name="applicationsignals-BatchGetServiceLevelObjectiveBudgetReport-request-SloIds"></a>
An array containing the IDs of the service level objectives that you want to include in the report.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

 ** [Timestamp](#API_BatchGetServiceLevelObjectiveBudgetReport_RequestSyntax) **   <a name="applicationsignals-BatchGetServiceLevelObjectiveBudgetReport-request-Timestamp"></a>
The date and time that you want the report to be for. It is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_BatchGetServiceLevelObjectiveBudgetReport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "Arn": "string",
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "Name": "string"
      }
   ],
   "Reports": [
      {
         "Arn": "string",
         "Attainment": number,
         "BudgetRequestsRemaining": number,
         "BudgetSecondsRemaining": number,
         "BudgetStatus": "string",
         "EvaluationType": "string",
         "Goal": {
            "AttainmentGoal": number,
            "Interval": { ... },
            "WarningThreshold": number
         },
         "Name": "string",
         "RequestBasedSli": {
            "ComparisonOperator": "string",
            "MetricThreshold": number,
            "RequestBasedSliMetric": {
               "CompositeSliConfig": {
                  "Components": [
                     { ... }
                  ],
                  "SelectionConfig": {
                     "Pattern": "string",
                     "Type": "string"
                  }
               },
               "DependencyConfig": {
                  "DependencyKeyAttributes": {
                     "string" : "string"
                  },
                  "DependencyOperationName": "string"
               },
               "KeyAttributes": {
                  "string" : "string"
               },
               "MetricSource": {
                  "MetricSourceAttributes": {
                     "string" : "string"
                  },
                  "MetricSourceKeyAttributes": {
                     "string" : "string"
                  }
               },
               "MetricType": "string",
               "MonitoredRequestCountMetric": { ... },
               "OperationName": "string",
               "TotalRequestCountMetric": [
                  {
                     "AccountId": "string",
                     "Expression": "string",
                     "Id": "string",
                     "Label": "string",
                     "MetricStat": {
                        "Metric": {
                           "Dimensions": [
                              {
                                 "Name": "string",
                                 "Value": "string"
                              }
                           ],
                           "MetricName": "string",
                           "Namespace": "string"
                        },
                        "Period": number,
                        "Stat": "string",
                        "Unit": "string"
                     },
                     "Period": number,
                     "ReturnData": boolean
                  }
               ]
            }
         },
         "Sli": {
            "ComparisonOperator": "string",
            "MetricThreshold": number,
            "SliMetric": {
               "CompositeSliConfig": {
                  "Components": [
                     { ... }
                  ],
                  "SelectionConfig": {
                     "Pattern": "string",
                     "Type": "string"
                  }
               },
               "DependencyConfig": {
                  "DependencyKeyAttributes": {
                     "string" : "string"
                  },
                  "DependencyOperationName": "string"
               },
               "KeyAttributes": {
                  "string" : "string"
               },
               "MetricDataQueries": [
                  {
                     "AccountId": "string",
                     "Expression": "string",
                     "Id": "string",
                     "Label": "string",
                     "MetricStat": {
                        "Metric": {
                           "Dimensions": [
                              {
                                 "Name": "string",
                                 "Value": "string"
                              }
                           ],
                           "MetricName": "string",
                           "Namespace": "string"
                        },
                        "Period": number,
                        "Stat": "string",
                        "Unit": "string"
                     },
                     "Period": number,
                     "ReturnData": boolean
                  }
               ],
               "MetricSource": {
                  "MetricSourceAttributes": {
                     "string" : "string"
                  },
                  "MetricSourceKeyAttributes": {
                     "string" : "string"
                  }
               },
               "MetricType": "string",
               "OperationName": "string"
            }
         },
         "TotalBudgetRequests": number,
         "TotalBudgetSeconds": number
      }
   ],
   "Timestamp": number
}
```

## Response Elements
<a name="API_BatchGetServiceLevelObjectiveBudgetReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchGetServiceLevelObjectiveBudgetReport_ResponseSyntax) **   <a name="applicationsignals-BatchGetServiceLevelObjectiveBudgetReport-response-Errors"></a>
An array of structures, where each structure includes an error indicating that one of the requests in the array was not valid.
Type: Array of [ServiceLevelObjectiveBudgetReportError](API_ServiceLevelObjectiveBudgetReportError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [Reports](#API_BatchGetServiceLevelObjectiveBudgetReport_ResponseSyntax) **   <a name="applicationsignals-BatchGetServiceLevelObjectiveBudgetReport-response-Reports"></a>
An array of structures, where each structure is one budget report.
Type: Array of [ServiceLevelObjectiveBudgetReport](API_ServiceLevelObjectiveBudgetReport.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [Timestamp](#API_BatchGetServiceLevelObjectiveBudgetReport_ResponseSyntax) **   <a name="applicationsignals-BatchGetServiceLevelObjectiveBudgetReport-response-Timestamp"></a>
The date and time that the report is for. It is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.
Type: Timestamp

## Errors
<a name="API_BatchGetServiceLevelObjectiveBudgetReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetServiceLevelObjectiveBudgetReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/BatchGetServiceLevelObjectiveBudgetReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/BatchGetServiceLevelObjectiveBudgetReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/BatchGetServiceLevelObjectiveBudgetReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/BatchGetServiceLevelObjectiveBudgetReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/BatchGetServiceLevelObjectiveBudgetReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/BatchGetServiceLevelObjectiveBudgetReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/BatchGetServiceLevelObjectiveBudgetReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/BatchGetServiceLevelObjectiveBudgetReport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/BatchGetServiceLevelObjectiveBudgetReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/BatchGetServiceLevelObjectiveBudgetReport)
