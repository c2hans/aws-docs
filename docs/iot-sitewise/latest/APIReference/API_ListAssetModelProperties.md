---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetModelProperties.html
---

# ListAssetModelProperties
<a name="API_ListAssetModelProperties"></a>

Retrieves a paginated list of properties associated with an asset model. If you update properties associated with the model before you finish listing all the properties, you need to start all over again.

## Request Syntax
<a name="API_ListAssetModelProperties_RequestSyntax"></a>

```
GET /asset-models/{{assetModelId}}/properties?assetModelVersion={{assetModelVersion}}&filter={{filter}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssetModelProperties_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetModelId](#API_ListAssetModelProperties_RequestSyntax) **   <a name="iotsitewise-ListAssetModelProperties-request-uri-assetModelId"></a>
The ID of the asset model. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [assetModelVersion](#API_ListAssetModelProperties_RequestSyntax) **   <a name="iotsitewise-ListAssetModelProperties-request-uri-assetModelVersion"></a>
The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is `LATEST`. See [ Asset model versions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html) in the * AWS IoT SiteWise User Guide*.
Pattern: `^(LATEST|ACTIVE)$`

 ** [filter](#API_ListAssetModelProperties_RequestSyntax) **   <a name="iotsitewise-ListAssetModelProperties-request-uri-filter"></a>
 Filters the requested list of asset model properties. You can choose one of the following options:
+  `ALL` – The list includes all asset model properties for a given asset model ID.
+  `BASE` – The list includes only base asset model properties for a given asset model ID.
Default: `BASE`
Valid Values: `ALL | BASE`

 ** [maxResults](#API_ListAssetModelProperties_RequestSyntax) **   <a name="iotsitewise-ListAssetModelProperties-request-uri-maxResults"></a>
The maximum number of results to return for each paginated request. If not specified, the default value is 50.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListAssetModelProperties_RequestSyntax) **   <a name="iotsitewise-ListAssetModelProperties-request-uri-nextToken"></a>
The token to be used for the next set of paginated results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

## Request Body
<a name="API_ListAssetModelProperties_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssetModelProperties_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assetModelPropertySummaries": [
      {
         "assetModelCompositeModelId": "string",
         "dataType": "string",
         "dataTypeSpec": "string",
         "externalId": "string",
         "id": "string",
         "interfaceSummaries": [
            {
               "interfaceAssetModelId": "string",
               "interfaceAssetModelPropertyId": "string"
            }
         ],
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
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAssetModelProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assetModelPropertySummaries](#API_ListAssetModelProperties_ResponseSyntax) **   <a name="iotsitewise-ListAssetModelProperties-response-assetModelPropertySummaries"></a>
A list that summarizes the properties associated with the specified asset model.
Type: Array of [AssetModelPropertySummary](API_AssetModelPropertySummary.md) objects

 ** [nextToken](#API_ListAssetModelProperties_ResponseSyntax) **   <a name="iotsitewise-ListAssetModelProperties-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_ListAssetModelProperties_Errors"></a>

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
<a name="API_ListAssetModelProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/ListAssetModelProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/ListAssetModelProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ListAssetModelProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/ListAssetModelProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ListAssetModelProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/ListAssetModelProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/ListAssetModelProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/ListAssetModelProperties)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/ListAssetModelProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ListAssetModelProperties)
