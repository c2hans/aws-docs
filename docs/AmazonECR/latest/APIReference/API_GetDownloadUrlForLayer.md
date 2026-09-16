---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetDownloadUrlForLayer.html
---

# GetDownloadUrlForLayer
<a name="API_GetDownloadUrlForLayer"></a>

Retrieves the pre-signed Amazon S3 download URL corresponding to an image layer. You can only get URLs for image layers that are referenced in an image.

When an image is pulled, the GetDownloadUrlForLayer API is called once per image layer that is not already cached.

**Note**
This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the `docker` CLI to pull, tag, and push images.

## Request Syntax
<a name="API_GetDownloadUrlForLayer_RequestSyntax"></a>

```
{
   "layerDigest": "{{string}}",
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDownloadUrlForLayer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [layerDigest](#API_GetDownloadUrlForLayer_RequestSyntax) **   <a name="ECR-GetDownloadUrlForLayer-request-layerDigest"></a>
The digest of the image layer to download.
Type: String
Pattern: `[a-zA-Z0-9-_+.]+:[a-fA-F0-9]+`
Required: Yes

 ** [registryId](#API_GetDownloadUrlForLayer_RequestSyntax) **   <a name="ECR-GetDownloadUrlForLayer-request-registryId"></a>
The AWS account ID associated with the registry that contains the image layer to download. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_GetDownloadUrlForLayer_RequestSyntax) **   <a name="ECR-GetDownloadUrlForLayer-request-repositoryName"></a>
The name of the repository that is associated with the image layer to download.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_GetDownloadUrlForLayer_ResponseSyntax"></a>

```
{
   "downloadUrl": "string",
   "layerDigest": "string"
}
```

## Response Elements
<a name="API_GetDownloadUrlForLayer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [downloadUrl](#API_GetDownloadUrlForLayer_ResponseSyntax) **   <a name="ECR-GetDownloadUrlForLayer-response-downloadUrl"></a>
The pre-signed Amazon S3 download URL for the requested layer.
Type: String

 ** [layerDigest](#API_GetDownloadUrlForLayer_ResponseSyntax) **   <a name="ECR-GetDownloadUrlForLayer-response-layerDigest"></a>
The digest of the image layer to download.
Type: String
Pattern: `[a-zA-Z0-9-_+.]+:[a-fA-F0-9]+`

## Errors
<a name="API_GetDownloadUrlForLayer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** LayerInaccessibleException **
The specified layer is not available because it is not associated with an image. Unassociated image layers may be cleaned up at any time.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** LayersNotFoundException **
The specified layers could not be found, or the specified layer is not valid for this repository.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** RepositoryNotFoundException **
The specified repository could not be found. Check the spelling of the specified repository and ensure that you are performing operations on the correct registry.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** UnableToGetUpstreamLayerException **
There was an issue getting the upstream layer matching the pull through cache rule.
HTTP Status Code: 400

## See Also
<a name="API_GetDownloadUrlForLayer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/GetDownloadUrlForLayer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/GetDownloadUrlForLayer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/GetDownloadUrlForLayer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/GetDownloadUrlForLayer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/GetDownloadUrlForLayer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/GetDownloadUrlForLayer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/GetDownloadUrlForLayer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/GetDownloadUrlForLayer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/GetDownloadUrlForLayer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/GetDownloadUrlForLayer)
