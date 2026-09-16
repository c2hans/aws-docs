---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListCompositionRelationships.html
---

# ListCompositionRelationships
<a name="API_ListCompositionRelationships"></a>

Retrieves a paginated list of composition relationships for an asset model of type `COMPONENT_MODEL`.

## Request Syntax
<a name="API_ListCompositionRelationships_RequestSyntax"></a>

```
GET /asset-models/{{assetModelId}}/composition-relationships?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCompositionRelationships_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetModelId](#API_ListCompositionRelationships_RequestSyntax) **   <a name="iotsitewise-ListCompositionRelationships-request-uri-assetModelId"></a>
The ID of the asset model. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** [maxResults](#API_ListCompositionRelationships_RequestSyntax) **   <a name="iotsitewise-ListCompositionRelationships-request-uri-maxResults"></a>
The maximum number of results to return for each paginated request.
Default: 50
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListCompositionRelationships_RequestSyntax) **   <a name="iotsitewise-ListCompositionRelationships-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

## Request Body
<a name="API_ListCompositionRelationships_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCompositionRelationships_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "compositionRelationshipSummaries": [
      {
         "assetModelCompositeModelId": "string",
         "assetModelCompositeModelType": "string",
         "assetModelId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCompositionRelationships_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [compositionRelationshipSummaries](#API_ListCompositionRelationships_ResponseSyntax) **   <a name="iotsitewise-ListCompositionRelationships-response-compositionRelationshipSummaries"></a>
A list that summarizes each composition relationship.
Type: Array of [CompositionRelationshipSummary](API_CompositionRelationshipSummary.md) objects

 ** [nextToken](#API_ListCompositionRelationships_ResponseSyntax) **   <a name="iotsitewise-ListCompositionRelationships-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_ListCompositionRelationships_Errors"></a>

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
<a name="API_ListCompositionRelationships_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/ListCompositionRelationships)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/ListCompositionRelationships)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ListCompositionRelationships)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/ListCompositionRelationships)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ListCompositionRelationships)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/ListCompositionRelationships)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/ListCompositionRelationships)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/ListCompositionRelationships)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/ListCompositionRelationships)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ListCompositionRelationships)
