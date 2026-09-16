---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html
---

# CreateAssetModelCompositeModel
<a name="API_CreateAssetModelCompositeModel"></a>

Creates a custom composite model from specified property and hierarchy definitions. There are two types of custom composite models, `inline` and `component-model-based`.

Use component-model-based custom composite models to define standard, reusable components. A component-model-based custom composite model consists of a name, a description, and the ID of the component model it references. A component-model-based custom composite model has no properties of its own; its referenced component model provides its associated properties to any created assets. For more information, see [Custom composite models (Components)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html) in the * AWS IoT SiteWise User Guide*.

Use inline custom composite models to organize the properties of an asset model. The properties of inline custom composite models are local to the asset model where they are included and can't be used to create multiple assets.

To create a component-model-based model, specify the `composedAssetModelId` of an existing asset model with `assetModelType` of `COMPONENT_MODEL`.

To create an inline model, specify the `assetModelCompositeModelProperties` and don't include an `composedAssetModelId`.

## Request Syntax
<a name="API_CreateAssetModelCompositeModel_RequestSyntax"></a>

```
POST /asset-models/{{assetModelId}}/composite-models HTTP/1.1
If-Match: {{ifMatch}}
If-None-Match: {{ifNoneMatch}}
Match-For-Version-Type: {{matchForVersionType}}
Content-type: application/json

{
   "assetModelCompositeModelDescription": "{{string}}",
   "assetModelCompositeModelExternalId": "{{string}}",
   "assetModelCompositeModelId": "{{string}}",
   "assetModelCompositeModelName": "{{string}}",
   "assetModelCompositeModelProperties": [
      {
         "dataType": "{{string}}",
         "dataTypeSpec": "{{string}}",
         "externalId": "{{string}}",
         "id": "{{string}}",
         "name": "{{string}}",
         "type": {
            "attribute": {
               "defaultValue": "{{string}}"
            },
            "measurement": {
               "processingConfig": {
                  "forwardingConfig": {
                     "state": "{{string}}"
                  }
               }
            },
            "metric": {
               "expression": "{{string}}",
               "processingConfig": {
                  "computeLocation": "{{string}}"
               },
               "variables": [
                  {
                     "name": "{{string}}",
                     "value": {
                        "hierarchyId": "{{string}}",
                        "propertyId": "{{string}}",
                        "propertyPath": [
                           {
                              "id": "{{string}}",
                              "name": "{{string}}"
                           }
                        ]
                     }
                  }
               ],
               "window": {
                  "tumbling": {
                     "interval": "{{string}}",
                     "offset": "{{string}}"
                  }
               }
            },
            "transform": {
               "expression": "{{string}}",
               "processingConfig": {
                  "computeLocation": "{{string}}",
                  "forwardingConfig": {
                     "state": "{{string}}"
                  }
               },
               "variables": [
                  {
                     "name": "{{string}}",
                     "value": {
                        "hierarchyId": "{{string}}",
                        "propertyId": "{{string}}",
                        "propertyPath": [
                           {
                              "id": "{{string}}",
                              "name": "{{string}}"
                           }
                        ]
                     }
                  }
               ]
            }
         },
         "unit": "{{string}}"
      }
   ],
   "assetModelCompositeModelType": "{{string}}",
   "clientToken": "{{string}}",
   "composedAssetModelId": "{{string}}",
   "parentAssetModelCompositeModelId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAssetModelCompositeModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetModelId](#API_CreateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-request-uri-assetModelId"></a>
The ID of the asset model this composite model is a part of.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [ifMatch](#API_CreateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-request-ifMatch"></a>
The expected current entity tag (ETag) for the asset model’s latest or active version (specified using `matchForVersionType`). The create request is rejected if the tag does not match the latest or active version's current entity tag. See [Optimistic locking for asset model writes](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html) in the * AWS IoT SiteWise User Guide*.
Pattern: `^[\w-]{43}$`

 ** [ifNoneMatch](#API_CreateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-request-ifNoneMatch"></a>
Accepts **\*** to reject the create request if an active version (specified using `matchForVersionType` as `ACTIVE`) already exists for the asset model.
Pattern: `\*`

 ** [matchForVersionType](#API_CreateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-request-matchForVersionType"></a>
Specifies the asset model version type (`LATEST` or `ACTIVE`) used in conjunction with `If-Match` or `If-None-Match` headers to determine the target ETag for the create operation.
Valid Values: `LATEST | ACTIVE`

## Request Body
<a name="API_CreateAssetModelCompositeModel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assetModelCompositeModelDescription](#API_CreateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-request-assetModelCompositeModelDescription"></a>
A description for the composite model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [assetModelCompositeModelExternalId](#API_CreateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-request-assetModelCompositeModelExternalId"></a>
An external ID to assign to the composite model.
If the composite model is a derived composite model, or one nested inside a component model, you can only set the external ID using `UpdateAssetModelCompositeModel` and specifying the derived ID of the model or property from the created model it's a part of.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** [assetModelCompositeModelId](#API_CreateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-request-assetModelCompositeModelId"></a>
The ID of the composite model. AWS IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** [assetModelCompositeModelName](#API_CreateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-request-assetModelCompositeModelName"></a>
A unique name for the composite model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** [assetModelCompositeModelProperties](#API_CreateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-request-assetModelCompositeModelProperties"></a>
The property definitions of the composite model. For more information, see [ Inline custom composite models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html#inline-composite-models) in the * AWS IoT SiteWise User Guide*.
You can specify up to 200 properties per composite model. For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
Type: Array of [AssetModelPropertyDefinition](API_AssetModelPropertyDefinition.md) objects
Required: No

 ** [assetModelCompositeModelType](#API_CreateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-request-assetModelCompositeModelType"></a>
The composite model type. Valid values are `AWS/ALARM`, `CUSTOM`, or ` AWS/L4E_ANOMALY`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** [clientToken](#API_CreateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [composedAssetModelId](#API_CreateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-request-composedAssetModelId"></a>
The ID of a component model which is reused to create this composite model.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** [parentAssetModelCompositeModelId](#API_CreateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-request-parentAssetModelCompositeModelId"></a>
The ID of the parent composite model in this asset model relationship.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

## Response Syntax
<a name="API_CreateAssetModelCompositeModel_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "assetModelCompositeModelId": "string",
   "assetModelCompositeModelPath": [
      {
         "id": "string",
         "name": "string"
      }
   ],
   "assetModelId": "string",
   "assetModelStatus": {
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
<a name="API_CreateAssetModelCompositeModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [assetModelCompositeModelId](#API_CreateAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-response-assetModelCompositeModelId"></a>
The ID of the composed asset model. You can use this ID when you call other AWS IoT SiteWise APIs.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetModelCompositeModelPath](#API_CreateAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-response-assetModelCompositeModelPath"></a>
The path to the composite model listing the parent composite models.
Type: Array of [AssetModelCompositeModelPathSegment](API_AssetModelCompositeModelPathSegment.md) objects

 ** [assetModelId](#API_CreateAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-response-assetModelId"></a>
The ID of the asset model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetModelStatus](#API_CreateAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-CreateAssetModelCompositeModel-response-assetModelStatus"></a>
Contains current status information for an asset model. For more information, see [Asset and model states](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-and-model-states.html) in the * AWS IoT SiteWise User Guide*.
Type: [AssetModelStatus](API_AssetModelStatus.md) object

## Errors
<a name="API_CreateAssetModelCompositeModel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

 ** PreconditionFailedException **
The precondition in one or more of the request-header fields evaluated to `FALSE`.
 ** resourceArn **
The ARN of the resource on which precondition failed with this operation.
 ** resourceId **
The ID of the resource on which precondition failed with this operation.
HTTP Status Code: 412

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** resourceArn **
The ARN of the resource that already exists.
 ** resourceId **
The ID of the resource that already exists.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_CreateAssetModelCompositeModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreateAssetModelCompositeModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreateAssetModelCompositeModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreateAssetModelCompositeModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreateAssetModelCompositeModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreateAssetModelCompositeModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreateAssetModelCompositeModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreateAssetModelCompositeModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreateAssetModelCompositeModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreateAssetModelCompositeModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreateAssetModelCompositeModel)
