---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-cassandra-cluster-on-amazon-ec2-with-private-static-ips-to-avoid-rebalancing.html
---

# Deploy a Cassandra cluster on Amazon EC2 with private static IPs to avoid rebalancing
<a name="deploy-a-cassandra-cluster-on-amazon-ec2-with-private-static-ips-to-avoid-rebalancing"></a>

*Dipin Jain, Amazon Web Services*

## Summary
<a name="deploy-a-cassandra-cluster-on-amazon-ec2-with-private-static-ips-to-avoid-rebalancing-summary"></a>

The private IP of an Amazon Elastic Compute Cloud (Amazon EC2) instance is retained throughout its lifecycle. However, the private IP might change during a planned or unplanned system crash; for example, during an Amazon Machine Image (AMI) upgrade. In some scenarios, retaining a private static IP can enhance the performance and recovery time of workloads. For example, using a static IP for an Apache Cassandra seed node prevents the cluster from incurring a rebalancing overhead.

This pattern describes how to attach a secondary elastic network interface to EC2 instances to keep the IP static during rehosting. The pattern focuses on Cassandra clusters, but you can use this implementation for any architecture that benefits from private static IPs.

## Prerequisites and limitations
<a name="deploy-a-cassandra-cluster-on-amazon-ec2-with-private-static-ips-to-avoid-rebalancing-prereqs"></a>

**Prerequisites **
+ An active Amazon Web Service (AWS) account

**Product versions**
+ DataStax version 5.11.1
+ Operating system: Ubuntu 16.04.6 LTS

## Architecture
<a name="deploy-a-cassandra-cluster-on-amazon-ec2-with-private-static-ips-to-avoid-rebalancing-architecture"></a>

**Source architecture**

The source could be a Cassandra cluster on an on-premises virtual machine (VM) or on EC2 instances in the AWS Cloud. The following diagram illustrates the second scenario. This example includes four cluster nodes: three seed nodes and one management node. In the source architecture, each node has a single network interface attached.

![Four Amazon EC2 cluster nodes that each have a single network interface attached.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/47ca4dbc-0922-4e65-b66c-4db5122fc4ac/images/5d80cfc9-4b72-4c72-aefd-b77cc0fb58e3.png)

**Target architecture**

The destination cluster is hosted on EC2 instances with a secondary elastic network interface attached to each node, as illustrated in the following diagram.

![Four Amazon EC2 cluster nodes that each have a secondary elastic network interface attached.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/47ca4dbc-0922-4e65-b66c-4db5122fc4ac/images/d1e22017-f041-426b-9204-31ac158a407d.png)

**Automation and scale**

You can also automate attaching a second elastic network interface to an EC2 Auto Scaling group, as described in an [AWS Knowledge Center video](https://www.youtube.com/watch?v=RmwGYXchb4E).

## Epics
<a name="deploy-a-cassandra-cluster-on-amazon-ec2-with-private-static-ips-to-avoid-rebalancing-epics"></a>

### Configure a Cassandra cluster on Amazon EC2
<a name="configure-a-cassandra-cluster-on-amazon-ec2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch EC2 nodes to host a Cassandra cluster. | On the [Amazon EC2 console](https://console.aws.amazon.com/ec2/), launch four EC2 instances for your Ubuntu nodes in your AWS account. Three (seed) nodes are used for the Cassandra cluster, and the fourth node acts as a cluster management node where you will install DataStax Enterprise (DSE) OpsCenter. For instructions, see the [Amazon EC2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance). | Cloud engineer |
| Confirm node communications. | Make sure that the four nodes can communicate with one another over the database and cluster management ports. | Network engineer |
| Install DSE OpsCenter on the management node. | Install DSE OpsCenter 6.1 from the Debian package on the management node. For instructions, see the [DataStax documentation](https://docs.datastax.com/en/opscenter/6.1/opsc/install/opscInstallDeb_t.html). | DBA |
| Create a secondary network interface. | Cassandra generates a universal unique identifier (UUID) for each node based on the IP address of the EC2 instance for that node. This UUID is used for distributing virtual nodes (vnodes) on the ring. When Cassandra is deployed on EC2 instances, IP addresses are assigned automatically to the instances as they are created.  In the event of a planned or unplanned outage, the IP address for the new EC2 instance changes, the data distribution changes, and the entire ring has to be rebalanced. This is not desirable. To preserve the assigned IP address, use a [secondary elastic network interface](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#scenarios-enis) with a fixed IP address.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-cassandra-cluster-on-amazon-ec2-with-private-static-ips-to-avoid-rebalancing.html)<br />For more information about creating a network interface, see the [Amazon EC2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#create_eni). | Cloud Engineer |
| Attach the secondary network interface to cluster nodes. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-cassandra-cluster-on-amazon-ec2-with-private-static-ips-to-avoid-rebalancing.html)For more information about attaching a network interface, see the [Amazon EC2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#attach_eni). | Cloud engineer |
| Add routes in Amazon EC2 to address asymmetric routing.  | When you attach the second network interface, the network will very likely perform asymmetric routing. To avoid this, you can add routes for the new network interfaces.<br />For an in-depth explanation and remediation of asymmetric routing, see the [AWS Knowledge Center video](https://www.youtube.com/watch?v=RmwGYXchb4E) or [Overcoming Asymmetric Routing on Multi-Home Servers](http://www.linuxjournal.com/article/7291) (article in *Linux Journal* by Patrick McManus, April 5, 2004). | Network engineer |
| Update DNS entries to point to the secondary network interface IP. | Point the fully qualified domain name (FQDN) of the node to the IP of the secondary network interface. | Network engineer |
| Install and configure the Cassandra cluster by using DSE OpsCenter. | When the cluster nodes are ready with the secondary network interfaces, you can install and configure the Cassandra cluster. | DBA |

### Recover cluster from node failure
<a name="recover-cluster-from-node-failure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AMI for the cluster seed node. | Make a backup of the nodes so you can restore them with database binaries in case of node failure. For instructions, see [Create an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ami.html) in the Amazon EC2 documentation. | Backup administrator |
| Recover from node failure. | Replace the failed node with a new EC2 instance launched from the AMI, and attach the secondary network interface of the failed node. | Backup administrator |
| Verify that the Cassandra cluster is healthy. | When the replacement node is up, verify cluster health in DSE OpsCenter. | DBA |

## Related resources
<a name="deploy-a-cassandra-cluster-on-amazon-ec2-with-private-static-ips-to-avoid-rebalancing-resources"></a>
+ [Installing DSE OpsCenter 6.1 from the Debian package](https://docs.datastax.com/en/opscenter/6.1/opsc/install/opscInstallDeb_t.html) (DataStax documentation)
+ [How to make a secondary network interface work in an Ubuntu EC2 instance](https://www.youtube.com/watch?v=RmwGYXchb4E) (AWS Knowledge Center video)
+ [Best Practices for Running Apache Cassandra on Amazon EC2](https://aws.amazon.com/blogs/big-data/best-practices-for-running-apache-cassandra-on-amazon-ec2/) (AWS blog post)
