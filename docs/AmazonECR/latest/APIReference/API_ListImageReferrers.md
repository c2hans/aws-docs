---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListImageReferrers.html
---

# ListImageReferrers
<a name="API_ListImageReferrers"></a>

Lists the artifacts associated with a specified subject image.

**Note**
The IAM principal invoking this operation must have the `ecr:BatchGetImage` permission.

## Request Syntax
<a name="API_ListImageReferrers_RequestSyntax"></a>

```
{
   "filter": {
      "artifactStatus": "{{string}}",
      "artifactTypes": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "registryId": "{{string}}",
   "repositoryName": "{{string}}",
   "subjectId": {
      "imageDigest": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ListImageReferrers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_ListImageReferrers_RequestSyntax) **   <a name="ECR-ListImageReferrers-request-filter"></a>
The filter key and value with which to filter your `ListImageReferrers` results. If no filter is specified, only artifacts with `ACTIVE` status are returned.
Type: [ListImageReferrersFilter](API_ListImageReferrersFilter.md) object
Required: No

 ** [maxResults](#API_ListImageReferrers_RequestSyntax) **   <a name="ECR-ListImageReferrers-request-maxResults"></a>
The maximum number of image referrer results returned by `ListImageReferrers` in paginated output. When this parameter is used, `ListImageReferrers` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListImageReferrers` request with the returned `nextToken` value. This value can be between 1 and 50. If this parameter is not used, then `ListImageReferrers` returns up to 20 results and a `nextToken` value, if applicable.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListImageReferrers_RequestSyntax) **   <a name="ECR-ListImageReferrers-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListImageReferrers` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

 ** [registryId](#API_ListImageReferrers_RequestSyntax) **   <a name="ECR-ListImageReferrers-request-registryId"></a>
The AWS account ID associated with the registry that contains the repository in which to list image referrers. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_ListImageReferrers_RequestSyntax) **   <a name="ECR-ListImageReferrers-request-repositoryName"></a>
The name of the repository that contains the subject image.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

 ** [subjectId](#API_ListImageReferrers_RequestSyntax) **   <a name="ECR-ListImageReferrers-request-subjectId"></a>
An object containing the image digest of the subject image for which to retrieve associated artifacts.
Type: [SubjectIdentifier](API_SubjectIdentifier.md) object
Required: Yes

## Response Syntax
<a name="API_ListImageReferrers_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "referrers": [
      {
         "annotations": {
            "string" : "string"
         },
         "artifactStatus": "string",
         "artifactType": "string",
         "digest": "string",
         "mediaType": "string",
         "size": number
      }
   ]
}
```

## Response Elements
<a name="API_ListImageReferrers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListImageReferrers_ResponseSyntax) **   <a name="ECR-ListImageReferrers-response-nextToken"></a>
The `nextToken` value to include in a future `ListImageReferrers` request. When the results of a `ListImageReferrers` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 ** [referrers](#API_ListImageReferrers_ResponseSyntax) **   <a name="ECR-ListImageReferrers-response-referrers"></a>
The list of artifacts associated with the subject image.
Type: Array of [ImageReferrer](API_ImageReferrer.md) objects

## Errors
<a name="API_ListImageReferrers_Errors"></a>

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

 ** UnableToListUpstreamImageReferrersException **
The referrer or referrers were unable to be listed using the pull through cache rule. This is usually caused because of an issue with the Secrets Manager secret containing the credentials for the upstream registry.
HTTP Status Code: 400

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## Examples
<a name="API_ListImageReferrers_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### To list artifacts associated with a subject image
<a name="API_ListImageReferrers_Example_1"></a>

This example lists all artifacts (such as Sigstore signatures) that reference a specific container image in the `sample-repo` repository.

#### Sample Request
<a name="API_ListImageReferrers_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: api.ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.ListImageReferrers
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0 Python/3.8.0 Darwin/20.0.0 botocore/2.0.0
X-Amz-Date: 20251117T220033Z
Authorization: AUTHPARAMS
Content-Length: 150

{
   "repositoryName": "sample-repo",
   "subjectId": {
      "imageDigest": "sha256:943e640159415616581703a53fa4ed87e96740655fd67daf2d2146a35337bce5"
   }
}
```

#### Sample Response
<a name="API_ListImageReferrers_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f
Content-Type: application/x-amz-json-1.1
Content-Length: 470
Connection: keep-alive

{
   "referrers": [
      {
         "digest": "sha256:270c60be5b6ed41e6e7c505ac0c4e2577748affc14147bcba76b533604dc7a07",
         "mediaType": "application/vnd.oci.image.manifest.v1+json",
         "artifactType": "application/vnd.dev.sigstore.bundle.v0.3+json",
         "size": 888,
         "annotations": {
            "dev.sigstore.bundle.predicateType": "https://sigstore.dev/cosign/sign/v1",
            "dev.sigstore.bundle.content": "dsse-envelope",
            "org.opencontainers.image.created": "2025-11-17T22:00:33Z"
         },
         "artifactStatus": "ACTIVE"
      }
   ]
}
```

## See Also
<a name="API_ListImageReferrers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/ListImageReferrers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/ListImageReferrers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ListImageReferrers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/ListImageReferrers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ListImageReferrers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/ListImageReferrers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/ListImageReferrers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/ListImageReferrers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/ListImageReferrers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ListImageReferrers)
