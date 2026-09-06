---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetDataQualityRuleset.html
---

# GetDataQualityRuleset
<a name="API_GetDataQualityRuleset"></a>

Returns an existing ruleset by identifier or name.

## Request Syntax
<a name="API_GetDataQualityRuleset_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDataQualityRuleset_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_GetDataQualityRuleset_RequestSyntax) **   <a name="Glue-GetDataQualityRuleset-request-Name"></a>
The name of the ruleset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetDataQualityRuleset_ResponseSyntax"></a>

```
{
   "CreatedOn": number,
   "DataQualitySecurityConfiguration": "string",
   "Description": "string",
   "LastModifiedOn": number,
   "Name": "string",
   "RecommendationRunId": "string",
   "Ruleset": "string",
   "TargetTable": {
      "CatalogId": "string",
      "DatabaseName": "string",
      "TableName": "string"
   }
}
```

## Response Elements
<a name="API_GetDataQualityRuleset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedOn](#API_GetDataQualityRuleset_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleset-response-CreatedOn"></a>
A timestamp. The time and date that this data quality ruleset was created.
Type: Timestamp

 ** [DataQualitySecurityConfiguration](#API_GetDataQualityRuleset_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleset-response-DataQualitySecurityConfiguration"></a>
The name of the security configuration created with the data quality encryption option.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [Description](#API_GetDataQualityRuleset_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleset-response-Description"></a>
A description of the ruleset.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 ** [LastModifiedOn](#API_GetDataQualityRuleset_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleset-response-LastModifiedOn"></a>
A timestamp. The last point in time when this data quality ruleset was modified.
Type: Timestamp

 ** [Name](#API_GetDataQualityRuleset_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleset-response-Name"></a>
The name of the ruleset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [RecommendationRunId](#API_GetDataQualityRuleset_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleset-response-RecommendationRunId"></a>
When a ruleset was created from a recommendation run, this run ID is generated to link the two together.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [Ruleset](#API_GetDataQualityRuleset_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleset-response-Ruleset"></a>
A Data Quality Definition Language (DQDL) ruleset. For more information, see the AWS Glue developer guide.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.

 ** [TargetTable](#API_GetDataQualityRuleset_ResponseSyntax) **   <a name="Glue-GetDataQualityRuleset-response-TargetTable"></a>
The name and database name of the target table.
Type: [DataQualityTargetTable](API_DataQualityTargetTable.md) object

## Errors
<a name="API_GetDataQualityRuleset_Errors"></a>

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
<a name="API_GetDataQualityRuleset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetDataQualityRuleset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetDataQualityRuleset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetDataQualityRuleset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetDataQualityRuleset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetDataQualityRuleset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetDataQualityRuleset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetDataQualityRuleset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetDataQualityRuleset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetDataQualityRuleset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetDataQualityRuleset)
