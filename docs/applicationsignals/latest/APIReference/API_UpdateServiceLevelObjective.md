---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UpdateServiceLevelObjective.html
---

# UpdateServiceLevelObjective
<a name="API_UpdateServiceLevelObjective"></a>

Updates an existing service level objective (SLO). If you omit parameters, the previous values of those parameters are retained.

You cannot change from a period-based SLO to a request-based SLO, or change from a request-based SLO to a period-based SLO.

## Request Syntax
<a name="API_UpdateServiceLevelObjective_RequestSyntax"></a>

```
PATCH /slo/{{Id}} HTTP/1.1
Content-type: application/json

{
   "BurnRateConfigurations": [
      {
         "LookBackWindowMinutes": {{number}}
      }
   ],
   "Description": "{{string}}",
   "Goal": {
      "AttainmentGoal": {{number}},
      "Interval": { ... },
      "WarningThreshold": {{number}}
   },
   "RequestBasedSliConfig": {
      "ComparisonOperator": "{{string}}",
      "MetricThreshold": {{number}},
      "RequestBasedSliMetricConfig": {
         "CompositeSliConfig": {
            "Components": [
               { ... }
            ],
            "SelectionConfig": {
               "Pattern": "{{string}}",
               "Type": "{{string}}"
            }
         },
         "DependencyConfig": {
            "DependencyKeyAttributes": {
               "{{string}}" : "{{string}}"
            },
            "DependencyOperationName": "{{string}}"
         },
         "KeyAttributes": {
            "{{string}}" : "{{string}}"
         },
         "MetricName": "{{string}}",
         "MetricSource": {
            "MetricSourceAttributes": {
               "{{string}}" : "{{string}}"
            },
            "MetricSourceKeyAttributes": {
               "{{string}}" : "{{string}}"
            }
         },
         "MetricType": "{{string}}",
         "MonitoredRequestCountMetric": { ... },
         "OperationName": "{{string}}",
         "TotalRequestCountMetric": [
            {
               "AccountId": "{{string}}",
               "Expression": "{{string}}",
               "Id": "{{string}}",
               "Label": "{{string}}",
               "MetricStat": {
                  "Metric": {
                     "Dimensions": [
                        {
                           "Name": "{{string}}",
                           "Value": "{{string}}"
                        }
                     ],
                     "MetricName": "{{string}}",
                     "Namespace": "{{string}}"
                  },
                  "Period": {{number}},
                  "Stat": "{{string}}",
                  "Unit": "{{string}}"
               },
               "Period": {{number}},
               "ReturnData": {{boolean}}
            }
         ]
      }
   },
   "SliConfig": {
      "ComparisonOperator": "{{string}}",
      "MetricThreshold": {{number}},
      "SliMetricConfig": {
         "CompositeSliConfig": {
            "Components": [
               { ... }
            ],
            "SelectionConfig": {
               "Pattern": "{{string}}",
               "Type": "{{string}}"
            }
         },
         "DependencyConfig": {
            "DependencyKeyAttributes": {
               "{{string}}" : "{{string}}"
            },
            "DependencyOperationName": "{{string}}"
         },
         "KeyAttributes": {
            "{{string}}" : "{{string}}"
         },
         "MetricDataQueries": [
            {
               "AccountId": "{{string}}",
               "Expression": "{{string}}",
               "Id": "{{string}}",
               "Label": "{{string}}",
               "MetricStat": {
                  "Metric": {
                     "Dimensions": [
                        {
                           "Name": "{{string}}",
                           "Value": "{{string}}"
                        }
                     ],
                     "MetricName": "{{string}}",
                     "Namespace": "{{string}}"
                  },
                  "Period": {{number}},
                  "Stat": "{{string}}",
                  "Unit": "{{string}}"
               },
               "Period": {{number}},
               "ReturnData": {{boolean}}
            }
         ],
         "MetricName": "{{string}}",
         "MetricSource": {
            "MetricSourceAttributes": {
               "{{string}}" : "{{string}}"
            },
            "MetricSourceKeyAttributes": {
               "{{string}}" : "{{string}}"
            }
         },
         "MetricType": "{{string}}",
         "OperationName": "{{string}}",
         "PeriodSeconds": {{number}},
         "Statistic": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateServiceLevelObjective_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-UpdateServiceLevelObjective-request-uri-Id"></a>
The Amazon Resource Name (ARN) or name of the service level objective that you want to update.
Pattern: `[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]$|^arn:(aws|aws-us-gov):application-signals:[^:]*:[^:]*:slo/[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
Required: Yes

## Request Body
<a name="API_UpdateServiceLevelObjective_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BurnRateConfigurations](#API_UpdateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-UpdateServiceLevelObjective-request-BurnRateConfigurations"></a>
Use this array to create *burn rates* for this SLO. Each burn rate is a metric that indicates how fast the service is consuming the error budget, relative to the attainment goal of the SLO.
Type: Array of [BurnRateConfiguration](API_BurnRateConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [Description](#API_UpdateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-UpdateServiceLevelObjective-request-Description"></a>
An optional description for the SLO.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [Goal](#API_UpdateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-UpdateServiceLevelObjective-request-Goal"></a>
A structure that contains the attributes that determine the goal of the SLO. This includes the time period for evaluation and the attainment threshold.
Type: [Goal](API_Goal.md) object
Required: No

 ** [RequestBasedSliConfig](#API_UpdateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-UpdateServiceLevelObjective-request-RequestBasedSliConfig"></a>
If this SLO is a request-based SLO, this structure defines the information about what performance metric this SLO will monitor.
You can't specify both `SliConfig` and `RequestBasedSliConfig` in the same operation.
Type: [RequestBasedServiceLevelIndicatorConfig](API_RequestBasedServiceLevelIndicatorConfig.md) object
Required: No

 ** [SliConfig](#API_UpdateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-UpdateServiceLevelObjective-request-SliConfig"></a>
If this SLO is a period-based SLO, this structure defines the information about what performance metric this SLO will monitor.
Type: [ServiceLevelIndicatorConfig](API_ServiceLevelIndicatorConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateServiceLevelObjective_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Slo": {
      "Arn": "string",
      "BurnRateConfigurations": [
         {
            "LookBackWindowMinutes": number
         }
      ],
      "CreatedTime": number,
      "Description": "string",
      "EvaluationType": "string",
      "Goal": {
         "AttainmentGoal": number,
         "Interval": { ... },
         "WarningThreshold": number
      },
      "LastUpdatedTime": number,
      "MetricSourceType": "string",
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
      }
   }
}
```

## Response Elements
<a name="API_UpdateServiceLevelObjective_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Slo](#API_UpdateServiceLevelObjective_ResponseSyntax) **   <a name="applicationsignals-UpdateServiceLevelObjective-response-Slo"></a>
A structure that contains information about the SLO that you just updated.
Type: [ServiceLevelObjective](API_ServiceLevelObjective.md) object

## Errors
<a name="API_UpdateServiceLevelObjective_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found.
 ** ResourceId **
Can't find the resource id.
 ** ResourceType **
The resource type is not valid.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateServiceLevelObjective_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/UpdateServiceLevelObjective)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/UpdateServiceLevelObjective)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/UpdateServiceLevelObjective)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/UpdateServiceLevelObjective)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/UpdateServiceLevelObjective)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/UpdateServiceLevelObjective)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/UpdateServiceLevelObjective)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/UpdateServiceLevelObjective)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/UpdateServiceLevelObjective)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/UpdateServiceLevelObjective)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
