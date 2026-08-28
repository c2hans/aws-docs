---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_AssociateProductWithPortfolio.html
---

# AssociateProductWithPortfolio
<a name="API_AssociateProductWithPortfolio"></a>

Associates the specified product with the specified portfolio.

A delegated admin is authorized to invoke this command.

## Request Syntax
<a name="API_AssociateProductWithPortfolio_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "PortfolioId": "{{string}}",
   "ProductId": "{{string}}",
   "SourcePortfolioId": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateProductWithPortfolio_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_AssociateProductWithPortfolio_RequestSyntax) **   <a name="servicecatalog-AssociateProductWithPortfolio-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [PortfolioId](#API_AssociateProductWithPortfolio_RequestSyntax) **   <a name="servicecatalog-AssociateProductWithPortfolio-request-PortfolioId"></a>
The portfolio identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [ProductId](#API_AssociateProductWithPortfolio_RequestSyntax) **   <a name="servicecatalog-AssociateProductWithPortfolio-request-ProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [SourcePortfolioId](#API_AssociateProductWithPortfolio_RequestSyntax) **   <a name="servicecatalog-AssociateProductWithPortfolio-request-SourcePortfolioId"></a>
The identifier of the source portfolio.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

## Response Elements
<a name="API_AssociateProductWithPortfolio_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateProductWithPortfolio_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** LimitExceededException **
The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_AssociateProductWithPortfolio_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/AssociateProductWithPortfolio)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/AssociateProductWithPortfolio)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/AssociateProductWithPortfolio)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/AssociateProductWithPortfolio)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/AssociateProductWithPortfolio)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/AssociateProductWithPortfolio)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/AssociateProductWithPortfolio)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/AssociateProductWithPortfolio)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/AssociateProductWithPortfolio)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/AssociateProductWithPortfolio)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
