---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_StartImageScan.html
---

# StartImageScan
<a name="API_StartImageScan"></a>

Starts a basic image vulnerability scan.

 A basic image scan can only be started once per 24 hours on an individual image. This limit includes if an image was scanned on initial push. You can start up to 100,000 basic scans per 24 hours. This limit includes both scans on initial push and scans initiated by the StartImageScan API. For more information, see [Basic scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-basic.html) in the *Amazon Elastic Container Registry User Guide*.

## Request Syntax
<a name="API_StartImageScan_RequestSyntax"></a>

```
{
   "imageId": {
      "imageDigest": "{{string}}",
      "imageTag": "{{string}}"
   },
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartImageScan_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [imageId](#API_StartImageScan_RequestSyntax) **   <a name="ECR-StartImageScan-request-imageId"></a>
An object with identifying information for an image in an Amazon ECR repository.
Type: [ImageIdentifier](API_ImageIdentifier.md) object
Required: Yes

 ** [registryId](#API_StartImageScan_RequestSyntax) **   <a name="ECR-StartImageScan-request-registryId"></a>
The AWS account ID associated with the registry that contains the repository in which to start an image scan request. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_StartImageScan_RequestSyntax) **   <a name="ECR-StartImageScan-request-repositoryName"></a>
The name of the repository that contains the images to scan.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_StartImageScan_ResponseSyntax"></a>

```
{
   "imageId": {
      "imageDigest": "string",
      "imageTag": "string"
   },
   "imageScanStatus": {
      "description": "string",
      "status": "string"
   },
   "registryId": "string",
   "repositoryName": "string"
}
```

## Response Elements
<a name="API_StartImageScan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageId](#API_StartImageScan_ResponseSyntax) **   <a name="ECR-StartImageScan-response-imageId"></a>
An object with identifying information for an image in an Amazon ECR repository.
Type: [ImageIdentifier](API_ImageIdentifier.md) object

 ** [imageScanStatus](#API_StartImageScan_ResponseSyntax) **   <a name="ECR-StartImageScan-response-imageScanStatus"></a>
The current state of the scan.
Type: [ImageScanStatus](API_ImageScanStatus.md) object

 ** [registryId](#API_StartImageScan_ResponseSyntax) **   <a name="ECR-StartImageScan-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryName](#API_StartImageScan_ResponseSyntax) **   <a name="ECR-StartImageScan-response-repositoryName"></a>
The repository name associated with the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`

## Errors
<a name="API_StartImageScan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ImageArchivedException **
The specified image is archived and cannot be scanned.
HTTP Status Code: 400

 ** ImageNotFoundException **
The image requested does not exist in the specified repository.
HTTP Status Code: 400

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

 ** UnsupportedImageTypeException **
The image is of a type that cannot be scanned.
HTTP Status Code: 400

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## Examples
<a name="API_StartImageScan_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_StartImageScan_Example_1"></a>

This example starts an image scan for and specified by the image digest in the `sample-repo` repository.

#### Sample Request
<a name="API_StartImageScan_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 141
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.StartImageScan
X-Amz-Date: 20161216T201255Z
User-Agent: aws-cli/1.16.310 Python/3.6.1 Darwin/18.7.0 botocore/1.13.46
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "repositoryName": "sample-repo",
    "imageId": {
        "imageDigest": "sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6"
    }
}
```

#### Sample Response
<a name="API_StartImageScan_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 24 Jan 2020 03:48:07 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 208
Connection: keep-alive
x-amzn-RequestId: 3081a92b-2066-41f8-8a47-0580288ada9e

{
    "registryId": "012345678910",
    "repositoryName": "sample-repo",
    "imageId": {
        "imageDigest": "sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6"
    },
    "imageScanStatus": {
        "status": "IN_PROGRESS"
    }
}
```

## See Also
<a name="API_StartImageScan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/StartImageScan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/StartImageScan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/StartImageScan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/StartImageScan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/StartImageScan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/StartImageScan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/StartImageScan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/StartImageScan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/StartImageScan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/StartImageScan)
