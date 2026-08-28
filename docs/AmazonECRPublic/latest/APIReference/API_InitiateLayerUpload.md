---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_InitiateLayerUpload.html
---

# InitiateLayerUpload
<a name="API_InitiateLayerUpload"></a>

Notifies Amazon ECR that you intend to upload an image layer.

When an image is pushed, the InitiateLayerUpload API is called once for each image layer that hasn't already been uploaded. Whether an image layer uploads is determined by the BatchCheckLayerAvailability API action.

**Note**
This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the `docker` CLI to pull, tag, and push images.

## Request Syntax
<a name="API_InitiateLayerUpload_RequestSyntax"></a>

```
{
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_InitiateLayerUpload_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [registryId](#API_InitiateLayerUpload_RequestSyntax) **   <a name="ecrpublic-InitiateLayerUpload-request-registryId"></a>
The AWS account ID, or registry alias, that's associated with the registry to which you intend to upload layers. If you do not specify a registry, the default public registry is assumed.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Required: No

 ** [repositoryName](#API_InitiateLayerUpload_RequestSyntax) **   <a name="ecrpublic-InitiateLayerUpload-request-repositoryName"></a>
The name of the repository that you want to upload layers to.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: Yes

## Response Syntax
<a name="API_InitiateLayerUpload_ResponseSyntax"></a>

```
{
   "partSize": number,
   "uploadId": "string"
}
```

## Response Elements
<a name="API_InitiateLayerUpload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [partSize](#API_InitiateLayerUpload_ResponseSyntax) **   <a name="ecrpublic-InitiateLayerUpload-response-partSize"></a>
The size, in bytes, that Amazon ECR expects future layer part uploads to be.
Type: Long
Valid Range: Minimum value of 0.

 ** [uploadId](#API_InitiateLayerUpload_ResponseSyntax) **   <a name="ecrpublic-InitiateLayerUpload-response-uploadId"></a>
The upload ID for the layer upload. This parameter is passed to further [UploadLayerPart](API_UploadLayerPart.md) and [CompleteLayerUpload](API_CompleteLayerUpload.md) operations.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

## Errors
<a name="API_InitiateLayerUpload_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
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

## See Also
<a name="API_InitiateLayerUpload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/InitiateLayerUpload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/InitiateLayerUpload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/InitiateLayerUpload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/InitiateLayerUpload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/InitiateLayerUpload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/InitiateLayerUpload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/InitiateLayerUpload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/InitiateLayerUpload)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/InitiateLayerUpload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/InitiateLayerUpload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECRPublic` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
