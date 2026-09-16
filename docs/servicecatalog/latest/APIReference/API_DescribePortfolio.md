---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribePortfolio.html
---

# DescribePortfolio
<a name="API_DescribePortfolio"></a>

Gets information about the specified portfolio.

A delegated admin is authorized to invoke this command.

## Request Syntax
<a name="API_DescribePortfolio_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Id": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePortfolio_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DescribePortfolio_RequestSyntax) **   <a name="servicecatalog-DescribePortfolio-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Id](#API_DescribePortfolio_RequestSyntax) **   <a name="servicecatalog-DescribePortfolio-request-Id"></a>
The portfolio identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_DescribePortfolio_ResponseSyntax"></a>

```
{
   "Budgets": [
      {
         "BudgetName": "string"
      }
   ],
   "PortfolioDetail": {
      "ARN": "string",
      "CreatedTime": number,
      "Description": "string",
      "DisplayName": "string",
      "Id": "string",
      "ProviderName": "string"
   },
   "TagOptions": [
      {
         "Active": boolean,
         "Id": "string",
         "Key": "string",
         "Owner": "string",
         "Value": "string"
      }
   ],
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribePortfolio_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Budgets](#API_DescribePortfolio_ResponseSyntax) **   <a name="servicecatalog-DescribePortfolio-response-Budgets"></a>
Information about the associated budgets.
Type: Array of [BudgetDetail](API_BudgetDetail.md) objects

 ** [PortfolioDetail](#API_DescribePortfolio_ResponseSyntax) **   <a name="servicecatalog-DescribePortfolio-response-PortfolioDetail"></a>
Information about the portfolio.
Type: [PortfolioDetail](API_PortfolioDetail.md) object

 ** [TagOptions](#API_DescribePortfolio_ResponseSyntax) **   <a name="servicecatalog-DescribePortfolio-response-TagOptions"></a>
Information about the TagOptions associated with the portfolio.
Type: Array of [TagOptionDetail](API_TagOptionDetail.md) objects

 ** [Tags](#API_DescribePortfolio_ResponseSyntax) **   <a name="servicecatalog-DescribePortfolio-response-Tags"></a>
Information about the tags associated with the portfolio.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.

## Errors
<a name="API_DescribePortfolio_Errors"></a>

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribePortfolio_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribePortfolio)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribePortfolio)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribePortfolio)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribePortfolio)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribePortfolio)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribePortfolio)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribePortfolio)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribePortfolio)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribePortfolio)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribePortfolio)
