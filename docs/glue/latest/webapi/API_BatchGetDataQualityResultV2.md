---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetDataQualityResultV2.html
---

# BatchGetDataQualityResultV2
<a name="API_BatchGetDataQualityResultV2"></a>

Retrieves a list of data quality results for the specified result IDs. You can specify up to 100 result IDs in a single request.

## Request Syntax
<a name="API_BatchGetDataQualityResultV2_RequestSyntax"></a>

```
{
   "ResultIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetDataQualityResultV2_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResultIds](#API_BatchGetDataQualityResultV2_RequestSyntax) **   <a name="Glue-BatchGetDataQualityResultV2-request-ResultIds"></a>
A list of unique result IDs for the data quality results.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_BatchGetDataQualityResultV2_ResponseSyntax"></a>

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
   ],
   "ResultsNotFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetDataQualityResultV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Results](#API_BatchGetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-BatchGetDataQualityResultV2-response-Results"></a>
A list of `DataQualityResultV2Item` objects representing the data quality results.
Type: Array of [DataQualityResultV2Item](API_DataQualityResultV2Item.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [ResultsNotFound](#API_BatchGetDataQualityResultV2_ResponseSyntax) **   <a name="Glue-BatchGetDataQualityResultV2-response-ResultsNotFound"></a>
A list of result IDs for which results were not found.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_BatchGetDataQualityResultV2_Errors"></a>

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
<a name="API_BatchGetDataQualityResultV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchGetDataQualityResultV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchGetDataQualityResultV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetDataQualityResultV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchGetDataQualityResultV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetDataQualityResultV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchGetDataQualityResultV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchGetDataQualityResultV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchGetDataQualityResultV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchGetDataQualityResultV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetDataQualityResultV2)
