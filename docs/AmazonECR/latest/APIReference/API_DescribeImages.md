---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImages.html
---

# DescribeImages
<a name="API_DescribeImages"></a>

Returns metadata about the images in a repository.

**Note**
Starting with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the `docker images` command shows the uncompressed image size. Therefore, Docker might return a larger image than the image shown in the AWS Management Console.

**Important**
The new version of Amazon ECR *Basic Scanning* doesn't use the [ImageDetail:imageScanFindingsSummary](API_ImageDetail.md#ECR-Type-ImageDetail-imageScanFindingsSummary) and [ImageDetail:imageScanStatus](API_ImageDetail.md#ECR-Type-ImageDetail-imageScanStatus) attributes from the API response to return scan results. Use the [DescribeImageScanFindings](API_DescribeImageScanFindings.md) API instead. For more information about AWS native basic scanning, see [ Scan images for software vulnerabilities in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html).

## Request Syntax
<a name="API_DescribeImages_RequestSyntax"></a>

```
{
   "filter": {
      "imageStatus": "{{string}}",
      "tagStatus": "{{string}}"
   },
   "imageIds": [
      {
         "imageDigest": "{{string}}",
         "imageTag": "{{string}}"
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeImages_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_DescribeImages_RequestSyntax) **   <a name="ECR-DescribeImages-request-filter"></a>
The filter key and value with which to filter your `DescribeImages` results.
Type: [DescribeImagesFilter](API_DescribeImagesFilter.md) object
Required: No

 ** [imageIds](#API_DescribeImages_RequestSyntax) **   <a name="ECR-DescribeImages-request-imageIds"></a>
The list of image IDs for the requested repository.
Type: Array of [ImageIdentifier](API_ImageIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [maxResults](#API_DescribeImages_RequestSyntax) **   <a name="ECR-DescribeImages-request-maxResults"></a>
The maximum number of repository results returned by `DescribeImages` in paginated output. When this parameter is used, `DescribeImages` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `DescribeImages` request with the returned `nextToken` value. This value can be between 1 and 1000. If this parameter is not used, then `DescribeImages` returns up to 100 results and a `nextToken` value, if applicable. This option cannot be used when you specify images with `imageIds`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeImages_RequestSyntax) **   <a name="ECR-DescribeImages-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `DescribeImages` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return. This option cannot be used when you specify images with `imageIds`.
Type: String
Required: No

 ** [registryId](#API_DescribeImages_RequestSyntax) **   <a name="ECR-DescribeImages-request-registryId"></a>
The AWS account ID associated with the registry that contains the repository in which to describe images. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_DescribeImages_RequestSyntax) **   <a name="ECR-DescribeImages-request-repositoryName"></a>
The repository that contains the images to describe.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_DescribeImages_ResponseSyntax"></a>

```
{
   "imageDetails": [
      {
         "artifactMediaType": "string",
         "imageDigest": "string",
         "imageManifestMediaType": "string",
         "imagePushedAt": number,
         "imageScanFindingsSummary": {
            "findingSeverityCounts": {
               "string" : number
            },
            "imageScanCompletedAt": number,
            "vulnerabilitySourceUpdatedAt": number
         },
         "imageScanStatus": {
            "description": "string",
            "status": "string"
         },
         "imageSizeInBytes": number,
         "imageStatus": "string",
         "imageTags": [ "string" ],
         "lastActivatedAt": number,
         "lastArchivedAt": number,
         "lastRecordedPullTime": number,
         "registryId": "string",
         "repositoryName": "string",
         "subjectManifestDigest": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeImages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageDetails](#API_DescribeImages_ResponseSyntax) **   <a name="ECR-DescribeImages-response-imageDetails"></a>
A list of [ImageDetail](API_ImageDetail.md) objects that contain data about the image.
Type: Array of [ImageDetail](API_ImageDetail.md) objects

 ** [nextToken](#API_DescribeImages_ResponseSyntax) **   <a name="ECR-DescribeImages-response-nextToken"></a>
The `nextToken` value to include in a future `DescribeImages` request. When the results of a `DescribeImages` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_DescribeImages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ImageNotFoundException **
The image requested does not exist in the specified repository.
HTTP Status Code: 400

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
<a name="API_DescribeImages_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeImages_Example_1"></a>

This example describes the images in a repository named `hello-repository` in the default account. Note that the image with the digest `sha256:7a64bc9c8843b0a8c8b8a7e4715b7615e4e1b0d8ca3c7e7a76ecEXAMPLE` is tagged as `latest` and `tagtest`.

#### Sample Request
<a name="API_DescribeImages_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 38
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.DescribeImages
X-Amz-Date: 20220301T194641Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.3.0 botocore/1.4.79
Content-Type: application/x-amz-json-1.1

Authorization: AUTHPARAMS

{
  "repositoryName": "hello-repository"
}
```

#### Sample Response
<a name="API_DescribeImages_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 16 Dec 2016 19:31:33 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 1107
Connection: keep-alive
x-amzn-RequestId: 404826b1-c3c6-11e6-a9e5-e3c203a2f07f

{
    "imageDetails": [
        {
            "registryId": "012345678910",
            "repositoryName": "hello-repository",
            "imageDigest": "sha256:7a64bc9c8843b0a8c8b8a7e4715b7615e4e1b0d8ca3c7e7a76ecEXAMPLE",
            "imageTags": [
                "tagtest"
            ],
            "imageSizeInBytes": 78447648,
            "imagePushedAt": "2021-12-03T20:36:09+00:00",
            "imageScanStatus": {
                "status": "COMPLETE",
                "description": "The scan was completed successfully."
            },
            "imageScanFindingsSummary": {
                "imageScanCompletedAt": "2021-12-03T20:36:14+00:00",
                "vulnerabilitySourceUpdatedAt": "2021-11-24T16:11:37+00:00",
                "findingSeverityCounts": {
                    "HIGH": 4,
                    "MEDIUM": 76,
                    "INFORMATIONAL": 9,
                    "LOW": 50
                }
            },
            "imageManifestMediaType": "application/vnd.docker.distribution.manifest.v2+json",
            "artifactMediaType": "application/vnd.docker.container.image.v1+json",
            "lastRecordedPullTime": "2022-02-23T05:06:01.514000+00:00"
        },
        {
            "registryId": "012345678910",
            "repositoryName": "hello-repository",
            "imageDigest": "sha256:7a64bc9c8843b0a8c8b8a7e4715b7615e4e1b0d8ca3c7e7a76ecEXAMPLE",
            "imageTags": [
                "latest"
            ],
            "imageSizeInBytes": 78447648,
            "imagePushedAt": "2020-01-23T17:56:13+00:00",
            "imageScanStatus": {
                "status": "COMPLETE",
                "description": "The scan was completed successfully."
            },
            "imageScanFindingsSummary": {
                "imageScanCompletedAt": "2020-01-24T04:11:45+00:00",
                "vulnerabilitySourceUpdatedAt": "2020-01-23T20:25:17+00:00",
                "findingSeverityCounts": {
                    "MEDIUM": 14,
                    "INFORMATIONAL": 11,
                    "LOW": 27
                }
            },
            "imageManifestMediaType": "application/vnd.docker.distribution.manifest.v2+json",
            "lastRecordedPullTime": "2022-02-24T07:35:16.530000+00:00"
        }
    ]
}
```

## See Also
<a name="API_DescribeImages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/DescribeImages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/DescribeImages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DescribeImages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/DescribeImages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DescribeImages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/DescribeImages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/DescribeImages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/DescribeImages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DescribeImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DescribeImages)
