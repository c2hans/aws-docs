---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeAnomaly.html
---

# DescribeAnomaly
<a name="API_DescribeAnomaly"></a>

**Note**
End of support notice: On September 30, 2027, AWS will end support for Amazon DevOps Guru. After September 30, 2027, you will no longer be able to access the Amazon DevOps Guru console or Amazon DevOps Guru resources. For more information, see [Amazon DevOps Guru end of support](https://docs.aws.amazon.com/devops-guru/latest/userguide/devops-guru-end-of-support.html).

 Returns details about an anomaly that you specify using its ID.

## Request Syntax
<a name="API_DescribeAnomaly_RequestSyntax"></a>

```
GET /anomalies/{{Id}}?AccountId={{AccountId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAnomaly_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountId](#API_DescribeAnomaly_RequestSyntax) **   <a name="DevOpsGuru-DescribeAnomaly-request-uri-AccountId"></a>
The ID of the member account.
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`

 ** [Id](#API_DescribeAnomaly_RequestSyntax) **   <a name="DevOpsGuru-DescribeAnomaly-request-uri-Id"></a>
 The ID of the anomaly.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w~.-]*$`
Required: Yes

## Request Body
<a name="API_DescribeAnomaly_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAnomaly_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProactiveAnomaly": {
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
   },
   "ReactiveAnomaly": {
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
}
```

## Response Elements
<a name="API_DescribeAnomaly_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProactiveAnomaly](#API_DescribeAnomaly_ResponseSyntax) **   <a name="DevOpsGuru-DescribeAnomaly-response-ProactiveAnomaly"></a>
 A `ProactiveAnomaly` object that represents the requested anomaly.
Type: [ProactiveAnomaly](API_ProactiveAnomaly.md) object

 ** [ReactiveAnomaly](#API_DescribeAnomaly_ResponseSyntax) **   <a name="DevOpsGuru-DescribeAnomaly-response-ReactiveAnomaly"></a>
 A `ReactiveAnomaly` object that represents the requested anomaly.
Type: [ReactiveAnomaly](API_ReactiveAnomaly.md) object

## Errors
<a name="API_DescribeAnomaly_Errors"></a>

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
<a name="API_DescribeAnomaly_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/DescribeAnomaly)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/DescribeAnomaly)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/DescribeAnomaly)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/DescribeAnomaly)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/DescribeAnomaly)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/DescribeAnomaly)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/DescribeAnomaly)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/DescribeAnomaly)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/DescribeAnomaly)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/DescribeAnomaly)
