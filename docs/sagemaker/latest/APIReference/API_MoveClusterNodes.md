---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MoveClusterNodes.html
---

# MoveClusterNodes

Moves running nodes from one instance group to another instance group. The target instance group can be in the same HyperPod cluster or in a different HyperPod cluster in the same account and Region. The underlying instances aren't terminated.

Each node keeps its instance ID, its `NodeLogicalId`, its network interfaces and IP addresses, and its capacity. The node then joins the target instance group with the target's configuration and lifecycle scripts.

**Important**
The move replaces the node's root Amazon Elastic Block Store (Amazon EBS) volume and secondary EBS volume, which deletes any data stored on them. Back up any data that you need before you move the node.

Specify the nodes to move with exactly one of `NodeIds`, `NodeLogicalIds`, or `InstanceCount`. The operation is asynchronous and returns after it accepts the nodes for the move. While a node moves, its status is `DetachInProgress` and then `AttachInProgress`. The node appears in the source cluster while it detaches. After HyperPod hands the node off to the target instance group, the node appears in the target cluster. To track the node, call `DescribeClusterNode` or `ListClusterNodes` on the source or target cluster.

**Note**
Both clusters must be `InService`, use Amazon EKS orchestration, and use `Continuous` as the `NodeProvisioningMode`.
The source and target instance groups must also use compatible configurations.

## Request Syntax
<a name="API_MoveClusterNodes_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "InstanceCount": {{number}},
   "NodeIds": [ "{{string}}" ],
   "NodeLogicalIds": [ "{{string}}" ],
   "SourceClusterArn": "{{string}}",
   "SourceInstanceGroupName": "{{string}}",
   "TargetClusterArn": "{{string}}",
   "TargetInstanceGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_MoveClusterNodes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_MoveClusterNodes_RequestSyntax) **   <a name="sagemaker-MoveClusterNodes-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry the request with the same client token and the same parameters within 8 hours, the service returns the original response. It doesn't start a new move. If you reuse a client token with different parameters, the request fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [InstanceCount](#API_MoveClusterNodes_RequestSyntax) **   <a name="sagemaker-MoveClusterNodes-request-InstanceCount"></a>
The number of nodes to move, from 1 to 50. HyperPod selects the nodes from the source instance group. If fewer than this number of nodes are eligible to move, the request fails and no nodes are moved. Specify exactly one of `NodeIds`, `NodeLogicalIds`, or `InstanceCount`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NodeIds](#API_MoveClusterNodes_RequestSyntax) **   <a name="sagemaker-MoveClusterNodes-request-NodeIds"></a>
A list of instance IDs of the nodes to move. You can specify up to 50 instance IDs. Each node is evaluated separately, so some nodes can be moved while others fail. The request fails if moving the eligible nodes would reduce the source instance group below its minimum instance count. Specify exactly one of `NodeIds`, `NodeLogicalIds`, or `InstanceCount`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: No

 ** [NodeLogicalIds](#API_MoveClusterNodes_RequestSyntax) **   <a name="sagemaker-MoveClusterNodes-request-NodeLogicalIds"></a>
A list of `NodeLogicalIds` of the nodes to move. You can specify up to 50 `NodeLogicalIds`. Each node is evaluated separately, so some nodes can be moved while others fail. The request fails if moving the eligible nodes would reduce the source instance group below its minimum instance count. Specify exactly one of `NodeIds`, `NodeLogicalIds`, or `InstanceCount`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]`
Required: No

 ** [SourceClusterArn](#API_MoveClusterNodes_RequestSyntax) **   <a name="sagemaker-MoveClusterNodes-request-SourceClusterArn"></a>
The Amazon Resource Name (ARN) of the HyperPod cluster that the nodes are moved from.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: Yes

 ** [SourceInstanceGroupName](#API_MoveClusterNodes_RequestSyntax) **   <a name="sagemaker-MoveClusterNodes-request-SourceInstanceGroupName"></a>
The name of the instance group in the source cluster that the nodes are moved from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** [TargetClusterArn](#API_MoveClusterNodes_RequestSyntax) **   <a name="sagemaker-MoveClusterNodes-request-TargetClusterArn"></a>
The Amazon Resource Name (ARN) of the HyperPod cluster that the nodes are moved to. The target cluster must be in the same account and Region as the source cluster, and can be the same cluster as the source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: Yes

 ** [TargetInstanceGroupName](#API_MoveClusterNodes_RequestSyntax) **   <a name="sagemaker-MoveClusterNodes-request-TargetInstanceGroupName"></a>
The name of the instance group in the target cluster that the nodes are moved to. If the target cluster is the same as the source cluster, the target instance group must be different from the source instance group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

## Response Syntax
<a name="API_MoveClusterNodes_ResponseSyntax"></a>

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
<a name="API_MoveClusterNodes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_MoveClusterNodes_ResponseSyntax) **   <a name="sagemaker-MoveClusterNodes-response-Failed"></a>
The instance IDs that could not be moved, each with an error code and message. The response includes this list when you specify `NodeIds`. If none of the specified nodes can be moved, the request fails and no nodes are moved.
Type: Array of [MoveClusterNodesError](API_MoveClusterNodesError.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

 ** [FailedNodeLogicalIds](#API_MoveClusterNodes_ResponseSyntax) **   <a name="sagemaker-MoveClusterNodes-response-FailedNodeLogicalIds"></a>
The `NodeLogicalIds` that could not be moved, each with an error code and message. The response includes this list when you specify `NodeLogicalIds`. If none of the specified nodes can be moved, the request fails and no nodes are moved.
Type: Array of [MoveClusterNodeLogicalIdsError](API_MoveClusterNodeLogicalIdsError.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

 ** [Successful](#API_MoveClusterNodes_ResponseSyntax) **   <a name="sagemaker-MoveClusterNodes-response-Successful"></a>
This list contains the instance IDs of the nodes that were accepted for the move. The response includes this list when you specify `NodeIds` or `InstanceCount`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`

 ** [SuccessfulNodeLogicalIds](#API_MoveClusterNodes_ResponseSyntax) **   <a name="sagemaker-MoveClusterNodes-response-SuccessfulNodeLogicalIds"></a>
The `NodeLogicalIds` of the nodes that were accepted for the move. The response includes this list when you specify `NodeLogicalIds`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]`

## Errors
<a name="API_MoveClusterNodes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_MoveClusterNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/MoveClusterNodes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/MoveClusterNodes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MoveClusterNodes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/MoveClusterNodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MoveClusterNodes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/MoveClusterNodes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/MoveClusterNodes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/MoveClusterNodes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/MoveClusterNodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MoveClusterNodes)
