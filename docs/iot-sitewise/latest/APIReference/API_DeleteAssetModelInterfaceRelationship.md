---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DeleteAssetModelInterfaceRelationship.html
---

# DeleteAssetModelInterfaceRelationship
<a name="API_DeleteAssetModelInterfaceRelationship"></a>

Deletes an interface relationship between an asset model and an interface asset model.

## Request Syntax
<a name="API_DeleteAssetModelInterfaceRelationship_RequestSyntax"></a>

```
DELETE /asset-models/{{assetModelId}}/interface/{{interfaceAssetModelId}}/asset-model-interface-relationship?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAssetModelInterfaceRelationship_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetModelId](#API_DeleteAssetModelInterfaceRelationship_RequestSyntax) **   <a name="iotsitewise-DeleteAssetModelInterfaceRelationship-request-uri-assetModelId"></a>
The ID of the asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** [clientToken](#API_DeleteAssetModelInterfaceRelationship_RequestSyntax) **   <a name="iotsitewise-DeleteAssetModelInterfaceRelationship-request-uri-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`

 ** [interfaceAssetModelId](#API_DeleteAssetModelInterfaceRelationship_RequestSyntax) **   <a name="iotsitewise-DeleteAssetModelInterfaceRelationship-request-uri-interfaceAssetModelId"></a>
The ID of the interface asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

## Request Body
<a name="API_DeleteAssetModelInterfaceRelationship_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAssetModelInterfaceRelationship_ResponseSyntax"></a>

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
   },
   "interfaceAssetModelId": "string"
}
```

## Response Elements
<a name="API_DeleteAssetModelInterfaceRelationship_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [assetModelArn](#API_DeleteAssetModelInterfaceRelationship_ResponseSyntax) **   <a name="iotsitewise-DeleteAssetModelInterfaceRelationship-response-assetModelArn"></a>
The ARN of the asset model, which has the following format. `arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [assetModelId](#API_DeleteAssetModelInterfaceRelationship_ResponseSyntax) **   <a name="iotsitewise-DeleteAssetModelInterfaceRelationship-response-assetModelId"></a>
The ID of the asset model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [assetModelStatus](#API_DeleteAssetModelInterfaceRelationship_ResponseSyntax) **   <a name="iotsitewise-DeleteAssetModelInterfaceRelationship-response-assetModelStatus"></a>
Contains current status information for an asset model. For more information, see [Asset and model states](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-and-model-states.html) in the * AWS IoT SiteWise User Guide*.
Type: [AssetModelStatus](API_AssetModelStatus.md) object

 ** [interfaceAssetModelId](#API_DeleteAssetModelInterfaceRelationship_ResponseSyntax) **   <a name="iotsitewise-DeleteAssetModelInterfaceRelationship-response-interfaceAssetModelId"></a>
The ID of the interface asset model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

## Errors
<a name="API_DeleteAssetModelInterfaceRelationship_Errors"></a>

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

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_DeleteAssetModelInterfaceRelationship_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DeleteAssetModelInterfaceRelationship)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DeleteAssetModelInterfaceRelationship)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DeleteAssetModelInterfaceRelationship)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DeleteAssetModelInterfaceRelationship)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DeleteAssetModelInterfaceRelationship)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DeleteAssetModelInterfaceRelationship)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DeleteAssetModelInterfaceRelationship)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DeleteAssetModelInterfaceRelationship)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DeleteAssetModelInterfaceRelationship)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DeleteAssetModelInterfaceRelationship)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
