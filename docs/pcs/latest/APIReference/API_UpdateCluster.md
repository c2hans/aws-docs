---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateCluster.html
---

# UpdateCluster
<a name="API_UpdateCluster"></a>

Updates a cluster configuration. You can update the scheduler version, modify scheduler settings, and update accounting configuration for an existing cluster. For more information about updating the scheduler version, see [Updating the scheduler version on a cluster](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_version_update.html) in the * AWS PCS User Guide*.

**Note**
You can only update clusters that are in `ACTIVE`, `UPDATE_FAILED`, or `SUSPENDED` state. All associated resources (queues and compute node groups) must be in `ACTIVE` state before you can update the cluster.

## Request Syntax
<a name="API_UpdateCluster_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "clusterIdentifier": "{{string}}",
   "scheduler": {
      "version": "{{string}}"
   },
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
   }
}
```

## Request Parameters
<a name="API_UpdateCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateCluster_RequestSyntax) **   <a name="PCS-UpdateCluster-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the AWS CLI and SDK automatically generate 1 for you.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 100.
Required: No

 ** [clusterIdentifier](#API_UpdateCluster_RequestSyntax) **   <a name="PCS-UpdateCluster-request-clusterIdentifier"></a>
The name or ID of the cluster to update.
Type: String
Pattern: `(pcs_[a-zA-Z0-9]+|[A-Za-z][A-Za-z0-9-]{2,40})`
Required: Yes

 ** [scheduler](#API_UpdateCluster_RequestSyntax) **   <a name="PCS-UpdateCluster-request-scheduler"></a>
The scheduler configuration to update for the cluster. Use this to update the scheduler version. For more information, see [Updating the scheduler version on a cluster](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_version_update.html) in the * AWS PCS User Guide*.
Type: [UpdateSchedulerRequest](API_UpdateSchedulerRequest.md) object
Required: No

 ** [slurmConfiguration](#API_UpdateCluster_RequestSyntax) **   <a name="PCS-UpdateCluster-request-slurmConfiguration"></a>
Additional options related to the Slurm scheduler.
Type: [UpdateClusterSlurmConfigurationRequest](API_UpdateClusterSlurmConfigurationRequest.md) object
Required: No

## Response Syntax
<a name="API_UpdateCluster_ResponseSyntax"></a>

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
<a name="API_UpdateCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cluster](#API_UpdateCluster_ResponseSyntax) **   <a name="PCS-UpdateCluster-response-cluster"></a>
The cluster resource and configuration.
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_UpdateCluster_Errors"></a>

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
<a name="API_UpdateCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pcs-2023-02-10/UpdateCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pcs-2023-02-10/UpdateCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/UpdateCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pcs-2023-02-10/UpdateCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/UpdateCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pcs-2023-02-10/UpdateCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pcs-2023-02-10/UpdateCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pcs-2023-02-10/UpdateCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pcs-2023-02-10/UpdateCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/UpdateCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
