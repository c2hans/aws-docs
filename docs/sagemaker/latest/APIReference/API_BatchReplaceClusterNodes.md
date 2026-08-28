---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchReplaceClusterNodes.html
---

# BatchReplaceClusterNodes
<a name="API_BatchReplaceClusterNodes"></a>

Replaces specific nodes within a SageMaker HyperPod cluster with new hardware. `BatchReplaceClusterNodes` terminates the specified instances and provisions new replacement instances with the same configuration but fresh hardware. The Amazon Machine Image (AMI) and instance configuration remain the same.

This operation is useful for recovering from hardware failures or persistent issues that cannot be resolved through a reboot.

**Important**
 **Data Loss Warning:** Replacing nodes destroys all instance volumes, including both root and secondary volumes. All data stored on these volumes will be permanently lost and cannot be recovered.
To safeguard your work, back up your data to Amazon S3 or an FSx for Lustre file system before invoking the API on a worker node group. This will help prevent any potential data loss from the instance root volume. For more information about backup, see [Use the backup script provided by SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-operate-cli-command.html#sagemaker-hyperpod-operate-cli-command-update-cluster-software-backup).
If you want to invoke this API on an existing cluster, you'll first need to patch the cluster by running the [UpdateClusterSoftware API](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html). For more information about patching a cluster, see [Update the SageMaker HyperPod platform software of a cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-operate-cli-command.html#sagemaker-hyperpod-operate-cli-command-update-cluster-software).
You can replace up to 25 nodes in a single request.

## Request Syntax
<a name="API_BatchReplaceClusterNodes_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "NodeIds": [ "{{string}}" ],
   "NodeLogicalIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchReplaceClusterNodes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_BatchReplaceClusterNodes_RequestSyntax) **   <a name="sagemaker-BatchReplaceClusterNodes-request-ClusterName"></a>
The name or Amazon Resource Name (ARN) of the SageMaker HyperPod cluster containing the nodes to replace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [NodeIds](#API_BatchReplaceClusterNodes_RequestSyntax) **   <a name="sagemaker-BatchReplaceClusterNodes-request-NodeIds"></a>
A list of EC2 instance IDs to replace with new hardware. You can specify between 1 and 25 instance IDs.
Replace operations destroy all instance volumes (root and secondary). Ensure you have backed up any important data before proceeding.
+ Either `NodeIds` or `NodeLogicalIds` must be provided (or both), but at least one is required.
+ Each instance ID must follow the pattern `i-` followed by 17 hexadecimal characters (for example, `i-0123456789abcdef0`).
+ For SageMaker HyperPod clusters using the Slurm workload manager, you cannot replace instances that are configured as Slurm controller nodes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: No

 ** [NodeLogicalIds](#API_BatchReplaceClusterNodes_RequestSyntax) **   <a name="sagemaker-BatchReplaceClusterNodes-request-NodeLogicalIds"></a>
A list of logical node IDs to replace with new hardware. You can specify between 1 and 25 logical node IDs.
The `NodeLogicalId` is a unique identifier that persists throughout the node's lifecycle and can be used to track nodes that are still being provisioned and don't yet have an EC2 instance ID assigned.
+ Replace operations destroy all instance volumes (root and secondary). Ensure you have backed up any important data before proceeding.
+ This parameter is only supported for clusters using `Continuous` as the `NodeProvisioningMode`. For clusters using the default provisioning mode, use `NodeIds` instead.
+ Either `NodeIds` or `NodeLogicalIds` must be provided (or both), but at least one is required.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]`
Required: No

## Response Syntax
<a name="API_BatchReplaceClusterNodes_ResponseSyntax"></a>

```
{
   "Failed": [
      {
         "ErrorCode": "string",
         "Message": "string",
         "NodeId": "string"
      }
   ],
   "FailedNodeLogicalIds": [
      {
         "ErrorCode": "string",
         "Message": "string",
         "NodeLogicalId": "string"
      }
   ],
   "Successful": [ "string" ],
   "SuccessfulNodeLogicalIds": [ "string" ]
}
```

## Response Elements
<a name="API_BatchReplaceClusterNodes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_BatchReplaceClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchReplaceClusterNodes-response-Failed"></a>
A list of errors encountered for EC2 instance IDs that could not be replaced. Each error includes the instance ID, an error code, and a descriptive message.
Type: Array of [BatchReplaceClusterNodesError](API_BatchReplaceClusterNodesError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [FailedNodeLogicalIds](#API_BatchReplaceClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchReplaceClusterNodes-response-FailedNodeLogicalIds"></a>
A list of errors encountered for logical node IDs that could not be replaced. Each error includes the logical node ID, an error code, and a descriptive message. This field is only present when `NodeLogicalIds` were provided in the request.
Type: Array of [BatchReplaceClusterNodeLogicalIdsError](API_BatchReplaceClusterNodeLogicalIdsError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [Successful](#API_BatchReplaceClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchReplaceClusterNodes-response-Successful"></a>
A list of EC2 instance IDs for which the replacement operation was successfully initiated.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3000 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`

 ** [SuccessfulNodeLogicalIds](#API_BatchReplaceClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchReplaceClusterNodes-response-SuccessfulNodeLogicalIds"></a>
A list of logical node IDs for which the replacement operation was successfully initiated. This field is only present when `NodeLogicalIds` were provided in the request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 99 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]`

## Errors
<a name="API_BatchReplaceClusterNodes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_BatchReplaceClusterNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/BatchReplaceClusterNodes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/BatchReplaceClusterNodes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BatchReplaceClusterNodes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/BatchReplaceClusterNodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BatchReplaceClusterNodes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/BatchReplaceClusterNodes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/BatchReplaceClusterNodes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/BatchReplaceClusterNodes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/BatchReplaceClusterNodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BatchReplaceClusterNodes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
