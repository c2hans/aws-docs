---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DescribeImages.html
---

# DescribeImages
<a name="API_DescribeImages"></a>

Returns metadata that's related to the images in a repository in a public registry.

**Note**
Beginning with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the `docker images` command shows the uncompressed image size. Therefore, it might return a larger image size than the image sizes that are returned by [DescribeImages](#API_DescribeImages).

## Request Syntax
<a name="API_DescribeImages_RequestSyntax"></a>

```
{
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

 ** [imageIds](#API_DescribeImages_RequestSyntax) **   <a name="ecrpublic-DescribeImages-request-imageIds"></a>
The list of image IDs for the requested repository.
Type: Array of [ImageIdentifier](API_ImageIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [maxResults](#API_DescribeImages_RequestSyntax) **   <a name="ecrpublic-DescribeImages-request-maxResults"></a>
The maximum number of repository results that's returned by `DescribeImages` in paginated output. When this parameter is used, `DescribeImages` only returns `maxResults` results in a single page along with a `nextToken` response element. You can see the remaining results of the initial request by sending another `DescribeImages` request with the returned `nextToken` value. This value can be between 1 and 1000. If this parameter isn't used, then `DescribeImages` returns up to 100 results and a `nextToken` value, if applicable. If you specify images with `imageIds`, you can't use this option.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeImages_RequestSyntax) **   <a name="ecrpublic-DescribeImages-request-nextToken"></a>
The `nextToken` value that's returned from a previous paginated `DescribeImages` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. If there are no more results to return, this value is `null`. If you specify images with `imageIds`, you can't use this option.
Type: String
Required: No

 ** [registryId](#API_DescribeImages_RequestSyntax) **   <a name="ecrpublic-DescribeImages-request-registryId"></a>
The AWS account ID that's associated with the public registry that contains the repository where images are described. If you do not specify a registry, the default public registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_DescribeImages_RequestSyntax) **   <a name="ecrpublic-DescribeImages-request-repositoryName"></a>
The repository that contains the images to describe.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
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
         "imageSizeInBytes": number,
         "imageTags": [ "string" ],
         "registryId": "string",
         "repositoryName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeImages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageDetails](#API_DescribeImages_ResponseSyntax) **   <a name="ecrpublic-DescribeImages-response-imageDetails"></a>
A list of [ImageDetail](API_ImageDetail.md) objects that contain data about the image.
Type: Array of [ImageDetail](API_ImageDetail.md) objects

 ** [nextToken](#API_DescribeImages_ResponseSyntax) **   <a name="ecrpublic-DescribeImages-response-nextToken"></a>
The `nextToken` value to include in a future `DescribeImages` request. When the results of a `DescribeImages` request exceed `maxResults`, you can use this value to retrieve the next page of results. If there are no more results to return, this value is `null`.
Type: String

## Errors
<a name="API_DescribeImages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ImageNotFoundException **
The image requested doesn't exist in the specified repository.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
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
<a name="API_DescribeImages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/DescribeImages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/DescribeImages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/DescribeImages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/DescribeImages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/DescribeImages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/DescribeImages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/DescribeImages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/DescribeImages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/DescribeImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/DescribeImages)
