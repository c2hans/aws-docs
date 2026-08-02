---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_BKS_ListTagsForResource"></a>

This operation returns the tags for a resource type.

## Request Syntax
<a name="API_BKS_ListTagsForResource_RequestSyntax"></a>

```
GET /tags/{{ResourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_BKS_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_BKS_ListTagsForResource_RequestSyntax) **   <a name="Backup-BKS_ListTagsForResource-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the resource.>
Required: Yes

## Request Body
<a name="API_BKS_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_BKS_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_BKS_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_BKS_ListTagsForResource_ResponseSyntax) **   <a name="Backup-BKS_ListTagsForResource-response-Tags"></a>
List of tags returned by the operation.
Type: String to string map

## Errors
<a name="API_BKS_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry your request.
 ** message **
Unexpected error during processing of request.
 ** retryAfterSeconds **
Retry the call after number of seconds.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource was not found for this request.
Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.
 ** message **
Request references a resource which does not exist.
 ** resourceId **
Hypothetical identifier of the resource affected.
 ** resourceType **
Hypothetical type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
Request was unsuccessful due to request throttling.
 ** quotaCode **
This is the code unique to the originating service with the quota.
 ** retryAfterSeconds **
Retry the call after number of seconds.
 ** serviceCode **
This is the code unique to the originating service.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
 ** message **
The input fails to satisfy the constraints specified by an Amazon service.
HTTP Status Code: 400

## See Also
<a name="API_BKS_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backupsearch-2018-05-10/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backupsearch-2018-05-10/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backupsearch-2018-05-10/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backupsearch-2018-05-10/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backupsearch-2018-05-10/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backupsearch-2018-05-10/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backupsearch-2018-05-10/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/ListTagsForResource)
