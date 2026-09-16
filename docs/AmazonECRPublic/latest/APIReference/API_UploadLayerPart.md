---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_UploadLayerPart.html
---

# UploadLayerPart
<a name="API_UploadLayerPart"></a>

Uploads an image layer part to Amazon ECR.

When an image is pushed, each new image layer is uploaded in parts. The maximum size of each image layer part can be 20971520 bytes (about 20MB). The UploadLayerPart API is called once for each new image layer part.

**Note**
This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the `docker` CLI to pull, tag, and push images.

## Request Syntax
<a name="API_UploadLayerPart_RequestSyntax"></a>

```
{
   "layerPartBlob": {{blob}},
   "partFirstByte": {{number}},
   "partLastByte": {{number}},
   "registryId": "{{string}}",
   "repositoryName": "{{string}}",
   "uploadId": "{{string}}"
}
```

## Request Parameters
<a name="API_UploadLayerPart_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [layerPartBlob](#API_UploadLayerPart_RequestSyntax) **   <a name="ecrpublic-UploadLayerPart-request-layerPartBlob"></a>
The base64-encoded layer part payload.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 20971520.
Required: Yes

 ** [partFirstByte](#API_UploadLayerPart_RequestSyntax) **   <a name="ecrpublic-UploadLayerPart-request-partFirstByte"></a>
The position of the first byte of the layer part witin the overall image layer.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** [partLastByte](#API_UploadLayerPart_RequestSyntax) **   <a name="ecrpublic-UploadLayerPart-request-partLastByte"></a>
The position of the last byte of the layer part within the overall image layer.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** [registryId](#API_UploadLayerPart_RequestSyntax) **   <a name="ecrpublic-UploadLayerPart-request-registryId"></a>
The AWS account ID, or registry alias, that's associated with the registry that you're uploading layer parts to. If you do not specify a registry, the default public registry is assumed.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Required: No

 ** [repositoryName](#API_UploadLayerPart_RequestSyntax) **   <a name="ecrpublic-UploadLayerPart-request-repositoryName"></a>
The name of the repository that you're uploading layer parts to.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: Yes

 ** [uploadId](#API_UploadLayerPart_RequestSyntax) **   <a name="ecrpublic-UploadLayerPart-request-uploadId"></a>
The upload ID from a previous [InitiateLayerUpload](API_InitiateLayerUpload.md) operation to associate with the layer part upload.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

## Response Syntax
<a name="API_UploadLayerPart_ResponseSyntax"></a>

```
{
   "lastByteReceived": number,
   "registryId": "string",
   "repositoryName": "string",
   "uploadId": "string"
}
```

## Response Elements
<a name="API_UploadLayerPart_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lastByteReceived](#API_UploadLayerPart_ResponseSyntax) **   <a name="ecrpublic-UploadLayerPart-response-lastByteReceived"></a>
The integer value of the last byte that's received in the request.
Type: Long
Valid Range: Minimum value of 0.

 ** [registryId](#API_UploadLayerPart_ResponseSyntax) **   <a name="ecrpublic-UploadLayerPart-response-registryId"></a>
The registry ID that's associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryName](#API_UploadLayerPart_ResponseSyntax) **   <a name="ecrpublic-UploadLayerPart-response-repositoryName"></a>
The repository name that's associated with the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`

 ** [uploadId](#API_UploadLayerPart_ResponseSyntax) **   <a name="ecrpublic-UploadLayerPart-response-uploadId"></a>
The upload ID that's associated with the request.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

## Errors
<a name="API_UploadLayerPart_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLayerPartException **
The layer part size isn't valid, or the first byte specified isn't consecutive to the last byte of a previous layer part upload.
 ** lastValidByteReceived **
The position of the last byte of the layer part.
 ** registryId **
The AWS account ID that's associated with the layer part.
 ** repositoryName **
The name of the repository.
 ** uploadId **
The upload ID that's associated with the layer part.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
HTTP Status Code: 400

 ** LimitExceededException **
The operation didn't succeed because it would have exceeded a service limit for your account. For more information, see [Amazon ECR Public service quotas](https://docs.aws.amazon.com/AmazonECR/latest/public/public-service-quotas.html) in the Amazon Elastic Container Registry Public User Guide.
HTTP Status Code: 400

 ** RegistryNotFoundException **
The registry doesn't exist.
HTTP Status Code: 400

 ** RepositoryNotFoundException **
The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
HTTP Status Code: 500

 ** UnsupportedCommandException **
The action isn't supported in this Region.
HTTP Status Code: 400

 ** UploadNotFoundException **
The upload can't be found, or the specified upload ID isn't valid for this repository.
HTTP Status Code: 400

## See Also
<a name="API_UploadLayerPart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/UploadLayerPart)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/UploadLayerPart)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/UploadLayerPart)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/UploadLayerPart)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/UploadLayerPart)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/UploadLayerPart)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/UploadLayerPart)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/UploadLayerPart)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/UploadLayerPart)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/UploadLayerPart)
