---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetCapacityTask.html
---

# GetCapacityTask
<a name="API_GetCapacityTask"></a>

Gets details of the specified capacity task.

## Request Syntax
<a name="API_GetCapacityTask_RequestSyntax"></a>

```
GET /outposts/{{OutpostId}}/capacity/{{CapacityTaskId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCapacityTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CapacityTaskId](#API_GetCapacityTask_RequestSyntax) **   <a name="outposts-GetCapacityTask-request-uri-CapacityTaskId"></a>
ID of the capacity task.
Length Constraints: Fixed length of 21.
Pattern: `^cap-[a-f0-9]{17}$`
Required: Yes

 ** [OutpostId](#API_GetCapacityTask_RequestSyntax) **   <a name="outposts-GetCapacityTask-request-uri-OutpostIdentifier"></a>
ID or ARN of the Outpost associated with the specified capacity task.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_GetCapacityTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCapacityTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AssetId": "string",
   "CapacityTaskId": "string",
   "CapacityTaskStatus": "string",
   "CompletionDate": number,
   "CreationDate": number,
   "DryRun": boolean,
   "Failed": {
      "Reason": "string",
      "Type": "string"
   },
   "InstancesToExclude": {
      "AccountIds": [ "string" ],
      "Instances": [ "string" ],
      "Services": [ "string" ]
   },
   "LastModifiedDate": number,
   "OrderId": "string",
   "OutpostId": "string",
   "RequestedInstancePools": [
      {
         "Count": number,
         "InstanceType": "string"
      }
   ],
   "TaskActionOnBlockingInstances": "string"
}
```

## Response Elements
<a name="API_GetCapacityTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssetId](#API_GetCapacityTask_ResponseSyntax) **   <a name="outposts-GetCapacityTask-response-AssetId"></a>
The ID of the Outpost asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(\w+)$`

 ** [CapacityTaskId](#API_GetCapacityTask_ResponseSyntax) **   <a name="outposts-GetCapacityTask-response-CapacityTaskId"></a>
ID of the capacity task.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^cap-[a-f0-9]{17}$`

 ** [CapacityTaskStatus](#API_GetCapacityTask_ResponseSyntax) **   <a name="outposts-GetCapacityTask-response-CapacityTaskStatus"></a>
Status of the capacity task.
A capacity task can have one of the following statuses:
+  `REQUESTED` - The capacity task was created and is awaiting the next step by AWS Outposts.
+  `IN_PROGRESS` - The capacity task is running and cannot be cancelled.
+  `FAILED` - The capacity task could not be completed.
+  `COMPLETED` - The capacity task has completed successfully.
+  `WAITING_FOR_EVACUATION` - The capacity task requires capacity to run. You must stop the recommended EC2 running instances to free up capacity for the task to run.
+  `CANCELLATION_IN_PROGRESS` - The capacity task has been cancelled and is in the process of cleaning up resources.
+  `CANCELLED` - The capacity task is cancelled.
Type: String
Valid Values: `REQUESTED | IN_PROGRESS | FAILED | COMPLETED | WAITING_FOR_EVACUATION | CANCELLATION_IN_PROGRESS | CANCELLED`

 ** [CompletionDate](#API_GetCapacityTask_ResponseSyntax) **   <a name="outposts-GetCapacityTask-response-CompletionDate"></a>
The date the capacity task ran successfully.
Type: Timestamp

 ** [CreationDate](#API_GetCapacityTask_ResponseSyntax) **   <a name="outposts-GetCapacityTask-response-CreationDate"></a>
The date the capacity task was created.
Type: Timestamp

 ** [DryRun](#API_GetCapacityTask_ResponseSyntax) **   <a name="outposts-GetCapacityTask-response-DryRun"></a>
Performs a dry run to determine if you are above or below instance capacity.
Type: Boolean

 ** [Failed](#API_GetCapacityTask_ResponseSyntax) **   <a name="outposts-GetCapacityTask-response-Failed"></a>
Reason why the capacity task failed.
Type: [CapacityTaskFailure](API_CapacityTaskFailure.md) object

 ** [InstancesToExclude](#API_GetCapacityTask_ResponseSyntax) **   <a name="outposts-GetCapacityTask-response-InstancesToExclude"></a>
Instances that the user specified they cannot stop in order to free up the capacity needed to run the capacity task.
Type: [InstancesToExclude](API_InstancesToExclude.md) object

 ** [LastModifiedDate](#API_GetCapacityTask_ResponseSyntax) **   <a name="outposts-GetCapacityTask-response-LastModifiedDate"></a>
The date the capacity task was last modified.
Type: Timestamp

 ** [OrderId](#API_GetCapacityTask_ResponseSyntax) **   <a name="outposts-GetCapacityTask-response-OrderId"></a>
ID of the AWS Outposts order associated with the specified capacity task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `oo-[a-f0-9]{17}$`

 ** [OutpostId](#API_GetCapacityTask_ResponseSyntax) **   <a name="outposts-GetCapacityTask-response-OutpostId"></a>
ID of the Outpost associated with the specified capacity task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`

 ** [RequestedInstancePools](#API_GetCapacityTask_ResponseSyntax) **   <a name="outposts-GetCapacityTask-response-RequestedInstancePools"></a>
List of instance pools requested in the capacity task.
Type: Array of [InstanceTypeCapacity](API_InstanceTypeCapacity.md) objects

 ** [TaskActionOnBlockingInstances](#API_GetCapacityTask_ResponseSyntax) **   <a name="outposts-GetCapacityTask-response-TaskActionOnBlockingInstances"></a>
User-specified option in case an instance is blocking the capacity task from running. Shows one of the following options:
+  `WAIT_FOR_EVACUATION` - Checks every 10 minutes over 48 hours to determine if instances have stopped and capacity is available to complete the task.
+  `FAIL_TASK` - The capacity task fails.
Type: String
Valid Values: `WAIT_FOR_EVACUATION | FAIL_TASK`

## Errors
<a name="API_GetCapacityTask_Errors"></a>

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
<a name="API_GetCapacityTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/GetCapacityTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/GetCapacityTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/GetCapacityTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/GetCapacityTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/GetCapacityTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/GetCapacityTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/GetCapacityTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/GetCapacityTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/GetCapacityTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/GetCapacityTask)
