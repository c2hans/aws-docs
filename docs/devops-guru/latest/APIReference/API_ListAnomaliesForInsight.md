---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListAnomaliesForInsight.html
---

# ListAnomaliesForInsight
<a name="API_ListAnomaliesForInsight"></a>

 Returns a list of the anomalies that belong to an insight that you specify using its ID.

## Request Syntax
<a name="API_ListAnomaliesForInsight_RequestSyntax"></a>

```
POST /anomalies/insight/{{InsightId}} HTTP/1.1
Content-type: application/json

{
   "AccountId": "{{string}}",
   "Filters": {
      "ServiceCollection": {
         "ServiceNames": [ "{{string}}" ]
      }
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StartTimeRange": {
      "FromTime": {{number}},
      "ToTime": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_ListAnomaliesForInsight_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InsightId](#API_ListAnomaliesForInsight_RequestSyntax) **   <a name="DevOpsGuru-ListAnomaliesForInsight-request-uri-InsightId"></a>
 The ID of the insight. The returned anomalies belong to this insight.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w-]*$`
Required: Yes

## Request Body
<a name="API_ListAnomaliesForInsight_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountId](#API_ListAnomaliesForInsight_RequestSyntax) **   <a name="DevOpsGuru-ListAnomaliesForInsight-request-AccountId"></a>
The ID of the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [Filters](#API_ListAnomaliesForInsight_RequestSyntax) **   <a name="DevOpsGuru-ListAnomaliesForInsight-request-Filters"></a>
 Specifies one or more service names that are used to list anomalies.
Type: [ListAnomaliesForInsightFilters](API_ListAnomaliesForInsightFilters.md) object
Required: No

 ** [MaxResults](#API_ListAnomaliesForInsight_RequestSyntax) **   <a name="DevOpsGuru-ListAnomaliesForInsight-request-MaxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_ListAnomaliesForInsight_RequestSyntax) **   <a name="DevOpsGuru-ListAnomaliesForInsight-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** [StartTimeRange](#API_ListAnomaliesForInsight_RequestSyntax) **   <a name="DevOpsGuru-ListAnomaliesForInsight-request-StartTimeRange"></a>
 A time range used to specify when the requested anomalies started. All returned anomalies started during this time range.
Type: [StartTimeRange](API_StartTimeRange.md) object
Required: No

## Response Syntax
<a name="API_ListAnomaliesForInsight_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ProactiveAnomalies": [
      {
         "AnomalyReportedTimeRange": {
            "CloseTime": number,
            "OpenTime": number
         },
         "AnomalyResources": [
            {
               "Name": "string",
               "Type": "string"
            }
         ],
         "AnomalyTimeRange": {
            "EndTime": number,
            "StartTime": number
         },
         "AssociatedInsightId": "string",
         "Description": "string",
         "Id": "string",
         "Limit": number,
         "PredictionTimeRange": {
            "EndTime": number,
            "StartTime": number
         },
         "ResourceCollection": {
            "CloudFormation": {
               "StackNames": [ "string" ]
            },
            "Tags": [
               {
                  "AppBoundaryKey": "string",
                  "TagValues": [ "string" ]
               }
            ]
         },
         "Severity": "string",
         "SourceDetails": {
            "CloudWatchMetrics": [
               {
                  "Dimensions": [
                     {
                        "Name": "string",
                        "Value": "string"
                     }
                  ],
                  "MetricDataSummary": {
                     "StatusCode": "string",
                     "TimestampMetricValuePairList": [
                        {
                           "MetricValue": number,
                           "Timestamp": number
                        }
                     ]
                  },
                  "MetricName": "string",
                  "Namespace": "string",
                  "Period": number,
                  "Stat": "string",
                  "Unit": "string"
               }
            ],
            "PerformanceInsightsMetrics": [
               {
                  "MetricDisplayName": "string",
                  "MetricQuery": {
                     "Filter": {
                        "string" : "string"
                     },
                     "GroupBy": {
                        "Dimensions": [ "string" ],
                        "Group": "string",
                        "Limit": number
                     },
                     "Metric": "string"
                  },
                  "ReferenceData": [
                     {
                        "ComparisonValues": {
                           "ReferenceMetric": {
                              "MetricQuery": {
                                 "Filter": {
                                    "string" : "string"
                                 },
                                 "GroupBy": {
                                    "Dimensions": [ "string" ],
                                    "Group": "string",
                                    "Limit": number
                                 },
                                 "Metric": "string"
                              }
                           },
                           "ReferenceScalar": {
                              "Value": number
                           }
                        },
                        "Name": "string"
                     }
                  ],
                  "StatsAtAnomaly": [
                     {
                        "Type": "string",
                        "Value": number
                     }
                  ],
                  "StatsAtBaseline": [
                     {
                        "Type": "string",
                        "Value": number
                     }
                  ],
                  "Unit": "string"
               }
            ]
         },
         "SourceMetadata": {
            "Source": "string",
            "SourceResourceName": "string",
            "SourceResourceType": "string"
         },
         "Status": "string",
         "UpdateTime": number
      }
   ],
   "ReactiveAnomalies": [
      {
         "AnomalyReportedTimeRange": {
            "CloseTime": number,
            "OpenTime": number
         },
         "AnomalyResources": [
            {
               "Name": "string",
               "Type": "string"
            }
         ],
         "AnomalyTimeRange": {
            "EndTime": number,
            "StartTime": number
         },
         "AssociatedInsightId": "string",
         "CausalAnomalyId": "string",
         "Description": "string",
         "Id": "string",
         "Name": "string",
         "ResourceCollection": {
            "CloudFormation": {
               "StackNames": [ "string" ]
            },
            "Tags": [
               {
                  "AppBoundaryKey": "string",
                  "TagValues": [ "string" ]
               }
            ]
         },
         "Severity": "string",
         "SourceDetails": {
            "CloudWatchMetrics": [
               {
                  "Dimensions": [
                     {
                        "Name": "string",
                        "Value": "string"
                     }
                  ],
                  "MetricDataSummary": {
                     "StatusCode": "string",
                     "TimestampMetricValuePairList": [
                        {
                           "MetricValue": number,
                           "Timestamp": number
                        }
                     ]
                  },
                  "MetricName": "string",
                  "Namespace": "string",
                  "Period": number,
                  "Stat": "string",
                  "Unit": "string"
               }
            ],
            "PerformanceInsightsMetrics": [
               {
                  "MetricDisplayName": "string",
                  "MetricQuery": {
                     "Filter": {
                        "string" : "string"
                     },
                     "GroupBy": {
                        "Dimensions": [ "string" ],
                        "Group": "string",
                        "Limit": number
                     },
                     "Metric": "string"
                  },
                  "ReferenceData": [
                     {
                        "ComparisonValues": {
                           "ReferenceMetric": {
                              "MetricQuery": {
                                 "Filter": {
                                    "string" : "string"
                                 },
                                 "GroupBy": {
                                    "Dimensions": [ "string" ],
                                    "Group": "string",
                                    "Limit": number
                                 },
                                 "Metric": "string"
                              }
                           },
                           "ReferenceScalar": {
                              "Value": number
                           }
                        },
                        "Name": "string"
                     }
                  ],
                  "StatsAtAnomaly": [
                     {
                        "Type": "string",
                        "Value": number
                     }
                  ],
                  "StatsAtBaseline": [
                     {
                        "Type": "string",
                        "Value": number
                     }
                  ],
                  "Unit": "string"
               }
            ]
         },
         "Status": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAnomaliesForInsight_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListAnomaliesForInsight_ResponseSyntax) **   <a name="DevOpsGuru-ListAnomaliesForInsight-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [ProactiveAnomalies](#API_ListAnomaliesForInsight_ResponseSyntax) **   <a name="DevOpsGuru-ListAnomaliesForInsight-response-ProactiveAnomalies"></a>
 An array of `ProactiveAnomalySummary` objects that represent the requested anomalies
Type: Array of [ProactiveAnomalySummary](API_ProactiveAnomalySummary.md) objects

 ** [ReactiveAnomalies](#API_ListAnomaliesForInsight_ResponseSyntax) **   <a name="DevOpsGuru-ListAnomaliesForInsight-response-ReactiveAnomalies"></a>
 An array of `ReactiveAnomalySummary` objects that represent the requested anomalies
Type: Array of [ReactiveAnomalySummary](API_ReactiveAnomalySummary.md) objects

## Errors
<a name="API_ListAnomaliesForInsight_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 403

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource could not be found
 ** ResourceId **
 The ID of the AWS resource that could not be found.
 ** ResourceType **
 The type of the AWS resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to a request throttling.
 ** QuotaCode **
 The code of the quota that was exceeded, causing the throttling exception.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the throttling exception can be retried.
 ** ServiceCode **
 The code of the service that caused the throttling exception.
HTTP Status Code: 429

 ** ValidationException **
 Contains information about data passed in to a field during a request that is not valid.
 ** Fields **
 An array of fields that are associated with the validation exception.
 ** Message **
 A message that describes the validation exception.
 ** Reason **
 The reason the validation exception was thrown.
HTTP Status Code: 400

## See Also
<a name="API_ListAnomaliesForInsight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/ListAnomaliesForInsight)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/ListAnomaliesForInsight)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ListAnomaliesForInsight)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/ListAnomaliesForInsight)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ListAnomaliesForInsight)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/ListAnomaliesForInsight)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/ListAnomaliesForInsight)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/ListAnomaliesForInsight)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/ListAnomaliesForInsight)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ListAnomaliesForInsight)
