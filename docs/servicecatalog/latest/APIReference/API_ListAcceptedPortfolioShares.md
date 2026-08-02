---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListAcceptedPortfolioShares.html
---

# ListAcceptedPortfolioShares
<a name="API_ListAcceptedPortfolioShares"></a>

Lists all imported portfolios for which account-to-account shares were accepted by this account. By specifying the `PortfolioShareType`, you can list portfolios for which organizational shares were accepted by this account.

## Request Syntax
<a name="API_ListAcceptedPortfolioShares_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "PortfolioShareType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAcceptedPortfolioShares_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_ListAcceptedPortfolioShares_RequestSyntax) **   <a name="servicecatalog-ListAcceptedPortfolioShares-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [PageSize](#API_ListAcceptedPortfolioShares_RequestSyntax) **   <a name="servicecatalog-ListAcceptedPortfolioShares-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [PageToken](#API_ListAcceptedPortfolioShares_RequestSyntax) **   <a name="servicecatalog-ListAcceptedPortfolioShares-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [PortfolioShareType](#API_ListAcceptedPortfolioShares_RequestSyntax) **   <a name="servicecatalog-ListAcceptedPortfolioShares-request-PortfolioShareType"></a>
The type of shared portfolios to list. The default is to list imported portfolios.
+  `AWS_ORGANIZATIONS` - List portfolios accepted and shared via organizational sharing by the management account or delegated administrator of your organization.
+  `AWS_SERVICECATALOG` - Deprecated type.
+  `IMPORTED` - List imported portfolios that have been accepted and shared through account-to-account sharing.
Type: String
Valid Values: `IMPORTED | AWS_SERVICECATALOG | AWS_ORGANIZATIONS`
Required: No

## Response Syntax
<a name="API_ListAcceptedPortfolioShares_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "PortfolioDetails": [
      {
         "ARN": "string",
         "CreatedTime": number,
         "Description": "string",
         "DisplayName": "string",
         "Id": "string",
         "ProviderName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAcceptedPortfolioShares_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_ListAcceptedPortfolioShares_ResponseSyntax) **   <a name="servicecatalog-ListAcceptedPortfolioShares-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [PortfolioDetails](#API_ListAcceptedPortfolioShares_ResponseSyntax) **   <a name="servicecatalog-ListAcceptedPortfolioShares-response-PortfolioDetails"></a>
Information about the portfolios.
Type: Array of [PortfolioDetail](API_PortfolioDetail.md) objects

## Errors
<a name="API_ListAcceptedPortfolioShares_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** OperationNotSupportedException **
The operation is not supported.
HTTP Status Code: 400

## See Also
<a name="API_ListAcceptedPortfolioShares_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/ListAcceptedPortfolioShares)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/ListAcceptedPortfolioShares)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ListAcceptedPortfolioShares)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/ListAcceptedPortfolioShares)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ListAcceptedPortfolioShares)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/ListAcceptedPortfolioShares)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ListAcceptedPortfolioShares)
