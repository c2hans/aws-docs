---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_ListQueues.html
---

# ListQueues
<a name="API_ListQueues"></a>

Returns a list of all queues associated with a cluster.

## Request Syntax
<a name="API_ListQueues_RequestSyntax"></a>

```
{
   "clusterIdentifier": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListQueues_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clusterIdentifier](#API_ListQueues_RequestSyntax) **   <a name="PCS-ListQueues-request-clusterIdentifier"></a>
The name or ID of the cluster to list queues for.
Type: String
Pattern: `(pcs_[a-zA-Z0-9]+|[A-Za-z][A-Za-z0-9-]{2,40})`
Required: Yes

 ** [maxResults](#API_ListQueues_RequestSyntax) **   <a name="PCS-ListQueues-request-maxResults"></a>
The maximum number of results that are returned per call. You can use `nextToken` to obtain further pages of results. The default is 10 results, and the maximum allowed page size is 100 results. A value of 0 uses the default.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListQueues_RequestSyntax) **   <a name="PCS-ListQueues-request-nextToken"></a>
The value of `nextToken` is a unique pagination token for each page of results returned. If `nextToken` is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token returns an `HTTP 400 InvalidToken` error.
Type: String
Required: No

## Response Syntax
<a name="API_ListQueues_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "queues": [
      {
         "arn": "string",
         "clusterId": "string",
         "createdAt": "string",
         "id": "string",
         "modifiedAt": "string",
         "name": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListQueues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListQueues_ResponseSyntax) **   <a name="PCS-ListQueues-response-nextToken"></a>
The value of `nextToken` is a unique pagination token for each page of results returned. If `nextToken` is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token returns an `HTTP 400 InvalidToken` error.
Type: String

 ** [queues](#API_ListQueues_ResponseSyntax) **   <a name="PCS-ListQueues-response-queues"></a>
The list of queues associated with the cluster.
Type: Array of [QueueSummary](API_QueueSummary.md) objects

## Errors
<a name="API_ListQueues_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
 *Examples*
+ The launch template instance profile doesn't pass `iam:PassRole` verification.
+ There is a mismatch between the account ID and cluster ID.
+ The cluster ID doesn't exist.
+ The EC2 instance isn't present.
HTTP Status Code: 400

 ** ConflictException **
Your request has conflicting operations. This can occur if you're trying to perform more than 1 operation on the same resource at the same time.
 *Examples*
+ A cluster with the same name already exists.
+ A cluster isn't in `ACTIVE` status.
+ A cluster to delete is in an unstable state. For example, because it still has `ACTIVE` node groups or queues.
+ A queue already exists in a cluster.
 ** resourceId **
 The unique identifier of the resource that caused the conflict exception.
 ** resourceType **
 The type or category of the resource that caused the conflict exception."
HTTP Status Code: 400

 ** InternalServerException **
 AWS PCS can't process your request right now. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found. The cluster, node group, or queue you're attempting to get, update, list, or delete doesn't exist.
 *Examples*
 ** resourceId **
 The unique identifier of the resource that was not found.
 ** resourceType **
 The type or category of the resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
Your request exceeded a request rate quota. Check the resource's request rate quota and try again.
 ** retryAfterSeconds **
 The number of seconds to wait before retrying the request.
HTTP Status Code: 400

 ** ValidationException **
The request isn't valid.
 *Examples*
+ Your request contains malformed JSON or unsupported characters.
+ The scheduler version isn't supported.
+ There are networking related errors, such as network validation failure.
+ AMI type is `CUSTOM` and the launch template doesn't define the AMI ID, or the AMI type is AL2 and the launch template defines the AMI.
 ** fieldList **
 A list of fields or properties that failed validation.
 ** reason **
 The specific reason or cause of the validation error.
HTTP Status Code: 400

## See Also
<a name="API_ListQueues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pcs-2023-02-10/ListQueues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pcs-2023-02-10/ListQueues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/ListQueues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pcs-2023-02-10/ListQueues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/ListQueues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pcs-2023-02-10/ListQueues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pcs-2023-02-10/ListQueues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pcs-2023-02-10/ListQueues)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pcs-2023-02-10/ListQueues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/ListQueues)
