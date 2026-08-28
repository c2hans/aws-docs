---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchRebootClusterNodes.html
---

# BatchRebootClusterNodes
<a name="API_BatchRebootClusterNodes"></a>

Reboots specific nodes within a SageMaker HyperPod cluster using a soft recovery mechanism. `BatchRebootClusterNodes` performs a graceful reboot of the specified nodes by calling the Amazon Elastic Compute Cloud `RebootInstances` API, which attempts to cleanly shut down the operating system before restarting the instance.

This operation is useful for recovering from transient issues or applying certain configuration changes that require a restart.

**Note**
Rebooting a node may cause temporary service interruption for workloads running on that node. Ensure your workloads can handle node restarts or use appropriate scheduling to minimize impact.
You can reboot up to 25 nodes in a single request.
For SageMaker HyperPod clusters using the Slurm workload manager, ensure rebooting nodes will not disrupt critical cluster operations.

## Request Syntax
<a name="API_BatchRebootClusterNodes_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "NodeIds": [ "{{string}}" ],
   "NodeLogicalIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchRebootClusterNodes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_BatchRebootClusterNodes_RequestSyntax) **   <a name="sagemaker-BatchRebootClusterNodes-request-ClusterName"></a>
The name or Amazon Resource Name (ARN) of the SageMaker HyperPod cluster containing the nodes to reboot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [NodeIds](#API_BatchRebootClusterNodes_RequestSyntax) **   <a name="sagemaker-BatchRebootClusterNodes-request-NodeIds"></a>
A list of EC2 instance IDs to reboot using soft recovery. You can specify between 1 and 25 instance IDs.
+ Either `NodeIds` or `NodeLogicalIds` must be provided (or both), but at least one is required.
+ Each instance ID must follow the pattern `i-` followed by 17 hexadecimal characters (for example, `i-0123456789abcdef0`).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: No

 ** [NodeLogicalIds](#API_BatchRebootClusterNodes_RequestSyntax) **   <a name="sagemaker-BatchRebootClusterNodes-request-NodeLogicalIds"></a>
A list of logical node IDs to reboot using soft recovery. You can specify between 1 and 25 logical node IDs.
The `NodeLogicalId` is a unique identifier that persists throughout the node's lifecycle and can be used to track nodes that are still being provisioned and don't yet have an EC2 instance ID assigned.
+ This parameter is only supported for clusters using `Continuous` as the `NodeProvisioningMode`. For clusters using the default provisioning mode, use `NodeIds` instead.
+ Either `NodeIds` or `NodeLogicalIds` must be provided (or both), but at least one is required.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]`
Required: No

## Response Syntax
<a name="API_BatchRebootClusterNodes_ResponseSyntax"></a>

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
<a name="API_BatchRebootClusterNodes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_BatchRebootClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchRebootClusterNodes-response-Failed"></a>
A list of errors encountered for EC2 instance IDs that could not be rebooted. Each error includes the instance ID, an error code, and a descriptive message.
Type: Array of [BatchRebootClusterNodesError](API_BatchRebootClusterNodesError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [FailedNodeLogicalIds](#API_BatchRebootClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchRebootClusterNodes-response-FailedNodeLogicalIds"></a>
A list of errors encountered for logical node IDs that could not be rebooted. Each error includes the logical node ID, an error code, and a descriptive message. This field is only present when `NodeLogicalIds` were provided in the request.
Type: Array of [BatchRebootClusterNodeLogicalIdsError](API_BatchRebootClusterNodeLogicalIdsError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [Successful](#API_BatchRebootClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchRebootClusterNodes-response-Successful"></a>
A list of EC2 instance IDs for which the reboot operation was successfully initiated.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3000 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`

 ** [SuccessfulNodeLogicalIds](#API_BatchRebootClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchRebootClusterNodes-response-SuccessfulNodeLogicalIds"></a>
A list of logical node IDs for which the reboot operation was successfully initiated. This field is only present when `NodeLogicalIds` were provided in the request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 99 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]`

## Errors
<a name="API_BatchRebootClusterNodes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_BatchRebootClusterNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/BatchRebootClusterNodes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/BatchRebootClusterNodes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BatchRebootClusterNodes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/BatchRebootClusterNodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BatchRebootClusterNodes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/BatchRebootClusterNodes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/BatchRebootClusterNodes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/BatchRebootClusterNodes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/BatchRebootClusterNodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BatchRebootClusterNodes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
