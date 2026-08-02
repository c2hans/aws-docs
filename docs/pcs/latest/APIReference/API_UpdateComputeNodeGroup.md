---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateComputeNodeGroup.html
---

# UpdateComputeNodeGroup
<a name="API_UpdateComputeNodeGroup"></a>

Updates a compute node group. You can update many of the fields related to your compute node group including the configurations for networking, compute nodes, and settings specific to your scheduler (such as Slurm).

## Request Syntax
<a name="API_UpdateComputeNodeGroup_RequestSyntax"></a>

```
{
   "amiId": "{{string}}",
   "clientToken": "{{string}}",
   "clusterIdentifier": "{{string}}",
   "computeNodeGroupIdentifier": "{{string}}",
   "customLaunchTemplate": {
      "id": "{{string}}",
      "version": "{{string}}"
   },
   "iamInstanceProfileArn": "{{string}}",
   "nodeLifecycleActions": {
      "scriptCachingPolicy": "{{string}}",
      "stages": {
         "nodeBootstrapped": [
            {
               "arguments": [ "{{string}}" ],
               "executionPolicy": "{{string}}",
               "name": "{{string}}",
               "onError": "{{string}}",
               "scriptSource": {
                  "checksum": "{{string}}",
                  "s3VersionId": "{{string}}",
                  "scriptLocation": "{{string}}"
               }
            }
         ],
         "nodeReady": [
            {
               "arguments": [ "{{string}}" ],
               "executionPolicy": "{{string}}",
               "name": "{{string}}",
               "onError": "{{string}}",
               "scriptSource": {
                  "checksum": "{{string}}",
                  "s3VersionId": "{{string}}",
                  "scriptLocation": "{{string}}"
               }
            }
         ]
      }
   },
   "purchaseOption": "{{string}}",
   "scalingConfiguration": {
      "maxInstanceCount": {{number}},
      "minInstanceCount": {{number}}
   },
   "slurmConfiguration": {
      "scaleDownIdleTimeInSeconds": {{number}},
      "slurmCustomSettings": [
         {
            "parameterName": "{{string}}",
            "parameterValue": "{{string}}"
         }
      ]
   },
   "spotOptions": {
      "allocationStrategy": "{{string}}"
   },
   "subnetIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateComputeNodeGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [amiId](#API_UpdateComputeNodeGroup_RequestSyntax) **   <a name="PCS-UpdateComputeNodeGroup-request-amiId"></a>
The ID of the Amazon Machine Image (AMI) that AWS PCS uses to launch instances. If not provided, AWS PCS uses the AMI ID specified in the custom launch template.
Type: String
Pattern: `ami-[a-z0-9]+`
Required: No

 ** [clientToken](#API_UpdateComputeNodeGroup_RequestSyntax) **   <a name="PCS-UpdateComputeNodeGroup-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the AWS CLI and SDK automatically generate 1 for you.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 100.
Required: No

 ** [clusterIdentifier](#API_UpdateComputeNodeGroup_RequestSyntax) **   <a name="PCS-UpdateComputeNodeGroup-request-clusterIdentifier"></a>
The name or ID of the cluster of the compute node group.
Type: String
Pattern: `(pcs_[a-zA-Z0-9]+|[A-Za-z][A-Za-z0-9-]{2,40})`
Required: Yes

 ** [computeNodeGroupIdentifier](#API_UpdateComputeNodeGroup_RequestSyntax) **   <a name="PCS-UpdateComputeNodeGroup-request-computeNodeGroupIdentifier"></a>
The name or ID of the compute node group.
Type: String
Pattern: `(pcs_[a-zA-Z0-9]+|[A-Za-z][A-Za-z0-9-]{2,25})`
Required: Yes

 ** [customLaunchTemplate](#API_UpdateComputeNodeGroup_RequestSyntax) **   <a name="PCS-UpdateComputeNodeGroup-request-customLaunchTemplate"></a>
An Amazon EC2 launch template AWS PCS uses to launch compute nodes.
Type: [CustomLaunchTemplate](API_CustomLaunchTemplate.md) object
Required: No

 ** [iamInstanceProfileArn](#API_UpdateComputeNodeGroup_RequestSyntax) **   <a name="PCS-UpdateComputeNodeGroup-request-iamInstanceProfileArn"></a>
The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances. The role contained in your instance profile must have the `pcs:RegisterComputeNodeGroupInstance` permission and the role name must start with `AWSPCS` or must have the path `/aws-pcs/`. For more information, see [IAM instance profiles for AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/security-instance-profiles.html) in the * AWS PCS User Guide*.
Type: String
Pattern: `arn:aws([a-zA-Z-]{0,10})?:iam::[0-9]{12}:instance-profile/([!-~]{1,510}/)?([\w+=,.@-]{1,128})`
Required: No

 ** [nodeLifecycleActions](#API_UpdateComputeNodeGroup_RequestSyntax) **   <a name="PCS-UpdateComputeNodeGroup-request-nodeLifecycleActions"></a>
The lifecycle actions to run on compute nodes in the compute node group. Use lifecycle actions to run custom scripts at defined stages of a compute node's lifecycle, such as when a compute node finishes bootstrapping or becomes ready to accept jobs.
Type: [UpdateNodeLifecycleActionsRequest](API_UpdateNodeLifecycleActionsRequest.md) object
Required: No

 ** [purchaseOption](#API_UpdateComputeNodeGroup_RequestSyntax) **   <a name="PCS-UpdateComputeNodeGroup-request-purchaseOption"></a>
Specifies how EC2 instances are purchased on your behalf. AWS PCS supports On-Demand Instances, Spot Instances, Interruptible Capacity Reservations, On-Demand Capacity Reservations, and Amazon EC2 Capacity Blocks for ML. For more information, see [Amazon EC2 billing and purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html) in the *Amazon Elastic Compute Cloud User Guide*. For more information about AWS PCS support for Capacity Blocks, see [Using Amazon EC2 Capacity Blocks for ML with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-blocks.html) in the * AWS PCS User Guide*. For more information about AWS PCS support for interruptible capacity reservations, see [Using I-ODCRs with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-iodcr.html) in the * AWS PCS User Guide*. Choose On-Demand if you plan to use an On-Demand Capacity Reservation (ODCR). For more information, see [Using ODCRs with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-odcr.html). If you don't provide this option, it defaults to On-Demand.
Type: String
Valid Values: `ONDEMAND | SPOT | CAPACITY_BLOCK | INTERRUPTIBLE_CAPACITY_RESERVATION`
Required: No

 ** [scalingConfiguration](#API_UpdateComputeNodeGroup_RequestSyntax) **   <a name="PCS-UpdateComputeNodeGroup-request-scalingConfiguration"></a>
Specifies the boundaries of the compute node group auto scaling.
Type: [ScalingConfigurationRequest](API_ScalingConfigurationRequest.md) object
Required: No

 ** [slurmConfiguration](#API_UpdateComputeNodeGroup_RequestSyntax) **   <a name="PCS-UpdateComputeNodeGroup-request-slurmConfiguration"></a>
Additional options related to the Slurm scheduler.
Type: [UpdateComputeNodeGroupSlurmConfigurationRequest](API_UpdateComputeNodeGroupSlurmConfigurationRequest.md) object
Required: No

 ** [spotOptions](#API_UpdateComputeNodeGroup_RequestSyntax) **   <a name="PCS-UpdateComputeNodeGroup-request-spotOptions"></a>
Additional configuration when you specify `SPOT` as the `purchaseOption` for the `CreateComputeNodeGroup` API action.
Type: [SpotOptions](API_SpotOptions.md) object
Required: No

 ** [subnetIds](#API_UpdateComputeNodeGroup_RequestSyntax) **   <a name="PCS-UpdateComputeNodeGroup-request-subnetIds"></a>
The list of subnet IDs where the compute node group provisions instances. The subnets must be in the same VPC as the cluster.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_UpdateComputeNodeGroup_ResponseSyntax"></a>

```
{
   "computeNodeGroup": {
      "amiId": "string",
      "arn": "string",
      "clusterId": "string",
      "createdAt": "string",
      "customLaunchTemplate": {
         "id": "string",
         "version": "string"
      },
      "errorInfo": [
         {
            "code": "string",
            "message": "string"
         }
      ],
      "iamInstanceProfileArn": "string",
      "id": "string",
      "instanceConfigs": [
         {
            "instanceType": "string"
         }
      ],
      "modifiedAt": "string",
      "name": "string",
      "nodeLifecycleActions": {
         "scriptCachingPolicy": "string",
         "stages": {
            "nodeBootstrapped": [
               {
                  "arguments": [ "string" ],
                  "executionPolicy": "string",
                  "name": "string",
                  "onError": "string",
                  "scriptSource": {
                     "checksum": "string",
                     "s3VersionId": "string",
                     "scriptLocation": "string"
                  }
               }
            ],
            "nodeReady": [
               {
                  "arguments": [ "string" ],
                  "executionPolicy": "string",
                  "name": "string",
                  "onError": "string",
                  "scriptSource": {
                     "checksum": "string",
                     "s3VersionId": "string",
                     "scriptLocation": "string"
                  }
               }
            ]
         }
      },
      "purchaseOption": "string",
      "scalingConfiguration": {
         "maxInstanceCount": number,
         "minInstanceCount": number
      },
      "slurmConfiguration": {
         "scaleDownIdleTimeInSeconds": number,
         "slurmCustomSettings": [
            {
               "parameterName": "string",
               "parameterValue": "string"
            }
         ]
      },
      "spotOptions": {
         "allocationStrategy": "string"
      },
      "status": "string",
      "subnetIds": [ "string" ]
   }
}
```

## Response Elements
<a name="API_UpdateComputeNodeGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [computeNodeGroup](#API_UpdateComputeNodeGroup_ResponseSyntax) **   <a name="PCS-UpdateComputeNodeGroup-response-computeNodeGroup"></a>
A compute node group associated with a cluster.
Type: [ComputeNodeGroup](API_ComputeNodeGroup.md) object

## Errors
<a name="API_UpdateComputeNodeGroup_Errors"></a>

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
<a name="API_UpdateComputeNodeGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pcs-2023-02-10/UpdateComputeNodeGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pcs-2023-02-10/UpdateComputeNodeGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/UpdateComputeNodeGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pcs-2023-02-10/UpdateComputeNodeGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/UpdateComputeNodeGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pcs-2023-02-10/UpdateComputeNodeGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pcs-2023-02-10/UpdateComputeNodeGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pcs-2023-02-10/UpdateComputeNodeGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pcs-2023-02-10/UpdateComputeNodeGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/UpdateComputeNodeGroup)
