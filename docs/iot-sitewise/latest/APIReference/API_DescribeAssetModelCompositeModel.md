---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModelCompositeModel.html
---

# DescribeAssetModelCompositeModel
<a name="API_DescribeAssetModelCompositeModel"></a>

Retrieves information about an asset model composite model (also known as an asset model component). For more information, see [Custom composite models (Components)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html) in the * AWS IoT SiteWise User Guide*.

## Request Syntax
<a name="API_DescribeAssetModelCompositeModel_RequestSyntax"></a>

```
GET /asset-models/{{assetModelId}}/composite-models/{{assetModelCompositeModelId}}?assetModelVersion={{assetModelVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAssetModelCompositeModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetModelCompositeModelId](#API_DescribeAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-request-uri-assetModelCompositeModelId"></a>
The ID of a composite model on this asset model. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [assetModelId](#API_DescribeAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-request-uri-assetModelId"></a>
The ID of the asset model. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [assetModelVersion](#API_DescribeAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-request-uri-assetModelVersion"></a>
The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is `LATEST`. See [ Asset model versions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html) in the * AWS IoT SiteWise User Guide*.
Pattern: `^(LATEST|ACTIVE)$`

## Request Body
<a name="API_DescribeAssetModelCompositeModel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAssetModelCompositeModel_ResponseSyntax"></a>

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
   "assetModelCompositeModelDescription": "string",
   "assetModelCompositeModelExternalId": "string",
   "assetModelCompositeModelId": "string",
   "assetModelCompositeModelName": "string",
   "assetModelCompositeModelPath": [
      {
         "id": "string",
         "name": "string"
      }
   ],
   "assetModelCompositeModelProperties": [
      {
         "dataType": "string",
         "dataTypeSpec": "string",
         "externalId": "string",
         "id": "string",
         "name": "string",
         "path": [
            {
               "id": "string",
               "name": "string"
            }
         ],
         "type": {
            "attribute": {
               "defaultValue": "string"
            },
            "measurement": {
               "processingConfig": {
                  "forwardingConfig": {
                     "state": "string"
                  }
               }
            },
            "metric": {
               "expression": "string",
               "processingConfig": {
                  "computeLocation": "string"
               },
               "variables": [
                  {
                     "name": "string",
                     "value": {
                        "hierarchyId": "string",
                        "propertyId": "string",
                        "propertyPath": [
                           {
                              "id": "string",
                              "name": "string"
                           }
                        ]
                     }
                  }
               ],
               "window": {
                  "tumbling": {
                     "interval": "string",
                     "offset": "string"
                  }
               }
            },
            "transform": {
               "expression": "string",
               "processingConfig": {
                  "computeLocation": "string",
                  "forwardingConfig": {
                     "state": "string"
                  }
               },
               "variables": [
                  {
                     "name": "string",
                     "value": {
                        "hierarchyId": "string",
                        "propertyId": "string",
                        "propertyPath": [
                           {
                              "id": "string",
                              "name": "string"
                           }
                        ]
                     }
                  }
               ]
            }
         },
         "unit": "string"
      }
   ],
   "assetModelCompositeModelSummaries": [
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
   "assetModelCompositeModelType": "string",
   "assetModelId": "string",
   "compositionDetails": {
      "compositionRelationship": [
         {
            "id": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeAssetModelCompositeModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionDefinitions](#API_DescribeAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-response-actionDefinitions"></a>
The available actions for a composite model on this asset model.
Type: Array of [ActionDefinition](API_ActionDefinition.md) objects

 ** [assetModelCompositeModelDescription](#API_DescribeAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-response-assetModelCompositeModelDescription"></a>
The description for the composite model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetModelCompositeModelExternalId](#API_DescribeAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-response-assetModelCompositeModelExternalId"></a>
The external ID of a composite model on this asset model.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`

 ** [assetModelCompositeModelId](#API_DescribeAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-response-assetModelCompositeModelId"></a>
The ID of a composite model on this asset model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetModelCompositeModelName](#API_DescribeAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-response-assetModelCompositeModelName"></a>
The unique, friendly name for the composite model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetModelCompositeModelPath](#API_DescribeAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-response-assetModelCompositeModelPath"></a>
The path to the composite model listing the parent composite models.
Type: Array of [AssetModelCompositeModelPathSegment](API_AssetModelCompositeModelPathSegment.md) objects

 ** [assetModelCompositeModelProperties](#API_DescribeAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-response-assetModelCompositeModelProperties"></a>
The property definitions of the composite model.
Type: Array of [AssetModelProperty](API_AssetModelProperty.md) objects

 ** [assetModelCompositeModelSummaries](#API_DescribeAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-response-assetModelCompositeModelSummaries"></a>
The list of composite model summaries for the composite model.
Type: Array of [AssetModelCompositeModelSummary](API_AssetModelCompositeModelSummary.md) objects

 ** [assetModelCompositeModelType](#API_DescribeAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-response-assetModelCompositeModelType"></a>
The composite model type. Valid values are `AWS/ALARM`, `CUSTOM`, or ` AWS/L4E_ANOMALY`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetModelId](#API_DescribeAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-response-assetModelId"></a>
The ID of the asset model, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [compositionDetails](#API_DescribeAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModelCompositeModel-response-compositionDetails"></a>
Metadata for the composition relationship established by using `composedAssetModelId` in [`CreateAssetModelCompositeModel`](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html). For instance, an array detailing the path of the composition relationship for this composite model.
Type: [CompositionDetails](API_CompositionDetails.md) object

## Errors
<a name="API_DescribeAssetModelCompositeModel_Errors"></a>

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
<a name="API_DescribeAssetModelCompositeModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeAssetModelCompositeModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeAssetModelCompositeModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeAssetModelCompositeModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeAssetModelCompositeModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeAssetModelCompositeModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeAssetModelCompositeModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeAssetModelCompositeModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeAssetModelCompositeModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeAssetModelCompositeModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeAssetModelCompositeModel)
