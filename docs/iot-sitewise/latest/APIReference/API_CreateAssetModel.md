---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html
---

# CreateAssetModel
<a name="API_CreateAssetModel"></a>

Creates an asset model from specified property and hierarchy definitions. You create assets from asset models. With asset models, you can easily create assets of the same type that have standardized definitions. Each asset created from a model inherits the asset model's property and hierarchy definitions. For more information, see [Defining asset models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/define-models.html) in the * AWS IoT SiteWise User Guide*.

You can create three types of asset models, `ASSET_MODEL`, `COMPONENT_MODEL`, or an `INTERFACE`.
+  **ASSET\_MODEL** – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.
+  **COMPONENT\_MODEL** – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model.
+  **INTERFACE** – An interface is a type of model that defines a standard structure that can be applied to different asset models.

## Request Syntax
<a name="API_CreateAssetModel_RequestSyntax"></a>

```
POST /asset-models HTTP/1.1
Content-type: application/json

{
   "assetModelCompositeModels": [
      {
         "description": "{{string}}",
         "externalId": "{{string}}",
         "id": "{{string}}",
         "name": "{{string}}",
         "properties": [
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
         "type": "{{string}}"
      }
   ],
   "assetModelDescription": "{{string}}",
   "assetModelExternalId": "{{string}}",
   "assetModelHierarchies": [
      {
         "childAssetModelId": "{{string}}",
         "externalId": "{{string}}",
         "id": "{{string}}",
         "name": "{{string}}"
      }
   ],
   "assetModelId": "{{string}}",
   "assetModelName": "{{string}}",
   "assetModelProperties": [
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
   "assetModelType": "{{string}}",
   "clientToken": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAssetModel_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAssetModel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assetModelCompositeModels](#API_CreateAssetModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModel-request-assetModelCompositeModels"></a>
The composite models that are part of this asset model. It groups properties (such as attributes, measurements, transforms, and metrics) and child composite models that model parts of your industrial equipment. Each composite model has a type that defines the properties that the composite model supports. Use composite models to define alarms on this asset model.
When creating custom composite models, you need to use [CreateAssetModelCompositeModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html). For more information, see [Creating custom composite models (Components)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-custom-composite-models.html) in the * AWS IoT SiteWise User Guide*.
Type: Array of [AssetModelCompositeModelDefinition](API_AssetModelCompositeModelDefinition.md) objects
Required: No

 ** [assetModelDescription](#API_CreateAssetModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModel-request-assetModelDescription"></a>
A description for the asset model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [assetModelExternalId](#API_CreateAssetModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModel-request-assetModelExternalId"></a>
An external ID to assign to the asset model. The external ID must be unique within your AWS account. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** [assetModelHierarchies](#API_CreateAssetModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModel-request-assetModelHierarchies"></a>
The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see [Asset hierarchies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html) in the * AWS IoT SiteWise User Guide*.
You can specify up to 10 hierarchies per asset model. For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
Type: Array of [AssetModelHierarchyDefinition](API_AssetModelHierarchyDefinition.md) objects
Required: No

 ** [assetModelId](#API_CreateAssetModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModel-request-assetModelId"></a>
The ID to assign to the asset model, if desired. AWS IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** [assetModelName](#API_CreateAssetModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModel-request-assetModelName"></a>
A unique name for the asset model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** [assetModelProperties](#API_CreateAssetModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModel-request-assetModelProperties"></a>
The property definitions of the asset model. For more information, see [Asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html) in the * AWS IoT SiteWise User Guide*.
You can specify up to 200 properties per asset model. For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
Type: Array of [AssetModelPropertyDefinition](API_AssetModelPropertyDefinition.md) objects
Required: No

 ** [assetModelType](#API_CreateAssetModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModel-request-assetModelType"></a>
The type of asset model.
+  **ASSET\_MODEL** – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.
+  **COMPONENT\_MODEL** – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model.
Type: String
Valid Values: `ASSET_MODEL | COMPONENT_MODEL | INTERFACE`
Required: No

 ** [clientToken](#API_CreateAssetModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModel-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [tags](#API_CreateAssetModel_RequestSyntax) **   <a name="iotsitewise-CreateAssetModel-request-tags"></a>
A list of key-value pairs that contain metadata for the asset model. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the * AWS IoT SiteWise User Guide*.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateAssetModel_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "assetModelArn": "string",
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
<a name="API_CreateAssetModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [assetModelArn](#API_CreateAssetModel_ResponseSyntax) **   <a name="iotsitewise-CreateAssetModel-response-assetModelArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the asset model, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [assetModelId](#API_CreateAssetModel_ResponseSyntax) **   <a name="iotsitewise-CreateAssetModel-response-assetModelId"></a>
The ID of the asset model, in UUID format. You can use this ID when you call other AWS IoT SiteWise API operations.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetModelStatus](#API_CreateAssetModel_ResponseSyntax) **   <a name="iotsitewise-CreateAssetModel-response-assetModelStatus"></a>
The status of the asset model, which contains a state (`CREATING` after successfully calling this operation) and any error message.
Type: [AssetModelStatus](API_AssetModelStatus.md) object

## Errors
<a name="API_CreateAssetModel_Errors"></a>

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
<a name="API_CreateAssetModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreateAssetModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreateAssetModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreateAssetModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreateAssetModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreateAssetModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreateAssetModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreateAssetModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreateAssetModel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreateAssetModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreateAssetModel)
