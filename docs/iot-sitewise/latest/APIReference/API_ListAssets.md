---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssets.html
---

# ListAssets
<a name="API_ListAssets"></a>

Retrieves a paginated list of asset summaries.

You can use this operation to do the following:
+ List assets based on a specific asset model.
+ List top-level assets.

You can't use this operation to list all assets. To retrieve summaries for all of your assets, use [ListAssetModels](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetModels.html) to get all of your asset model IDs. Then, use ListAssets to get all assets for each asset model.

## Request Syntax
<a name="API_ListAssets_RequestSyntax"></a>

```
GET /assets?assetModelId={{assetModelId}}&filter={{filter}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetModelId](#API_ListAssets_RequestSyntax) **   <a name="iotsitewise-ListAssets-request-uri-assetModelId"></a>
The ID of the asset model by which to filter the list of assets. This parameter is required if you choose `ALL` for `filter`. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`

 ** [filter](#API_ListAssets_RequestSyntax) **   <a name="iotsitewise-ListAssets-request-uri-filter"></a>
The filter for the requested list of assets. Choose one of the following options:
+  `ALL` – The list includes all assets for a given asset model ID. The `assetModelId` parameter is required if you filter by `ALL`.
+  `TOP_LEVEL` – The list includes only top-level assets in the asset hierarchy tree.
Default: `ALL`
Valid Values: `ALL | TOP_LEVEL`

 ** [maxResults](#API_ListAssets_RequestSyntax) **   <a name="iotsitewise-ListAssets-request-uri-maxResults"></a>
The maximum number of results to return for each paginated request.
Default: 50
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListAssets_RequestSyntax) **   <a name="iotsitewise-ListAssets-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

## Request Body
<a name="API_ListAssets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assetSummaries": [
      {
         "arn": "string",
         "assetModelId": "string",
         "creationDate": number,
         "description": "string",
         "externalId": "string",
         "hierarchies": [
            {
               "externalId": "string",
               "id": "string",
               "name": "string"
            }
         ],
         "id": "string",
         "lastUpdateDate": number,
         "name": "string",
         "status": {
            "error": {
               "code": "string",
               "details": [
                  {
                     "code": "string",
                     "message": "string"
                  }
               ],
               "message": "string"
            },
            "state": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAssets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assetSummaries](#API_ListAssets_ResponseSyntax) **   <a name="iotsitewise-ListAssets-response-assetSummaries"></a>
A list that summarizes each asset.
Type: Array of [AssetSummary](API_AssetSummary.md) objects

 ** [nextToken](#API_ListAssets_ResponseSyntax) **   <a name="iotsitewise-ListAssets-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_ListAssets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_ListAssets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/ListAssets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/ListAssets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ListAssets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/ListAssets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ListAssets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/ListAssets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/ListAssets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/ListAssets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/ListAssets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ListAssets)
