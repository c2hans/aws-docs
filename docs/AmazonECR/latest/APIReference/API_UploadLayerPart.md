---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UploadLayerPart.html
---

# UploadLayerPart
<a name="API_UploadLayerPart"></a>

Uploads an image layer part to Amazon ECR.

When an image is pushed, each new image layer is uploaded in parts. The maximum size of each image layer part can be 20971520 bytes (or about 20MB). The UploadLayerPart API is called once per each new image layer part.

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

 ** [layerPartBlob](#API_UploadLayerPart_RequestSyntax) **   <a name="ECR-UploadLayerPart-request-layerPartBlob"></a>
The base64-encoded layer part payload.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 20971520.
Required: Yes

 ** [partFirstByte](#API_UploadLayerPart_RequestSyntax) **   <a name="ECR-UploadLayerPart-request-partFirstByte"></a>
The position of the first byte of the layer part witin the overall image layer.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** [partLastByte](#API_UploadLayerPart_RequestSyntax) **   <a name="ECR-UploadLayerPart-request-partLastByte"></a>
The position of the last byte of the layer part within the overall image layer.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** [registryId](#API_UploadLayerPart_RequestSyntax) **   <a name="ECR-UploadLayerPart-request-registryId"></a>
The AWS account ID associated with the registry to which you are uploading layer parts. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_UploadLayerPart_RequestSyntax) **   <a name="ECR-UploadLayerPart-request-repositoryName"></a>
The name of the repository to which you are uploading layer parts.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

 ** [uploadId](#API_UploadLayerPart_RequestSyntax) **   <a name="ECR-UploadLayerPart-request-uploadId"></a>
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

 ** [lastByteReceived](#API_UploadLayerPart_ResponseSyntax) **   <a name="ECR-UploadLayerPart-response-lastByteReceived"></a>
The integer value of the last byte received in the request.
Type: Long
Valid Range: Minimum value of 0.

 ** [registryId](#API_UploadLayerPart_ResponseSyntax) **   <a name="ECR-UploadLayerPart-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryName](#API_UploadLayerPart_ResponseSyntax) **   <a name="ECR-UploadLayerPart-response-repositoryName"></a>
The repository name associated with the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`

 ** [uploadId](#API_UploadLayerPart_ResponseSyntax) **   <a name="ECR-UploadLayerPart-response-uploadId"></a>
The upload ID associated with the request.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

## Errors
<a name="API_UploadLayerPart_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLayerPartException **
The layer part size is not valid, or the first byte specified is not consecutive to the last byte of a previous layer part upload.
 ** lastValidByteReceived **
The last valid byte received from the layer part upload that is associated with the exception.
 ** message **
The error message associated with the exception.
 ** registryId **
The registry ID associated with the exception.
 ** repositoryName **
The repository name associated with the exception.
 ** uploadId **
The upload ID associated with the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** KmsException **
The operation failed due to a KMS exception.
 ** kmsError **
The error code returned by AWS KMS.
HTTP Status Code: 400

 ** LimitExceededException **
The operation did not succeed because it would have exceeded a service limit for your account. For more information, see [Amazon ECR service quotas](https://docs.aws.amazon.com/AmazonECR/latest/userguide/service-quotas.html) in the Amazon Elastic Container Registry User Guide.
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

 ** UploadNotFoundException **
The upload could not be found, or the specified upload ID is not valid for this repository.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_UploadLayerPart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/UploadLayerPart)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/UploadLayerPart)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/UploadLayerPart)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/UploadLayerPart)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/UploadLayerPart)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/UploadLayerPart)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/UploadLayerPart)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/UploadLayerPart)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/UploadLayerPart)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/UploadLayerPart)
