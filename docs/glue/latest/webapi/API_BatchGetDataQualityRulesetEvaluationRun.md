---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetDataQualityRulesetEvaluationRun.html
---

# BatchGetDataQualityRulesetEvaluationRun
<a name="API_BatchGetDataQualityRulesetEvaluationRun"></a>

Retrieves the details of multiple evaluation runs in a single request.

## Request Syntax
<a name="API_BatchGetDataQualityRulesetEvaluationRun_RequestSyntax"></a>

```
{
   "RunIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetDataQualityRulesetEvaluationRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RunIds](#API_BatchGetDataQualityRulesetEvaluationRun_RequestSyntax) **   <a name="Glue-BatchGetDataQualityRulesetEvaluationRun-request-RunIds"></a>
A list of unique run identifiers for the evaluation runs to retrieve.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_BatchGetDataQualityRulesetEvaluationRun_ResponseSyntax"></a>

```
{
   "Runs": [
      {
         "AdditionalDataSources": {
            "string" : {
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
            }
         },
         "AdditionalRunOptions": {
            "CloudWatchMetricsEnabled": boolean,
            "CompositeRuleEvaluationMethod": "string",
            "CustomLogGroupPrefix": "string",
            "DataQualityRuleResults": {
               "CatalogTableConfig": {
                  "CatalogId": "string",
                  "DatabaseName": "string",
                  "S3Location": "string",
                  "TableName": "string"
               },
               "WriteDataQualityRuleResultsEnabled": boolean
            },
            "ObservationMode": "string",
            "ObservationResults": {
               "CatalogTableConfig": {
                  "CatalogId": "string",
                  "DatabaseName": "string",
                  "S3Location": "string",
                  "TableName": "string"
               },
               "WriteObservationResultsEnabled": boolean
            },
            "ObservationScope": "string",
            "ProfilingResults": {
               "CatalogTableConfig": {
                  "CatalogId": "string",
                  "DatabaseName": "string",
                  "S3Location": "string",
                  "TableName": "string"
               },
               "DistributionResults": {
                  "CatalogTableConfig": {
                     "CatalogId": "string",
                     "DatabaseName": "string",
                     "S3Location": "string",
                     "TableName": "string"
                  },
                  "WriteDistributionResultsEnabled": boolean
               },
               "WriteProfilingResultsEnabled": boolean
            },
            "ResultsS3Prefix": "string",
            "RowLevelResults": {
               "CatalogTableConfig": {
                  "CatalogId": "string",
                  "DatabaseName": "string",
                  "S3Location": "string",
                  "TableName": "string"
               },
               "MaxRowsToWrite": number,
               "ResultType": "string"
            }
         },
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
         "ErrorString": "string",
         "ExecutionTime": number,
         "LastModifiedOn": number,
         "NumberOfWorkers": number,
         "ResultIds": [ "string" ],
         "Role": "string",
         "RulesetNames": [ "string" ],
         "RunId": "string",
         "StartedOn": number,
         "Status": "string",
         "Timeout": number
      }
   ],
   "RunsNotFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetDataQualityRulesetEvaluationRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Runs](#API_BatchGetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-BatchGetDataQualityRulesetEvaluationRun-response-Runs"></a>
A list of evaluation run details for the requested run IDs.
Type: Array of [DataQualityRulesetEvaluationRun](API_DataQualityRulesetEvaluationRun.md) objects

 ** [RunsNotFound](#API_BatchGetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-BatchGetDataQualityRulesetEvaluationRun-response-RunsNotFound"></a>
A list of run IDs that were not found.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_BatchGetDataQualityRulesetEvaluationRun_Errors"></a>

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
<a name="API_BatchGetDataQualityRulesetEvaluationRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchGetDataQualityRulesetEvaluationRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchGetDataQualityRulesetEvaluationRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetDataQualityRulesetEvaluationRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchGetDataQualityRulesetEvaluationRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetDataQualityRulesetEvaluationRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchGetDataQualityRulesetEvaluationRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchGetDataQualityRulesetEvaluationRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchGetDataQualityRulesetEvaluationRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchGetDataQualityRulesetEvaluationRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetDataQualityRulesetEvaluationRun)
