---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListCatalogItems.html
---

# ListCatalogItems
<a name="API_ListCatalogItems"></a>

Lists the items in the catalog.

Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.

## Request Syntax
<a name="API_ListCatalogItems_RequestSyntax"></a>

```
GET /catalog/items?EC2FamilyFilter={{EC2FamilyFilter}}&ItemClassFilter={{ItemClassFilter}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&SupportedStorageFilter={{SupportedStorageFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCatalogItems_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EC2FamilyFilter](#API_ListCatalogItems_RequestSyntax) **   <a name="outposts-ListCatalogItems-request-uri-EC2FamilyFilter"></a>
Filters the results by EC2 family (for example, M5).
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^[a-z0-9]+[a-z0-9-]*[a-z0-9]+$`

 ** [ItemClassFilter](#API_ListCatalogItems_RequestSyntax) **   <a name="outposts-ListCatalogItems-request-uri-ItemClassFilter"></a>
Filters the results by item class.
Valid Values: `RACK | SERVER`

 ** [MaxResults](#API_ListCatalogItems_RequestSyntax) **   <a name="outposts-ListCatalogItems-request-uri-MaxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListCatalogItems_RequestSyntax) **   <a name="outposts-ListCatalogItems-request-uri-NextToken"></a>
The pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [SupportedStorageFilter](#API_ListCatalogItems_RequestSyntax) **   <a name="outposts-ListCatalogItems-request-uri-SupportedStorageFilter"></a>
Filters the results by storage option.
Valid Values: `EBS | S3`

## Request Body
<a name="API_ListCatalogItems_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCatalogItems_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CatalogItems": [
      {
         "CatalogItemId": "string",
         "EC2Capacities": [
            {
               "Family": "string",
               "MaxSize": "string",
               "Quantity": "string"
            }
         ],
         "ItemStatus": "string",
         "PowerKva": number,
         "RackScalingType": "string",
         "SupportedStorage": [ "string" ],
         "SupportedUplinkGbps": [ number ],
         "WeightLbs": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCatalogItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CatalogItems](#API_ListCatalogItems_ResponseSyntax) **   <a name="outposts-ListCatalogItems-response-CatalogItems"></a>
Information about the catalog items.
Type: Array of [CatalogItem](API_CatalogItem.md) objects

 ** [NextToken](#API_ListCatalogItems_ResponseSyntax) **   <a name="outposts-ListCatalogItems-response-NextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

## Errors
<a name="API_ListCatalogItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListCatalogItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/ListCatalogItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/ListCatalogItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ListCatalogItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/ListCatalogItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ListCatalogItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/ListCatalogItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/ListCatalogItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/ListCatalogItems)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/ListCatalogItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ListCatalogItems)
