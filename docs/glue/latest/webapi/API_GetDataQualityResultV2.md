---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetDataQualityResultV2.html
---

# GetDataQualityResultV2
<a name="API_GetDataQualityResultV2"></a>

Retrieves the result of a data quality rule evaluation published from any supported data platform.

## Request Syntax
<a name="API_GetDataQualityResultV2_RequestSyntax"></a>

```
{
   "ResultId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDataQualityResultV2_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResultId](#API_GetDataQualityResultV2_RequestSyntax) **   <a name="Glue-GetDataQualityResultV2-request-ResultId"></a>
A unique result ID for the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetDataQualityResultV2_ResponseSyntax"></a>

```
{
   "AggregatedMetrics": {
      "TotalRowsFailed": number,
      "TotalRowsPassed": number,
      "TotalRowsProcessed": number,
      "TotalRulesFailed": number,
      "TotalRulesPassed": number,
      "TotalRulesProcessed": number
   },
   "AnalyzerResults": [
      {
         "Description": "string",
         "EvaluatedDistributions": {
            "string" : {
               "BinEdges": [ "string" ],
               "Count": [ number ],
               "DataType": "string"
            }
         },
         "EvaluatedMetrics": {
            "string" : number
         },
         "EvaluationMessage": "string",
         "Name": "string"
      }
   ],
   "DataQualityEvaluationConfig": "string",
   "DataSource": {
      "DataQualityGlueTable": {
         "AdditionalOptions": {
            "string" : "string"
         },
         "CatalogId": "string",
         "ConnectionName": "string",
         "DatabaseName": "string",
         "PreProcessingQuery": "string",
         "TableName": "string"
      },
      "GlueTable": {
         "AdditionalOptions": {
            "string" : "string"
         },
         "CatalogId": "string",
         "ConnectionName": "string",
         "DatabaseName": "string",
         "TableName": "string"
      }
   },
   "Descriptors": {
      "string" : "string"
   },
   "Dimensions": {
      "string" : "string"
   },
   "EvaluationContext": "string",
   "EvaluationRunMode": "string",
   "ExecutionCompletedOn": number,
   "ExecutionStartedOn": number,
   "Observations": [
      {
         "Description": "string",
         "MetricBasedObservation": {
            "MetricName": "string",
            "MetricValues": {
               "ActualValue": number,
               "ExpectedValue": number,
               "LowerLimit": number,
               "UpperLimit": number
            },
            "NewRules": [ "string" ],
            "StatisticId": "string"
         }
      }
   ],
   "ProfileId": "string",
   "ResultId": "string",
   "ResultPublishedOn": number,
   "RuleResults": [
      {
         "Description": "string",
         "EvaluatedMetrics": {
            "string" : number
         },
         "EvaluatedRule": "string",
         "EvaluationMessage": "string",
         "Labels": {
            "string" : "string"
         },
         "Name": "string",
         "Result": "string",
         "RuleMetrics": {
            "string" : number
         }
      }
   ],
   "RulesetName": "string",
   "Score": number,
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetDataQualityResultV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AggregatedMetrics](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-AggregatedMetrics"></a>
A summary of `DataQualityAggregatedMetrics` objects showing the total counts of processed rows and rules, including their pass/fail statistics based on row-level results.
Type: [DataQualityAggregatedMetrics](API_DataQualityAggregatedMetrics.md) object

 ** [AnalyzerResults](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-AnalyzerResults"></a>
A list of `DataQualityAnalyzerResult` objects representing the results for each analyzer.
Type: Array of [DataQualityAnalyzerResult](API_DataQualityAnalyzerResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2000 items.

 ** [DataQualityEvaluationConfig](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-DataQualityEvaluationConfig"></a>
The name of the data quality evaluation configuration that started the evaluation run, returned when `EvaluationRunMode` is `EVALUATION_CONFIG`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [DataSource](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-DataSource"></a>
The table associated with the data quality result, if any.
Type: [DataSource](API_DataSource.md) object

 ** [Descriptors](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-Descriptors"></a>
A map of user-provided descriptors that add contextual metadata and configuration to the data quality result, such as database name, table name, team, or environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [Dimensions](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-Dimensions"></a>
A map of platform-specific identifiers, such as cluster, application, workgroup, or project IDs, that identify where the data quality evaluation ran.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [EvaluationContext](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-EvaluationContext"></a>
The evaluation context for the data quality result. This value identifies a specific data quality result, or a series of related results, within a run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [EvaluationRunMode](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-EvaluationRunMode"></a>
How the evaluation run that produced the result started: `ON_DEMAND` for a run started by `StartDataQualityRulesetEvaluationRun`, or `EVALUATION_CONFIG` for a run started by a data quality evaluation configuration. Not returned for results that no evaluation run produced, such as results from any ETL job.
Type: String
Valid Values: `ON_DEMAND | EVALUATION_CONFIG`

 ** [ExecutionCompletedOn](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-ExecutionCompletedOn"></a>
The date and time when this data quality run completed.
Type: Timestamp

 ** [ExecutionStartedOn](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-ExecutionStartedOn"></a>
The date and time when this data quality run started.
Type: Timestamp

 ** [Observations](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-Observations"></a>
A list of `DataQualityObservation` objects representing the anomaly detection observations generated after evaluating the rules and analyzers.
Type: Array of [DataQualityObservation](API_DataQualityObservation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [ProfileId](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-ProfileId"></a>
The Profile ID for the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [ResultId](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-ResultId"></a>
A unique result ID for the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [ResultPublishedOn](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-ResultPublishedOn"></a>
The date and time when this data quality result was published.
Type: Timestamp

 ** [RuleResults](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-RuleResults"></a>
A list of `DataQualityRuleResult` objects representing the results for each rule.
Type: Array of [DataQualityRuleResult](API_DataQualityRuleResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2000 items.

 ** [RulesetName](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-RulesetName"></a>
The name of the ruleset associated with the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [Score](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-Score"></a>
An aggregate data quality score. Represents the ratio of rules that passed to the total number of rules.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.

 ** [Tags](#API_GetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-GetDataQualityResultV2-response-Tags"></a>
A map of tags associated with the data quality result.
Type: String to string map
Map Entries: Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_GetDataQualityResultV2_Errors"></a>

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
<a name="API_GetDataQualityResultV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetDataQualityResultV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetDataQualityResultV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetDataQualityResultV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetDataQualityResultV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetDataQualityResultV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetDataQualityResultV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetDataQualityResultV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetDataQualityResultV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetDataQualityResultV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetDataQualityResultV2)
