---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/globally-scoped-operations-best-practices.html
---

# Globally scoped operations best practices
<a name="globally-scoped-operations-best-practices"></a>

This section provides best practices for using services with globally scoped operations, particularly dependencies on Route 53, in your recovery operations.

This section covers the following topics:
+ [AWS IAM service-linked roles](#aws-iam-service-linked-roles)
+ [Application Load Balancers (ALB)](#application-load-balancers)
+ [Network Load Balancers (NLB)](#network-load-balancers)
+ [Amazon EC2](#amazon-ec2)
+ [Amazon Relational Database Service databases](#amazon-rds-databases)
  + [Microsoft SQL Server](#microsoft-sql-server)
+ [Amazon Aurora](#amazon-aurora)
  + [Aurora DB clusters](#aurora-db-clusters)
  + [Amazon Aurora Global Database](#amazon-aurora-global-database)
  + [Amazon Aurora Serverless v2](#amazon-aurora-serverless-v2)
  + [Amazon Aurora DSQL](#amazon-aurora-dsql)
+ [AWS IAM Identity Center](#aws-iam-identity-center)

## AWS IAM service-linked roles
<a name="aws-iam-service-linked-roles"></a>

 A [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html) is a unique type of IAM role that’s linked directly to an AWS service. Service-linked roles (SLR) are predefined by the service and include all the permissions that the service requires to call other AWS services on your behalf. The first time you provision a resource that requires an SLR in any Region, the AWS service might try to provision that SLR on your behalf. This operation depends on the IAM control plane. When planning for dependencies on services that use an SLR, you should make sure that the SLR has been pre-provisioned to avoid dependencies on the IAM control plane during recovery. See [the IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) for a list of the services that use an SLR.

## Application Load Balancers (ALB)
<a name="application-load-balancers"></a>

 The ALB control plane uses the Route 53 control plane to register new load balancer nodes in the ALB’s DNS A record. This happens when you provision the load balancer, unhealthy load balancer nodes are replaced, or as the load balancer scales up and out. The Elastic Load Balancing service uses the Route 53 control plane in `us-east-1` in addition to the internal recovery endpoint for these operations. Provisioning a load balancer also requires Route 53 health check provisioning, which depends on the Route 53 control plane in `us-east-1`. In the unlikely event the Route 53 control plane is unavailable in `us-east-1`, ELB can still replace unhealthy nodes or scale using the recovery Route 53 endpoint, though these operations might be delayed. When planning for dependencies on ALB for multi-Region failover, pre-provision your load balancers in the failover Region to prevent a dependency on `us-east-1` during recovery.

## Network Load Balancers (NLB)
<a name="network-load-balancers"></a>

 The NLB control plane uses the Route 53 control plane to register the IP address for each zonal node in different Availability Zones when you provision the load balancer. The Elastic Load Balancing service uses the Route 53 control plane in `us-east-1` in addition to the internal recovery endpoint for these operations. Provisioning a load balancer also requires Route 53 health check provisioning, which depends on the Route 53 control plane in `us-east-1`. When planning for dependencies on NLB for multi-Region failover, pre-provision your load balancers in the failover Region to prevent a dependency on `us-east-1` during recovery.

## Amazon EC2
<a name="amazon-ec2"></a>

Amazon EC2 instances with public IP addresses also get assigned a public DNS name like:
+ `ec2-1-2-3-4.region.compute.amazonaws.com`
+ `ec2-54-210-12-34.compute-1.amazonaws.com`

 The public DNS names are created in Route 53 public hosted zones. Launching an Amazon EC2 instance with a public IP address depends on the Route 53 control plane in `us-east-1`. To create a statically stable design, either pre-provision all required public Amazon EC2 instances for your recovery or use private Amazon EC2 instances behind a pre-provisioned public endpoint like a load balancer or API Gateway.

Private Amazon EC2 instances use the VPC DNS service for [instance hostnames](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) which exists independently in each AWS Region and doesn’t depend on the Route 53 control plane. Records that AWS creates for private Amazon EC2 instances in the VPC DNS service are like the following:
+ `ip-10-0-10.ec2.internal`
+ `ip-10-0-1-5.compute.us-west-2.compute.internal`
+ `i-0123456789abcdef.ec2.internal`
+ `i-0123456789abcdef.us-west-2.compute.internal`

These records don’t rely on the Route 53 control plane in `us-east-1`.

## Amazon Relational Database Service databases
<a name="amazon-rds-databases"></a>

 You can use [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) (for MySQL, MariaDB, PostgreSQL, Oracle, Microsoft SQL, and Db2) to provision single-AZ and Multi-AZ databases in addition to in-Region and cross-Region read replicas. Amazon RDS uses both the primary and recovery Route 53 endpoints for provisioning and managing Amazon RDS instances, including restoring a database from a backup. Amazon RDS uses a combination of the primary and recovery Route 53 control plane endpoints, Route 53 health checks, and internal services to reliably propagate changes in DNS without a single point of failure for database recovery.

**Single-AZ Databases:** Single-AZ databases can be provisioned successfully without the need for Route 53 health checks (which are provisioned through the Route 53 control plane in `us-east-1`). Single-AZ databases take the following steps for recovery:

1. The Amazon RDS health check system detects an unresponsive or failing host

1. A scenario-specific waiting period is observed to prevent false-positives

1. A new Amazon EC2 host is provisioned using the same ENI and monitored until it becomes fully operational

1. The existing data Amazon EBS volumes are attached to the new host

1. The database engine is started and verified

**Multi-AZ Databases:** When you provision an Amazon RDS Multi-AZ database instance (one standby) or a Multi-AZ database cluster (two standbys, only MySQL and PostgreSQL support this option), Amazon RDS starts by provisioning a single-AZ instance. This can succeed without the creation of Route 53 health checks (which are provisioned through the Route 53 control plane in `us-east-1`), and you can start using the single-AZ instance after it’s provisioned. In the background, Amazon RDS begins converting the single-AZ instance to Multi-AZ. If Amazon RDS can’t provision the required Route 53 health checks (because of an impairment to the Route 53 control plane in `us-east-1`), the conversion to Multi-AZ is paused until that creation succeeds. During that time, you can continue to use the single-AZ instance, but it will not replicate data to the other Availability Zones and the other nodes will not be available failover targets. If the single-AZ instance becomes impaired, it follows the single-AZ recovery steps above.

Normally operating Multi-AZ database instances take the following steps for failover to another Availability Zone:

1. The Amazon RDS health check system detects an unresponsive or failing primary instance

1. A scenario-specific waiting period is observed to prevent false-positives

1. Amazon RDS promotes a secondary instance to be the primary

1. The system monitors the promoted secondary instance until the database engine is fully operational

1. The Amazon RDS health check updates DNS to have the secondary instance take over the primary DNS record

To failover a Multi-AZ DB cluster deployment to another Availability Zone, Amazon RDS takes the following steps:

1. The Amazon RDS quorum service detects an unresponsive or failing primary instance

1. A scenario-specific waiting period is observed to prevent false-positives

1. The quorum service initiates the leader election process, selecting the most up-to-date node

1. The Amazon RDS health check service updates DNS to have the new leader take over the primary DNS record

**Read replicas:** Provisioning Amazon RDS in-Region and cross-Region read replicas uses the Route 53 primary and recovery control plane endpoints to create the associated DNS records, but doesn’t require the creation of Route 53 health checks. Promoting a read replica, both in-Region and cross-Region, isn’t a process that’s automated by Amazon RDS. You must manually promote the read replica, which doesn’t rely on the Route 53 control plane. Your application must be configured to write and optionally read from this newly promoted instance.

To re-establish cross-Region replication or to restore scaled out reads in the same Region, you need to create a new read replica. The new instance will have a new DNS name that your application must communicate with for reads or for writes after a failover. One option is to update your application configuration or environment variables to provide that new DNS name to your application. A second option is to use an alias or CNAME record in your application, which removes the need to update your application configuration, but requires you to change the value of the alias or CNAME record to point to the new instance. This update would depend on the Route 53 control plane in `us-east-1`.

### Microsoft SQL Server
<a name="microsoft-sql-server"></a>

 Amazon RDS supports [Microsoft SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerMultiAZ.html) by using either SQL Server database mirroring (DBM), Always On Availability Groups (AGs), or block level replication based on the version of SQL Server that you deploy. Each replication option provides a cluster endpoint that’s managed by Amazon RDS and follows the same failover process for Route 53 DNS records as described previously for the other database engines. For Always On AGs, you also have access to the [AG listener endpoint](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/listeners-client-connectivity-application-failover), which returns all of the available IP addresses for the cluster, but only one is active at a time. If you use this endpoint, the client determines which IP address to use with the [MultiSubnetFailover configuration](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/listeners-client-connectivity-application-failover?view=sql-server-ver17#SupportAgMultiSubnetFailover).

 You manage cross-Region failover for distributed Always On AGs through MS SQL Server. You must manually promote the cross-Region replica. Performing this promotion doesn’t rely on the Route 53 control plane. Your application must be configured to write and optionally read from this newly promoted instance.

## Amazon Aurora
<a name="amazon-aurora"></a>

This section provides guidance for the different configuration options available in [Amazon Aurora](https://aws.amazon.com/rds/aurora/).

### Aurora DB clusters
<a name="aurora-db-clusters"></a>

 Aurora database (DB) clusters consist of one or more DB instances and a cluster volume that are deployed across multiple Availability Zones within a Region. There are two types of DB instances, a primary (writer) instance and replica (reader) instances.

 An Aurora DB cluster also provides several types of endpoints for connecting to the database. Each Aurora cluster has a single built-in cluster endpoint that connects to the current primary instance where you can perform reads and writes. It also has a reader endpoint that provides connection-balancing support for read-only connections. If the cluster contains one or more [Aurora Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html), the reader endpoint balances each connection request among the Aurora Replicas. If the cluster only contains a primary instance and no Aurora Replicas, the reader endpoint connects to the primary instance. An instance endpoint connects to a specific DB instance within an Aurora cluster. A custom endpoint for an Aurora cluster represents a set of DB instances that you choose. When you connect to the endpoint, Aurora performs connection balancing and chooses one of the instances in the group to handle the connection.

You can associate a DB instance with more than one custom endpoint. For example, suppose that you add a new DB instance to a cluster, or that Aurora adds a DB instance automatically through [Aurora Auto Scaling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html). In these cases, the DB instance is added to all custom endpoints for which it’s eligible. Which endpoints the DB instance is added to is based on the custom endpoint type of READER or ANY, plus any static or exclusion lists defined for each endpoint.

 Each endpoint is a DNS name that resolves to the appropriate instances in the Aurora DB cluster. Aurora uses a combination of the primary and recovery Route 53 control plane endpoints, Route 53 health checks, and internal services for provisioning and managing Aurora clusters, including primary instance failover and [autoscaling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html). This approach reliably propagates changes to DNS by preventing a single point of failure on the Route 53 control plane in `us-east-1`. If the primary instance in a DB cluster fails, Aurora automatically recovers in one of two ways:
+ By promoting an existing Aurora Replica to the new primary instance
+ If there are no replicas, by replacing the primary instance

For a single DB instance Aurora takes the following steps to recover:

1. The Aurora external monitoring agent detects an unresponsive or failing host

1. A scenario-specific waiting period is observed to prevent false-positives

1. A new Amazon EC2 host is provisioned using the same ENI and monitored until it becomes fully operational

1. The instance connects to the Aurora cluster volume

1. The database engine is started and verified

For a Multi-AZ deployment, Aurora takes the following steps to recover:

1. The Aurora external monitoring agent detects an unresponsive or failing host

1. A scenario-specific waiting period is observed to prevent false-positives

1. A reader replica is chosen for promotion based on a priority you specify and other criteria

1. The selected replica is restarted to become the new primary

1. The Aurora external monitoring agent begins responding to the new primary node’s Route 53 health check as healthy and responds to the Route 53 health checks for the other nodes as unhealthy, resulting in the new primary’s IP address being returned for the cluster endpoint

### Amazon Aurora Global Database
<a name="amazon-aurora-global-database"></a>

 With the Amazon Aurora Global Database feature, you set up multiple Aurora DB clusters that span multiple AWS Regions. An Aurora global database has a primary DB cluster in one Region where the writer instance is located, and up to 10 secondary DB clusters in different Regions that support only reader instances. A secondary cluster can be promoted to primary using [switchover or failover](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html), which moves the primary writer instance to that cluster.

Each Aurora Global Database has three types of endpoints.
+ **Global writer** – The single read/write endpoint that points to the current writer DB instance for the global database cluster. This endpoint is automatically updated when a replica cluster takes over as primary or the primary writer changes within a cluster.
+ **Writer** – The connection endpoint for read/write requests to the primary DB instance in each DB cluster. Using this endpoint for a replica cluster will result in failed writes because it doesn’t have an active writer instance.
+ **Reader** – The connection endpoint for read-only requests in each DB cluster in the global database cluster. To minimize latency, choose whichever reader endpoint is in your AWS Region or the AWS Region closest to your application.

When your primary DB instance is impacted, Aurora takes the same steps to recover or failover the primary instance to another instance in the same Region as described above. You can also choose to manually invoke a switchover or failover to an Aurora cluster in a different Region as part of your multi-Region failover. When you perform this failover, Aurora reliably updates the global writer endpoint to the new primary writer node using the same combination of the primary and recovery Route 53 endpoints, Route 53 health checks, and internal services. These updates are performed asynchronously and you are notified through [events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Messages.html#USER_Events.Messages.cluster) when the failover operation completes and when the global writer endpoint is updated. [Switchover](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-disaster-recovery.managed-failover) is a controlled scenario that prevents data loss and maintains the existing replication topology. It requires the primary and secondary clusters are healthy and available. In the case of an unplanned service disruption, a switchover might not work and you can instead use a [failover](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-failover) to recover. Managed failover doesn’t require the old primary to be healthy and can succeed if it’s unavailable. It’s the recommended approach and maintains the original cluster topology by automatically adding the old primary cluster as a secondary when it becomes available again. Manual failover can be used if managed failover isn’t an option. The failover commands should be run and target resources in the secondary Region.

### Amazon Aurora Serverless v2
<a name="amazon-aurora-serverless-v2"></a>

Failover and instance recovery works the same way as provisioned Aurora DB clusters and has the same dependencies on the Route 53 control plane.

### Amazon Aurora DSQL
<a name="amazon-aurora-dsql"></a>

 Amazon Aurora DSQL is a serverless, distributed relational database service optimized for transactional workloads. Each component in a DSQL cluster provides redundancy across three Availability Zones, with automatic cluster scaling and self-healing in case of component failures. You can configure both single-Region and multi-Region clusters. Aurora DSQL fully automates cluster recovery, which eliminates the need for traditional primary-secondary failover operations. Multi-Region clusters provide two active Regional endpoints that clients can read or write to indiscriminately in either Region.

 Provisioning new Aurora DSQL clusters does depend on the Route 53 control plane in `us-east-1`, which includes restoring a backup. If you choose to use a backup and restore multi-Region strategy where you restore a backup of a single Region cluster to a different Region, this approach might not work if the Route 53 control plane is unavailable. For multi-Region resilience with Aurora DSQL, we recommend you deploy multi-Region clusters. After provisioning, Aurora DSQL clusters have no dependencies on Route 53 for runtime operations or recovery from cluster-level failures.

## AWS IAM Identity Center
<a name="aws-iam-identity-center"></a>

 The [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center) control plane consists of all public APIs provided by the service. Some of these operations have a dependency on the IAM control plane and the AWS Organizations control plane, both of which are in `us-east-1`. Permission set provisioning creates IAM policies, and creating policies depends on the IAM control plane. If the IAM control plane is unavailable, creating or updating permission sets might fail. The AWS Management Console for IAM Identity Center relies on information about your organization, which depends on the AWS Organizations control plane. If it’s unavailable, the Identity Center console might not load. Creating an instance of Identity Center in any Region also depends on `us-east-1` to help make sure each instance of Identity Center has a globally unique identifier. Finally, if [Amazon Simple Email Service (Amazon SES)](https://aws.amazon.com/ses) isn’t available in the same Region as your Identity Center instance, [Identity Center will call Amazon SES endpoints in a different AWS Region](https://docs.aws.amazon.com/singlesignon/latest/userguide/regions.html#cross-region-calls) to send emails to end users.

 The IAM Identity Center data plane consists of the Identity Center console that’s used to access AWS accounts through the AWS Management Console, AWS CLI, AWS SDK, and AWS managed applications. When you authenticate with Identity Center, it uses the AWS Sign-In service SAML endpoint in the Region where your Identity Center instance is deployed. By default, when using Identity Center to access the AWS Management Console, Identity Center redirects you to the global management console endpoint, [https://console.aws.amazon.com](https://console.aws.amazon.com). This endpoint is hosted redundantly across three Regions and is the right choice in most cases. However, you might want to control which Regions you depend on for AWS access. To use a specific regional console endpoint for a permission set, update the [relay state](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtopermrelaystate.html) for that permission set to use your desired regional endpoint.

 When planning for dependencies on IAM Identity Center during recovery, you shouldn’t depend on control plane operations, particularly creating or updating permission sets or updating Identity Center’s configuration. Identity Center supports deployment across [multiple Regions](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-iam-identity-center.html). If your primary Region is impacted, you can [failover](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-failover.html) to Identity Center in a different Region that you’ve configured. Alternatively, you can implement the [emergency access](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access.html) solution to allow your IdP to federate directly with AWS. In this case, make sure the assertion consumer service (ACS) configured in your IdP is set to use a SAML endpoint in a different Region than where Identity Center is deployed and the relay state is configured to use either the global or a Region-specific management console endpoint. For example, if you deployed Identity Center in `us-east-1`, set the relying party endpoint, also known as the ACS URL, to be `https://us-west-2.signin.aws.amazon.com/saml` and the relay state to be `https://us-west-2.console.aws.amazon.com` in your IdP configuration. This helps make sure the emergency access approach isn’t impacted by the event impacting the Region where Identity Center is deployed. It’s possible that your IdP is also impaired at the same time as Identity Center, perhaps because your IdP also primarily operates in the same Region where you deployed Identity Center. In this case, follow the break-glass guidance for IAM users provided in the best practices for third-party identity providers.
