---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/instance-placement.html
---

# Instance placement
<a name="instance-placement"></a>

 Outposts have a finite number of compute hosts. If your application deploys multiple related instances on Outposts; without additional configuration, the instances may deploy on the same hosts or on hosts in the same rack. Today, there are three mechanisms you may use to distribute instances to mitigate the risk of running related instances on the same infrastructure:

 **Multi-Outpost deployment** – similar to a multi-AZ strategy in the Region, you can deploy Outposts to separate data centers and deploy application resources to specific Outposts. This allows you to run instances on the desired Outpost (a logical set of racks). [Intra-VPC Communication](https://aws.amazon.com/about-aws/whats-new/2023/08/aws-outposts-rack-intra-vpc-communication-multiple-outposts/) Across Multiple Outposts with Direct VPC Routing is another strategy that can be used to spread workloads across multiple Outposts within the same VPC using the Outpost local gateways (LGW) to create routes between the subnets on the Outposts. A multi-Outpost strategy may be employed to protect against rack and data center failure modes and, if the Outposts are anchored to separate AZs or Regions, may also provide protection against AZ or Region failure modes. For more information about multi-Outpost architectures, see the [Larger Failure Modes](larger-failure-modes.md).

 **Amazon EC2 placement groups on Outposts** (single-Outpost multi-rack instance placement) – You can create [placement groups on Outposts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups-outpost.html) that you have created in your account. This allows you to spread out instances across underlying hardware on an Outpost at your site. When you create a placement group with a spread strategy on an Outpost, you can choose to have the placement group spread instances across hosts or racks.

 A spread placement group provides a simple way distribute single instances across racks or hosts to reduce the potential for correlated failures. You may only deploy into the group as many instances as you have hosts in your Outpost.

![Diagram showing EC2 spread placement group on an Outpost with three racks](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/ec2-spread-placement-group.png)

 You can also distribute instances across multiple racks with partition placement groups. Use automatic distribution to spread instances across partitions in the group or deploy instances to selected target partitions. Deploying instances to target partitions allows you to deploy selected resources to the same rack while distributing other resources across racks. For example, if you have a logical Outpost with three racks, creating a partition placement group with three partitions allows you to distribute resources across the racks.

![Diagram showing EC2 partition placement groups on an Outpost with three racks](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/ec2-partition-placement-groups.png)

 **Creative server slotting** – if you have a single-rack Outpost or if the service you are using on Outposts does not support placement groups, you may be able to use creative slotting to ensure your instances do not deploy on the same physical server. If the related instances are the same EC2 instance size, you may be able to slot your servers to limit the number of slots of that size configured on each server – spreading the slots across the servers. Server slotting will limit the number of instances (of that size) that can run on a single server.

 As an example, consider the slotting layout shown previously in Figure 13. If your application needed to deploy three `m5.4xlarge` instances on the Outpost configured with this slotting layout, EC2 would place each instance on a separate server and there would be no possibility that these instances could run on the same server – as long as the slotting configuration does not change to open additional `m5.4xlarge` slots on the servers.

## Recommended practices for compute instance placement
<a name="recommended-practices-for-compute-instance-placement"></a>
+  Use [Amazon EC2 placement groups on Outposts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups-outpost.html) to control placement of instances across racks within a single logical Outpost.
+  Instead of ordering an Outpost with a single medium or large Outpost rack, consider splitting the capacity into two small or medium racks to allow you to take advantage of the EC2 placement groups ability to distribute instances across racks.
+ Amazon EC2 Placement group on Outposts can be used to influence the placement of EKS nodegroups, Control Plane Nodes for EKS Local Cluster and [ECS Task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html).
+ Use Intra-VPC Communication to spread workloads across multiple Outposts within the same VPC.
