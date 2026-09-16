---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetDataQualityRulesetEvaluationRun.html
---

# GetDataQualityRulesetEvaluationRun
<a name="API_GetDataQualityRulesetEvaluationRun"></a>

Retrieves a specific run where a ruleset is evaluated against a data source.

## Request Syntax
<a name="API_GetDataQualityRulesetEvaluationRun_RequestSyntax"></a>

```
{
   "RunId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDataQualityRulesetEvaluationRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RunId](#API_GetDataQualityRulesetEvaluationRun_RequestSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-request-RunId"></a>
The unique run identifier associated with this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetDataQualityRulesetEvaluationRun_ResponseSyntax"></a>

```
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
      "ResultsS3Prefix": "string"
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
```

## Response Elements
<a name="API_GetDataQualityRulesetEvaluationRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdditionalDataSources](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-AdditionalDataSources"></a>
A map of reference strings to additional data sources you can specify for an evaluation run.
Type: String to [DataSource](API_DataSource.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [AdditionalRunOptions](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-AdditionalRunOptions"></a>
Additional run options you can specify for an evaluation run.
Type: [DataQualityEvaluationRunAdditionalRunOptions](API_DataQualityEvaluationRunAdditionalRunOptions.md) object

 ** [CompletedOn](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-CompletedOn"></a>
The date and time when this run was completed.
Type: Timestamp

 ** [DataSource](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-DataSource"></a>
The data source (an AWS Glue table) associated with this evaluation run.
Type: [DataSource](API_DataSource.md) object

 ** [ErrorString](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-ErrorString"></a>
The error strings that are associated with the run.
Type: String

 ** [ExecutionTime](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-ExecutionTime"></a>
The amount of time (in seconds) that the run consumed resources.
Type: Integer

 ** [LastModifiedOn](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-LastModifiedOn"></a>
A timestamp. The last point in time when this data quality rule recommendation run was modified.
Type: Timestamp

 ** [NumberOfWorkers](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-NumberOfWorkers"></a>
The number of `G.1X` workers to be used in the run. The default is 5.
Type: Integer

 ** [ResultIds](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-ResultIds"></a>
A list of result IDs for the data quality results for the run.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [Role](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-Role"></a>
An IAM role supplied to encrypt the results of the run.
Type: String

 ** [RulesetNames](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-RulesetNames"></a>
A list of ruleset names for the run. Currently, this parameter takes only one Ruleset name.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [RunId](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-RunId"></a>
The unique run identifier associated with this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [StartedOn](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-StartedOn"></a>
The date and time when this run started.
Type: Timestamp

 ** [Status](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-Status"></a>
The status for this run.
Type: String
Valid Values: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT`

 ** [Timeout](#API_GetDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRulesetEvaluationRun-response-Timeout"></a>
The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters `TIMEOUT` status. The default is 2,880 minutes (48 hours).
Type: Integer
Valid Range: Minimum value of 1.

## Errors
<a name="API_GetDataQualityRulesetEvaluationRun_Errors"></a>

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
<a name="API_GetDataQualityRulesetEvaluationRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetDataQualityRulesetEvaluationRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetDataQualityRulesetEvaluationRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetDataQualityRulesetEvaluationRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetDataQualityRulesetEvaluationRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetDataQualityRulesetEvaluationRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetDataQualityRulesetEvaluationRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetDataQualityRulesetEvaluationRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetDataQualityRulesetEvaluationRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetDataQualityRulesetEvaluationRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetDataQualityRulesetEvaluationRun)
