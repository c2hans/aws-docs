---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchCheckLayerAvailability.html
---

# BatchCheckLayerAvailability
<a name="API_BatchCheckLayerAvailability"></a>

Checks the availability of one or more image layers in a repository.

When an image is pushed to a repository, each image layer is checked to verify if it has been uploaded before. If it has been uploaded, then the image layer is skipped.

**Note**
This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the `docker` CLI to pull, tag, and push images.

## Request Syntax
<a name="API_BatchCheckLayerAvailability_RequestSyntax"></a>

```
{
   "layerDigests": [ "{{string}}" ],
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchCheckLayerAvailability_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [layerDigests](#API_BatchCheckLayerAvailability_RequestSyntax) **   <a name="ECR-BatchCheckLayerAvailability-request-layerDigests"></a>
The digests of the image layers to check.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** [registryId](#API_BatchCheckLayerAvailability_RequestSyntax) **   <a name="ECR-BatchCheckLayerAvailability-request-registryId"></a>
The AWS account ID associated with the registry that contains the image layers to check. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_BatchCheckLayerAvailability_RequestSyntax) **   <a name="ECR-BatchCheckLayerAvailability-request-repositoryName"></a>
The name of the repository that is associated with the image layers to check.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_BatchCheckLayerAvailability_ResponseSyntax"></a>

```
{
   "failures": [
      {
         "failureCode": "string",
         "failureReason": "string",
         "layerDigest": "string"
      }
   ],
   "layers": [
      {
         "layerAvailability": "string",
         "layerDigest": "string",
         "layerSize": number,
         "mediaType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchCheckLayerAvailability_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_BatchCheckLayerAvailability_ResponseSyntax) **   <a name="ECR-BatchCheckLayerAvailability-response-failures"></a>
Any failures associated with the call.
Type: Array of [LayerFailure](API_LayerFailure.md) objects

 ** [layers](#API_BatchCheckLayerAvailability_ResponseSyntax) **   <a name="ECR-BatchCheckLayerAvailability-response-layers"></a>
A list of image layer objects corresponding to the image layer references in the request.
Type: Array of [Layer](API_Layer.md) objects

## Errors
<a name="API_BatchCheckLayerAvailability_Errors"></a>

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
<a name="API_BatchCheckLayerAvailability_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_BatchCheckLayerAvailability_Example_1"></a>

This example checks the availability of an image layer in the `amazonlinux` repository.

#### Sample Request
<a name="API_BatchCheckLayerAvailability_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 126
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.BatchCheckLayerAvailability
X-Amz-Date: 20161216T195733Zc
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.3.0 botocore/1.4.79
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
  "layerDigests": [
    "sha256:8e3fa21c4cc40232e835a6761332d225c7af3235c5755f44ada2ed9d0e4ab7e8"
  ],
  "repositoryName": "amazonlinux"
}
```

#### Sample Response
<a name="API_BatchCheckLayerAvailability_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 16 Dec 2016 19:57:33 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 233
Connection: keep-alive
x-amzn-RequestId: e2422faf-c3c9-11e6-a3ee-63b3b5dcf3b9

{
  "failures": [],
  "layers": [
    {
      "layerAvailability": "AVAILABLE",
      "layerDigest": "sha256:8e3fa21c4cc40232e835a6761332d225c7af3235c5755f44ada2ed9d0e4ab7e8",
      "layerSize": 91768077,
      "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip"
    }
  ]
}
```

## See Also
<a name="API_BatchCheckLayerAvailability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/BatchCheckLayerAvailability)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/BatchCheckLayerAvailability)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/BatchCheckLayerAvailability)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/BatchCheckLayerAvailability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/BatchCheckLayerAvailability)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/BatchCheckLayerAvailability)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/BatchCheckLayerAvailability)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/BatchCheckLayerAvailability)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/BatchCheckLayerAvailability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/BatchCheckLayerAvailability)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
