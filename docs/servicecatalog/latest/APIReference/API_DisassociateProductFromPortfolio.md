---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DisassociateProductFromPortfolio.html
---

# DisassociateProductFromPortfolio
<a name="API_DisassociateProductFromPortfolio"></a>

Disassociates the specified product from the specified portfolio.

A delegated admin is authorized to invoke this command.

## Request Syntax
<a name="API_DisassociateProductFromPortfolio_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "PortfolioId": "{{string}}",
   "ProductId": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateProductFromPortfolio_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DisassociateProductFromPortfolio_RequestSyntax) **   <a name="servicecatalog-DisassociateProductFromPortfolio-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [PortfolioId](#API_DisassociateProductFromPortfolio_RequestSyntax) **   <a name="servicecatalog-DisassociateProductFromPortfolio-request-PortfolioId"></a>
The portfolio identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [ProductId](#API_DisassociateProductFromPortfolio_RequestSyntax) **   <a name="servicecatalog-DisassociateProductFromPortfolio-request-ProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Elements
<a name="API_DisassociateProductFromPortfolio_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateProductFromPortfolio_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceInUseException **
A resource that is currently in use. Ensure that the resource is not in use and retry the operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateProductFromPortfolio_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DisassociateProductFromPortfolio)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DisassociateProductFromPortfolio)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DisassociateProductFromPortfolio)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DisassociateProductFromPortfolio)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DisassociateProductFromPortfolio)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DisassociateProductFromPortfolio)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DisassociateProductFromPortfolio)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DisassociateProductFromPortfolio)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DisassociateProductFromPortfolio)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DisassociateProductFromPortfolio)
