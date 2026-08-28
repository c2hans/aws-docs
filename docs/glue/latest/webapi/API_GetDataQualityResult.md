---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetDataQualityResult.html
---

# GetDataQualityResult
<a name="API_GetDataQualityResult"></a>

Retrieves the result of a data quality rule evaluation.

## Request Syntax
<a name="API_GetDataQualityResult_RequestSyntax"></a>

```
{
   "ResultId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDataQualityResult_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResultId](#API_GetDataQualityResult_RequestSyntax) **   <a name="Glue-GetDataQualityResult-request-ResultId"></a>
A unique result ID for the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetDataQualityResult_ResponseSyntax"></a>

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
         "EvaluatedMetrics": {
            "string" : number
         },
         "EvaluationMessage": "string",
         "Name": "string"
      }
   ],
   "CompletedOn": number,
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
   "EvaluationContext": "string",
   "JobName": "string",
   "JobRunId": "string",
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
   "RulesetEvaluationRunId": "string",
   "RulesetName": "string",
   "Score": number,
   "StartedOn": number
}
```

## Response Elements
<a name="API_GetDataQualityResult_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AggregatedMetrics](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-AggregatedMetrics"></a>
 A summary of `DataQualityAggregatedMetrics` objects showing the total counts of processed rows and rules, including their pass/fail statistics based on row-level results.
Type: [DataQualityAggregatedMetrics](API_DataQualityAggregatedMetrics.md) object

 ** [AnalyzerResults](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-AnalyzerResults"></a>
A list of `DataQualityAnalyzerResult` objects representing the results for each analyzer.
Type: Array of [DataQualityAnalyzerResult](API_DataQualityAnalyzerResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2000 items.

 ** [CompletedOn](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-CompletedOn"></a>
The date and time when the run for this data quality result was completed.
Type: Timestamp

 ** [DataSource](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-DataSource"></a>
The table associated with the data quality result, if any.
Type: [DataSource](API_DataSource.md) object

 ** [EvaluationContext](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-EvaluationContext"></a>
In the context of a job in AWS Glue Studio, each node in the canvas is typically assigned some sort of name and data quality nodes will have names. In the case of multiple nodes, the `evaluationContext` can differentiate the nodes.
Type: String

 ** [JobName](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-JobName"></a>
The job name associated with the data quality result, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [JobRunId](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-JobRunId"></a>
The job run ID associated with the data quality result, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [Observations](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-Observations"></a>
A list of `DataQualityObservation` objects representing the observations generated after evaluating the rules and analyzers.
Type: Array of [DataQualityObservation](API_DataQualityObservation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [ProfileId](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-ProfileId"></a>
The Profile ID for the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [ResultId](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-ResultId"></a>
A unique result ID for the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [RuleResults](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-RuleResults"></a>
A list of `DataQualityRuleResult` objects representing the results for each rule.
Type: Array of [DataQualityRuleResult](API_DataQualityRuleResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2000 items.

 ** [RulesetEvaluationRunId](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-RulesetEvaluationRunId"></a>
The unique run ID associated with the ruleset evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [RulesetName](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-RulesetName"></a>
The name of the ruleset associated with the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [Score](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-Score"></a>
An aggregate data quality score. Represents the ratio of rules that passed to the total number of rules.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.

 ** [StartedOn](#API_GetDataQualityResult_ResponseSyntax) **   <a name="Glue-GetDataQualityResult-response-StartedOn"></a>
The date and time when the run for this data quality result started.
Type: Timestamp

## Errors
<a name="API_GetDataQualityResult_Errors"></a>

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
<a name="API_GetDataQualityResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetDataQualityResult)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetDataQualityResult)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetDataQualityResult)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetDataQualityResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetDataQualityResult)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetDataQualityResult)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetDataQualityResult)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetDataQualityResult)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetDataQualityResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetDataQualityResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
