---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchDeleteImage.html
---

# BatchDeleteImage
<a name="API_BatchDeleteImage"></a>

Deletes a list of specified images within a repository. Images are specified with either an `imageTag` or `imageDigest`.

You can remove a tag from an image by specifying the image's tag in your request. When you remove the last tag from an image, the image is deleted from your repository.

You can completely delete an image (and all of its tags) by specifying the image's digest in your request.

## Request Syntax
<a name="API_BatchDeleteImage_RequestSyntax"></a>

```
{
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
<a name="API_BatchDeleteImage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [imageIds](#API_BatchDeleteImage_RequestSyntax) **   <a name="ECR-BatchDeleteImage-request-imageIds"></a>
A list of image ID references that correspond to images to delete. The format of the `imageIds` reference is `imageTag=tag` or `imageDigest=digest`.
Type: Array of [ImageIdentifier](API_ImageIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [registryId](#API_BatchDeleteImage_RequestSyntax) **   <a name="ECR-BatchDeleteImage-request-registryId"></a>
The AWS account ID associated with the registry that contains the image to delete. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_BatchDeleteImage_RequestSyntax) **   <a name="ECR-BatchDeleteImage-request-repositoryName"></a>
The repository that contains the image to delete.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_BatchDeleteImage_ResponseSyntax"></a>

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
   "imageIds": [
      {
         "imageDigest": "string",
         "imageTag": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_BatchDeleteImage_ResponseSyntax) **   <a name="ECR-BatchDeleteImage-response-failures"></a>
Any failures associated with the call.
Type: Array of [ImageFailure](API_ImageFailure.md) objects

 ** [imageIds](#API_BatchDeleteImage_ResponseSyntax) **   <a name="ECR-BatchDeleteImage-response-imageIds"></a>
The image IDs of the deleted images.
Type: Array of [ImageIdentifier](API_ImageIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

## Errors
<a name="API_BatchDeleteImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
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

## Examples
<a name="API_BatchDeleteImage_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_BatchDeleteImage_Example_1"></a>

This example deletes an image in the `ubuntu` repository with the `imageTag` value of `xenial`.

#### Sample Request
<a name="API_BatchDeleteImage_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 66
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.BatchDeleteImage
X-Amz-Date: 20161216T193711Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.3.0 botocore/1.4.79
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "repositoryName": "ubuntu",
  "imageIds": [
    {
      "imageTag": "xenial"
    }
  ]
}
```

#### Sample Response
<a name="API_BatchDeleteImage_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 16 Dec 2016 19:37:11 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 138
Connection: keep-alive
x-amzn-RequestId: 09cc7023-c3c7-11e6-8acf-61b7dd8abe56

{
  "failures": [],
  "imageIds": [
    {
      "imageDigest": "sha256:7a64bc9c8843b0a8c8b8a7e4715b7615e4e1b0d8ca3c7e7a76ec8250899c397a",
      "imageTag": "xenial"
    }
  ]
}
```

### Example
<a name="API_BatchDeleteImage_Example_2"></a>

This example deletes an image (and all of its tags) in the `ubuntu` repository with the `imageDigest` value of `sha256:7a64bc9c8843b0a8c8b8a7e4715b7615e4e1b0d8ca3c7e7a76ec8250899c397a`.

#### Sample Request
<a name="API_BatchDeleteImage_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 134
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.BatchDeleteImage
X-Amz-Date: 20161216T194250Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.3.0 botocore/1.4.79
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "repositoryName": "ubuntu",
  "imageIds": [
    {
      "imageDigest": "sha256:7a64bc9c8843b0a8c8b8a7e4715b7615e4e1b0d8ca3c7e7a76ec8250899c397a"
    }
  ]
}
```

#### Sample Response
<a name="API_BatchDeleteImage_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 16 Dec 2016 19:42:50 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 248
Connection: keep-alive
x-amzn-RequestId: d441a9f6-c3c7-11e6-8acf-61b7dd8abe56

{
  "failures": [],
  "imageIds": [
    {
      "imageDigest": "sha256:7a64bc9c8843b0a8c8b8a7e4715b7615e4e1b0d8ca3c7e7a76ec8250899c397a",
      "imageTag": "xenial"
    },
    {
      "imageDigest": "sha256:7a64bc9c8843b0a8c8b8a7e4715b7615e4e1b0d8ca3c7e7a76ec8250899c397a",
      "imageTag": "latest"
    }
  ]
}
```

## See Also
<a name="API_BatchDeleteImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/BatchDeleteImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/BatchDeleteImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/BatchDeleteImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/BatchDeleteImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/BatchDeleteImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/BatchDeleteImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/BatchDeleteImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/BatchDeleteImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/BatchDeleteImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/BatchDeleteImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
