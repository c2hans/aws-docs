---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetProperty.html
---

# DescribeAssetProperty
<a name="API_DescribeAssetProperty"></a>

Retrieves information about an asset property.

**Note**
When you call this operation for an attribute property, this response includes the default attribute value that you define in the asset model. If you update the default value in the model, this operation's response includes the new default value.

This operation doesn't return the value of the asset property. To get the value of an asset property, use [GetAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValue.html).

## Request Syntax
<a name="API_DescribeAssetProperty_RequestSyntax"></a>

```
GET /assets/{{assetId}}/properties/{{propertyId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAssetProperty_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetId](#API_DescribeAssetProperty_RequestSyntax) **   <a name="iotsitewise-DescribeAssetProperty-request-uri-assetId"></a>
The ID of the asset. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [propertyId](#API_DescribeAssetProperty_RequestSyntax) **   <a name="iotsitewise-DescribeAssetProperty-request-uri-propertyId"></a>
The ID of the asset property. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

## Request Body
<a name="API_DescribeAssetProperty_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAssetProperty_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assetExternalId": "string",
   "assetId": "string",
   "assetModelId": "string",
   "assetName": "string",
   "assetProperty": {
      "alias": "string",
      "dataType": "string",
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
   },
   "compositeModel": {
      "assetProperty": {
         "alias": "string",
         "dataType": "string",
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
      },
      "externalId": "string",
      "id": "string",
      "name": "string",
      "type": "string"
   }
}
```

## Response Elements
<a name="API_DescribeAssetProperty_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assetExternalId](#API_DescribeAssetProperty_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetProperty-response-assetExternalId"></a>
The external ID of the asset. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`

 ** [assetId](#API_DescribeAssetProperty_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetProperty-response-assetId"></a>
The ID of the asset, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetModelId](#API_DescribeAssetProperty_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetProperty-response-assetModelId"></a>
The ID of the asset model, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetName](#API_DescribeAssetProperty_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetProperty-response-assetName"></a>
The name of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [assetProperty](#API_DescribeAssetProperty_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetProperty-response-assetProperty"></a>
The asset property's definition, alias, and notification state.
This response includes this object for normal asset properties. If you describe an asset property in a composite model, this response includes the asset property information in `compositeModel`.
Type: [Property](API_Property.md) object

 ** [compositeModel](#API_DescribeAssetProperty_ResponseSyntax) **   <a name="iotsitewise-DescribeAssetProperty-response-compositeModel"></a>
The composite model that declares this asset property, if this asset property exists in a composite model.
Type: [CompositeModelProperty](API_CompositeModelProperty.md) object

## Errors
<a name="API_DescribeAssetProperty_Errors"></a>

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
<a name="API_DescribeAssetProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeAssetProperty)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeAssetProperty)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeAssetProperty)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeAssetProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeAssetProperty)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeAssetProperty)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeAssetProperty)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeAssetProperty)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeAssetProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeAssetProperty)
