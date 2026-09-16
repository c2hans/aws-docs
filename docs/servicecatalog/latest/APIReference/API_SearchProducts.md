---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_SearchProducts.html
---

# SearchProducts
<a name="API_SearchProducts"></a>

Gets information about the products to which the caller has access.

## Request Syntax
<a name="API_SearchProducts_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Filters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_SearchProducts_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_SearchProducts_RequestSyntax) **   <a name="servicecatalog-SearchProducts-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Filters](#API_SearchProducts_RequestSyntax) **   <a name="servicecatalog-SearchProducts-request-Filters"></a>
The search filters. If no search filters are specified, the output includes all products to which the caller has access.
Type: String to array of strings map
Valid Keys: `FullTextSearch | Owner | ProductType | SourceProductId`
Required: No

 ** [PageSize](#API_SearchProducts_RequestSyntax) **   <a name="servicecatalog-SearchProducts-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [PageToken](#API_SearchProducts_RequestSyntax) **   <a name="servicecatalog-SearchProducts-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [SortBy](#API_SearchProducts_RequestSyntax) **   <a name="servicecatalog-SearchProducts-request-SortBy"></a>
The sort field. If no value is specified, the results are not sorted.
Type: String
Valid Values: `Title | VersionCount | CreationDate`
Required: No

 ** [SortOrder](#API_SearchProducts_RequestSyntax) **   <a name="servicecatalog-SearchProducts-request-SortOrder"></a>
The sort order. If no value is specified, the results are not sorted.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_SearchProducts_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "ProductViewAggregations": {
      "string" : [
         {
            "ApproximateCount": number,
            "Value": "string"
         }
      ]
   },
   "ProductViewSummaries": [
      {
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
      }
   ]
}
```

## Response Elements
<a name="API_SearchProducts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_SearchProducts_ResponseSyntax) **   <a name="servicecatalog-SearchProducts-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [ProductViewAggregations](#API_SearchProducts_ResponseSyntax) **   <a name="servicecatalog-SearchProducts-response-ProductViewAggregations"></a>
The product view aggregations.
Type: String to array of [ProductViewAggregationValue](API_ProductViewAggregationValue.md) objects map

 ** [ProductViewSummaries](#API_SearchProducts_ResponseSyntax) **   <a name="servicecatalog-SearchProducts-response-ProductViewSummaries"></a>
Information about the product views.
Type: Array of [ProductViewSummary](API_ProductViewSummary.md) objects

## Errors
<a name="API_SearchProducts_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

## Examples
<a name="API_SearchProducts_Examples"></a>

### Search for all available products
<a name="API_SearchProducts_Example_1"></a>

The following JSON example retrieves all products available to the current user.

#### Sample Request
<a name="API_SearchProducts_Example_1_Request"></a>

```
POST
/
content-type:application/x-amz-json-1.1
host:servicecatalog.us-west-2.amazonaws.com
user-agent:aws-cli/1.10.19 Python/2.7.10 Darwin/15.5.0 botocore/1.4.10
x-amz-date:20160607T224008Z
x-amz-target:AWS242ServiceCatalogService.SearchProducts
```

#### Sample Response
<a name="API_SearchProducts_Example_1_Response"></a>

```
{
   "ProductViewAggregations":
   {
      "Owner":
      [
         {
            "ApproximateCount":4,
            "Value":"387896429941"
         }
      ],
      "ProductType":
      [
         {
            "ApproximateCount":4,
            "Value":"ServiceCatalog"
         }
      ],
      "Vendor":
      [
         {
            "ApproximateCount":1,
            "Value":""
         },
         {
            "ApproximateCount":1,
            "Value":"me"
         }
      ]
   },
   "ProductViewSummaries":
   [
      {
         "HasDefaultPath":false,
         "Id":"prodview-w35uhtf6nrqqy",
         "Name":"RDS template",
         "Owner":"AWS",
         "ProductId":"prod-3tsertlc2g7pw",
         "ShortDescription":"Test 2",
         "Type":"Base"
      },
      {
         "HasDefaultPath":false,
         "Id":"prodview-r2tzjgsao7mc4",
         "Name":"Devo enviro 2",
         "Owner":"asda",
         "ProductId":"prod-enx2jvf33gi52",
         "ShortDescription":"asd",
         "Type":"Base"
      },
      {
         "Distributor":"",
         "HasDefaultPath":false,
         "Id":"prodview-e64tf73gp3gl4",
         "Name":"Devo environment",
         "Owner":"test",
         "ProductId":"prod-3p2k2ejvcsdvi",
         "ShortDescription":"test",
         "Type":"Base"
      },
      {
         "Distributor":"Me",
         "HasDefaultPath":false,
         "Id":"prodview-3fmrw464floam",
         "Name":"Testtemplate",
         "Owner":"MSP XYZ",
         "ProductId":"prod-eqeqzgemstiea",
         "ShortDescription":"asdas",
         "Type":"Base"
      }
   ]
}
```

## See Also
<a name="API_SearchProducts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/SearchProducts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/SearchProducts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/SearchProducts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/SearchProducts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/SearchProducts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/SearchProducts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/SearchProducts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/SearchProducts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/SearchProducts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/SearchProducts)
