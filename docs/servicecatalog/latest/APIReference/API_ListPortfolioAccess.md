---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListPortfolioAccess.html
---

# ListPortfolioAccess
<a name="API_ListPortfolioAccess"></a>

Lists the account IDs that have access to the specified portfolio.

A delegated admin can list the accounts that have access to the shared portfolio. Note that if a delegated admin is de-registered, they can no longer perform this operation.

## Request Syntax
<a name="API_ListPortfolioAccess_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "OrganizationParentId": "{{string}}",
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "PortfolioId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPortfolioAccess_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_ListPortfolioAccess_RequestSyntax) **   <a name="servicecatalog-ListPortfolioAccess-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [OrganizationParentId](#API_ListPortfolioAccess_RequestSyntax) **   <a name="servicecatalog-ListPortfolioAccess-request-OrganizationParentId"></a>
The ID of an organization node the portfolio is shared with. All children of this node with an inherited portfolio share will be returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [PageSize](#API_ListPortfolioAccess_RequestSyntax) **   <a name="servicecatalog-ListPortfolioAccess-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [PageToken](#API_ListPortfolioAccess_RequestSyntax) **   <a name="servicecatalog-ListPortfolioAccess-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [PortfolioId](#API_ListPortfolioAccess_RequestSyntax) **   <a name="servicecatalog-ListPortfolioAccess-request-PortfolioId"></a>
The portfolio identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_ListPortfolioAccess_ResponseSyntax"></a>

```
{
   "AccountIds": [ "string" ],
   "NextPageToken": "string"
}
```

## Response Elements
<a name="API_ListPortfolioAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountIds](#API_ListPortfolioAccess_ResponseSyntax) **   <a name="servicecatalog-ListPortfolioAccess-response-AccountIds"></a>
Information about the AWS accounts with access to the portfolio.
Type: Array of strings
Pattern: `^[0-9]{12}$`

 ** [NextPageToken](#API_ListPortfolioAccess_ResponseSyntax) **   <a name="servicecatalog-ListPortfolioAccess-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

## Errors
<a name="API_ListPortfolioAccess_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListPortfolioAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/ListPortfolioAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/ListPortfolioAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ListPortfolioAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/ListPortfolioAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ListPortfolioAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListPortfolioAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/ListPortfolioAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/ListPortfolioAccess)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/ListPortfolioAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ListPortfolioAccess)
