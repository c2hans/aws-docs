---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetRelationships.html
---

# ListAssetRelationships
<a name="API_ListAssetRelationships"></a>

Retrieves a paginated list of asset relationships for an asset. You can use this operation to identify an asset's root asset and all associated assets between that asset and its root.

## Request Syntax
<a name="API_ListAssetRelationships_RequestSyntax"></a>

```
GET /assets/{{assetId}}/assetRelationships?maxResults={{maxResults}}&nextToken={{nextToken}}&traversalType={{traversalType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssetRelationships_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetId](#API_ListAssetRelationships_RequestSyntax) **   <a name="iotsitewise-ListAssetRelationships-request-uri-assetId"></a>
The ID of the asset. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [maxResults](#API_ListAssetRelationships_RequestSyntax) **   <a name="iotsitewise-ListAssetRelationships-request-uri-maxResults"></a>
The maximum number of results to return for each paginated request.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListAssetRelationships_RequestSyntax) **   <a name="iotsitewise-ListAssetRelationships-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

 ** [traversalType](#API_ListAssetRelationships_RequestSyntax) **   <a name="iotsitewise-ListAssetRelationships-request-uri-traversalType"></a>
The type of traversal to use to identify asset relationships. Choose the following option:
+  `PATH_TO_ROOT` – Identify the asset's parent assets up to the root asset. The asset that you specify in `assetId` is the first result in the list of `assetRelationshipSummaries`, and the root asset is the last result.
Valid Values: `PATH_TO_ROOT`
Required: Yes

## Request Body
<a name="API_ListAssetRelationships_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssetRelationships_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assetRelationshipSummaries": [
      {
         "hierarchyInfo": {
            "childAssetId": "string",
            "parentAssetId": "string"
         },
         "relationshipType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAssetRelationships_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assetRelationshipSummaries](#API_ListAssetRelationships_ResponseSyntax) **   <a name="iotsitewise-ListAssetRelationships-response-assetRelationshipSummaries"></a>
A list that summarizes each asset relationship.
Type: Array of [AssetRelationshipSummary](API_AssetRelationshipSummary.md) objects

 ** [nextToken](#API_ListAssetRelationships_ResponseSyntax) **   <a name="iotsitewise-ListAssetRelationships-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_ListAssetRelationships_Errors"></a>

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
<a name="API_ListAssetRelationships_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/ListAssetRelationships)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/ListAssetRelationships)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ListAssetRelationships)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/ListAssetRelationships)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ListAssetRelationships)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/ListAssetRelationships)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/ListAssetRelationships)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/ListAssetRelationships)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/ListAssetRelationships)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ListAssetRelationships)
