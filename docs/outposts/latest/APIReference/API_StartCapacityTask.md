---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_StartCapacityTask.html
---

# StartCapacityTask
<a name="API_StartCapacityTask"></a>

Starts the specified capacity task. You can have one active capacity task for each order and each Outpost.

## Request Syntax
<a name="API_StartCapacityTask_RequestSyntax"></a>

```
POST /outposts/{{OutpostId}}/capacity HTTP/1.1
Content-type: application/json

{
   "AssetId": "{{string}}",
   "DryRun": {{boolean}},
   "InstancePools": [
      {
         "Count": {{number}},
         "InstanceType": "{{string}}"
      }
   ],
   "InstancesToExclude": {
      "AccountIds": [ "{{string}}" ],
      "Instances": [ "{{string}}" ],
      "Services": [ "{{string}}" ]
   },
   "OrderId": "{{string}}",
   "TaskActionOnBlockingInstances": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartCapacityTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [OutpostId](#API_StartCapacityTask_RequestSyntax) **   <a name="outposts-StartCapacityTask-request-uri-OutpostIdentifier"></a>
The ID or ARN of the Outposts associated with the specified capacity task.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_StartCapacityTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AssetId](#API_StartCapacityTask_RequestSyntax) **   <a name="outposts-StartCapacityTask-request-AssetId"></a>
The ID of the Outpost asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{10}`
Required: No

 ** [DryRun](#API_StartCapacityTask_RequestSyntax) **   <a name="outposts-StartCapacityTask-request-DryRun"></a>
You can request a dry run to determine if the instance type and instance size changes is above or below available instance capacity. Requesting a dry run does not make any changes to your plan.
Type: Boolean
Required: No

 ** [InstancePools](#API_StartCapacityTask_RequestSyntax) **   <a name="outposts-StartCapacityTask-request-InstancePools"></a>
The instance pools specified in the capacity task.
Type: Array of [InstanceTypeCapacity](API_InstanceTypeCapacity.md) objects
Required: Yes

 ** [InstancesToExclude](#API_StartCapacityTask_RequestSyntax) **   <a name="outposts-StartCapacityTask-request-InstancesToExclude"></a>
List of user-specified running instances that must not be stopped in order to free up the capacity needed to run the capacity task.
Type: [InstancesToExclude](API_InstancesToExclude.md) object
Required: No

 ** [OrderId](#API_StartCapacityTask_RequestSyntax) **   <a name="outposts-StartCapacityTask-request-OrderId"></a>
The ID of the AWS Outposts order associated with the specified capacity task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `oo-[a-f0-9]{17}$`
Required: No

 ** [TaskActionOnBlockingInstances](#API_StartCapacityTask_RequestSyntax) **   <a name="outposts-StartCapacityTask-request-TaskActionOnBlockingInstances"></a>
Specify one of the following options in case an instance is blocking the capacity task from running.
+  `WAIT_FOR_EVACUATION` - Checks every 10 minutes over 48 hours to determine if instances have stopped and capacity is available to complete the task.
+  `FAIL_TASK` - The capacity task fails.
Type: String
Valid Values: `WAIT_FOR_EVACUATION | FAIL_TASK`
Required: No

## Response Syntax
<a name="API_StartCapacityTask_ResponseSyntax"></a>

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
<a name="API_StartCapacityTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssetId](#API_StartCapacityTask_ResponseSyntax) **   <a name="outposts-StartCapacityTask-response-AssetId"></a>
The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(\w+)$`

 ** [CapacityTaskId](#API_StartCapacityTask_ResponseSyntax) **   <a name="outposts-StartCapacityTask-response-CapacityTaskId"></a>
ID of the capacity task that you want to start.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^cap-[a-f0-9]{17}$`

 ** [CapacityTaskStatus](#API_StartCapacityTask_ResponseSyntax) **   <a name="outposts-StartCapacityTask-response-CapacityTaskStatus"></a>
Status of the specified capacity task.
Type: String
Valid Values: `REQUESTED | IN_PROGRESS | FAILED | COMPLETED | WAITING_FOR_EVACUATION | CANCELLATION_IN_PROGRESS | CANCELLED`

 ** [CompletionDate](#API_StartCapacityTask_ResponseSyntax) **   <a name="outposts-StartCapacityTask-response-CompletionDate"></a>
Date that the specified capacity task ran successfully.
Type: Timestamp

 ** [CreationDate](#API_StartCapacityTask_ResponseSyntax) **   <a name="outposts-StartCapacityTask-response-CreationDate"></a>
Date that the specified capacity task was created.
Type: Timestamp

 ** [DryRun](#API_StartCapacityTask_ResponseSyntax) **   <a name="outposts-StartCapacityTask-response-DryRun"></a>
Results of the dry run showing if the specified capacity task is above or below the available instance capacity.
Type: Boolean

 ** [Failed](#API_StartCapacityTask_ResponseSyntax) **   <a name="outposts-StartCapacityTask-response-Failed"></a>
Reason that the specified capacity task failed.
Type: [CapacityTaskFailure](API_CapacityTaskFailure.md) object

 ** [InstancesToExclude](#API_StartCapacityTask_ResponseSyntax) **   <a name="outposts-StartCapacityTask-response-InstancesToExclude"></a>
User-specified instances that must not be stopped in order to free up the capacity needed to run the capacity task.
Type: [InstancesToExclude](API_InstancesToExclude.md) object

 ** [LastModifiedDate](#API_StartCapacityTask_ResponseSyntax) **   <a name="outposts-StartCapacityTask-response-LastModifiedDate"></a>
Date that the specified capacity task was last modified.
Type: Timestamp

 ** [OrderId](#API_StartCapacityTask_ResponseSyntax) **   <a name="outposts-StartCapacityTask-response-OrderId"></a>
ID of the AWS Outposts order of the host associated with the capacity task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `oo-[a-f0-9]{17}$`

 ** [OutpostId](#API_StartCapacityTask_ResponseSyntax) **   <a name="outposts-StartCapacityTask-response-OutpostId"></a>
ID of the Outpost associated with the capacity task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`

 ** [RequestedInstancePools](#API_StartCapacityTask_ResponseSyntax) **   <a name="outposts-StartCapacityTask-response-RequestedInstancePools"></a>
List of the instance pools requested in the specified capacity task.
Type: Array of [InstanceTypeCapacity](API_InstanceTypeCapacity.md) objects

 ** [TaskActionOnBlockingInstances](#API_StartCapacityTask_ResponseSyntax) **   <a name="outposts-StartCapacityTask-response-TaskActionOnBlockingInstances"></a>
User-specified option in case an instance is blocking the capacity task from running.
+  `WAIT_FOR_EVACUATION` - Checks every 10 minutes over 48 hours to determine if instances have stopped and capacity is available to complete the task.
+  `FAIL_TASK` - The capacity task fails.
Type: String
Valid Values: `WAIT_FOR_EVACUATION | FAIL_TASK`

## Errors
<a name="API_StartCapacityTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting this resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource causing the conflict.
 ** ResourceType **
The type of the resource causing the conflict.
HTTP Status Code: 409

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
<a name="API_StartCapacityTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/StartCapacityTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/StartCapacityTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/StartCapacityTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/StartCapacityTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/StartCapacityTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/StartCapacityTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/StartCapacityTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/StartCapacityTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/StartCapacityTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/StartCapacityTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
