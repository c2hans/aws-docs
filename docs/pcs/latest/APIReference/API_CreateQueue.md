---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateQueue.html
---

# CreateQueue
<a name="API_CreateQueue"></a>

Creates a job queue. You must associate 1 or more compute node groups with the queue. You can associate 1 compute node group with multiple queues.

## Request Syntax
<a name="API_CreateQueue_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "clusterIdentifier": "{{string}}",
   "computeNodeGroupConfigurations": [
      {
         "computeNodeGroupId": "{{string}}"
      }
   ],
   "queueName": "{{string}}",
   "slurmConfiguration": {
      "slurmCustomSettings": [
         {
            "parameterName": "{{string}}",
            "parameterValue": "{{string}}"
         }
      ]
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateQueue_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateQueue_RequestSyntax) **   <a name="PCS-CreateQueue-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the AWS CLI and SDK automatically generate 1 for you.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 100.
Required: No

 ** [clusterIdentifier](#API_CreateQueue_RequestSyntax) **   <a name="PCS-CreateQueue-request-clusterIdentifier"></a>
The name or ID of the cluster for which to create a queue.
Type: String
Pattern: `(pcs_[a-zA-Z0-9]+|[A-Za-z][A-Za-z0-9-]{2,40})`
Required: Yes

 ** [computeNodeGroupConfigurations](#API_CreateQueue_RequestSyntax) **   <a name="PCS-CreateQueue-request-computeNodeGroupConfigurations"></a>
The list of compute node group configurations to associate with the queue. Queues assign jobs to associated compute node groups.
Type: Array of [ComputeNodeGroupConfiguration](API_ComputeNodeGroupConfiguration.md) objects
Required: No

 ** [queueName](#API_CreateQueue_RequestSyntax) **   <a name="PCS-CreateQueue-request-queueName"></a>
A name to identify the queue.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 25.
Pattern: `(?!pcs_)^[A-Za-z][A-Za-z0-9-]+`
Required: Yes

 ** [slurmConfiguration](#API_CreateQueue_RequestSyntax) **   <a name="PCS-CreateQueue-request-slurmConfiguration"></a>
Additional options related to the Slurm scheduler.
Type: [QueueSlurmConfigurationRequest](API_QueueSlurmConfigurationRequest.md) object
Required: No

 ** [tags](#API_CreateQueue_RequestSyntax) **   <a name="PCS-CreateQueue-request-tags"></a>
1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateQueue_ResponseSyntax"></a>

```
{
   "queue": {
      "arn": "string",
      "clusterId": "string",
      "computeNodeGroupConfigurations": [
         {
            "computeNodeGroupId": "string"
         }
      ],
      "createdAt": "string",
      "errorInfo": [
         {
            "code": "string",
            "message": "string"
         }
      ],
      "id": "string",
      "modifiedAt": "string",
      "name": "string",
      "slurmConfiguration": {
         "slurmCustomSettings": [
            {
               "parameterName": "string",
               "parameterValue": "string"
            }
         ]
      },
      "status": "string"
   }
}
```

## Response Elements
<a name="API_CreateQueue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [queue](#API_CreateQueue_ResponseSyntax) **   <a name="PCS-CreateQueue-response-queue"></a>
A queue resource.
Type: [Queue](API_Queue.md) object

## Errors
<a name="API_CreateQueue_Errors"></a>

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

 ** ServiceQuotaExceededException **
You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. To learn how to increase your service quota, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*
 *Examples*
+ The max number of clusters or queues has been reached for the account.
+ The max number of compute node groups has been reached for the associated cluster.
+ The total of `maxInstances` across all compute node groups has been reached for associated cluster.
 ** quotaCode **
 The **quota code** of the service quota that was exceeded.
 ** resourceId **
 The unique identifier of the resource that caused the quota to be exceeded.
 ** resourceType **
 The type or category of the resource that caused the quota to be exceeded.
 ** serviceCode **
 The service code associated with the quota that was exceeded.
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
<a name="API_CreateQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pcs-2023-02-10/CreateQueue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pcs-2023-02-10/CreateQueue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/CreateQueue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pcs-2023-02-10/CreateQueue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/CreateQueue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pcs-2023-02-10/CreateQueue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pcs-2023-02-10/CreateQueue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pcs-2023-02-10/CreateQueue)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pcs-2023-02-10/CreateQueue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/CreateQueue)
