---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/smcluster-eks-move-nodes.html
---

# Move nodes between instance groups and clusters

Use the [MoveClusterNodes](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MoveClusterNodes.html) API to move running nodes from one instance group to another, within a cluster or between clusters, in a single call. Because the move reuses your running instances instead of releasing them and launching new ones, the capacity is ready for its new workload in much less time. Your instances spend less time idle when you shift capacity from one workload to another.

Move nodes to put capacity where you need it as demand changes, for example shifting GPUs from training to inference during the day and back overnight. You keep the capacity you already have, including its Flexible Training Plan, SageMaker HyperPod managed reservation, On-Demand, or Spot capacity.

Both the source and target clusters must be in the same AWS account and Region. A cross-Region move is rejected: both cluster ARNs must be in the Region that serves the call.

There is no additional charge to move nodes, and the instance stays billed on the target cluster after the movement.

Node movement is available for Amazon EKS orchestrated SageMaker HyperPod clusters with continuous provisioning. For more information about continuous provisioning, see [Continuous provisioning for enhanced cluster operations on Amazon EKS](sagemaker-hyperpod-scaling-eks.md).

## Pre-requisites
<a name="smcluster-eks-move-nodes-requirements"></a>

A move must meet all of the following conditions. Conditions that depend on a single node, such as its instance type or subnet in a flexible instance group, are checked per node. For more information, see [Troubleshooting](#smcluster-eks-move-nodes-troubleshooting).

Basic requirements apply to every move.

| Requirement | Details |
| --- | --- |
| Same account and Region | Both clusters are in the same AWS account and Region, because both cluster ARNs must be in the Region that serves the call. A cross-Region move is rejected. |
| Cluster and instance group state | Both clusters are `InService`, are Amazon EKS orchestrated with continuous provisioning, and their Amazon EKS clusters still exist. Slurm clusters are not supported, and restricted instance groups are not supported. |
| Subnets | The source and target instance groups must be in the same subnet. |
| Instance type | The target instance group must support the node's instance type. For a standard instance group, that means the same instance type. For a flexible instance group, the type must be one of the target group's allowed types. |
| Same capacity | Both instance groups use the same capacity: the same Flexible Training Plan, the same SageMaker HyperPod managed reservation, both On-Demand, or both Spot. Two different reservations do not match, even when both are On-Demand Capacity Reservations. |
| Same root volume size | Both instance groups use the same root volume size, which is 100 GB when it is not set. |
| Source minimum instance count | The move cannot take the source instance group below its minimum instance count. Otherwise the request is rejected. To move more nodes, lower the minimum instance count first. |
| No conflicting operation in progress | Neither cluster nor instance group is being deleted or in maintenance mode, and neither instance group has an update, patch, AMI change, or software update in progress. |
| Target software supports node movement | The target instance group runs platform and AMI software that supports node movement. The source instance group does not need to be updated. |

Advanced-feature requirements apply only if the source or target instance group uses that feature. Each row names the feature first.

| Feature | Requirement |
| --- | --- |
| Flexible instance groups | Flexible instance groups: the target instance group allows each node's instance type and its subnet. |
| Multi-Instance GPU (MIG) | MIG: both instance groups use the same `nvidia.com/mig.config` label. |
| EFA | EFA: both instance groups use the same interface type, `efa` or `efa-only`. |
| ThreadsPerCore | `ThreadsPerCore`: both instance groups use the same `ThreadsPerCore` value. |
| Customer managed AWS KMS keys | Encryption: moving nodes to or from an instance group that uses a customer managed AWS KMS key is not supported. The move is rejected if either instance group sets `VolumeKmsKeyId` in any `EbsVolumeConfig` of its `InstanceStorageConfigs`, including the root volume, even when both groups use the same key. |

Security groups and Kubernetes versions can differ between the source and target instance groups.

## Permissions
<a name="smcluster-eks-move-nodes-permissions"></a>

The calling IAM identity needs `sagemaker:MoveClusterNodesFrom` on the source cluster and `sagemaker:MoveClusterNodesTo` on the target cluster. Each side also needs the existing scaling permission: `sagemaker:BatchDeleteClusterNodes` on the source and `sagemaker:BatchAddClusterNodes` on the target. An existing `Deny` on scaling therefore also blocks a move.

The move verifies that the Amazon EKS clusters behind both the source and target SageMaker HyperPod clusters still exist, using the caller's credentials. The calling identity therefore also needs `eks:DescribeCluster` on the Amazon EKS cluster of each SageMaker HyperPod cluster.

Replace `REGION`, `ACCOUNT_ID`, `SOURCE_CLUSTER_ID`, `TARGET_CLUSTER_ID`, `SOURCE_EKS_CLUSTER_ARN`, and `TARGET_EKS_CLUSTER_ARN` with your values. This example uses specific cluster ARNs, but you can scope the `Resource` more broadly, for example `*` with a condition, as shown in the tag example that follows. For more information about IAM for SageMaker HyperPod, see [AWS Identity and Access Management for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md). The following policy grants the calling identity the required permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "MoveNodesFromSource",
      "Effect": "Allow",
      "Action": [
        "sagemaker:MoveClusterNodesFrom",
        "sagemaker:BatchDeleteClusterNodes"
      ],
      "Resource": "arn:aws:sagemaker:{{REGION}}:{{ACCOUNT_ID}}:cluster/{{SOURCE_CLUSTER_ID}}"
    },
    {
      "Sid": "MoveNodesToTarget",
      "Effect": "Allow",
      "Action": [
        "sagemaker:MoveClusterNodesTo",
        "sagemaker:BatchAddClusterNodes"
      ],
      "Resource": "arn:aws:sagemaker:{{REGION}}:{{ACCOUNT_ID}}:cluster/{{TARGET_CLUSTER_ID}}"
    },
    {
      "Sid": "VerifyEksClusters",
      "Effect": "Allow",
      "Action": "eks:DescribeCluster",
      "Resource": [
        "{{SOURCE_EKS_CLUSTER_ARN}}",
        "{{TARGET_EKS_CLUSTER_ARN}}"
      ]
    }
  ]
}
```

`SOURCE_CLUSTER_ID` and `TARGET_CLUSTER_ID` are the IDs at the end of each cluster's ARN. To find the `SOURCE_EKS_CLUSTER_ARN` and `TARGET_EKS_CLUSTER_ARN` for your SageMaker HyperPod clusters, run the following command for each:

```
aws sagemaker describe-cluster --cluster-name {{name}} --query Orchestrator.Eks.ClusterArn
```

For a move within one cluster, both pairs of values are the same.

You can scope `sagemaker:MoveClusterNodesFrom` and `sagemaker:MoveClusterNodesTo` with condition keys. For example, use `aws:ResourceTag/{{key}}` on the source and target cluster ARNs so that only tagged clusters can give or receive nodes. Global condition keys such as `aws:SourceIp`, `aws:SourceVpce`, `aws:PrincipalOrgID`, and `aws:MultiFactorAuthPresent` also work. To scope the source and target independently, use two separate statements in place of the `MoveClusterNodesFrom` and `MoveClusterNodesTo` actions in the policy above. The first statement allows `sagemaker:MoveClusterNodesFrom` on tagged source clusters, and the second allows `sagemaker:MoveClusterNodesTo` on tagged target clusters, each with its own `aws:ResourceTag` condition. Allow statements add up, so a condition on one statement does not limit another statement that allows the same action.

```json
[
  {
    "Sid": "ScopeMoveFromTaggedSourceClusters",
    "Effect": "Allow",
    "Action": "sagemaker:MoveClusterNodesFrom",
    "Resource": "*",
    "Condition": {
      "StringEquals": {
        "aws:ResourceTag/move-source": "allowed"
      }
    }
  },
  {
    "Sid": "ScopeMoveToTaggedTargetClusters",
    "Effect": "Allow",
    "Action": "sagemaker:MoveClusterNodesTo",
    "Resource": "*",
    "Condition": {
      "StringEquals": {
        "aws:ResourceTag/move-target": "allowed"
      }
    }
  }
]
```

Separately from the calling identity, the target instance group's execution role needs `ec2:ModifyNetworkInterfaceAttribute`. During the attach, SageMaker HyperPod updates the security groups on the moved node's network interfaces as that execution role. This permission is not in the `AmazonSageMakerClusterInstanceRolePolicy` managed policy. Execution roles set up as described in [IAM role for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod) (the Amazon EKS tab) already have it.

## Prepare the target instance group
<a name="smcluster-eks-move-nodes-prepare"></a>

Before your first move, prepare the target instance group:

1. Update the target instance group to the latest AMI with `UpdateClusterSoftware`.

1. Create or update the target instance group so that it meets every requirement in [Pre-requisites](#smcluster-eks-move-nodes-requirements), including instance type, capacity, subnet, and root volume size, and, if you use them, EFA interface type, `ThreadsPerCore`, and MIG configuration.

1. If the target instance group has custom taints but no nodes yet, make sure the NVIDIA and EFA device plugin DaemonSets in the target cluster tolerate those taints. Otherwise the moved node reports zero GPUs to Kubernetes.

## Move nodes
<a name="smcluster-eks-move-nodes-move"></a>

Call `MoveClusterNodes` with the source and target cluster ARNs and instance group names. For a move within one cluster, use the same cluster ARN for both with different instance group names.

Choose which nodes to move with one of the following three parameters. The parameters are mutually exclusive.

| Parameter | Behavior |
| --- | --- |
| --instance-count | SageMaker HyperPod picks eligible `Running` nodes. If too few are eligible, SageMaker HyperPod rejects the whole request and nothing moves. |
| --node-ids | The Amazon EC2 instance IDs you list. Eligible nodes move, and each ineligible node is returned in `Failed` with a reason. |
| --node-logical-ids | The node logical IDs you list. Eligible nodes move, and results come back in `SuccessfulNodeLogicalIds` and `FailedNodeLogicalIds`. |

Each request moves 1 to 50 nodes. A node can be in only one move at a time, and several requests can share a source or target instance group.

**Note**
To retry safely after a network error, pass your own `--client-token` and repeat the request with the same value. SageMaker HyperPod returns the original response for at least eight hours and moves nothing new. If you omit `--client-token`, the AWS CLI generates one that you cannot reuse.

The response lists the accepted nodes in `Successful` (instance IDs) when you use `--node-ids` or `--instance-count`, or in `SuccessfulNodeLogicalIds` when you use `--node-logical-ids`.

```json
{"Successful": ["i-0a1b2c3d4e5f67890", "i-0b2c3d4e5f6789012"]}
```

Acceptance is not completion. After the call, each node moves in the background on its own, so nodes in the same request can finish at different times.

The following AWS CLI example moves two nodes that SageMaker HyperPod selects.

```
aws sagemaker move-cluster-nodes \
    --source-cluster-arn {{source-cluster-arn}} --source-instance-group-name {{source-ig}} \
    --target-cluster-arn {{target-cluster-arn}} --target-instance-group-name {{target-ig}} \
    --instance-count 2 \
    --client-token {{unique-token}}
