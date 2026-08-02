---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetCatalogItem.html
---

# GetCatalogItem
<a name="API_GetCatalogItem"></a>

Gets information about the specified catalog item.

## Request Syntax
<a name="API_GetCatalogItem_RequestSyntax"></a>

```
GET /catalog/item/{{CatalogItemId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCatalogItem_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CatalogItemId](#API_GetCatalogItem_RequestSyntax) **   <a name="outposts-GetCatalogItem-request-uri-CatalogItemId"></a>
The ID of the catalog item.
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `OR-[A-Z0-9]{7}`
Required: Yes

## Request Body
<a name="API_GetCatalogItem_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCatalogItem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CatalogItem": {
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
      "SupportedStorage": [ "string" ],
      "SupportedUplinkGbps": [ number ],
      "WeightLbs": number
   }
}
```

## Response Elements
<a name="API_GetCatalogItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CatalogItem](#API_GetCatalogItem_ResponseSyntax) **   <a name="outposts-GetCatalogItem-response-CatalogItem"></a>
Information about this catalog item.
Type: [CatalogItem](API_CatalogItem.md) object

## Errors
<a name="API_GetCatalogItem_Errors"></a>

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
<a name="API_GetCatalogItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/GetCatalogItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/GetCatalogItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/GetCatalogItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/GetCatalogItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/GetCatalogItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/GetCatalogItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/GetCatalogItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/GetCatalogItem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/GetCatalogItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/GetCatalogItem)
