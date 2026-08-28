---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CreatePortfolio.html
---

# CreatePortfolio
<a name="API_CreatePortfolio"></a>

Creates a portfolio.

A delegated admin is authorized to invoke this command.

## Request Syntax
<a name="API_CreatePortfolio_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "ProviderName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreatePortfolio_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_CreatePortfolio_RequestSyntax) **   <a name="servicecatalog-CreatePortfolio-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Description](#API_CreatePortfolio_RequestSyntax) **   <a name="servicecatalog-CreatePortfolio-request-Description"></a>
The description of the portfolio.
Type: String
Length Constraints: Maximum length of 2000.
Required: No

 ** [DisplayName](#API_CreatePortfolio_RequestSyntax) **   <a name="servicecatalog-CreatePortfolio-request-DisplayName"></a>
The name to use for display purposes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [IdempotencyToken](#API_CreatePortfolio_RequestSyntax) **   <a name="servicecatalog-CreatePortfolio-request-IdempotencyToken"></a>
A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [ProviderName](#API_CreatePortfolio_RequestSyntax) **   <a name="servicecatalog-CreatePortfolio-request-ProviderName"></a>
The name of the portfolio provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** [Tags](#API_CreatePortfolio_RequestSyntax) **   <a name="servicecatalog-CreatePortfolio-request-Tags"></a>
One or more tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 20 items.
Required: No

## Response Syntax
<a name="API_CreatePortfolio_ResponseSyntax"></a>

```
{
   "PortfolioDetail": {
      "ARN": "string",
      "CreatedTime": number,
      "Description": "string",
      "DisplayName": "string",
      "Id": "string",
      "ProviderName": "string"
   },
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreatePortfolio_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PortfolioDetail](#API_CreatePortfolio_ResponseSyntax) **   <a name="servicecatalog-CreatePortfolio-response-PortfolioDetail"></a>
Information about the portfolio.
Type: [PortfolioDetail](API_PortfolioDetail.md) object

 ** [Tags](#API_CreatePortfolio_ResponseSyntax) **   <a name="servicecatalog-CreatePortfolio-response-Tags"></a>
Information about the tags associated with the portfolio.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.

## Errors
<a name="API_CreatePortfolio_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** LimitExceededException **
The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.
HTTP Status Code: 400

 ** TagOptionNotMigratedException **
An operation requiring TagOptions failed because the TagOptions migration process has not been performed for this account. Use the AWS Management Console to perform the migration process before retrying the operation.
HTTP Status Code: 400

## See Also
<a name="API_CreatePortfolio_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/CreatePortfolio)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/CreatePortfolio)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/CreatePortfolio)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/CreatePortfolio)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/CreatePortfolio)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CreatePortfolio)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/CreatePortfolio)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/CreatePortfolio)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/CreatePortfolio)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/CreatePortfolio)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
