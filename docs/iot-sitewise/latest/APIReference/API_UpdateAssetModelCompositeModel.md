---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModelCompositeModel.html
---

# UpdateAssetModelCompositeModel
<a name="API_UpdateAssetModelCompositeModel"></a>

Updates a composite model and all of the assets that were created from the model. Each asset created from the model inherits the updated asset model's property and hierarchy definitions. For more information, see [Updating assets and models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html) in the * AWS IoT SiteWise User Guide*.

**Important**
If you remove a property from a composite asset model, AWS IoT SiteWise deletes all previous data for that property. You can’t change the type or data type of an existing property.
To replace an existing composite asset model property with a new one with the same `name`, do the following:
Submit an `UpdateAssetModelCompositeModel` request with the entire existing property removed.
Submit a second `UpdateAssetModelCompositeModel` request that includes the new property. The new asset property will have the same `name` as the previous one and AWS IoT SiteWise will generate a new unique `id`.

## Request Syntax
<a name="API_UpdateAssetModelCompositeModel_RequestSyntax"></a>

```
PUT /asset-models/{{assetModelId}}/composite-models/{{assetModelCompositeModelId}} HTTP/1.1
If-Match: {{ifMatch}}
If-None-Match: {{ifNoneMatch}}
Match-For-Version-Type: {{matchForVersionType}}
Content-type: application/json

{
   "assetModelCompositeModelDescription": "{{string}}",
   "assetModelCompositeModelExternalId": "{{string}}",
   "assetModelCompositeModelName": "{{string}}",
   "assetModelCompositeModelProperties": [
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
<a name="API_UpdateAssetModelCompositeModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetModelCompositeModelId](#API_UpdateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModelCompositeModel-request-uri-assetModelCompositeModelId"></a>
The ID of a composite model on this asset model.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [assetModelId](#API_UpdateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModelCompositeModel-request-uri-assetModelId"></a>
The ID of the asset model, in UUID format.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [ifMatch](#API_UpdateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModelCompositeModel-request-ifMatch"></a>
The expected current entity tag (ETag) for the asset model’s latest or active version (specified using `matchForVersionType`). The update request is rejected if the tag does not match the latest or active version's current entity tag. See [Optimistic locking for asset model writes](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html) in the * AWS IoT SiteWise User Guide*.
Pattern: `^[\w-]{43}$`

 ** [ifNoneMatch](#API_UpdateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModelCompositeModel-request-ifNoneMatch"></a>
Accepts **\*** to reject the update request if an active version (specified using `matchForVersionType` as `ACTIVE`) already exists for the asset model.
Pattern: `\*`

 ** [matchForVersionType](#API_UpdateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModelCompositeModel-request-matchForVersionType"></a>
Specifies the asset model version type (`LATEST` or `ACTIVE`) used in conjunction with `If-Match` or `If-None-Match` headers to determine the target ETag for the update operation.
Valid Values: `LATEST | ACTIVE`

## Request Body
<a name="API_UpdateAssetModelCompositeModel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assetModelCompositeModelDescription](#API_UpdateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModelCompositeModel-request-assetModelCompositeModelDescription"></a>
A description for the composite model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [assetModelCompositeModelExternalId](#API_UpdateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModelCompositeModel-request-assetModelCompositeModelExternalId"></a>
An external ID to assign to the asset model. You can only set the external ID of the asset model if it wasn't set when it was created, or you're setting it to the exact same thing as when it was created.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** [assetModelCompositeModelName](#API_UpdateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModelCompositeModel-request-assetModelCompositeModelName"></a>
A unique name for the composite model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** [assetModelCompositeModelProperties](#API_UpdateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModelCompositeModel-request-assetModelCompositeModelProperties"></a>
The property definitions of the composite model. For more information, see [ Inline custom composite models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html#inline-composite-models) in the * AWS IoT SiteWise User Guide*.
You can specify up to 200 properties per composite model. For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
Type: Array of [AssetModelProperty](API_AssetModelProperty.md) objects
Required: No

 ** [clientToken](#API_UpdateAssetModelCompositeModel_RequestSyntax) **   <a name="iotsitewise-UpdateAssetModelCompositeModel-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

## Response Syntax
<a name="API_UpdateAssetModelCompositeModel_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
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
<a name="API_UpdateAssetModelCompositeModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [assetModelCompositeModelPath](#API_UpdateAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-UpdateAssetModelCompositeModel-response-assetModelCompositeModelPath"></a>
The path to the composite model listing the parent composite models.
Type: Array of [AssetModelCompositeModelPathSegment](API_AssetModelCompositeModelPathSegment.md) objects

 ** [assetModelId](#API_UpdateAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-UpdateAssetModelCompositeModel-response-assetModelId"></a>
The ID of the asset model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetModelStatus](#API_UpdateAssetModelCompositeModel_ResponseSyntax) **   <a name="iotsitewise-UpdateAssetModelCompositeModel-response-assetModelStatus"></a>
Contains current status information for an asset model. For more information, see [Asset and model states](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-and-model-states.html) in the * AWS IoT SiteWise User Guide*.
Type: [AssetModelStatus](API_AssetModelStatus.md) object

## Errors
<a name="API_UpdateAssetModelCompositeModel_Errors"></a>

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
<a name="API_UpdateAssetModelCompositeModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/UpdateAssetModelCompositeModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/UpdateAssetModelCompositeModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/UpdateAssetModelCompositeModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/UpdateAssetModelCompositeModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/UpdateAssetModelCompositeModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/UpdateAssetModelCompositeModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/UpdateAssetModelCompositeModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/UpdateAssetModelCompositeModel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/UpdateAssetModelCompositeModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/UpdateAssetModelCompositeModel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
