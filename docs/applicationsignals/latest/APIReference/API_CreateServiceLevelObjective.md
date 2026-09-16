---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CreateServiceLevelObjective.html
---

# CreateServiceLevelObjective
<a name="API_CreateServiceLevelObjective"></a>

Creates a service level objective (SLO), which can help you ensure that your critical business operations are meeting customer expectations. Use SLOs to set and track specific target levels for the reliability and availability of your applications and services. SLOs use service level indicators (SLIs) to calculate whether the application is performing at the level that you want.

Create an SLO to set a target for a service or operation’s availability or latency. CloudWatch measures this target frequently you can find whether it has been breached.

The target performance quality that is defined for an SLO is the *attainment goal*.

You can set SLO targets for your applications that are discovered by Application Signals, using critical metrics such as latency and availability. You can also set SLOs against any CloudWatch metric or math expression that produces a time series.

**Note**
You can't create an SLO for a service operation that was discovered by Application Signals until after that operation has reported standard metrics to Application Signals.

When you create an SLO, you specify whether it is a *period-based SLO* or a *request-based SLO*. Each type of SLO has a different way of evaluating your application's performance against its attainment goal.
+ A *period-based SLO* uses defined *periods* of time within a specified total time interval. For each period of time, Application Signals determines whether the application met its goal. The attainment rate is calculated as the `number of good periods/number of total periods`.

  For example, for a period-based SLO, meeting an attainment goal of 99.9% means that within your interval, your application must meet its performance goal during at least 99.9% of the time periods.
+ A *request-based SLO* doesn't use pre-defined periods of time. Instead, the SLO measures `number of good requests/number of total requests` during the interval. At any time, you can find the ratio of good requests to total requests for the interval up to the time stamp that you specify, and measure that ratio against the goal set in your SLO.

After you have created an SLO, you can retrieve error budget reports for it. An *error budget* is the amount of time or amount of requests that your application can be non-compliant with the SLO's goal, and still have your application meet the goal.
+ For a period-based SLO, the error budget starts at a number defined by the highest number of periods that can fail to meet the threshold, while still meeting the overall goal. The *remaining error budget* decreases with every failed period that is recorded. The error budget within one interval can never increase.

  For example, an SLO with a threshold that 99.95% of requests must be completed under 2000ms every month translates to an error budget of 21.9 minutes of downtime per month.
+ For a request-based SLO, the remaining error budget is dynamic and can increase or decrease, depending on the ratio of good requests to total requests.

For more information about SLOs, see [ Service level objectives (SLOs)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html).

When you perform a `CreateServiceLevelObjective` operation, Application Signals creates the *AWSServiceRoleForCloudWatchApplicationSignals* service-linked role, if it doesn't already exist in your account. This service- linked role has the following permissions:
+  `xray:GetServiceGraph`
+  `logs:StartQuery`
+  `logs:GetQueryResults`
+  `cloudwatch:GetMetricData`
+  `cloudwatch:ListMetrics`
+  `tag:GetResources`
+  `autoscaling:DescribeAutoScalingGroups`

## Request Syntax
<a name="API_CreateServiceLevelObjective_RequestSyntax"></a>

```
POST /slo HTTP/1.1
Content-type: application/json

{
   "BurnRateConfigurations": [
      {
         "LookBackWindowMinutes": {{number}}
      }
   ],
   "CreateRecommendedSlo": {{boolean}},
   "Description": "{{string}}",
   "Goal": {
      "AttainmentGoal": {{number}},
      "Interval": { ... },
      "WarningThreshold": {{number}}
   },
   "Name": "{{string}}",
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
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateServiceLevelObjective_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateServiceLevelObjective_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BurnRateConfigurations](#API_CreateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-CreateServiceLevelObjective-request-BurnRateConfigurations"></a>
Use this array to create *burn rates* for this SLO. Each burn rate is a metric that indicates how fast the service is consuming the error budget, relative to the attainment goal of the SLO.
Type: Array of [BurnRateConfiguration](API_BurnRateConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [CreateRecommendedSlo](#API_CreateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-CreateServiceLevelObjective-request-CreateRecommendedSlo"></a>
Set this to `true` to create a recommended SLO out of the box. When set to `true`, you don't need to specify the `MetricThreshold` or `ComparisonOperator` in the `SliConfig` or `RequestBasedSliConfig`. The default value is `false`.
This is supported for SLOs on a service, service operation, or a dependency.
Type: Boolean
Required: No

 ** [Description](#API_CreateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-CreateServiceLevelObjective-request-Description"></a>
An optional description for this SLO.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [Goal](#API_CreateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-CreateServiceLevelObjective-request-Goal"></a>
This structure contains the attributes that determine the goal of the SLO.
Type: [Goal](API_Goal.md) object
Required: No

 ** [Name](#API_CreateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-CreateServiceLevelObjective-request-Name"></a>
A name for this SLO.
Type: String
Pattern: `[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
Required: Yes

 ** [RequestBasedSliConfig](#API_CreateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-CreateServiceLevelObjective-request-RequestBasedSliConfig"></a>
If this SLO is a request-based SLO, this structure defines the information about what performance metric this SLO will monitor.
You can't specify both `RequestBasedSliConfig` and `SliConfig` in the same operation.
Type: [RequestBasedServiceLevelIndicatorConfig](API_RequestBasedServiceLevelIndicatorConfig.md) object
Required: No

 ** [SliConfig](#API_CreateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-CreateServiceLevelObjective-request-SliConfig"></a>
If this SLO is a period-based SLO, this structure defines the information about what performance metric this SLO will monitor.
You can't specify both `RequestBasedSliConfig` and `SliConfig` in the same operation.
Type: [ServiceLevelIndicatorConfig](API_ServiceLevelIndicatorConfig.md) object
Required: No

 ** [Tags](#API_CreateServiceLevelObjective_RequestSyntax) **   <a name="applicationsignals-CreateServiceLevelObjective-request-Tags"></a>
A list of key-value pairs to associate with the SLO. You can associate as many as 50 tags with an SLO. To be able to associate tags with the SLO when you create the SLO, you must have the `cloudwatch:TagResource` permission.
Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateServiceLevelObjective_ResponseSyntax"></a>

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
<a name="API_CreateServiceLevelObjective_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Slo](#API_CreateServiceLevelObjective_ResponseSyntax) **   <a name="applicationsignals-CreateServiceLevelObjective-response-Slo"></a>
A structure that contains information about the SLO that you just created.
Type: [ServiceLevelObjective](API_ServiceLevelObjective.md) object

## Errors
<a name="API_CreateServiceLevelObjective_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This operation attempted to create a resource that already exists.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
This request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateServiceLevelObjective_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/CreateServiceLevelObjective)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/CreateServiceLevelObjective)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/CreateServiceLevelObjective)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/CreateServiceLevelObjective)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/CreateServiceLevelObjective)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/CreateServiceLevelObjective)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/CreateServiceLevelObjective)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/CreateServiceLevelObjective)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/CreateServiceLevelObjective)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/CreateServiceLevelObjective)
