---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListBlockingInstancesForCapacityTask.html
---

# ListBlockingInstancesForCapacityTask
<a name="API_ListBlockingInstancesForCapacityTask"></a>

A list of Amazon EC2 instances running on the Outpost and belonging to the account that initiated the capacity task. Use this list to specify the instances you cannot stop to free up capacity to run the capacity task.

## Request Syntax
<a name="API_ListBlockingInstancesForCapacityTask_RequestSyntax"></a>

```
GET /outposts/{{OutpostId}}/capacity/{{CapacityTaskId}}/blockingInstances?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBlockingInstancesForCapacityTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CapacityTaskId](#API_ListBlockingInstancesForCapacityTask_RequestSyntax) **   <a name="outposts-ListBlockingInstancesForCapacityTask-request-uri-CapacityTaskId"></a>
The ID of the capacity task.
Length Constraints: Fixed length of 21.
Pattern: `^cap-[a-f0-9]{17}$`
Required: Yes

 ** [MaxResults](#API_ListBlockingInstancesForCapacityTask_RequestSyntax) **   <a name="outposts-ListBlockingInstancesForCapacityTask-request-uri-MaxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListBlockingInstancesForCapacityTask_RequestSyntax) **   <a name="outposts-ListBlockingInstancesForCapacityTask-request-uri-NextToken"></a>
The pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [OutpostId](#API_ListBlockingInstancesForCapacityTask_RequestSyntax) **   <a name="outposts-ListBlockingInstancesForCapacityTask-request-uri-OutpostIdentifier"></a>
The ID or ARN of the Outpost associated with the specified capacity task.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_ListBlockingInstancesForCapacityTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBlockingInstancesForCapacityTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BlockingInstances": [
      {
         "AccountId": "string",
         "AwsServiceName": "string",
         "InstanceId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListBlockingInstancesForCapacityTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BlockingInstances](#API_ListBlockingInstancesForCapacityTask_ResponseSyntax) **   <a name="outposts-ListBlockingInstancesForCapacityTask-response-BlockingInstances"></a>
A list of all running Amazon EC2 instances on the Outpost. Stopping one or more of these instances can free up the capacity needed to run the capacity task.
Type: Array of [BlockingInstance](API_BlockingInstance.md) objects

 ** [NextToken](#API_ListBlockingInstancesForCapacityTask_ResponseSyntax) **   <a name="outposts-ListBlockingInstancesForCapacityTask-response-NextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

## Errors
<a name="API_ListBlockingInstancesForCapacityTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListBlockingInstancesForCapacityTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/ListBlockingInstancesForCapacityTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/ListBlockingInstancesForCapacityTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ListBlockingInstancesForCapacityTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/ListBlockingInstancesForCapacityTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ListBlockingInstancesForCapacityTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/ListBlockingInstancesForCapacityTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/ListBlockingInstancesForCapacityTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/ListBlockingInstancesForCapacityTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/ListBlockingInstancesForCapacityTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ListBlockingInstancesForCapacityTask)
