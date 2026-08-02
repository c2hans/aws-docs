---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Nodes.viewing.html
---

# Viewing ElastiCache Node Status
<a name="Nodes.viewing"></a>

Using the [ElastiCache console](https://console.aws.amazon.com/elasticache/), you can quickly access the status of your ElastiCache node. The status of an ElastiCache node indicates the health of the node. You can use the following procedures to view the ElastiCache node status in the Amazon ElastiCache console, the AWS CLI command, or the API operation.

The possible status values for ElastiCache nodes are in the following table. This table also shows if you will be billed for the ElastiCache node.

| **Type** | **Billed** | **Description** |
| --- | --- | --- |
| `available` | Billed | The ElastiCache node is healthy and available. |
| `creating` | Not billed | The ElastiCache node is being created. The Node is inaccessible while it is being created. |
| `deleting` | Not billed | The ElastiCache node is being deleted. |
| `modifying` | Billed | The ElastiCache node is being modified because of a customer request to modify the node. |
| `updating` | Billed | An **Updating** state indicates one or more of the following is true of the Amazon ElastiCache node:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Nodes.viewing.html) |
| `rebooting cluster nodes` | Billed | The ElastiCache node is being rebooted because of a customer request or an Amazon ElastiCache process that requires the rebooting of the node. |
| `incompatible_parameters` | Not billed | Amazon ElastiCache can't start the node because the parameters specified in the node's parameter group aren't compatible with the node. Either revert the parameter changes or make them compatible with the node to regain access to your node. For more information about the incompatible parameters, check the [Events](https://us-east-1.console.aws.amazon.com/elasticache/home?region=us-east-1#/events) list for the ElastiCache node. |
| `incompatible_network` | Not billed | An incompatible-network state indicates one or more of the following is true of the Amazon ElastiCache node:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Nodes.viewing.html) |
| `restore_failed` | Not billed | A restore-failed state indicates one of the following is true of the Amazon ElastiCache node:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Nodes.viewing.html) |
| `snapshotting` | Billed | ElastiCache is creating a snapshot of the Valkey or Redis OSS node. |

## Viewing ElastiCache Node Status with the console
<a name="Nodes.viewing.console"></a>

To view the status of an ElastiCache Node with the console:

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. In the navigation pane, choose **Redis OSS Clusters** or **Memcached Clusters**. The **Caches page** appears with the list of ElastiCache Nodes. For each node, the status value is displayed.

1. You can then navigate to the **Service Updates** tab for the cache to display the list of service Updates applicable to the cache.

## Viewing ElastiCache Node Status with the AWS CLI
<a name="Nodes.viewing.cli"></a>

To view ElastiCache node and its status information by using the AWS CLI, use the `describe-cache-cluster` command. For example, the following AWS CLI command displays each ElastiCache node.

```
aws elasticache describe-cache-clusters
```

## Viewing ElastiCache Node Status through the API
<a name="Nodes.viewing.api"></a>

 To view the status of the ElastiCache node using the Amazon ElastiCache API, call the `DescribeCacheClusteroperation` with the `ShowCacheNodeInfo` flag to retrieve information about the individual cache nodes.
