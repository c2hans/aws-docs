---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html
---

# DescribeAssetModel
<a name="API_DescribeAssetModel"></a>

Retrieves information about an asset model. This includes details about the asset model's properties, hierarchies, composite models, and any interface relationships if the asset model implements interfaces.

## Request Syntax
<a name="API_DescribeAssetModel_RequestSyntax"></a>

```
GET /asset-models/{{assetModelId}}?assetModelVersion={{assetModelVersion}}&excludeProperties={{excludeProperties}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAssetModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetModelId](#API_DescribeAssetModel_RequestSyntax) **   <a name="iotsitewise-DescribeAssetModel-request-uri-assetModelId"></a>
The ID of the asset model. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [assetModelVersion](#API_DescribeAssetModel_RequestSyntax) **   <a name="iotsitewise-DescribeAssetModel-request-uri-assetModelVersion"></a>
The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is `LATEST`. See [ Asset model versions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html) in the * AWS IoT SiteWise User Guide*.
Pattern: `^(LATEST|ACTIVE)$`

 ** [excludeProperties](#API_DescribeAssetModel_RequestSyntax) **   <a name="iotsitewise-DescribeAssetModel-request-uri-excludeProperties"></a>
 Whether or not to exclude asset model properties from the response.

## Request Body
<a name="API_DescribeAssetModel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAssetModel_ResponseSyntax"></a>

```
HTTP/1.1 200
ETag: {{eTag}}
Content-type: application/json

{
   "assetModelArn": "string",
   "assetModelCompositeModels": [
      {
         "description": "string",
         "externalId": "string",
         "id": "string",
         "name": "string",
         "properties": [
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
         "type": "string"
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
   "assetModelCreationDate": number,
   "assetModelDescription": "string",
   "assetModelExternalId": "string",
   "assetModelHierarchies": [
      {
         "childAssetModelId": "string",
         "externalId": "string",
         "id": "string",
         "name": "string"
      }
   ],
   "assetModelId": "string",
   "assetModelLastUpdateDate": number,
   "assetModelName": "string",
   "assetModelProperties": [
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
   },
   "assetModelType": "string",
   "assetModelVersion": "string",
   "interfaceDetails": [
      {
         "id": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeAssetModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [eTag](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-eTag"></a>
The entity tag (ETag) is a hash of the retrieved version of the asset model. It's used to make concurrent updates safely to the resource. See [Optimistic locking for asset model writes](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html) in the * AWS IoT SiteWise User Guide*.
See [ Optimistic locking for asset model writes](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html) in the * AWS IoT SiteWise User Guide*.
Pattern: `^[\w-]{43}$`

The following data is returned in JSON format by the service.

 ** [assetModelArn](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the asset model, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [assetModelCompositeModels](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelCompositeModels"></a>
The list of built-in composite models for the asset model, such as those with those of type `AWS/ALARMS`.
Type: Array of [AssetModelCompositeModel](API_AssetModelCompositeModel.md) objects

 ** [assetModelCompositeModelSummaries](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelCompositeModelSummaries"></a>
The list of the immediate child custom composite model summaries for the asset model.
Type: Array of [AssetModelCompositeModelSummary](API_AssetModelCompositeModelSummary.md) objects

 ** [assetModelCreationDate](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelCreationDate"></a>
The date the asset model was created, in Unix epoch time.
Type: Timestamp

 ** [assetModelDescription](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelDescription"></a>
The asset model's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetModelExternalId](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelExternalId"></a>
The external ID of the asset model, if any.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`

 ** [assetModelHierarchies](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelHierarchies"></a>
A list of asset model hierarchies that each contain a `childAssetModelId` and a `hierarchyId` (named `id`). A hierarchy specifies allowed parent/child asset relationships for an asset model.
Type: Array of [AssetModelHierarchy](API_AssetModelHierarchy.md) objects

 ** [assetModelId](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelId"></a>
The ID of the asset model, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetModelLastUpdateDate](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelLastUpdateDate"></a>
The date the asset model was last updated, in Unix epoch time.
Type: Timestamp

 ** [assetModelName](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelName"></a>
The name of the asset model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetModelProperties](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelProperties"></a>
The list of asset properties for the asset model.
This object doesn't include properties that you define in composite models. You can find composite model properties in the `assetModelCompositeModels` object.
Type: Array of [AssetModelProperty](API_AssetModelProperty.md) objects

 ** [assetModelStatus](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelStatus"></a>
The current status of the asset model, which contains a state and any error message.
Type: [AssetModelStatus](API_AssetModelStatus.md) object

 ** [assetModelType](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelType"></a>
The type of asset model.
+  **ASSET\_MODEL** – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.
+  **COMPONENT\_MODEL** – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model.
Type: String
Valid Values: `ASSET_MODEL | COMPONENT_MODEL | INTERFACE`

 ** [assetModelVersion](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-assetModelVersion"></a>
The version of the asset model. See [ Asset model versions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

 ** [interfaceDetails](#API_DescribeAssetModel_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetModel-response-interfaceDetails"></a>
A list of interface details that describe the interfaces implemented by this asset model, including interface asset model IDs and property mappings.
Type: Array of [InterfaceRelationship](API_InterfaceRelationship.md) objects

## Errors
<a name="API_DescribeAssetModel_Errors"></a>

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
<a name="API_DescribeAssetModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeAssetModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeAssetModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeAssetModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeAssetModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeAssetModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeAssetModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeAssetModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeAssetModel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeAssetModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeAssetModel)
