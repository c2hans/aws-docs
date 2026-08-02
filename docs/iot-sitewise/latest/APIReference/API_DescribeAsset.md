---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html
---

# DescribeAsset
<a name="API_DescribeAsset"></a>

Retrieves information about an asset.

## Request Syntax
<a name="API_DescribeAsset_RequestSyntax"></a>

```
GET /assets/{{assetId}}?excludeProperties={{excludeProperties}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAsset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetId](#API_DescribeAsset_RequestSyntax) **   <a name="iotsitewise-DescribeAsset-request-uri-assetId"></a>
The ID of the asset. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [excludeProperties](#API_DescribeAsset_RequestSyntax) **   <a name="iotsitewise-DescribeAsset-request-uri-excludeProperties"></a>
 Whether or not to exclude asset properties from the response.

## Request Body
<a name="API_DescribeAsset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAsset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assetArn": "string",
   "assetCompositeModels": [
      {
         "description": "string",
         "externalId": "string",
         "id": "string",
         "name": "string",
         "properties": [
            {
               "alias": "string",
               "dataType": "string",
               "dataTypeSpec": "string",
               "externalId": "string",
               "id": "string",
               "name": "string",
               "notification": {
                  "state": "string",
                  "topic": "string"
               },
               "path": [
                  {
                     "id": "string",
                     "name": "string"
                  }
               ],
               "unit": "string"
            }
         ],
         "type": "string"
      }
   ],
   "assetCompositeModelSummaries": [
      {
         "description": "string",
         "externalId": "string",
         "id": "string",
         "name": "string",
         "path": [
            {
               "id": "string",
               "name": "string"
            }
         ],
         "type": "string"
      }
   ],
   "assetCreationDate": number,
   "assetDescription": "string",
   "assetExternalId": "string",
   "assetHierarchies": [
      {
         "externalId": "string",
         "id": "string",
         "name": "string"
      }
   ],
   "assetId": "string",
   "assetLastUpdateDate": number,
   "assetModelId": "string",
   "assetName": "string",
   "assetProperties": [
      {
         "alias": "string",
         "dataType": "string",
         "dataTypeSpec": "string",
         "externalId": "string",
         "id": "string",
         "name": "string",
         "notification": {
            "state": "string",
            "topic": "string"
         },
         "path": [
            {
               "id": "string",
               "name": "string"
            }
         ],
         "unit": "string"
      }
   ],
   "assetStatus": {
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
```

## Response Elements
<a name="API_DescribeAsset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assetArn](#API_DescribeAsset_ResponseSyntax) **   <a name="iotsitewise-DescribeAsset-response-assetArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the asset, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:asset/${AssetId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [assetCompositeModels](#API_DescribeAsset_ResponseSyntax) **   <a name="iotsitewise-DescribeAsset-response-assetCompositeModels"></a>
The composite models for the asset.
Type: Array of [AssetCompositeModel](API_AssetCompositeModel.md) objects

 ** [assetCompositeModelSummaries](#API_DescribeAsset_ResponseSyntax) **   <a name="iotsitewise-DescribeAsset-response-assetCompositeModelSummaries"></a>
The list of the immediate child custom composite model summaries for the asset.
Type: Array of [AssetCompositeModelSummary](API_AssetCompositeModelSummary.md) objects

 ** [assetCreationDate](#API_DescribeAsset_ResponseSyntax) **   <a name="iotsitewise-DescribeAsset-response-assetCreationDate"></a>
The date the asset was created, in Unix epoch time.
Type: Timestamp

 ** [assetDescription](#API_DescribeAsset_ResponseSyntax) **   <a name="iotsitewise-DescribeAsset-response-assetDescription"></a>
A description for the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetExternalId](#API_DescribeAsset_ResponseSyntax) **   <a name="iotsitewise-DescribeAsset-response-assetExternalId"></a>
The external ID of the asset, if any.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`

 ** [assetHierarchies](#API_DescribeAsset_ResponseSyntax) **   <a name="iotsitewise-DescribeAsset-response-assetHierarchies"></a>
A list of asset hierarchies that each contain a `hierarchyId`. A hierarchy specifies allowed parent/child asset relationships.
Type: Array of [AssetHierarchy](API_AssetHierarchy.md) objects

 ** [assetId](#API_DescribeAsset_ResponseSyntax) **   <a name="iotsitewise-DescribeAsset-response-assetId"></a>
The ID of the asset, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetLastUpdateDate](#API_DescribeAsset_ResponseSyntax) **   <a name="iotsitewise-DescribeAsset-response-assetLastUpdateDate"></a>
The date the asset was last updated, in Unix epoch time.
Type: Timestamp

 ** [assetModelId](#API_DescribeAsset_ResponseSyntax) **   <a name="iotsitewise-DescribeAsset-response-assetModelId"></a>
The ID of the asset model that was used to create the asset.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetName](#API_DescribeAsset_ResponseSyntax) **   <a name="iotsitewise-DescribeAsset-response-assetName"></a>
The name of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetProperties](#API_DescribeAsset_ResponseSyntax) **   <a name="iotsitewise-DescribeAsset-response-assetProperties"></a>
The list of asset properties for the asset.
This object doesn't include properties that you define in composite models. You can find composite model properties in the `assetCompositeModels` object.
Type: Array of [AssetProperty](API_AssetProperty.md) objects

 ** [assetStatus](#API_DescribeAsset_ResponseSyntax) **   <a name="iotsitewise-DescribeAsset-response-assetStatus"></a>
The current status of the asset, which contains a state and any error message.
Type: [AssetStatus](API_AssetStatus.md) object

## Errors
<a name="API_DescribeAsset_Errors"></a>

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
<a name="API_DescribeAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeAsset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeAsset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeAsset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeAsset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeAsset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeAsset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeAsset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeAsset)
