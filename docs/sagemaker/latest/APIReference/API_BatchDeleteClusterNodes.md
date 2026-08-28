---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchDeleteClusterNodes.html
---

# BatchDeleteClusterNodes
<a name="API_BatchDeleteClusterNodes"></a>

Deletes specific nodes within a SageMaker HyperPod cluster. `BatchDeleteClusterNodes` accepts a cluster name and a list of node IDs.

**Important**
To safeguard your work, back up your data to Amazon S3 or an FSx for Lustre file system before invoking the API on a worker node group. This will help prevent any potential data loss from the instance root volume. For more information about backup, see [Use the backup script provided by SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-operate-cli-command.html#sagemaker-hyperpod-operate-cli-command-update-cluster-software-backup).
If you want to invoke this API on an existing cluster, you'll first need to patch the cluster by running the [UpdateClusterSoftware API](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html). For more information about patching a cluster, see [Update the SageMaker HyperPod platform software of a cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-operate-cli-command.html#sagemaker-hyperpod-operate-cli-command-update-cluster-software).

## Request Syntax
<a name="API_BatchDeleteClusterNodes_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "NodeIds": [ "{{string}}" ],
   "NodeLogicalIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchDeleteClusterNodes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_BatchDeleteClusterNodes_RequestSyntax) **   <a name="sagemaker-BatchDeleteClusterNodes-request-ClusterName"></a>
The name of the SageMaker HyperPod cluster from which to delete the specified nodes.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [NodeIds](#API_BatchDeleteClusterNodes_RequestSyntax) **   <a name="sagemaker-BatchDeleteClusterNodes-request-NodeIds"></a>
A list of node IDs to be deleted from the specified cluster.
+ For SageMaker HyperPod clusters using the Slurm workload manager, you cannot remove instances that are configured as Slurm controller nodes.
+ If you need to delete more than 99 instances, contact [Support](http://aws.amazon.com/contact-us/) for assistance.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3000 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: No

 ** [NodeLogicalIds](#API_BatchDeleteClusterNodes_RequestSyntax) **   <a name="sagemaker-BatchDeleteClusterNodes-request-NodeLogicalIds"></a>
A list of `NodeLogicalIds` identifying the nodes to be deleted. You can specify up to 50 `NodeLogicalIds`. You must specify either `NodeLogicalIds`, `InstanceIds`, or both, with a combined maximum of 50 identifiers.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 99 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]`
Required: No

## Response Syntax
<a name="API_BatchDeleteClusterNodes_ResponseSyntax"></a>

```
{
   "Failed": [
      {
         "Code": "string",
         "Message": "string",
         "NodeId": "string"
      }
   ],
   "FailedNodeLogicalIds": [
      {
         "Code": "string",
         "Message": "string",
         "NodeLogicalId": "string"
      }
   ],
   "Successful": [ "string" ],
   "SuccessfulNodeLogicalIds": [ "string" ]
}
```

## Response Elements
<a name="API_BatchDeleteClusterNodes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_BatchDeleteClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchDeleteClusterNodes-response-Failed"></a>
A list of errors encountered when deleting the specified nodes.
Type: Array of [BatchDeleteClusterNodesError](API_BatchDeleteClusterNodesError.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3000 items.

 ** [FailedNodeLogicalIds](#API_BatchDeleteClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchDeleteClusterNodes-response-FailedNodeLogicalIds"></a>
A list of `NodeLogicalIds` that could not be deleted, along with error information explaining why the deletion failed.
Type: Array of [BatchDeleteClusterNodeLogicalIdsError](API_BatchDeleteClusterNodeLogicalIdsError.md) objects
Array Members: Minimum number of 1 item. Maximum number of 99 items.

 ** [Successful](#API_BatchDeleteClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchDeleteClusterNodes-response-Successful"></a>
A list of node IDs that were successfully deleted from the specified cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3000 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`

 ** [SuccessfulNodeLogicalIds](#API_BatchDeleteClusterNodes_ResponseSyntax) **   <a name="sagemaker-BatchDeleteClusterNodes-response-SuccessfulNodeLogicalIds"></a>
A list of `NodeLogicalIds` that were successfully deleted from the cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 99 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]`

## Errors
<a name="API_BatchDeleteClusterNodes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_BatchDeleteClusterNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/BatchDeleteClusterNodes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/BatchDeleteClusterNodes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BatchDeleteClusterNodes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/BatchDeleteClusterNodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BatchDeleteClusterNodes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/BatchDeleteClusterNodes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/BatchDeleteClusterNodes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/BatchDeleteClusterNodes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/BatchDeleteClusterNodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BatchDeleteClusterNodes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
