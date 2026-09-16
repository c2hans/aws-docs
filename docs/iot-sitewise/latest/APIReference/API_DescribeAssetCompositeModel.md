---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetCompositeModel.html
---

# DescribeAssetCompositeModel
<a name="API_DescribeAssetCompositeModel"></a>

Retrieves information about an asset composite model (also known as an asset component). An `AssetCompositeModel` is an instance of an `AssetModelCompositeModel`. If you want to see information about the model this is based on, call [DescribeAssetModelCompositeModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModelCompositeModel.html).

## Request Syntax
<a name="API_DescribeAssetCompositeModel_RequestSyntax"></a>

```
GET /assets/{{assetId}}/composite-models/{{assetCompositeModelId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAssetCompositeModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetCompositeModelId](#API_DescribeAssetCompositeModel_RequestSyntax) **   <a name="iotsitewise-DescribeAssetCompositeModel-request-uri-assetCompositeModelId"></a>
The ID of a composite model on this asset. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [assetId](#API_DescribeAssetCompositeModel_RequestSyntax) **   <a name="iotsitewise-DescribeAssetCompositeModel-request-uri-assetId"></a>
The ID of the asset. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

## Request Body
<a name="API_DescribeAssetCompositeModel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAssetCompositeModel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionDefinitions": [
      {
         "actionDefinitionId": "string",
         "actionName": "string",
         "actionType": "string"
      }
   ],
   "assetCompositeModelDescription": "string",
   "assetCompositeModelExternalId": "string",
   "assetCompositeModelId": "string",
   "assetCompositeModelName": "string",
   "assetCompositeModelPath": [
      {
         "id": "string",
         "name": "string"
      }
   ],
   "assetCompositeModelProperties": [
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
   "assetCompositeModelType": "string",
   "assetId": "string"
}
```

## Response Elements
<a name="API_DescribeAssetCompositeModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionDefinitions](#API_DescribeAssetCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetCompositeModel-response-actionDefinitions"></a>
The available actions for a composite model on this asset.
Type: Array of [ActionDefinition](API_ActionDefinition.md) objects

 ** [assetCompositeModelDescription](#API_DescribeAssetCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetCompositeModel-response-assetCompositeModelDescription"></a>
A description for the composite model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetCompositeModelExternalId](#API_DescribeAssetCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetCompositeModel-response-assetCompositeModelExternalId"></a>
An external ID to assign to the asset model.
If the composite model is a component-based composite model, or one nested inside a component model, you can only set the external ID using `UpdateAssetModelCompositeModel` and specifying the derived ID of the model or property from the created model it's a part of.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`

 ** [assetCompositeModelId](#API_DescribeAssetCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetCompositeModel-response-assetCompositeModelId"></a>
The ID of a composite model on this asset.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetCompositeModelName](#API_DescribeAssetCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetCompositeModel-response-assetCompositeModelName"></a>
The unique, friendly name for the composite model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetCompositeModelPath](#API_DescribeAssetCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetCompositeModel-response-assetCompositeModelPath"></a>
The path to the composite model listing the parent composite models.
Type: Array of [AssetCompositeModelPathSegment](API_AssetCompositeModelPathSegment.md) objects

 ** [assetCompositeModelProperties](#API_DescribeAssetCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetCompositeModel-response-assetCompositeModelProperties"></a>
The property definitions of the composite model that was used to create the asset.
Type: Array of [AssetProperty](API_AssetProperty.md) objects

 ** [assetCompositeModelSummaries](#API_DescribeAssetCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetCompositeModel-response-assetCompositeModelSummaries"></a>
The list of composite model summaries.
Type: Array of [AssetCompositeModelSummary](API_AssetCompositeModelSummary.md) objects

 ** [assetCompositeModelType](#API_DescribeAssetCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetCompositeModel-response-assetCompositeModelType"></a>
The composite model type. Valid values are `AWS/ALARM`, `CUSTOM`, or ` AWS/L4E_ANOMALY`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetId](#API_DescribeAssetCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetCompositeModel-response-assetId"></a>
The ID of the asset, in UUID format. This ID uniquely identifies the asset within AWS IoT SiteWise and can be used with other AWS IoT SiteWise APIs.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

## Errors
<a name="API_DescribeAssetCompositeModel_Errors"></a>

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
<a name="API_DescribeAssetCompositeModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeAssetCompositeModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeAssetCompositeModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeAssetCompositeModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeAssetCompositeModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeAssetCompositeModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeAssetCompositeModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeAssetCompositeModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeAssetCompositeModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeAssetCompositeModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeAssetCompositeModel)
