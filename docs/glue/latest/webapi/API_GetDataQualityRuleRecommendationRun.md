---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetDataQualityRuleRecommendationRun.html
---

# GetDataQualityRuleRecommendationRun
<a name="API_GetDataQualityRuleRecommendationRun"></a>

Gets the specified recommendation run that was used to generate rules.

## Request Syntax
<a name="API_GetDataQualityRuleRecommendationRun_RequestSyntax"></a>

```
{
   "RunId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDataQualityRuleRecommendationRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RunId](#API_GetDataQualityRuleRecommendationRun_RequestSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-request-RunId"></a>
The unique run identifier associated with this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetDataQualityRuleRecommendationRun_ResponseSyntax"></a>

```
{
   "CompletedOn": number,
   "CreatedRulesetName": "string",
   "DataQualitySecurityConfiguration": "string",
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
   "RecommendedRuleset": "string",
   "Role": "string",
   "RunId": "string",
   "StartedOn": number,
   "Status": "string",
   "Timeout": number
}
```

## Response Elements
<a name="API_GetDataQualityRuleRecommendationRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompletedOn](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-CompletedOn"></a>
The date and time when this run was completed.
Type: Timestamp

 ** [CreatedRulesetName](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-CreatedRulesetName"></a>
The name of the ruleset that was created by the run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [DataQualitySecurityConfiguration](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-DataQualitySecurityConfiguration"></a>
The name of the security configuration created with the data quality encryption option.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [DataSource](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-DataSource"></a>
The data source (an AWS Glue table) associated with this run.
Type: [DataSource](API_DataSource.md) object

 ** [ErrorString](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-ErrorString"></a>
The error strings that are associated with the run.
Type: String

 ** [ExecutionTime](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-ExecutionTime"></a>
The amount of time (in seconds) that the run consumed resources.
Type: Integer

 ** [LastModifiedOn](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-LastModifiedOn"></a>
A timestamp. The last point in time when this data quality rule recommendation run was modified.
Type: Timestamp

 ** [NumberOfWorkers](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-NumberOfWorkers"></a>
The number of `G.1X` workers to be used in the run. The default is 5.
Type: Integer

 ** [RecommendedRuleset](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-RecommendedRuleset"></a>
When a start rule recommendation run completes, it creates a recommended ruleset (a set of rules). This member has those rules in Data Quality Definition Language (DQDL) format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.

 ** [Role](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-Role"></a>
An IAM role supplied to encrypt the results of the run.
Type: String

 ** [RunId](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-RunId"></a>
The unique run identifier associated with this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [StartedOn](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-StartedOn"></a>
The date and time when this run started.
Type: Timestamp

 ** [Status](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-Status"></a>
The status for this run.
Type: String
Valid Values: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT`

 ** [Timeout](#API_GetDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleRecommendationRun-response-Timeout"></a>
The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters `TIMEOUT` status. The default is 2,880 minutes (48 hours).
Type: Integer
Valid Range: Minimum value of 1.

## Errors
<a name="API_GetDataQualityRuleRecommendationRun_Errors"></a>

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
<a name="API_GetDataQualityRuleRecommendationRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetDataQualityRuleRecommendationRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetDataQualityRuleRecommendationRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetDataQualityRuleRecommendationRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetDataQualityRuleRecommendationRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetDataQualityRuleRecommendationRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetDataQualityRuleRecommendationRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetDataQualityRuleRecommendationRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetDataQualityRuleRecommendationRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetDataQualityRuleRecommendationRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetDataQualityRuleRecommendationRun)
