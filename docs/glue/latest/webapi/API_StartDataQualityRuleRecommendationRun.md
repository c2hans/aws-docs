---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StartDataQualityRuleRecommendationRun.html
---

# StartDataQualityRuleRecommendationRun
<a name="API_StartDataQualityRuleRecommendationRun"></a>

Starts a recommendation run that is used to generate rules when you don't know what rules to write. AWS Glue Data Quality analyzes the data and comes up with recommendations for a potential ruleset. You can then triage the ruleset and modify the generated ruleset to your liking.

Recommendation runs are automatically deleted after 90 days.

## Request Syntax
<a name="API_StartDataQualityRuleRecommendationRun_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "CreatedRulesetName": "{{string}}",
   "DataQualitySecurityConfiguration": "{{string}}",
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
   "Timeout": {{number}}
}
```

## Request Parameters
<a name="API_StartDataQualityRuleRecommendationRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_StartDataQualityRuleRecommendationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRuleRecommendationRun-request-ClientToken"></a>
Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [CreatedRulesetName](#API_StartDataQualityRuleRecommendationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRuleRecommendationRun-request-CreatedRulesetName"></a>
A name for the ruleset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DataQualitySecurityConfiguration](#API_StartDataQualityRuleRecommendationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRuleRecommendationRun-request-DataQualitySecurityConfiguration"></a>
The name of the security configuration created with the data quality encryption option.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DataSource](#API_StartDataQualityRuleRecommendationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRuleRecommendationRun-request-DataSource"></a>
The data source (AWS Glue table) associated with this run.
Type: [DataSource](API_DataSource.md) object
Required: Yes

 ** [NumberOfWorkers](#API_StartDataQualityRuleRecommendationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRuleRecommendationRun-request-NumberOfWorkers"></a>
The number of `G.1X` workers to be used in the run. The default is 5.
Type: Integer
Required: No

 ** [Role](#API_StartDataQualityRuleRecommendationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRuleRecommendationRun-request-Role"></a>
An IAM role supplied to encrypt the results of the run.
Type: String
Required: Yes

 ** [Timeout](#API_StartDataQualityRuleRecommendationRun_RequestSyntax) **   <a name="Glue-StartDataQualityRuleRecommendationRun-request-Timeout"></a>
The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters `TIMEOUT` status. The default is 2,880 minutes (48 hours).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## Response Syntax
<a name="API_StartDataQualityRuleRecommendationRun_ResponseSyntax"></a>

```
{
   "RunId": "string"
}
```

## Response Elements
<a name="API_StartDataQualityRuleRecommendationRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RunId](#API_StartDataQualityRuleRecommendationRun_ResponseSyntax) **   <a name="Glue-StartDataQualityRuleRecommendationRun-response-RunId"></a>
The unique run identifier associated with this run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_StartDataQualityRuleRecommendationRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The `CreatePartitions` API was called on a table that has indexes enabled.
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
<a name="API_StartDataQualityRuleRecommendationRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/StartDataQualityRuleRecommendationRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/StartDataQualityRuleRecommendationRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StartDataQualityRuleRecommendationRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/StartDataQualityRuleRecommendationRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StartDataQualityRuleRecommendationRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/StartDataQualityRuleRecommendationRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/StartDataQualityRuleRecommendationRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/StartDataQualityRuleRecommendationRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/StartDataQualityRuleRecommendationRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StartDataQualityRuleRecommendationRun)
