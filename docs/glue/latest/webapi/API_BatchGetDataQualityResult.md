---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetDataQualityResult.html
---

# BatchGetDataQualityResult
<a name="API_BatchGetDataQualityResult"></a>

Retrieves a list of data quality results for the specified result IDs.

## Request Syntax
<a name="API_BatchGetDataQualityResult_RequestSyntax"></a>

```
{
   "ResultIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetDataQualityResult_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResultIds](#API_BatchGetDataQualityResult_RequestSyntax) **   <a name="Glue-BatchGetDataQualityResult-request-ResultIds"></a>
A list of unique result IDs for the data quality results.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_BatchGetDataQualityResult_ResponseSyntax"></a>

```
{
   "Results": [
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
   ],
   "ResultsNotFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetDataQualityResult_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Results](#API_BatchGetDataQualityResult_ResponseSyntax) **   <a name="Glue-BatchGetDataQualityResult-response-Results"></a>
A list of `DataQualityResult` objects representing the data quality results.
Type: Array of [DataQualityResult](API_DataQualityResult.md) objects

 ** [ResultsNotFound](#API_BatchGetDataQualityResult_ResponseSyntax) **   <a name="Glue-BatchGetDataQualityResult-response-ResultsNotFound"></a>
A list of result IDs for which results were not found.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_BatchGetDataQualityResult_Errors"></a>

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
<a name="API_BatchGetDataQualityResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchGetDataQualityResult)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchGetDataQualityResult)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetDataQualityResult)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchGetDataQualityResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetDataQualityResult)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchGetDataQualityResult)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchGetDataQualityResult)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchGetDataQualityResult)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchGetDataQualityResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetDataQualityResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
