---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateDataQualityRuleset.html
---

# CreateDataQualityRuleset
<a name="API_CreateDataQualityRuleset"></a>

Creates a data quality ruleset with DQDL rules applied to a specified AWS Glue table.

You create the ruleset using the Data Quality Definition Language (DQDL). For more information, see the AWS Glue developer guide.

## Request Syntax
<a name="API_CreateDataQualityRuleset_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DataQualitySecurityConfiguration": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Ruleset": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TargetTable": {
      "CatalogId": "{{string}}",
      "DatabaseName": "{{string}}",
      "TableName": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateDataQualityRuleset_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateDataQualityRuleset_RequestSyntax) **   <a name="Glue-CreateDataQualityRuleset-request-ClientToken"></a>
Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DataQualitySecurityConfiguration](#API_CreateDataQualityRuleset_RequestSyntax) **   <a name="Glue-CreateDataQualityRuleset-request-DataQualitySecurityConfiguration"></a>
The name of the security configuration created with the data quality encryption option.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Description](#API_CreateDataQualityRuleset_RequestSyntax) **   <a name="Glue-CreateDataQualityRuleset-request-Description"></a>
A description of the data quality ruleset.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [Name](#API_CreateDataQualityRuleset_RequestSyntax) **   <a name="Glue-CreateDataQualityRuleset-request-Name"></a>
A unique name for the data quality ruleset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Ruleset](#API_CreateDataQualityRuleset_RequestSyntax) **   <a name="Glue-CreateDataQualityRuleset-request-Ruleset"></a>
A Data Quality Definition Language (DQDL) ruleset. For more information, see the AWS Glue developer guide.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Required: Yes

 ** [Tags](#API_CreateDataQualityRuleset_RequestSyntax) **   <a name="Glue-CreateDataQualityRuleset-request-Tags"></a>
A list of tags applied to the data quality ruleset.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [TargetTable](#API_CreateDataQualityRuleset_RequestSyntax) **   <a name="Glue-CreateDataQualityRuleset-request-TargetTable"></a>
A target table associated with the data quality ruleset.
Type: [DataQualityTargetTable](API_DataQualityTargetTable.md) object
Required: No

## Response Syntax
<a name="API_CreateDataQualityRuleset_ResponseSyntax"></a>

```
{
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateDataQualityRuleset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_CreateDataQualityRuleset_ResponseSyntax) **   <a name="Glue-CreateDataQualityRuleset-response-Name"></a>
A unique name for the data quality ruleset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_CreateDataQualityRuleset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
A resource to be created or added already exists.
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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateDataQualityRuleset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateDataQualityRuleset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateDataQualityRuleset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateDataQualityRuleset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateDataQualityRuleset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateDataQualityRuleset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateDataQualityRuleset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateDataQualityRuleset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateDataQualityRuleset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateDataQualityRuleset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateDataQualityRuleset)
