---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PublishDataQualityResultV2.html
---

# PublishDataQualityResultV2
<a name="API_PublishDataQualityResultV2"></a>

**Note**
This operation is intended for internal use. Do not call it directly.

AWS Glue Data Quality uses this operation to publish a data quality result.

## Request Syntax
<a name="API_PublishDataQualityResultV2_RequestSyntax"></a>

```
{
   "AggregatedMetrics": {
      "TotalRowsFailed": {{number}},
      "TotalRowsPassed": {{number}},
      "TotalRowsProcessed": {{number}},
      "TotalRulesFailed": {{number}},
      "TotalRulesPassed": {{number}},
      "TotalRulesProcessed": {{number}}
   },
   "AnalyzerResults": [
      {
         "Description": "{{string}}",
         "EvaluatedDistributions": {
            "{{string}}" : {
               "BinEdges": [ "{{string}}" ],
               "Count": [ {{number}} ],
               "DataType": "{{string}}"
            }
         },
         "EvaluatedMetrics": {
            "{{string}}" : {{number}}
         },
         "EvaluationMessage": "{{string}}",
         "Name": "{{string}}"
      }
   ],
   "ClientToken": "{{string}}",
   "DataQualitySecurityConfiguration": "{{string}}",
   "Descriptors": {
      "{{string}}" : "{{string}}"
   },
   "Dimensions": {
      "{{string}}" : "{{string}}"
   },
   "EvaluationContext": "{{string}}",
   "ExecutionCompletedOn": {{number}},
   "ExecutionStartedOn": {{number}},
   "Observations": [
      {
         "Description": "{{string}}",
         "MetricBasedObservation": {
            "MetricName": "{{string}}",
            "MetricValues": {
               "ActualValue": {{number}},
               "ExpectedValue": {{number}},
               "LowerLimit": {{number}},
               "UpperLimit": {{number}}
            },
            "NewRules": [ "{{string}}" ],
            "StatisticId": "{{string}}"
         }
      }
   ],
   "RuleResults": [
      {
         "Description": "{{string}}",
         "EvaluatedMetrics": {
            "{{string}}" : {{number}}
         },
         "EvaluatedRule": "{{string}}",
         "EvaluationMessage": "{{string}}",
         "Labels": {
            "{{string}}" : "{{string}}"
         },
         "Name": "{{string}}",
         "Result": "{{string}}",
         "RuleMetrics": {
            "{{string}}" : {{number}}
         }
      }
   ],
   "RulesetName": "{{string}}",
   "RunConfiguration": {
      "ObservationMode": "{{string}}",
      "ObservationsEnabled": "{{string}}"
   },
   "Score": {{number}},
   "Statistics": [
      {
         "ColumnsReferenced": [ "{{string}}" ],
         "DistributionValue": {
            "BinEdges": [ "{{string}}" ],
            "Count": [ {{number}} ],
            "DataType": "{{string}}"
         },
         "DoubleValue": {{number}},
         "EvaluationLevel": "{{string}}",
         "InclusionAnnotation": {
            "LastModifiedOn": {{number}},
            "Value": "{{string}}"
         },
         "ProfileId": "{{string}}",
         "RecordedOn": {{number}},
         "ReferencedDatasets": [ "{{string}}" ],
         "RunIdentifier": {
            "JobRunId": "{{string}}",
            "RunId": "{{string}}"
         },
         "StatisticId": "{{string}}",
         "StatisticName": "{{string}}",
         "StatisticProperties": {
            "{{string}}" : "{{string}}"
         }
      }
   ],
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Telemetry": {
      "Engine": "{{string}}",
      "FlagsEnabled": {
         "{{string}}" : "{{string}}"
      },
      "HostRuntimeVersion": "{{string}}",
      "LibraryVersion": "{{string}}",
      "SparkVersion": "{{string}}",
      "VcpuHours": {{number}}
   }
}
```

## Request Parameters
<a name="API_PublishDataQualityResultV2_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AggregatedMetrics](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-AggregatedMetrics"></a>
The aggregated metrics for the result.
Type: [DataQualityAggregatedMetrics](API_DataQualityAggregatedMetrics.md) object
Required: No

 ** [AnalyzerResults](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-AnalyzerResults"></a>
The analyzer level results.
Type: Array of [DataQualityAnalyzerResult](API_DataQualityAnalyzerResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2000 items.
Required: No

 ** [ClientToken](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-ClientToken"></a>
The client token for the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** [DataQualitySecurityConfiguration](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-DataQualitySecurityConfiguration"></a>
The security configuration for the result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Descriptors](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-Descriptors"></a>
The descriptors for the result.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Dimensions](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-Dimensions"></a>
The dimensions for the result.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [EvaluationContext](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-EvaluationContext"></a>
The evaluation context for the result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [ExecutionCompletedOn](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-ExecutionCompletedOn"></a>
The time execution completed for the result.
Type: Timestamp
Required: No

 ** [ExecutionStartedOn](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-ExecutionStartedOn"></a>
The time execution started for the result.
Type: Timestamp
Required: No

 ** [Observations](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-Observations"></a>
The observations for the result.
Type: Array of [DataQualityObservation](API_DataQualityObservation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [RuleResults](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-RuleResults"></a>
The rule level results.
Type: Array of [DataQualityRuleResult](API_DataQualityRuleResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2000 items.
Required: Yes

 ** [RulesetName](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-RulesetName"></a>
The ruleset name for the result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [RunConfiguration](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-RunConfiguration"></a>
The run configuration for the result.
Type: [DataQualityConfigurationV2](API_DataQualityConfigurationV2.md) object
Required: No

 ** [Score](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-Score"></a>
The score for the result.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: Yes

 ** [Statistics](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-Statistics"></a>
The statistics for the result.
Type: Array of [StatisticSummary](API_StatisticSummary.md) objects
Required: No

 ** [Tags](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-Tags"></a>
The tags for the result.
Type: String to string map
Map Entries: Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Telemetry](#API_PublishDataQualityResultV2_RequestSyntax) **   <a name="Glue-PublishDataQualityResultV2-request-Telemetry"></a>

Type: [DataQualityTelemetry](API_DataQualityTelemetry.md) object
Required: No

## Response Syntax
<a name="API_PublishDataQualityResultV2_ResponseSyntax"></a>

```
{
   "ResultId": "string"
}
```

## Response Elements
<a name="API_PublishDataQualityResultV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResultId](#API_PublishDataQualityResultV2_ResponseSyntax) **   <a name="Glue-PublishDataQualityResultV2-response-ResultId"></a>
The ID of the result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_PublishDataQualityResultV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IdempotentParameterMismatchException **
The same unique identifier was associated with two different records.
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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_PublishDataQualityResultV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/PublishDataQualityResultV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/PublishDataQualityResultV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PublishDataQualityResultV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/PublishDataQualityResultV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PublishDataQualityResultV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/PublishDataQualityResultV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/PublishDataQualityResultV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/PublishDataQualityResultV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/PublishDataQualityResultV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PublishDataQualityResultV2)
