---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StartDataQualityRulesetEvaluationRun.html
---

# StartDataQualityRulesetEvaluationRun
<a name="API_StartDataQualityRulesetEvaluationRun"></a>

Once you have a ruleset definition (either recommended or your own), you call this operation to evaluate the ruleset against a data source (AWS Glue table). The evaluation computes results which you can retrieve with the `GetDataQualityResult` API.

## Request Syntax
<a name="API_StartDataQualityRulesetEvaluationRun_RequestSyntax"></a>

```
{
   "AdditionalDataSources": {
      "{{string}}" : {
         "DataQualityGlueTable": {
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "CatalogId": "{{string}}",
            "ConnectionName": "{{string}}",
            "DatabaseName": "{{string}}",
            "PreProcessingQuery": "{{string}}",
            "TableName": "{{string}}"
         },
         "GlueTable": {
            "AdditionalOptions": {
               "{{string}}" : "{{string}}"
            },
            "CatalogId": "{{string}}",
            "ConnectionName": "{{string}}",
            "DatabaseName": "{{string}}",
            "TableName": "{{string}}"
         }
      }
   },
   "AdditionalRunOptions": {
      "CloudWatchMetricsEnabled": {{boolean}},
      "CompositeRuleEvaluationMethod": "{{string}}",
      "ResultsS3Prefix": "{{string}}"
   },
   "ClientToken": "{{string}}",
   "DataSource": {
      "DataQualityGlueTable": {
         "AdditionalOptions": {
            "{{string}}" : "{{string}}"
         },
         "CatalogId": "{{string}}",
         "ConnectionName": "{{string}}",
         "DatabaseName": "{{string}}",
         "PreProcessingQuery": "{{string}}",
         "TableName": "{{string}}"
      },
      "GlueTable": {
         "AdditionalOptions": {
            "{{string}}" : "{{string}}"
         },
         "CatalogId": "{{string}}",
         "ConnectionName": "{{string}}",
         "DatabaseName": "{{string}}",
         "TableName": "{{string}}"
      }
   },
   "NumberOfWorkers": {{number}},
   "Role": "{{string}}",
   "RulesetNames": [ "{{string}}" ],
   "Timeout": {{number}}
}
```

## Request Parameters
<a name="API_StartDataQualityRulesetEvaluationRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AdditionalDataSources](#API_StartDataQualityRulesetEvaluationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRulesetEvaluationRun-request-AdditionalDataSources"></a>
A map of reference strings to additional data sources you can specify for an evaluation run.
Type: String to [DataSource](API_DataSource.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [AdditionalRunOptions](#API_StartDataQualityRulesetEvaluationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRulesetEvaluationRun-request-AdditionalRunOptions"></a>
Additional run options you can specify for an evaluation run.
Type: [DataQualityEvaluationRunAdditionalRunOptions](API_DataQualityEvaluationRunAdditionalRunOptions.md) object
Required: No

 ** [ClientToken](#API_StartDataQualityRulesetEvaluationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRulesetEvaluationRun-request-ClientToken"></a>
Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DataSource](#API_StartDataQualityRulesetEvaluationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRulesetEvaluationRun-request-DataSource"></a>
The data source (AWS Glue table) associated with this run.
Type: [DataSource](API_DataSource.md) object
Required: Yes

 ** [NumberOfWorkers](#API_StartDataQualityRulesetEvaluationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRulesetEvaluationRun-request-NumberOfWorkers"></a>
The number of `G.1X` workers to be used in the run. The default is 5.
Type: Integer
Required: No

 ** [Role](#API_StartDataQualityRulesetEvaluationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRulesetEvaluationRun-request-Role"></a>
An IAM role supplied to encrypt the results of the run.
Type: String
Required: Yes

 ** [RulesetNames](#API_StartDataQualityRulesetEvaluationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRulesetEvaluationRun-request-RulesetNames"></a>
A list of ruleset names.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Timeout](#API_StartDataQualityRulesetEvaluationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRulesetEvaluationRun-request-Timeout"></a>
The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters `TIMEOUT` status. The default is 2,880 minutes (48 hours).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## Response Syntax
<a name="API_StartDataQualityRulesetEvaluationRun_ResponseSyntax"></a>

```
{
   "RunId": "string"
}
```

## Response Elements
<a name="API_StartDataQualityRulesetEvaluationRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RunId](#API_StartDataQualityRulesetEvaluationRun_ResponseSyntax) **   <a name="Glue-StartDataQualityRulesetEvaluationRun-response-RunId"></a>
The unique run identifier associated with this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_StartDataQualityRulesetEvaluationRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The `CreatePartitions` API was called on a table that has indexes enabled.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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
<a name="API_StartDataQualityRulesetEvaluationRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/StartDataQualityRulesetEvaluationRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/StartDataQualityRulesetEvaluationRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StartDataQualityRulesetEvaluationRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/StartDataQualityRulesetEvaluationRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StartDataQualityRulesetEvaluationRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/StartDataQualityRulesetEvaluationRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/StartDataQualityRulesetEvaluationRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/StartDataQualityRulesetEvaluationRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/StartDataQualityRulesetEvaluationRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StartDataQualityRulesetEvaluationRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
