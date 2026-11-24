---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/network-topology.html
---

# Network topology-aware scheduling in AWS PCS

The instances in an AWS Region are connected through a hierarchy of network switches. Instances under the same switch communicate over fewer network hops. Traffic between instances under different switches crosses higher levels of the hierarchy. Tightly coupled multi-node jobs, such as Message Passing Interface (MPI) jobs, run faster when their nodes are close together.

With network topology-aware scheduling, AWS PCS tells Slurm where each compute node sits in the network. Slurm's [topology/tree](https://slurm.schedmd.com/topology.html) plugin then allocates each multi-node job under the lowest-level switch that can satisfy it.

Slurm chooses among the nodes available at that time, so the allocation can still span more switches than optimal. You can limit how many leaf switches a job uses with the `--switches` option.

This topic describes how to enable network topology-aware scheduling on a queue, how AWS PCS discovers the topology, and what affects the result. For the topology inside a node, such as CPU topology and GPU affinity, see [Configuring hardware topology in AWS PCS](hardware-topology.md).

**Note**
On compute nodes in compute node groups created before November 1, 2026, the network topology might not match where the node sits in the network. AWS PCS will correct the network topology of these compute nodes over the coming weeks. This page will be updated when that is complete.

## Requirements
<a name="network-topology-requirements"></a>
+ The cluster uses Slurm 26.05 or later.
+ The queue has no UltraServer compute node groups. UltraServer queues use block topology instead. For more information, see [UltraServer queues](#network-topology-ultraserver).
+ To get a full switch path for each node, the compute node groups of the queue use instance types that support Amazon EC2 instance topology. For more information, see [Supported instance types](#network-topology-instance-types).

## Enable network topology-aware scheduling on a queue
<a name="network-topology-enable"></a>

Network topology-aware scheduling is off by default. You enable it per queue with the `Topology` custom Slurm setting, which accepts the following values:
+ `network-tree` – Slurm allocates the jobs of the queue by network topology.
+ `flat` – Slurm treats all nodes of the queue as equally close. This is the same as not setting `Topology`.

You can set `Topology` when you create or update a queue. For the full queue update procedure, see [Updating an AWS PCS queue](working-with_queues_update.md).

------
#### [ AWS Management Console ]

**To enable network topology-aware scheduling on a queue**

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters).

1. Choose your cluster, and then choose **Queues**.

1. Choose the queue, and then choose **Edit**.

1. For **Topology**, choose `network-tree`.

1. Choose **Update**. The queue status is *Updating* while AWS PCS applies the change, and returns to *Active* when network topology-aware scheduling is enabled for the queue.

------
#### [ AWS CLI ]

Run the following AWS CLI command to set `Topology` on a queue:

**Example – Enabling network topology-aware scheduling on a queue**

```bash
aws pcs update-queue --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --queue-identifier {{my-queue}} \
    --slurm-configuration \
    'slurmCustomSettings=[{parameterName=Topology,parameterValue=network-tree}]'
```

In the command, make the following replacements:
+ Replace {{region}} with the ID of the AWS Region where your cluster is, such as `us-east-1`.
+ Replace {{my-cluster}} with the name or `clusterId` of your cluster.
+ Replace {{my-queue}} with the name or `queueId` of your queue.

The `--slurm-configuration` option replaces all custom Slurm settings of the queue. Include the queue's other custom settings in the same list to keep them.

It can take several minutes to update the queue. Network topology-aware scheduling is enabled when the queue status returns to `ACTIVE`. To check the status, run the following command:

```bash
aws pcs get-queue --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --queue-identifier {{my-queue}}
```

------

The change takes effect when the queue update completes. The update doesn't affect running jobs or replace running nodes. AWS PCS assigns their topology shortly after the update. To disable network topology-aware scheduling, set `Topology` to `flat` or remove the setting.

A compute node group can belong both to a queue that uses `network-tree` and to a queue that doesn't. The topology of its nodes only affects jobs in the `network-tree` queue.

## Network topology discovery
<a name="network-topology-how"></a>

When a compute node launches, AWS PCS reads its position in the network from Amazon EC2 and assigns it to the Slurm node. The position is a switch path from the root of the tree to the switch the node is attached to:
+ `sw-root` – The root of the tree, shared by all nodes.
+ Region and Availability Zone ID – The AWS Region and Availability Zone of the node. Nodes in different Availability Zones share only the top of the tree.
+ Network nodes – The network nodes that Amazon EC2 returns for the instance under its Availability Zone, from the broadest to the narrowest. For more information, see [Amazon EC2 instance topology](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology.html) in the *Amazon Elastic Compute Cloud User Guide*.

For example, a node in the `euw1-az1` Availability Zone of eu-west-1 has the following topology:

```
network-tree:sw-root:eu-west-1:euw1-az1:nn-bb:nn-cc
```

AWS PCS assigns the topology asynchronously, on a best-effort basis, and doesn't delay scheduling for it.

Until AWS PCS assigns topology to a compute node, the node is under a default switch, `sw-default`, with the other compute nodes that don't have topology yet. Slurm treats those nodes as equally close, and can schedule jobs on them in the meantime.

When a node powers down, it goes back under `sw-default`, and AWS PCS assigns its topology again the next time it launches. The switches that AWS PCS added for the node stay in the output of `scontrol show topology` with no nodes, until the Slurm controller reloads its configuration.

To see the switch tree and the topology of a node, run the following commands on the cluster:

```bash
scontrol show topology network-tree
scontrol show node {{node-name}}
```

## Supported instance types
<a name="network-topology-instance-types"></a>

Amazon EC2 returns network topology only for some instance types. For the list, see [Prerequisites for Amazon EC2 instance topology](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology-prerequisites.html) in the *Amazon Elastic Compute Cloud User Guide*.

AWS PCS places nodes of other instance types under a single switch in their Availability Zone, named after the Availability Zone ID, for example:

```
network-tree:sw-root:eu-west-1:euw1-az1:euw1-az1-standard
```

Slurm treats all of these compute nodes as one hop apart, regardless of their actual position in the network, and only separates them by Availability Zone.

### Mixed instance type queues
<a name="network-topology-mixed-types"></a>

If a `network-tree` queue includes both instance types that support instance topology and types that don't, Slurm allocates jobs less precisely than in a queue that has only supported instance types:
+ Because all compute nodes of unsupported instance types in an Availability Zone appear one hop apart, Slurm can prefer them over supported nodes for multi-node jobs.
+ Slurm allocates a job that spans both kinds of nodes through the Availability Zone switch.
+ On compute nodes of unsupported instance types, `--switches` doesn't keep a job close together in the network. Slurm counts all of these compute nodes in an Availability Zone as being under one switch, so any allocation of them within one Availability Zone meets the limit.

All nodes stay schedulable. To get the most from network topology-aware scheduling, use separate queues for supported and unsupported instance types, or use `--constraint` to keep tightly coupled jobs on supported instance types.

## Best practices
<a name="network-topology-best-practices"></a>

To get the most from network topology-aware scheduling, follow these practices:
+ **Use a cluster placement group** – A cluster placement group packs instances close together in one Availability Zone, so Slurm has more nodes under the same switches to choose from. For more information, see [Placement groups for EC2 instances in AWS PCS](working-with_networking_placement-groups.md).
+ **Keep a queue in one Availability Zone** – If a queue spans Availability Zones and one Availability Zone doesn't have enough available nodes, Slurm can allocate a multi-node job across Availability Zones. Traffic between Availability Zones has higher latency.
+ **Limit the number of switches for a job** – Use the `--switches={{count}}[@{{max-time}}]` option of `sbatch`, `salloc`, or `srun` to ask Slurm to allocate a job under at most {{count}} leaf switches. Slurm waits up to {{max-time}} for them. This is best effort, because AWS PCS assigns topology asynchronously. Nodes that don't have their topology yet count as being under the same default switch. Slurm also allocates idle nodes that are running before nodes that are powered down, even if the powered-down nodes are closer together in the network. For more information, see [--switches](https://slurm.schedmd.com/sbatch.html#OPT_switches) in the Slurm documentation.

## UltraServer queues
<a name="network-topology-ultraserver"></a>

A Slurm partition uses one topology. Queues with UltraServer compute node groups use block topology, so that jobs stay within an UltraServer. For more information, see [Configure UltraServer instances](capacity-blocks-nvidia-imex.md).

AWS PCS rejects the `Topology` setting on a queue with UltraServer compute node groups. AWS PCS also rejects a compute node group update that would add UltraServer capacity to a queue that sets `Topology`.
