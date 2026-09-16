---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteAssetModel.html
---

# DeleteAssetModel
<a name="API_DeleteAssetModel"></a>

Deletes an asset model. This action can't be undone. You must delete all assets created from an asset model before you can delete the model. Also, you can't delete an asset model if a parent asset model exists that contains a property formula expression that depends on the asset model that you want to delete. For more information, see [Deleting assets and models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html) in the * AWS IoT SiteWise User Guide*.

## Request Syntax
<a name="API_DeleteAssetModel_RequestSyntax"></a>

```
DELETE /asset-models/{{assetModelId}}?clientToken={{clientToken}} HTTP/1.1
If-Match: {{ifMatch}}
If-None-Match: {{ifNoneMatch}}
Match-For-Version-Type: {{matchForVersionType}}
```

## URI Request Parameters
<a name="API_DeleteAssetModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetModelId](#API_DeleteAssetModel_RequestSyntax) **   <a name="iotsitewise-DeleteAssetModel-request-uri-assetModelId"></a>
The ID of the asset model to delete. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [clientToken](#API_DeleteAssetModel_RequestSyntax) **   <a name="iotsitewise-DeleteAssetModel-request-uri-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`

 ** [ifMatch](#API_DeleteAssetModel_RequestSyntax) **   <a name="iotsitewise-DeleteAssetModel-request-ifMatch"></a>
The expected current entity tag (ETag) for the asset model’s latest or active version (specified using `matchForVersionType`). The delete request is rejected if the tag does not match the latest or active version's current entity tag. See [Optimistic locking for asset model writes](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html) in the * AWS IoT SiteWise User Guide*.
Pattern: `^[\w-]{43}$`

 ** [ifNoneMatch](#API_DeleteAssetModel_RequestSyntax) **   <a name="iotsitewise-DeleteAssetModel-request-ifNoneMatch"></a>
Accepts **\*** to reject the delete request if an active version (specified using `matchForVersionType` as `ACTIVE`) already exists for the asset model.
Pattern: `\*`

 ** [matchForVersionType](#API_DeleteAssetModel_RequestSyntax) **   <a name="iotsitewise-DeleteAssetModel-request-matchForVersionType"></a>
Specifies the asset model version type (`LATEST` or `ACTIVE`) used in conjunction with `If-Match` or `If-None-Match` headers to determine the target ETag for the delete operation.
Valid Values: `LATEST | ACTIVE`

## Request Body
<a name="API_DeleteAssetModel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAssetModel_ResponseSyntax"></a>

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
<a name="API_DeleteAssetModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [assetModelId](#API_DeleteAssetModel_ResponseSyntax) **   <a name="iotsitewise-DeleteAssetModel-response-assetModelId"></a>
The ID of the asset model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetModelStatus](#API_DeleteAssetModel_ResponseSyntax) **   <a name="iotsitewise-DeleteAssetModel-response-assetModelStatus"></a>
The status of the asset model, which contains a state (`DELETING` after successfully calling this operation) and any error message.
Type: [AssetModelStatus](API_AssetModelStatus.md) object

## Errors
<a name="API_DeleteAssetModel_Errors"></a>

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

 ** PreconditionFailedException **
The precondition in one or more of the request-header fields evaluated to `FALSE`.
 ** resourceArn **
The ARN of the resource on which precondition failed with this operation.
 ** resourceId **
The ID of the resource on which precondition failed with this operation.
HTTP Status Code: 412

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_DeleteAssetModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DeleteAssetModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DeleteAssetModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DeleteAssetModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DeleteAssetModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DeleteAssetModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DeleteAssetModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DeleteAssetModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DeleteAssetModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DeleteAssetModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DeleteAssetModel)
