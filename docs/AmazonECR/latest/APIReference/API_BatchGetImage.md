---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchGetImage.html
---

# BatchGetImage
<a name="API_BatchGetImage"></a>

Gets detailed information for an image. Images are specified with either an `imageTag` or `imageDigest`.

When an image is pulled, the BatchGetImage API is called once to retrieve the image manifest.

## Request Syntax
<a name="API_BatchGetImage_RequestSyntax"></a>

```
{
   "acceptedMediaTypes": [ "{{string}}" ],
   "imageIds": [
      {
         "imageDigest": "{{string}}",
         "imageTag": "{{string}}"
      }
   ],
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchGetImage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [acceptedMediaTypes](#API_BatchGetImage_RequestSyntax) **   <a name="ECR-BatchGetImage-request-acceptedMediaTypes"></a>
The accepted media types for the request.
Valid values: `application/vnd.docker.distribution.manifest.v1+json` \| `application/vnd.docker.distribution.manifest.v2+json` \| `application/vnd.oci.image.manifest.v1+json`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [imageIds](#API_BatchGetImage_RequestSyntax) **   <a name="ECR-BatchGetImage-request-imageIds"></a>
A list of image ID references that correspond to images to describe. The format of the `imageIds` reference is `imageTag=tag` or `imageDigest=digest`.
Type: Array of [ImageIdentifier](API_ImageIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [registryId](#API_BatchGetImage_RequestSyntax) **   <a name="ECR-BatchGetImage-request-registryId"></a>
The AWS account ID associated with the registry that contains the images to describe. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_BatchGetImage_RequestSyntax) **   <a name="ECR-BatchGetImage-request-repositoryName"></a>
The repository that contains the images to describe.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_BatchGetImage_ResponseSyntax"></a>

```
{
   "failures": [
      {
         "failureCode": "string",
         "failureReason": "string",
         "imageId": {
            "imageDigest": "string",
            "imageTag": "string"
         }
      }
   ],
   "images": [
      {
         "imageId": {
            "imageDigest": "string",
            "imageTag": "string"
         },
         "imageManifest": "string",
         "imageManifestMediaType": "string",
         "registryId": "string",
         "repositoryName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_BatchGetImage_ResponseSyntax) **   <a name="ECR-BatchGetImage-response-failures"></a>
Any failures associated with the call.
Type: Array of [ImageFailure](API_ImageFailure.md) objects

 ** [images](#API_BatchGetImage_ResponseSyntax) **   <a name="ECR-BatchGetImage-response-images"></a>
A list of image objects corresponding to the image references in the request.
Type: Array of [Image](API_Image.md) objects

## Errors
<a name="API_BatchGetImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
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

 ** UnableToGetUpstreamImageException **
The image or images were unable to be pulled using the pull through cache rule. This is usually caused because of an issue with the Secrets Manager secret containing the credentials for the upstream registry.
HTTP Status Code: 400

## Examples
<a name="API_BatchGetImage_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_BatchGetImage_Example_1"></a>

This example describes an image in the `amazonlinux` repository with the `imageTag` value of `latest`.

#### Sample Request
<a name="API_BatchGetImage_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 71
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.BatchGetImage
X-Amz-Date: 20161216T195356Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.3.0 botocore/1.4.79
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "repositoryName": "amazonlinux",
  "imageIds": [
    {
      "imageTag": "latest"
    }
  ]
}
```

#### Sample Response
<a name="API_BatchGetImage_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 16 Dec 2016 19:53:56 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 800
Connection: keep-alive
x-amzn-RequestId: 60dc1ea1-c3c9-11e6-aa04-25c3a5fb1b54

{
  "failures": [],
  "images": [
    {
      "imageId": {
        "imageDigest": "sha256:f1d4ae3f7261a72e98c6ebefe9985cf10a0ea5bd762585a43e0700ed99863807",
        "imageTag": "latest"
      },
      "imageManifest": "{\n   \"schemaVersion\": 2,\n   \"mediaType\": \"application/vnd.docker.distribution.manifest.v2+json\",\n   \"config\": {\n      \"mediaType\": \"application/vnd.docker.container.image.v1+json\",\n      \"size\": 1486,\n      \"digest\": \"sha256:5b52b314511a611975c2c65e695d920acdf8ae8848fe0ef00b7d018d1f118b64\"\n   },\n   \"layers\": [\n      {\n         \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n         \"size\": 91768077,\n         \"digest\": \"sha256:8e3fa21c4cc40232e835a6761332d225c7af3235c5755f44ada2ed9d0e4ab7e8\"\n      }\n   ]\n}",
      "registryId": "012345678910",
      "repositoryName": "amazonlinux"
    }
  ]
}
```

## See Also
<a name="API_BatchGetImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/BatchGetImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/BatchGetImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/BatchGetImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/BatchGetImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/BatchGetImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/BatchGetImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/BatchGetImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/BatchGetImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/BatchGetImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/BatchGetImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
