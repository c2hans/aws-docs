---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html
---

# UpdateAssetModel
<a name="API_UpdateAssetModel"></a>

Updates an asset model and all of the assets that were created from the model. Each asset created from the model inherits the updated asset model's property and hierarchy definitions. For more information, see [Updating assets and models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html) in the * AWS IoT SiteWise User Guide*.

**Important**
If you remove a property from an asset model, AWS IoT SiteWise deletes all previous data for that property. You can’t change the type or data type of an existing property.
To replace an existing asset model property with a new one with the same `name`, do the following:
Submit an `UpdateAssetModel` request with the entire existing property removed.
Submit a second `UpdateAssetModel` request that includes the new property. The new asset property will have the same `name` as the previous one and AWS IoT SiteWise will generate a new unique `id`.

## Request Syntax
<a name="API_UpdateAssetModel_RequestSyntax"></a>

```
PUT /asset-models/{{assetModelId}} HTTP/1.1
If-Match: {{ifMatch}}
If-None-Match: {{ifNoneMatch}}
Match-For-Version-Type: {{matchForVersionType}}
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
               "path": [
                  {
                     "id": "{{string}}",
                     "name": "{{string}}"
                  }
               ],
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
   "assetModelName": "{{string}}",
   "assetModelProperties": [
      {
         "dataType": "{{string}}",
         "dataTypeSpec": "{{string}}",
         "externalId": "{{string}}",
         "id": "{{string}}",
         "name": "{{string}}",
         "path": [
            {
               "id": "{{string}}",
               "name": "{{string}}"
            }
         ],
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
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAssetModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetModelId](#API_UpdateAssetModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModel-request-uri-assetModelId"></a>
The ID of the asset model to update. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [ifMatch](#API_UpdateAssetModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModel-request-ifMatch"></a>
The expected current entity tag (ETag) for the asset model’s latest or active version (specified using `matchForVersionType`). The update request is rejected if the tag does not match the latest or active version's current entity tag. See [Optimistic locking for asset model writes](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html) in the * AWS IoT SiteWise User Guide*.
Pattern: `^[\w-]{43}$`

 ** [ifNoneMatch](#API_UpdateAssetModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModel-request-ifNoneMatch"></a>
Accepts **\*** to reject the update request if an active version (specified using `matchForVersionType` as `ACTIVE`) already exists for the asset model.
Pattern: `\*`

 ** [matchForVersionType](#API_UpdateAssetModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModel-request-matchForVersionType"></a>
Specifies the asset model version type (`LATEST` or `ACTIVE`) used in conjunction with `If-Match` or `If-None-Match` headers to determine the target ETag for the update operation.
Valid Values: `LATEST | ACTIVE`

## Request Body
<a name="API_UpdateAssetModel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assetModelCompositeModels](#API_UpdateAssetModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModel-request-assetModelCompositeModels"></a>
The composite models that are part of this asset model. It groups properties (such as attributes, measurements, transforms, and metrics) and child composite models that model parts of your industrial equipment. Each composite model has a type that defines the properties that the composite model supports. Use composite models to define alarms on this asset model.
When creating custom composite models, you need to use [CreateAssetModelCompositeModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html). For more information, see [Creating custom composite models (Components)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-custom-composite-models.html) in the * AWS IoT SiteWise User Guide*.
Type: Array of [AssetModelCompositeModel](API_AssetModelCompositeModel.md) objects
Required: No

 ** [assetModelDescription](#API_UpdateAssetModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModel-request-assetModelDescription"></a>
A description for the asset model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [assetModelExternalId](#API_UpdateAssetModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModel-request-assetModelExternalId"></a>
An external ID to assign to the asset model. The asset model must not already have an external ID. The external ID must be unique within your AWS account. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** [assetModelHierarchies](#API_UpdateAssetModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModel-request-assetModelHierarchies"></a>
The updated hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see [Asset hierarchies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html) in the * AWS IoT SiteWise User Guide*.
You can specify up to 10 hierarchies per asset model. For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
Type: Array of [AssetModelHierarchy](API_AssetModelHierarchy.md) objects
Required: No

 ** [assetModelName](#API_UpdateAssetModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModel-request-assetModelName"></a>
A unique name for the asset model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** [assetModelProperties](#API_UpdateAssetModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModel-request-assetModelProperties"></a>
The updated property definitions of the asset model. For more information, see [Asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html) in the * AWS IoT SiteWise User Guide*.
You can specify up to 200 properties per asset model. For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
Type: Array of [AssetModelProperty](API_AssetModelProperty.md) objects
Required: No

 ** [clientToken](#API_UpdateAssetModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModel-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

## Response Syntax
<a name="API_UpdateAssetModel_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
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
<a name="API_UpdateAssetModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [assetModelId](#API_UpdateAssetModel_ResponseSyntax) **   <a name="iotsitewise-UpdateAssetModel-response-assetModelId"></a>
The ID of the asset model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetModelStatus](#API_UpdateAssetModel_ResponseSyntax) **   <a name="iotsitewise-UpdateAssetModel-response-assetModelStatus"></a>
The status of the asset model, which contains a state (`UPDATING` after successfully calling this operation) and any error message.
Type: [AssetModelStatus](API_AssetModelStatus.md) object

## Errors
<a name="API_UpdateAssetModel_Errors"></a>

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
<a name="API_UpdateAssetModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/UpdateAssetModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/UpdateAssetModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/UpdateAssetModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/UpdateAssetModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/UpdateAssetModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/UpdateAssetModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/UpdateAssetModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/UpdateAssetModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/UpdateAssetModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/UpdateAssetModel)
