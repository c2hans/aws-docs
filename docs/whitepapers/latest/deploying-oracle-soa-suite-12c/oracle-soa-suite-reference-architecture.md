---
source_url: https://docs.aws.amazon.com/whitepapers/latest/deploying-oracle-soa-suite-12c/oracle-soa-suite-reference-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Oracle SOA Suite reference architecture
<a name="oracle-soa-suite-reference-architecture"></a>

 The following reference architecture shows how you can deploy Oracle SOA Suite 12c on AWS.

![A diagram showing high-level architecture of Oracle SOA Suite 12c on AWS.](http://docs.aws.amazon.com/whitepapers/latest/deploying-oracle-soa-suite-12c/images/soa-architecture.jpeg)

 This reference architecture includes a separate WebLogic domain for each component of Oracle SOA Suite (Oracle SOA, OSB, Oracle BPM, Oracle BAM, and Oracle ADF). Each WebLogic domain has one Administrative Server and multiple Managed Servers grouped into a WebLogic Server Cluster. The SOA metadata repository (MDS) is deployed on [Amazon Relational Database Service](https://aws.amazon.com/rds) (Amazon RDS). Amazon EFS is used for shared storage.

## Traffic distribution
<a name="traffic-distribution"></a>

 [Amazon Route 53](https://aws.amazon.com/route53/) domain name system (DNS) directs users to the application deployed on Oracle SOA Suite. [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) (ELB) distributes incoming requests across the Oracle HTTP Servers and the WebLogic Managed Servers (for T3 traffic). The Oracle HTTP Server (OHS) along with the WebLogic Server Plugin serves as the reverse proxy routing the traffic to the respective WebLogic Managed Server instance. The WebLogic Managed Server instances host the various components of Oracle SOA Suite.

 The Application Load Balancer load balances HTTP(S) traffic and the Network Load Balancer load balances T3 traffic.

### Java Message Service (JMS) integration and T3 load balancing
<a name="java-message-service-jms-integration-and-t3-load-balancing"></a>

 Remote Method Invocation (RMI) communications in the WebLogic Server use the T3 protocol to transport data between WebLogic Servers and other Java programs, including clients and other WebLogic Server instances. When deploying on AWS, you can use a [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html) for load balancing T3 requests. WebLogic Server clients that use RMI can interoperate with a load balancer by tunneling T3 over HTTP/HTTPS or using T3 directly with the load balancer. Refer to [WebLogic RMI Integration with Load Balancers](https://docs.oracle.com/cd/E24329_01/web.1211/e24389/load_balance.htm#WLRMI256) on the [*Oracle Help Center*](https://docs.oracle.com/en/) for more information.

### Storage
<a name="storage"></a>

 If you use file-based persistence, you must have storage for the Oracle WebLogic Server product binaries, common files and scripts, domain configuration files, logs, and persistence stores for Java Message Service (JMS) and Java Transaction API (JTA).

 You can either use shared storage or [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) volumes to store these files.

### Shared storage
<a name="shared-storage"></a>

 Using Oracle Fusion Middleware, you can configure multiple WebLogic Server domains from a single Oracle home. This configuration allows you to install the Oracle home in a single location on a shared volume and reuse the Oracle home for multiple host installations.

 Amazon EFS provides a simple, scalable, fully-managed elastic network file system (NFS). Amazon EFS can store the artifacts for Oracle Fusion Middleware, including Oracle home, Domain Home, Application Home, JTA Transaction Logs, and JMS Stores for persisting the JMS messages.

 The reference architecture uses Amazon EFS for shared storage. The Oracle WebLogic product binaries, common files and scripts, domain configuration files, and logs are stored in Amazon EFS, which includes the *commons*, *domains*, *middleware*, and *logs* file systems.

 Amazon EFS has two throughput modes for your file system: Bursting Throughput and Provisioned Throughput. With Bursting Throughput mode, throughput on Amazon EFS scales as your file system grows. With Provisioned Throughput mode, you can instantly provision the throughput of your file system in MiB/s, independent of the amount of data stored. For better performance, we recommend you select Provisioned Throughput mode while using Amazon EFS. With Provisioned Throughput mode, you can provision up to 1024 MiB/s of throughput for your file system. You can change the file system throughput in Provisioned Throughput mode at any time after you create the file system.

 We recommend mounting the Amazon EFS on Amazon EC2 with a DNS name and the recommended NFS mount options. For more information, refer to [Mounting on Amazon EC2 with a DNS name](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html) and[ Recommended NFS mount options](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-nfs-mount-settings.html).

## High availability
<a name="high-availability"></a>

 The Managed Servers for each domain are grouped into a WebLogic Server Cluster that spans two Availability Zones (AZs). Use [Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) to operate production applications and databases that are more highly available, fault tolerant, and scalable than is possible from a single data center. In the unlikely event of failure of one AZ, user requests are routed to your application instances in the second zone. This ensures that your application continues to remain available at all times.

 You can add and remove Oracle HTTP Server (OHS) instances from your load balancer as your needs change, either manually or with [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/), without disrupting the overall flow of information. ELB ensures that only healthy instances receive traffic by detecting unhealthy instances and rerouting traffic across the remaining healthy instances. If an instance fails, ELB automatically reroutes the traffic to the remaining running instances. If a failed instance is restored, ELB restores the traffic to that instance.

 Oracle Metadata Services (MDS) Repository database contains the metadata for Oracle Fusion Middleware components, such as the Oracle Application Developer Framework. The MDS is hosted on [Amazon RDS for Oracle](https://aws.amazon.com/rds/oracle/). Amazon RDS for Oracle makes it easy to use replication to enhance availability and reliability for production workloads. Using the Multi-AZ deployment option, you can run MDS with high-availability and a built-in automated failover from your primary database to a synchronously-replicated secondary database in case of a failure. Since the endpoint for your database instance remains the same after a failover, applications can resume database operations as soon as the failover is complete without the need for manual administrative intervention. You can run Amazon RDS for Oracle under two different licensing models: License Included or Bring-Your-Own-License (BYOL). In the License Included service model, you do not need to purchase Oracle licenses separately; the Oracle Database software has been licensed by AWS.

 Amazon EFS is designed to be highly available and durable. Your data in Amazon EFS is redundantly stored across multiple AZs, which means that your data is available in the unlikely event of an AZ failure.

### State management
<a name="state-management"></a>

 For the stateful components of Oracle SOA Suite such as Oracle BAM web services, you can configure Oracle WebLogic Server to replicate the HTTP session state in memory to another Managed Server in the Oracle WebLogic Server Cluster. Oracle WebLogic Server uses a cookie to track the location of the Managed Servers hosting the primary and the replica copies of the session state. If the Managed Server hosting the primary copy of the session state fails, Oracle WebLogic Server can retrieve the HTTP session state from the replica. For more information about HTTP session state replication, refer to [*Oracle WebLogic Server 12c: Managing HTTP Sessions in a Cluster*](https://www.oracle.com/webfolder/technetwork/tutorials/obe/fmw/wls/12c/12-ManageSessions--4478/session.htm).

### High availability and state management of Oracle SOA Suite 12c components
<a name="high-availability-and-state-management-of-oracle-soa-suite-12c-components"></a>

 The following table lists the various Oracle SOA Suite 12c components and the strategies used for failure protection, high availability, and state management.

 Table 1: High availability and state management of Oracle SOA Suite 12c components

- **** Oracle SOA ****
  - **Oracle SOA Suite component:** SOA Service Infrastructure
  - **High availability:** Active-Active
  - **State management:** Stateless

- ** **
  - **Oracle SOA Suite component:** SOA Admin
  - **High availability:** Singleton (Active- Passive)
  - **State management:** Stateless

- ** **
  - **Oracle SOA Suite component:** SOA BPEL
  - **High availability:** Active-Active
  - **State management:** Stateless

- ** **
  - **Oracle SOA Suite component:** BPM Suite
  - **High availability:** Active-Active
  - **State management:**

- ** **
  - **Oracle SOA Suite component:** B2B UI
  - **High availability:** Active-Active
  - **State management:** Stateful (HTTP Session)

- ** **
  - **Oracle SOA Suite component:** Mediator
  - **High availability:** Active-Active
  - **State management:** Stateless

- ** **
  - **Oracle SOA Suite component:** Human workflow / **High availability:** Active-Active / **State management:** Stateless
  - **Oracle SOA Suite component:** Oracle WSM / **High availability:** Active-Active / **State management:** Stateless
  - **Oracle SOA Suite component:** Oracle UMS  / **High availability:** Active-Active  / **State management:**
  - **Oracle SOA Suite component:** Oracle JCA Adapters  / **High availability:** Active-Active  / **State management:** Stateless

- ** **Oracle BAM** **
  - **Oracle SOA Suite component:** Web Apps  / **High availability:** Active-Active  / **State management:** BAM web applications are stateful and need session replication for high availability.
  - **Oracle SOA Suite component:** BAM Server  / **High availability:** Singleton Active-Passive  / **State management:** Stateless

- ** **OSB** **
  - **Oracle SOA Suite component:**
  - **High availability:** Active-Active
  - **State management:**

## Failure scenarios
<a name="failure-scenarios"></a>

 The following section describes how failure scenarios are addressed for the various components in the architecture.

### Oracle HTTP server failure
<a name="oracle-http-server-failure"></a>

 You can also configure an [Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) with EC2 instances running Oracle HTTP Server in multiple AZs. Amazon EC2 Auto Scaling spins up new instances in case of failure of the Oracle HTTP Server.

 If the underlying host for the OHS experiences a failure, you can also [configure automatic recovery for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) to recover the failed server instances. When using automatic recovery for Amazon EC2 instances, several system status checks monitor the instance and the other components required for your instance. Among other things, the system status checks monitor for loss of network connectivity, loss of system power, software issues on the physical host, and hardware issues on the physical host. If a system status check of the underlying hardware fails, the instance is rebooted (on new hardware if necessary), but it retains its instance ID, IP address, Elastic IP addresses, EBS volume attachments, and other configuration details.

### WebLogic Server node failure
<a name="weblogic-server-node-failure"></a>

 Because SOA components run in an Oracle WebLogic Server Cluster, the components remain highly available as long as the components are running in Active-Active mode and deployed across multiple WebLogic Managed Servers.

### WebLogic managed server failure
<a name="weblogic-managed-server-failure"></a>

 In the event of a Managed Server failure, Oracle WebLogic Node Manager restarts the WebLogic Managed Server.

### Administration server failure
<a name="administration-server-failure"></a>

 The Administration Server is used to configure, manage, and monitor the resources in the domain, including the Managed Server instances. Because the failure of the Administration Server does not affect the functioning of the Managed Servers in the domain, the Managed Servers continue to run, and your application is still available.

 However, if the Administration Server fails, the WebLogic Server Administration Console is unavailable and you cannot make changes to the domain configuration.

 If the underlying host for the Administration Server experiences a failure, you can use the [automatic recovery for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) to recover the failed server instances.

 Another option is to put the Administration Server instances in an [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) group that spans multiple AZs, and set the minimum and maximum size of the group to one. Automatic scaling ensures that an instance of the Administration Server is running in the selected AZs. This configuration ensures high availability of the Administration Server if an AZ failure occurs.

### MDS database failure
<a name="mds-database-failure"></a>

 The database instance failure can be handled by using [Amazon RDS for Oracle](https://aws.amazon.com/rds/oracle/) with active-standby setup using Multi-AZ deployment. Refer to [Multi-AZ deployments for high availability](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) for more details on Multi-AZ deployments.

## Considerations for deploying Oracle SOA Suite 12c on AWS
<a name="considerations-for-deploying-oracle-soa-suite-12c-on-aws"></a>

 The following are some points to consider when deploying Oracle SOA Suite 12c on AWS.
+  Configure Oracle WebLogic Server in unicast mode and make sure to allow the port number in the AWS Security Group configuration.
+  Make sure to set the appropriate value of the Java property `networkaddress.cache.ttl` so that appropriate caching policy is set in the JVM for successful DNS lookups. See *Setting the JVM TTL for DNS Name Lookups* in [Multi-AZ deployments for high availability](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) for more information.
+  Allow appropriate inbound and outbound traffic in the application security groups including the ports configured for T3, HTTP(S), Internal WebLogic Server Cluster intercommunication, and Internal Coherence cluster communication.
+  If SOA nodes are not synchronizing after deploying the BPEL process, tune the Linux kernel parameters `net.core.rmem_max` and `net.core.wmem_max`. Refer to the Oracle Support document [Nodes Not Syncing In 12C (Doc ID 2315273.1)](https://support.oracle.com/knowledge/Middleware/2315273_1.html) for more information.
