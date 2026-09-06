---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribePortfolioShares.html
---

# DescribePortfolioShares
<a name="API_DescribePortfolioShares"></a>

Returns a summary of each of the portfolio shares that were created for the specified portfolio.

You can use this API to determine which accounts or organizational nodes this portfolio have been shared, whether the recipient entity has imported the share, and whether TagOptions are included with the share.

The `PortfolioId` and `Type` parameters are both required.

## Request Syntax
<a name="API_DescribePortfolioShares_RequestSyntax"></a>

```
{
   "DeduplicateShares": {{boolean}},
   "IncludeAllMemberAccounts": {{boolean}},
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "PortfolioId": "{{string}}",
   "Status": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePortfolioShares_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DeduplicateShares](#API_DescribePortfolioShares_RequestSyntax) **   <a name="servicecatalog-DescribePortfolioShares-request-DeduplicateShares"></a>

Type: Boolean
Required: No

 ** [IncludeAllMemberAccounts](#API_DescribePortfolioShares_RequestSyntax) **   <a name="servicecatalog-DescribePortfolioShares-request-IncludeAllMemberAccounts"></a>
>
Type: Boolean
Required: No

 ** [PageSize](#API_DescribePortfolioShares_RequestSyntax) **   <a name="servicecatalog-DescribePortfolioShares-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [PageToken](#API_DescribePortfolioShares_RequestSyntax) **   <a name="servicecatalog-DescribePortfolioShares-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [PortfolioId](#API_DescribePortfolioShares_RequestSyntax) **   <a name="servicecatalog-DescribePortfolioShares-request-PortfolioId"></a>
The unique identifier of the portfolio for which shares will be retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [Status](#API_DescribePortfolioShares_RequestSyntax) **   <a name="servicecatalog-DescribePortfolioShares-request-Status"></a>
Status of the portfolio share operation.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | ERROR`
Required: No

 ** [Type](#API_DescribePortfolioShares_RequestSyntax) **   <a name="servicecatalog-DescribePortfolioShares-request-Type"></a>
The type of portfolio share to summarize. This field acts as a filter on the type of portfolio share, which can be one of the following:
1. `ACCOUNT` - Represents an external account to account share.
2. `ORGANIZATION` - Represents a share to an organization. This share is available to every account in the organization.
3. `ORGANIZATIONAL_UNIT` - Represents a share to an organizational unit.
4. `ORGANIZATION_MEMBER_ACCOUNT` - Represents a share to an account in the organization.
Type: String
Valid Values: `ACCOUNT | ORGANIZATION | ORGANIZATIONAL_UNIT | ORGANIZATION_MEMBER_ACCOUNT`
Required: No

## Response Syntax
<a name="API_DescribePortfolioShares_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "PortfolioShareDetails": [
      {
         "Accepted": boolean,
         "PrincipalARN": "string",
         "PrincipalId": "string",
         "SharePrincipals": boolean,
         "ShareTagOptions": boolean,
         "Status": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribePortfolioShares_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_DescribePortfolioShares_ResponseSyntax) **   <a name="servicecatalog-DescribePortfolioShares-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [PortfolioShareDetails](#API_DescribePortfolioShares_ResponseSyntax) **   <a name="servicecatalog-DescribePortfolioShares-response-PortfolioShareDetails"></a>
Summaries about each of the portfolio shares.
Type: Array of [PortfolioShareDetail](API_PortfolioShareDetail.md) objects

## Errors
<a name="API_DescribePortfolioShares_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribePortfolioShares_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribePortfolioShares)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribePortfolioShares)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribePortfolioShares)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribePortfolioShares)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribePortfolioShares)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribePortfolioShares)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribePortfolioShares)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribePortfolioShares)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribePortfolioShares)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribePortfolioShares)
