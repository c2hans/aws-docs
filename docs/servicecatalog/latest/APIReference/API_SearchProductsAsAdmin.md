---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_SearchProductsAsAdmin.html
---

# SearchProductsAsAdmin
<a name="API_SearchProductsAsAdmin"></a>

Gets information about the products for the specified portfolio or all products.

## Request Syntax
<a name="API_SearchProductsAsAdmin_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Filters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "PortfolioId": "{{string}}",
   "ProductSource": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_SearchProductsAsAdmin_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_SearchProductsAsAdmin_RequestSyntax) **   <a name="servicecatalog-SearchProductsAsAdmin-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Filters](#API_SearchProductsAsAdmin_RequestSyntax) **   <a name="servicecatalog-SearchProductsAsAdmin-request-Filters"></a>
The search filters. If no search filters are specified, the output includes all products to which the administrator has access.
Type: String to array of strings map
Valid Keys: `FullTextSearch | Owner | ProductType | SourceProductId`
Required: No

 ** [PageSize](#API_SearchProductsAsAdmin_RequestSyntax) **   <a name="servicecatalog-SearchProductsAsAdmin-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [PageToken](#API_SearchProductsAsAdmin_RequestSyntax) **   <a name="servicecatalog-SearchProductsAsAdmin-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [PortfolioId](#API_SearchProductsAsAdmin_RequestSyntax) **   <a name="servicecatalog-SearchProductsAsAdmin-request-PortfolioId"></a>
The portfolio identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [ProductSource](#API_SearchProductsAsAdmin_RequestSyntax) **   <a name="servicecatalog-SearchProductsAsAdmin-request-ProductSource"></a>
Access level of the source of the product.
Type: String
Valid Values: `ACCOUNT`
Required: No

 ** [SortBy](#API_SearchProductsAsAdmin_RequestSyntax) **   <a name="servicecatalog-SearchProductsAsAdmin-request-SortBy"></a>
The sort field. If no value is specified, the results are not sorted.
Type: String
Valid Values: `Title | VersionCount | CreationDate`
Required: No

 ** [SortOrder](#API_SearchProductsAsAdmin_RequestSyntax) **   <a name="servicecatalog-SearchProductsAsAdmin-request-SortOrder"></a>
The sort order. If no value is specified, the results are not sorted.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_SearchProductsAsAdmin_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "ProductViewDetails": [
      {
         "CreatedTime": number,
         "ProductARN": "string",
         "ProductViewSummary": {
            "Distributor": "string",
            "HasDefaultPath": boolean,
            "Id": "string",
            "Name": "string",
            "Owner": "string",
            "ProductId": "string",
            "ShortDescription": "string",
            "SupportDescription": "string",
            "SupportEmail": "string",
            "SupportUrl": "string",
            "Type": "string"
         },
         "SourceConnection": {
            "ConnectionParameters": {
               "CodeStar": {
                  "ArtifactPath": "string",
                  "Branch": "string",
                  "ConnectionArn": "string",
                  "Repository": "string"
               }
            },
            "LastSync": {
               "LastSuccessfulSyncProvisioningArtifactId": "string",
               "LastSuccessfulSyncTime": number,
               "LastSyncStatus": "string",
               "LastSyncStatusMessage": "string",
               "LastSyncTime": number
            },
            "Type": "string"
         },
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchProductsAsAdmin_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_SearchProductsAsAdmin_ResponseSyntax) **   <a name="servicecatalog-SearchProductsAsAdmin-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [ProductViewDetails](#API_SearchProductsAsAdmin_ResponseSyntax) **   <a name="servicecatalog-SearchProductsAsAdmin-response-ProductViewDetails"></a>
Information about the product views.
Type: Array of [ProductViewDetail](API_ProductViewDetail.md) objects

## Errors
<a name="API_SearchProductsAsAdmin_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_SearchProductsAsAdmin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/SearchProductsAsAdmin)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/SearchProductsAsAdmin)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/SearchProductsAsAdmin)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/SearchProductsAsAdmin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/SearchProductsAsAdmin)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/SearchProductsAsAdmin)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/SearchProductsAsAdmin)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/SearchProductsAsAdmin)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/SearchProductsAsAdmin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/SearchProductsAsAdmin)
