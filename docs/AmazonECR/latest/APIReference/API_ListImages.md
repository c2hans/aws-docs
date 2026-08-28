---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListImages.html
---

# ListImages
<a name="API_ListImages"></a>

Lists all the image IDs for the specified repository.

You can filter images based on whether or not they are tagged by using the `tagStatus` filter and specifying either `TAGGED`, `UNTAGGED` or `ANY`. For example, you can filter your results to return only `UNTAGGED` images and then pipe that result to a [BatchDeleteImage](API_BatchDeleteImage.md) operation to delete them. Or, you can filter your results to return only `TAGGED` images to list all of the tags in your repository.

## Request Syntax
<a name="API_ListImages_RequestSyntax"></a>

```
{
   "filter": {
      "imageStatus": "{{string}}",
      "tagStatus": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListImages_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_ListImages_RequestSyntax) **   <a name="ECR-ListImages-request-filter"></a>
The filter key and value with which to filter your `ListImages` results.
Type: [ListImagesFilter](API_ListImagesFilter.md) object
Required: No

 ** [maxResults](#API_ListImages_RequestSyntax) **   <a name="ECR-ListImages-request-maxResults"></a>
The maximum number of image results returned by `ListImages` in paginated output. When this parameter is used, `ListImages` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListImages` request with the returned `nextToken` value. This value can be between 1 and 1000. If this parameter is not used, then `ListImages` returns up to 100 results and a `nextToken` value, if applicable.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListImages_RequestSyntax) **   <a name="ECR-ListImages-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListImages` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

 ** [registryId](#API_ListImages_RequestSyntax) **   <a name="ECR-ListImages-request-registryId"></a>
The AWS account ID associated with the registry that contains the repository in which to list images. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_ListImages_RequestSyntax) **   <a name="ECR-ListImages-request-repositoryName"></a>
The repository with image IDs to be listed.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_ListImages_ResponseSyntax"></a>

```
{
   "imageIds": [
      {
         "imageDigest": "string",
         "imageTag": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListImages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [imageIds](#API_ListImages_ResponseSyntax) **   <a name="ECR-ListImages-response-imageIds"></a>
The list of image IDs for the requested repository.
Type: Array of [ImageIdentifier](API_ImageIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [nextToken](#API_ListImages_ResponseSyntax) **   <a name="ECR-ListImages-response-nextToken"></a>
The `nextToken` value to include in a future `ListImages` request. When the results of a `ListImages` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_ListImages_Errors"></a>

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
<a name="API_ListImages_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListImages_Example_1"></a>

This example lists all of the images in the `amazonlinux` repository.

#### Sample Request
<a name="API_ListImages_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 33
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.ListImages
X-Amz-Date: 20161216T200542Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.3.0 botocore/1.4.79
Content-Type: application/x-amz-json-1.1
Authorization: AWUTHPARAMS

{
  "repositoryName": "amazonlinux"
}
```

#### Sample Response
<a name="API_ListImages_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 16 Dec 2016 20:05:42 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 235
Connection: keep-alive
x-amzn-RequestId: 05bfc4ac-c3cb-11e6-99fb-b1be070cc24b

{
  "imageIds": [
    {
      "imageDigest": "sha256:f1d4ae3f7261a72e98c6ebefe9985cf10a0ea5bd762585a43e0700ed99863807",
      "imageTag": "2016.09"
    },
    {
      "imageDigest": "sha256:f1d4ae3f7261a72e98c6ebefe9985cf10a0ea5bd762585a43e0700ed99863807",
      "imageTag": "latest"
    }
  ]
}
```

## See Also
<a name="API_ListImages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/ListImages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/ListImages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ListImages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/ListImages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ListImages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/ListImages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/ListImages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/ListImages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/ListImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ListImages)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
