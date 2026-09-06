---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchAssociateProjectAssets.html
---

# BatchAssociateProjectAssets
<a name="API_BatchAssociateProjectAssets"></a>

**Important**
The AWS IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025 . If you would like to use the AWS IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS IoT SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

Associates a group (batch) of assets with an AWS IoT SiteWise Monitor project.

## Request Syntax
<a name="API_BatchAssociateProjectAssets_RequestSyntax"></a>

```
POST /projects/{{projectId}}/assets/associate HTTP/1.1
Content-type: application/json

{
   "assetIds": [ "{{string}}" ],
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchAssociateProjectAssets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [projectId](#API_BatchAssociateProjectAssets_RequestSyntax) **   <a name="iotsitewise-BatchAssociateProjectAssets-request-uri-projectId"></a>
The ID of the project to which to associate the assets.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Request Body
<a name="API_BatchAssociateProjectAssets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assetIds](#API_BatchAssociateProjectAssets_RequestSyntax) **   <a name="iotsitewise-BatchAssociateProjectAssets-request-assetIds"></a>
The IDs of the assets to be associated to the project.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** [clientToken](#API_BatchAssociateProjectAssets_RequestSyntax) **   <a name="iotsitewise-BatchAssociateProjectAssets-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

## Response Syntax
<a name="API_BatchAssociateProjectAssets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "assetId": "string",
         "code": "string",
         "message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchAssociateProjectAssets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchAssociateProjectAssets_ResponseSyntax) **   <a name="iotsitewise-BatchAssociateProjectAssets-response-errors"></a>
A list of associated error information, if any.
Type: Array of [AssetErrorDetails](API_AssetErrorDetails.md) objects

## Errors
<a name="API_BatchAssociateProjectAssets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_BatchAssociateProjectAssets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/BatchAssociateProjectAssets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/BatchAssociateProjectAssets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchAssociateProjectAssets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/BatchAssociateProjectAssets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchAssociateProjectAssets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/BatchAssociateProjectAssets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/BatchAssociateProjectAssets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/BatchAssociateProjectAssets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/BatchAssociateProjectAssets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchAssociateProjectAssets)