```

## Monitor a move
<a name="smcluster-eks-move-nodes-monitor"></a>

Each node goes through these statuses: `DetachInProgress` on the source cluster, `AttachInProgress` on the target cluster, and `Running` on the target cluster.

Use the instance ID from the `Successful` field. Call `describe-cluster-node` against the source cluster while the node shows `DetachInProgress`, then against the target cluster once it shows `AttachInProgress`, until it shows `Running`.

If you moved nodes by logical ID, call `describe-cluster-node` with `--node-logical-id` instead of `--node-id`.

```
aws sagemaker describe-cluster-node --cluster-name {{cluster}} --node-id i-0a1b2c3d4e5f67890 --query 'NodeDetails.InstanceStatus'
```

To see all arriving nodes, list the nodes in the target instance group.

```
aws sagemaker list-cluster-nodes --cluster-name {{cluster}} --instance-group-name-contains {{target-ig}}
```

The `InstanceStatus.Message` field explains anything you need to act on.

To follow a move without polling, use cluster events. The source cluster records the detach events and the target cluster records the attach events. For how to view and subscribe to events, see [SageMaker HyperPod EKS cluster events](sagemaker-hyperpod-cluster-events-eks-page.md). For the event fields and types, see [SageMaker HyperPod cluster events reference](sagemaker-hyperpod-cluster-events-reference.md). Each `MoveClusterNodes` call is also recorded in AWS CloudTrail.

## What happens to a moved node
<a name="smcluster-eks-move-nodes-result"></a>

Make sure your workloads checkpoint or tolerate interruption before you move their nodes.

The move changes the following storage and memory:

**Important**
The move replaces the node's root Amazon EBS volume and secondary Amazon EBS volume, which deletes any data stored on them. Back up any data that you need before you move the node.
+ The root Amazon EBS volume is replaced from the target instance group's AMI.
+ SageMaker HyperPod deletes and recreates the secondary Amazon EBS volume it creates at `/opt/sagemaker`, empty, using the target instance group's storage configuration.
+ GPU and CPU memory are cleared.
+ Data on local instance store (NVMe) is kept, so caches such as datasets or model weights stay warm on the new instance group. If the cache is large or you do not need it on the target, you can clear it before you move the node, or in the target instance group's lifecycle scripts.

**Note**
A node that has an Amazon EBS volume you attached yourself cannot be moved.

The node keeps its Amazon EC2 instance ID, its node logical ID, its network interfaces and IP addresses, its capacity reservation, and your own Amazon EC2 tags. SageMaker HyperPod updates the tags it sets to name the target cluster and instance group.

The move sets the node up as a member of the target instance group. It gives the node the target group's AMI, storage configuration, execution role, security groups, tags, labels, and taints. It then runs the target instance group's lifecycle scripts, so the node ends up configured like any other node in that group. Source labels and taints are not carried over. The node registers as a new Kubernetes `Node` in the target cluster. Its SSM target name changes to name the target cluster and instance group, and the source name stops connecting.

A move does not rerun the basic or deep health checks. To validate a moved node, run an on-demand health check with [StartClusterHealthCheck](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartClusterHealthCheck.html).

## Troubleshooting
<a name="smcluster-eks-move-nodes-troubleshooting"></a>

When SageMaker HyperPod rejects a whole request, it returns one of the following exceptions.

| Error | Cause | Fix |
| --- | --- | --- |
| ValidationException (HTTP 400) | The request does not meet a requirement. For example: a cluster that is not `InService`, is in maintenance, or is not Amazon EKS with continuous provisioning; a restricted instance group; a customer managed AWS KMS key; an instance group that is updating, in maintenance, or has a software update in progress; a target AMI that is too old; or a mismatched interface type, `ThreadsPerCore`, MIG configuration, or root volume size. Also returned when `--instance-count` has too few eligible nodes, the move would take the source below its minimum instance count, the node list has duplicates or no eligible nodes, or a `--client-token` was reused with different parameters. The cause also includes the caller not having `eks:DescribeCluster` on the source or target Amazon EKS cluster, which returns the message `Unable to retrieve EKS cluster with Arn ...`. | 1.  Read the message to find the requirement that failed. <br />2.  Use `ListClusterNodes` or `DescribeClusterNode` to check which nodes are eligible. <br />3.  Fix the request and retry. For that message, grant `eks:DescribeCluster` as shown in [Permissions](#smcluster-eks-move-nodes-permissions). |
| ResourceNotFound | The source or target cluster or instance group does not exist. | Check the cluster ARNs and instance group names. |
| InternalFailure | A temporary internal error occurred, or other changes to the same nodes kept conflicting with the request. | Retry with the same `--client-token` that you passed. |

Per-node entries come back only with `--node-ids` or `--node-logical-ids`, and only when at least one node is accepted. Each ineligible node is returned in `Failed` or `FailedNodeLogicalIds` with a `Code` and `Message`. If no node can move, the whole request fails with `ValidationException` and the message lists each node's reason. The `--instance-count` parameter never reports per-node errors.

| Code | Cause | Fix |
| --- | --- | --- |
| NodeIdNotFound | The node is not in the source cluster or instance group. | Check the ID and the source instance group. |
| NodeIdInUse | Another operation is running on the node: a move, termination, replacement, reboot, repair, software update, deep health check, or maintenance mode; a labels and taints update, including a pending MIG change; a Spot interruption; draining; or provisioning, including lifecycle scripts still running. | Retry after it finishes. |
| InvalidNodeStatus | The node is not `Running`, for example it is `Failed`; it has no instance yet; its subnet is not in the target instance group, for a flexible source group; or it has an Amazon EBS volume you attached yourself. | Replace or reboot a failed node, pick a target instance group that uses the node's subnet, or detach your volume. |
| NodeInstanceTypeMismatch | The node's instance type is not allowed by the target instance group. | For a flexible target instance group, the node's instance type must be one of the target's allowed types. For a standard target instance group, choose a target with the same instance type. |

### Stop, reverse, or recover a move
<a name="smcluster-eks-move-nodes-recover"></a>
+ To stop a move, call `BatchDeleteClusterNodes` on whichever cluster currently lists the node: the source cluster while the node shows `DetachInProgress`, and the target cluster once it shows `AttachInProgress`. This terminates and releases the instance. The node does not go back to the source.
+ To move nodes back, call `MoveClusterNodes` again with the source and target swapped.
+ To recover from a failed attach, check the target instance group's lifecycle script logs and fix the scripts before you move more nodes to that group. When the target instance group's lifecycle scripts fail, SageMaker HyperPod replaces the node in the target instance group: it terminates the instance and launches a new one. The cluster event for the failure links to the logs. SageMaker HyperPod retries a transient internal error on the same instance, and it needs no action from you.
+ To resume automatic recovery, wait until the node is `Running` in the target instance group. SageMaker HyperPod health monitoring, automatic node recovery, and repair do not act on a node during a move. After the node is `Running` in the target instance group, they cover it like any other node.

For more information about scaling down a cluster, see [Scaling down a SageMaker HyperPod cluster](smcluster-scale-down.md).
