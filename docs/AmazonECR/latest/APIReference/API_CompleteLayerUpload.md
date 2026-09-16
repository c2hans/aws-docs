---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CompleteLayerUpload.html
---

# CompleteLayerUpload
<a name="API_CompleteLayerUpload"></a>

Informs Amazon ECR that the image layer upload has completed for a specified registry, repository name, and upload ID. You can optionally provide a `sha256` digest of the image layer for data validation purposes.

When an image is pushed, the CompleteLayerUpload API is called once per each new image layer to verify that the upload has completed.

**Note**
This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the `docker` CLI to pull, tag, and push images.

## Request Syntax
<a name="API_CompleteLayerUpload_RequestSyntax"></a>

```
{
   "layerDigests": [ "{{string}}" ],
   "registryId": "{{string}}",
   "repositoryName": "{{string}}",
   "uploadId": "{{string}}"
}
```

## Request Parameters
<a name="API_CompleteLayerUpload_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [layerDigests](#API_CompleteLayerUpload_RequestSyntax) **   <a name="ECR-CompleteLayerUpload-request-layerDigests"></a>
The `sha256` digest of the image layer.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `[a-zA-Z0-9-_+.]+:[a-fA-F0-9]+`
Required: Yes

 ** [registryId](#API_CompleteLayerUpload_RequestSyntax) **   <a name="ECR-CompleteLayerUpload-request-registryId"></a>
The AWS account ID associated with the registry to which to upload layers. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_CompleteLayerUpload_RequestSyntax) **   <a name="ECR-CompleteLayerUpload-request-repositoryName"></a>
The name of the repository to associate with the image layer.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

 ** [uploadId](#API_CompleteLayerUpload_RequestSyntax) **   <a name="ECR-CompleteLayerUpload-request-uploadId"></a>
The upload ID from a previous [InitiateLayerUpload](API_InitiateLayerUpload.md) operation to associate with the image layer.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

## Response Syntax
<a name="API_CompleteLayerUpload_ResponseSyntax"></a>

```
{
   "layerDigest": "string",
   "registryId": "string",
   "repositoryName": "string",
   "uploadId": "string"
}
```

## Response Elements
<a name="API_CompleteLayerUpload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [layerDigest](#API_CompleteLayerUpload_ResponseSyntax) **   <a name="ECR-CompleteLayerUpload-response-layerDigest"></a>
The `sha256` digest of the image layer.
Type: String
Pattern: `[a-zA-Z0-9-_+.]+:[a-fA-F0-9]+`

 ** [registryId](#API_CompleteLayerUpload_ResponseSyntax) **   <a name="ECR-CompleteLayerUpload-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryName](#API_CompleteLayerUpload_ResponseSyntax) **   <a name="ECR-CompleteLayerUpload-response-repositoryName"></a>
The repository name associated with the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`

 ** [uploadId](#API_CompleteLayerUpload_ResponseSyntax) **   <a name="ECR-CompleteLayerUpload-response-uploadId"></a>
The upload ID associated with the layer.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

## Errors
<a name="API_CompleteLayerUpload_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EmptyUploadException **
The specified layer upload does not contain any layer parts.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** InvalidLayerException **
The layer digest calculation performed by Amazon ECR upon receipt of the image layer does not match the digest specified.
 ** message **
The error message associated with the exception.
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

 ** LayerAlreadyExistsException **
The image layer already exists in the associated repository.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** LayerPartTooSmallException **
Layer parts must be at least 5 MiB in size.
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
<a name="API_CompleteLayerUpload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/CompleteLayerUpload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/CompleteLayerUpload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/CompleteLayerUpload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/CompleteLayerUpload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/CompleteLayerUpload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/CompleteLayerUpload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/CompleteLayerUpload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/CompleteLayerUpload)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/CompleteLayerUpload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/CompleteLayerUpload)
