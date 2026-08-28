---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetLifecyclePolicyPreview.html
---

# GetLifecyclePolicyPreview
<a name="API_GetLifecyclePolicyPreview"></a>

Retrieves the results of the lifecycle policy preview request for the specified repository.

## Request Syntax
<a name="API_GetLifecyclePolicyPreview_RequestSyntax"></a>

```
{
   "filter": {
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
<a name="API_GetLifecyclePolicyPreview_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_GetLifecyclePolicyPreview_RequestSyntax) **   <a name="ECR-GetLifecyclePolicyPreview-request-filter"></a>
An optional parameter that filters results based on image tag status and all tags, if tagged.
Type: [LifecyclePolicyPreviewFilter](API_LifecyclePolicyPreviewFilter.md) object
Required: No

 ** [imageIds](#API_GetLifecyclePolicyPreview_RequestSyntax) **   <a name="ECR-GetLifecyclePolicyPreview-request-imageIds"></a>
The list of imageIDs to be included.
Type: Array of [ImageIdentifier](API_ImageIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [maxResults](#API_GetLifecyclePolicyPreview_RequestSyntax) **   <a name="ECR-GetLifecyclePolicyPreview-request-maxResults"></a>
The maximum number of repository results returned by `GetLifecyclePolicyPreviewRequest` in  paginated output. When this parameter is used, `GetLifecyclePolicyPreviewRequest` only returns  `maxResults` results in a single page along with a `nextToken`  response element. The remaining results of the initial request can be seen by sending  another `GetLifecyclePolicyPreviewRequest` request with the returned `nextToken`  value. This value can be between 1 and 100. If this  parameter is not used, then `GetLifecyclePolicyPreviewRequest` returns up to 100 results and a `nextToken` value, if  applicable. This option cannot be used when you specify images with `imageIds`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_GetLifecyclePolicyPreview_RequestSyntax) **   <a name="ECR-GetLifecyclePolicyPreview-request-nextToken"></a>
The `nextToken` value returned from a previous paginated  `GetLifecyclePolicyPreviewRequest` request where `maxResults` was used and the  results exceeded the value of that parameter. Pagination continues from the end of the  previous results that returned the `nextToken` value. This value is  `null` when there are no more results to return. This option cannot be used when you specify images with `imageIds`.
Type: String
Required: No

 ** [registryId](#API_GetLifecyclePolicyPreview_RequestSyntax) **   <a name="ECR-GetLifecyclePolicyPreview-request-registryId"></a>
The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_GetLifecyclePolicyPreview_RequestSyntax) **   <a name="ECR-GetLifecyclePolicyPreview-request-repositoryName"></a>
The name of the repository.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

## Response Syntax
<a name="API_GetLifecyclePolicyPreview_ResponseSyntax"></a>

```
{
   "lifecyclePolicyText": "string",
   "nextToken": "string",
   "previewResults": [
      {
         "action": {
            "targetStorageClass": "string",
            "type": "string"
         },
         "appliedRulePriority": number,
         "imageDigest": "string",
         "imagePushedAt": number,
         "imageTags": [ "string" ],
         "storageClass": "string"
      }
   ],
   "registryId": "string",
   "repositoryName": "string",
   "status": "string",
   "summary": {
      "expiringImageTotalCount": number,
      "transitioningImageTotalCounts": [
         {
            "imageTotalCount": number,
            "targetStorageClass": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetLifecyclePolicyPreview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecyclePolicyText](#API_GetLifecyclePolicyPreview_ResponseSyntax) **   <a name="ECR-GetLifecyclePolicyPreview-response-lifecyclePolicyText"></a>
The JSON lifecycle policy text.
Type: String
Length Constraints: Minimum length of 100. Maximum length of 30720.

 ** [nextToken](#API_GetLifecyclePolicyPreview_ResponseSyntax) **   <a name="ECR-GetLifecyclePolicyPreview-response-nextToken"></a>
The `nextToken` value to include in a future `GetLifecyclePolicyPreview` request. When the results of a `GetLifecyclePolicyPreview` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 ** [previewResults](#API_GetLifecyclePolicyPreview_ResponseSyntax) **   <a name="ECR-GetLifecyclePolicyPreview-response-previewResults"></a>
The results of the lifecycle policy preview request.
Type: Array of [LifecyclePolicyPreviewResult](API_LifecyclePolicyPreviewResult.md) objects

 ** [registryId](#API_GetLifecyclePolicyPreview_ResponseSyntax) **   <a name="ECR-GetLifecyclePolicyPreview-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [repositoryName](#API_GetLifecyclePolicyPreview_ResponseSyntax) **   <a name="ECR-GetLifecyclePolicyPreview-response-repositoryName"></a>
The repository name associated with the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`

 ** [status](#API_GetLifecyclePolicyPreview_ResponseSyntax) **   <a name="ECR-GetLifecyclePolicyPreview-response-status"></a>
The status of the lifecycle policy preview request.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | EXPIRED | FAILED`

 ** [summary](#API_GetLifecyclePolicyPreview_ResponseSyntax) **   <a name="ECR-GetLifecyclePolicyPreview-response-summary"></a>
The list of images that is returned as a result of the action.
Type: [LifecyclePolicyPreviewSummary](API_LifecyclePolicyPreviewSummary.md) object

## Errors
<a name="API_GetLifecyclePolicyPreview_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** LifecyclePolicyPreviewNotFoundException **
There is no dry run for this repository.
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

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## Examples
<a name="API_GetLifecyclePolicyPreview_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_GetLifecyclePolicyPreview_Example_1"></a>

This example retrieves the result of a lifecycle policy preview for a repository called `project-a/amazon-ecs-sample` in the default registry for an account.

#### Sample Request
<a name="API_GetLifecyclePolicyPreview_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ecr.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonEC2ContainerRegistry_V20150921.GetLifecyclePolicyPreview
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.11.144 Python/3.6.1 Darwin/16.6.0 botocore/1.7.2
X-Amz-Date: 20170901T222304Z
Authorization: AUTHPARAMS
Content-Length: 48

{
   "repositoryName": "project-a/amazon-ecs-sample"
}
```

#### Sample Response
<a name="API_GetLifecyclePolicyPreview_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 01 Sep 2017 22:23:06 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 640
Connection: keep-alive
x-amzn-RequestId: 123a4b56-7c89-01d2-3ef4-example5678f

{
   "lifecyclePolicyText":"{\n    \"rules\": [\n        {\n            \"rulePriority\": 1,\n            \"description\": \"Expire images older than 14 days\",\n            \"selection\": {\n                \"tagStatus\": \"untagged\",\n                \"countType\": \"sinceImagePushed\",\n                \"countUnit\": \"days\",\n                \"countNumber\": 14\n            },\n            \"action\": {\n                \"type\": \"expire\"\n            }\n        }\n    ]\n}\n",
   "previewResults":[],
   "registryId":"012345678910",
   "repositoryName":"project-a/amazon-ecs-sample",
   "status":"COMPLETE",
   "summary":{"expiringImageTotalCount":0}
}
```

## See Also
<a name="API_GetLifecyclePolicyPreview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/GetLifecyclePolicyPreview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/GetLifecyclePolicyPreview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/GetLifecyclePolicyPreview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/GetLifecyclePolicyPreview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/GetLifecyclePolicyPreview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/GetLifecyclePolicyPreview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/GetLifecyclePolicyPreview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/GetLifecyclePolicyPreview)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/GetLifecyclePolicyPreview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/GetLifecyclePolicyPreview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
