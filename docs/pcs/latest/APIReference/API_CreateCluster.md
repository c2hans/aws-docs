---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateCluster.html
---

# CreateCluster
<a name="API_CreateCluster"></a>

Creates a cluster in your account. AWS PCS creates the cluster controller in a service-owned account. The cluster controller communicates with the cluster resources in your account. The subnets and security groups for the cluster must already exist before you use this API action.

**Note**
It takes time for AWS PCS to create the cluster. The cluster is in a `Creating` state until it is ready to use. There can only be 1 cluster in a `Creating` state per AWS Region per AWS account. `CreateCluster` fails with a `ServiceQuotaExceededException` if there is already a cluster in a `Creating` state.

## Request Syntax
<a name="API_CreateCluster_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "clusterName": "{{string}}",
   "networking": {
      "networkType": "{{string}}",
      "securityGroupIds": [ "{{string}}" ],
      "subnetIds": [ "{{string}}" ]
   },
   "scheduler": {
      "type": "{{string}}",
      "version": "{{string}}"
   },
   "size": "{{string}}",
   "slurmConfiguration": {
      "accounting": {
         "defaultPurgeTimeInDays": {{number}},
         "mode": "{{string}}"
      },
      "cgroupCustomSettings": [
         {
            "parameterName": "{{string}}",
            "parameterValue": "{{string}}"
         }
      ],
      "scaleDownIdleTimeInSeconds": {{number}},
      "slurmCustomSettings": [
         {
            "parameterName": "{{string}}",
            "parameterValue": "{{string}}"
         }
      ],
      "slurmdbdCustomSettings": [
         {
            "parameterName": "{{string}}",
            "parameterValue": "{{string}}"
         }
      ],
      "slurmRest": {
         "mode": "{{string}}"
      }
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateCluster_RequestSyntax) **   <a name="PCS-CreateCluster-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the AWS CLI and SDK automatically generate 1 for you.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 100.
Required: No

 ** [clusterName](#API_CreateCluster_RequestSyntax) **   <a name="PCS-CreateCluster-request-clusterName"></a>
A name to identify the cluster. Example: `MyCluster`
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!pcs_)^[A-Za-z][A-Za-z0-9-]+`
Required: Yes

 ** [networking](#API_CreateCluster_RequestSyntax) **   <a name="PCS-CreateCluster-request-networking"></a>
The networking configuration used to set up the cluster's control plane.
Type: [NetworkingRequest](API_NetworkingRequest.md) object
Required: Yes

 ** [scheduler](#API_CreateCluster_RequestSyntax) **   <a name="PCS-CreateCluster-request-scheduler"></a>
The cluster management and job scheduling software associated with the cluster.
Type: [SchedulerRequest](API_SchedulerRequest.md) object
Required: Yes

 ** [size](#API_CreateCluster_RequestSyntax) **   <a name="PCS-CreateCluster-request-size"></a>
A value that determines the maximum number of compute nodes in the cluster and the maximum number of jobs (active and queued).
+  `SMALL`: 32 compute nodes and 256 jobs
+  `MEDIUM`: 512 compute nodes and 8192 jobs
+  `LARGE`: 2048 compute nodes and 16,384 jobs
Type: String
Valid Values: `SMALL | MEDIUM | LARGE`
Required: Yes

 ** [slurmConfiguration](#API_CreateCluster_RequestSyntax) **   <a name="PCS-CreateCluster-request-slurmConfiguration"></a>
Additional options related to the Slurm scheduler.
Type: [ClusterSlurmConfigurationRequest](API_ClusterSlurmConfigurationRequest.md) object
Required: No

 ** [tags](#API_CreateCluster_RequestSyntax) **   <a name="PCS-CreateCluster-request-tags"></a>
1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateCluster_ResponseSyntax"></a>

```
{
   "cluster": {
      "arn": "string",
      "createdAt": "string",
      "endpoints": [
         {
            "ipv6Address": "string",
            "port": "string",
            "privateIpAddress": "string",
            "publicIpAddress": "string",
            "type": "string"
         }
      ],
      "errorInfo": [
         {
            "code": "string",
            "message": "string"
         }
      ],
      "id": "string",
      "modifiedAt": "string",
      "name": "string",
      "networking": {
         "networkType": "string",
         "securityGroupIds": [ "string" ],
         "subnetIds": [ "string" ]
      },
      "scheduler": {
         "type": "string",
         "version": "string"
      },
      "size": "string",
      "slurmConfiguration": {
         "accounting": {
            "defaultPurgeTimeInDays": number,
            "mode": "string"
         },
         "authKey": {
            "secretArn": "string",
            "secretVersion": "string"
         },
         "cgroupCustomSettings": [
            {
               "parameterName": "string",
               "parameterValue": "string"
            }
         ],
         "jwtAuth": {
            "jwtKey": {
               "secretArn": "string",
               "secretVersion": "string"
            }
         },
         "scaleDownIdleTimeInSeconds": number,
         "slurmCustomSettings": [
            {
               "parameterName": "string",
               "parameterValue": "string"
            }
         ],
         "slurmdbdCustomSettings": [
            {
               "parameterName": "string",
               "parameterValue": "string"
            }
         ],
         "slurmRest": {
            "mode": "string"
         }
      },
      "status": "string"
   }
}
```

## Response Elements
<a name="API_CreateCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cluster](#API_CreateCluster_ResponseSyntax) **   <a name="PCS-CreateCluster-response-cluster"></a>
The cluster resource.
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_CreateCluster_Errors"></a>

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
<a name="API_CreateCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pcs-2023-02-10/CreateCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pcs-2023-02-10/CreateCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/CreateCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pcs-2023-02-10/CreateCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/CreateCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pcs-2023-02-10/CreateCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pcs-2023-02-10/CreateCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pcs-2023-02-10/CreateCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pcs-2023-02-10/CreateCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/CreateCluster)
