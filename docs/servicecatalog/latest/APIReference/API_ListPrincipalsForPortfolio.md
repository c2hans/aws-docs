---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListPrincipalsForPortfolio.html
---

# ListPrincipalsForPortfolio
<a name="API_ListPrincipalsForPortfolio"></a>

Lists all `PrincipalARN`s and corresponding `PrincipalType`s associated with the specified portfolio.

## Request Syntax
<a name="API_ListPrincipalsForPortfolio_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "PortfolioId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPrincipalsForPortfolio_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_ListPrincipalsForPortfolio_RequestSyntax) **   <a name="servicecatalog-ListPrincipalsForPortfolio-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [PageSize](#API_ListPrincipalsForPortfolio_RequestSyntax) **   <a name="servicecatalog-ListPrincipalsForPortfolio-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [PageToken](#API_ListPrincipalsForPortfolio_RequestSyntax) **   <a name="servicecatalog-ListPrincipalsForPortfolio-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [PortfolioId](#API_ListPrincipalsForPortfolio_RequestSyntax) **   <a name="servicecatalog-ListPrincipalsForPortfolio-request-PortfolioId"></a>
The portfolio identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_ListPrincipalsForPortfolio_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "Principals": [
      {
         "PrincipalARN": "string",
         "PrincipalType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPrincipalsForPortfolio_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_ListPrincipalsForPortfolio_ResponseSyntax) **   <a name="servicecatalog-ListPrincipalsForPortfolio-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [Principals](#API_ListPrincipalsForPortfolio_ResponseSyntax) **   <a name="servicecatalog-ListPrincipalsForPortfolio-response-Principals"></a>
The `PrincipalARN`s and corresponding `PrincipalType`s associated with the portfolio.
Type: Array of [Principal](API_Principal.md) objects

## Errors
<a name="API_ListPrincipalsForPortfolio_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListPrincipalsForPortfolio_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/ListPrincipalsForPortfolio)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/ListPrincipalsForPortfolio)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ListPrincipalsForPortfolio)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/ListPrincipalsForPortfolio)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ListPrincipalsForPortfolio)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/ListPrincipalsForPortfolio)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ListPrincipalsForPortfolio)
