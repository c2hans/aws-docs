---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-a-highly-available-peoplesoft-architecture-on-aws.html
---

# Set up a highly available PeopleSoft architecture on AWS
<a name="set-up-a-highly-available-peoplesoft-architecture-on-aws"></a>

*Ramanathan Muralidhar, Amazon Web Services*

## Summary
<a name="set-up-a-highly-available-peoplesoft-architecture-on-aws-summary"></a>

When you migrate your PeopleSoft workloads to AWS, resiliency is an important objective. It ensures that your PeopleSoft application is always highly available and able to recover from failures quickly.

This pattern provides an architecture for your PeopleSoft applications on AWS to ensure high availability (HA) at the network, application, and database tiers. It uses an [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) for Oracle or Amazon RDS for SQL Server database for the database tier. This architecture also includes AWS services such as [Amazon Route 53](https://aws.amazon.com/route53/), [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) Linux instances, [Amazon Elastic Block Storage (Amazon EBS)](https://aws.amazon.com/ebs/), [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/), and an [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer), and is scalable.

[Oracle PeopleSoft](https://www.oracle.com/applications/peoplesoft/) provides a suite of tools and applications for workforce management and other business operations.

## Prerequisites and limitations
<a name="set-up-a-highly-available-peoplesoft-architecture-on-aws-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A PeopleSoft environment with the necessary licenses for setting it up on AWS
+ A virtual private cloud (VPC) set up in your AWS account with the following resources:
  + At least two Availability Zones
  + One public subnet and three private subnets in each Availability Zone
  + A NAT gateway and an internet gateway
  + Route tables for each subnet to route the traffic
  + Network access control lists (network ACLs) and security groups defined to help ensure the security of the PeopleSoft application in accordance with your organization’s standards

**Limitations**
+ This pattern provides a high availability (HA) solution. It doesn’t support disaster recovery (DR) scenarios. In the rare occurrence that the entire AWS Region for the HA implementation goes down, the application will become unavailable.

**Product versions**
+ PeopleSoft applications running PeopleTools 8.52 and later

## Architecture
<a name="set-up-a-highly-available-peoplesoft-architecture-on-aws-architecture"></a>

**Target architecture**

Downtime or outage of your PeopleSoft production application impacts the availability of the application and causes major disruptions to your business.

We recommend that you design your PeopleSoft production application so that it is always highly available. You can achieve this by eliminating single points of failure, adding reliable crossover or failover points, and detecting failures. The following diagram illustrates an HA architecture for PeopleSoft on AWS.

![Highly available architecture for PeopleSoft on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/0db96376-dadb-4545-b130-ebbe64acd4e9/images/5d585a8e-320a-495d-a049-97171633e90f.png)

This architecture deployment uses Amazon RDS for Oracle as the PeopleSoft database, and EC2 instances that are running on Red Hat Enterprise Linux (RHEL). You can also use Amazon RDS for SQL Server as the Peoplesoft database.

This architecture contains the following components:
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) is used as the Domain Name Server (DNS) for routing requests from the internet to the PeopleSoft application.
+ [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) helps you protect against common web exploits and bots that can affect availability, compromise security, or consume excessive resources. [AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) (not illustrated) provides much broader protection.
+ An [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) load-balances HTTP and HTTPS traffic with advanced request routing targeted at the web servers.
+ The web servers, application servers, process scheduler servers, and Elasticsearch servers that support the PeopleSoft application run in multiple Availability Zones and use [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html).
+ The database used by the PeopleSoft application runs on [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) in a Multi-AZ configuration.
+ The file share used by the PeopleSoft application is configured on [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) and is used to access files across instances.
+ [Amazon Machine Images (AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)s) are used by Amazon EC2 Auto Scaling to ensure that PeopleSoft components are cloned quickly when needed.
+ The [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) connect instances in a private subnet to services outside your VPC, and ensure that external services cannot initiate a connection with those instances.
+ The [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet.
+ The bastion hosts in the public subnet provide access to the servers in the private subnet from an external network, such as the internet or on-premises network. The bastion hosts provide controlled and secure access to the servers in the private subnets.

**Architecture details**

The PeopleSoft database is housed in an Amazon RDS for Oracle (or Amazon RDS for SQL Server) database in a Multi-AZ configuration. The [Amazon RDS Multi-AZ feature](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) replicates database updates across two Availability Zones to increase durability and availability. Amazon RDS automatically fails over to the standby database for planned maintenance and unplanned disruptions.

The PeopleSoft web and middle tier are installed on EC2 instances. These instances are spread across multiple Availability Zones and tied by an [Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html). This ensures that these components are always highly available. A minimum number of required instances are maintained to ensure that the application is always available and can scale when required.

We recommend that you use a current generation EC2 instance type for the OEM EC2 instances. Current generation instance types, such as [instances built on the AWS Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances), support hardware virtual machines (HVMs). The HVM AMIs are required to take advantage of [enhanced networking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html), and they also offer increased security. The EC2 instances that are part of each Auto Scaling group use their own AMI when replacing or scaling up instances. We recommend that you select EC2 instance types based on the load you want your PeopleSoft application to handle and the minimum values recommended by Oracle for your PeopleSoft application and PeopleTools release. For more information about hardware and software requirements, see the [Oracle support website](https://support.oracle.com).

The PeopleSoft web and middle tier share an Amazon EFS mount to share reports, data files, and (if needed) the `PS_HOME` directory. Amazon EFS is configured with mount targets in each Availability Zone for performance and cost reasons.

An Application Load Balancer is provisioned to support the traffic that accesses the PeopleSoft application and load-balances the traffic among the web servers across different Availability Zones. An Application Load Balancer is a network device that provides HA in at least two Availability Zones. The web servers distribute the traffic to different application servers by using a load balancing configuration. Load balancing among the web server and application server ensures that load is distributed evenly across the instances, and helps avoid bottlenecks and service disruptions due to overloaded instances.

Amazon Route 53 is used as the DNS service to route traffic to the Application Load Balancer from the internet. Route 53 is a highly available and scalable DNS web service.

**HA details**
+ Databases: The Multi-AZ feature of Amazon RDS operates two databases in multiple Availability Zones with synchronous replication. This creates a highly available environment with automatic failover. Amazon RDS has failover event detection and initiates automated failover when these events occur. You can also initiate manual failover through the Amazon RDS API. For a detailed explanation, see the blog post [Amazon RDS Under The Hood: Multi-AZ](https://aws.amazon.com/blogs/database/amazon-rds-under-the-hood-multi-az/). The failover is seamless and the application automatically reconnects to the database when it happens. However, any process scheduler jobs during the failover generate errors and have to be resubmitted.
+ PeopleSoft application servers: The application servers are spread across multiple Availability Zones and have an Auto Scaling group defined for them. If an instance fails, the Auto Scaling group immediately replaces it with a healthy instance that’s cloned from the AMI of the application server template. Specifically, *jolt pooling* is enabled, so when an application server instance goes down, the sessions automatically fail over to another application server, and the Auto Scaling group automatically spins up another instance, brings up the application server, and registers it in the Amazon EFS mount. The newly created application server is automatically added to the web servers by using the `PSSTRSETUP.SH` script in the web servers. This ensures that the application server is always highly available and recovers from failure quickly.
+ Process schedulers: The process schedulers servers are spread across multiple Availability Zones and have an Auto Scaling group defined for them. If an instance fails, the Auto Scaling group immediately replaces it with a healthy instance that’s cloned from the AMI of the process scheduler server template. Specifically, when a process scheduler instance goes down, the Auto Scaling group automatically spins up another instance and brings up the process scheduler. Any jobs that were running when the instance failed must be resubmitted. This ensures that the process scheduler is always highly available and recovers from failure quickly.
+ Elasticsearch servers: The Elasticsearch servers have an Auto Scaling group defined for them. If an instance fails, the Auto Scaling group immediately replaces it with a healthy instance that’s cloned from the AMI of the Elasticsearch server template. Specifically, when an Elasticsearch instance goes down, the Application Load Balancer that serves requests to it detects the failure and stops sending traffic to it. The Auto Scaling group automatically spins up another instance and brings up the Elasticsearch instance. When the Elasticsearch instance is back up, the Application Load Balancer detects that it’s healthy and starts sending requests to it again. This ensures that the Elasticsearch server is always highly available and recovers from failure quickly.
+ Web servers: The web servers have an Auto Scaling group defined for them. If an instance fails, the Auto Scaling group immediately replaces it with a healthy instance that’s cloned from the AMI of the web server template. Specifically, when a web server instance goes down, the Application Load Balancer that serves requests to it detects the failure and stops sending traffic to it. The Auto Scaling group automatically spins up another instance and brings up the web server instance. When the web server instance is back up, the Application Load Balancer detects that it’s healthy and starts sending requests to it again. This ensures that the web server is always highly available and recovers from failure quickly.

## Tools
<a name="set-up-a-highly-available-peoplesoft-architecture-on-aws-tools"></a>

**AWS services**
+ [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/) distribute incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones.
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) provides block-level storage volumes for use with Amazon Elastic Compute Cloud (Amazon EC2) instances.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) helps you create and configure shared file systems in the AWS Cloud.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) is a highly available and scalable DNS web service.

## Best practices
<a name="set-up-a-highly-available-peoplesoft-architecture-on-aws-best-practices"></a>

**Operational best practices**
+ When you run PeopleSoft on AWS, use Route 53 to route the traffic from the internet and locally. Use the [failover option](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html) to reroute traffic to the disaster recovery (DR) site if the primary DB instance isn’t available.
+ Always use an Application Load Balancer in front of the PeopleSoft environment. This ensures that traffic is load-balanced to the web servers in a secure fashion.
+ In the Application Load Balancer target group settings, make sure that [stickiness is turned on](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/sticky-sessions.html) with a load balancer generated cookie.
**Note**
You might need to use an application-based cookie if you use external single sign-on (SSO). This ensures that connections are consistent across the web servers and application servers.
+ For a PeopleSoft production application, the Application Load Balancer idle timeout must match what is set in the web profile you use. This prevents user sessions from expiring at the load balancer layer.
+ For a PeopleSoft production application, set the application server [recycle count](https://docs.oracle.com/cd/F28299_01/pt857pbr3/eng/pt/tsvt/concept_PSAPPSRVOptions-c07f06.html?pli=ul_d96e90_tsvt) to a value that minimizes memory leaks.
+ If you’re using an Amazon RDS database for your PeopleSoft production application, as described in this pattern, run it in [Multi-AZ format for high availability](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).
+ If your database is running on an EC2 instance for your PeopleSoft production application, make sure that a [standby database is running on another Availability Zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/ec2-oracle.html#ec2-oracle-ha) for high availability.
+ For DR, make sure that your Amazon RDS database or EC2 instance has a standby configured in a separate AWS Region from the production database. This ensures that in event of a disaster in the Region, you can switch the application over to another Region.
+ For DR, use [Amazon Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) to set up application-level components in a separate Region from production components. This ensures that in the event of a disaster in the Region, you can switch the application over to another Region.
+ Use Amazon EFS (for moderate I/O requirements) or [Amazon FSx](https://aws.amazon.com/fsx/) (for high I/O requirements) to store your PeopleSoft reports, attachments, and data files. This ensures that the content is stored in one central location and can be accessed from anywhere within the infrastructure.
+ Use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) (basic and detailed) to monitor the AWS Cloud resources that your PeopleSoft application is using in near real time. This ensures that you are alerted of issues instantly and can address them quickly before they affect the availability of the environment.
+ If you’re using an Amazon RDS database as the PeopleSoft database, use [Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.overview.html). This feature provides access to over 50 metrics, including CPU, memory, file system I/O, and disk I/O.
+ Use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) to monitor API calls on the AWS resources that your PeopleSoft application is using. This helps you perform security analysis, resource change tracking, and compliance auditing.

**Security best practices**
+ To protect your PeopleSoft application from common exploits such as SQL injection or cross-site scripting (XSS), use [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). Consider using [AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) for tailored detection and mitigation services.
+ Add a rule to the Application Load Balancer to redirect traffic from HTTP to HTTPS automatically to help secure your PeopleSoft application.
+ Set up a separate security group for the Application Load Balancer. This security group should allow only HTTPS/HTTP inbound traffic and no outbound traffic. This ensures that only intended traffic is allowed and helps secure your application.
+ Use private subnets for the application servers, web servers, and database, and use [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) for outbound internet traffic. This ensures that the servers that support the application aren’t reachable publicly, while providing public access only to the servers that need it.
+ Use different VPCs to run your PeopleSoft production and non-production environments. Use [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/), [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html), [network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), and [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) to control the traffic flow between the [VPC](https://aws.amazon.com/vpc/)s and, if necessary, your on-premises data center.
+ Follow the principle of least privilege. Grant access to the AWS resources used by the PeopleSoft application only to users who absolutely need it. Grant only the minimum privileges required to perform a task. For more information, see the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html) of the AWS Well-Architected Framework.
+ Wherever possible, use [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) to access the EC2 instances that the PeopleSoft application uses.

**Reliability best practices**
+ When you use an Application Load Balancer, register a single target for each enabled Availability Zone. This makes the load balancer most effective.
+ We recommend that you have three distinct URLs for each PeopleSoft production environment: one URL to access the application, one to serve the integration broker, and one to view reports. If possible, each URL should have its own dedicated web servers and application servers. This design helps make your PeopleSoft application more secure, because each URL has a distinct functionality and controlled access. It also minimizes the scope of impact if the underlying services fail.
+ We recommend that you configure [health checks on the load balancer target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html) for your PeopleSoft application. The health checks should be performed on the web servers instead of the EC2 instances running those servers. This ensures that if the web server crashes or the EC2 instance that hosts the web server goes down, the Application Load Balancer reflects that information accurately.
+ For a PeopleSoft production application, we recommend that you spread the web servers across at least three Availability Zones. This ensures that the PeopleSoft application is always highly available even if one of the Availability Zones goes down.
+ For a PeopleSoft production application, enable jolt pooling (`joltPooling=true`). This ensures that your application fails over to another application server if a server is down for patching purposes or because of a VM failure.
+ For a PeopleSoft production application, set `DynamicConfigReload `to 1. This setting is supported in PeopleTools version 8.52 and later. It adds new application servers to the web server dynamically, without restarting the servers.
+ To minimize downtime when you apply PeopleTools patches, use the blue/green deployment method for your Auto Scaling group launch configurations for the web and application servers. For more information, see the [Overview of deployment options on AWS](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/bluegreen-deployments.html) whitepaper.
+ Use [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) to back up your PeopleSoft application on AWS. AWS Backup is a cost-effective, fully managed, policy-based service that simplifies data protection at scale.

**Performance best practices**
+ Terminate the SSL at the Application Load Balancer for optimal performance of the PeopleSoft environment, unless your business requires encrypted traffic throughout the environment.
+ Create [interface VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) for AWS services like such as [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) and [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) so that traffic is always internal. This is cost-effective and helps keep your application secure.

**Cost optimization best practices**
+ Tag all the resources used by your PeopleSoft environment, and enable [cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html). These tags help you view and manage your resource costs.
+ For a PeopleSoft production application, set up Auto Scaling groups for the web servers and the application servers. This maintains a minimal number of web and application servers to support your application. You can use [Auto Scaling group policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html) to scale the the servers up and down as required.
+ Use [billing alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html) to get alerts when costs exceed a budget threshold that you specify.

**Sustainability best practices**
+ Use [infrastructure as code](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html) (IaC) to maintain your PeopleSoft environments. This helps you build consistent environments and maintain change control.

## Epics
<a name="set-up-a-highly-available-peoplesoft-architecture-on-aws-epics"></a>

### Migrate your PeopleSoft database to Amazon RDS
<a name="migrate-your-peoplesoft-database-to-amazon-rds"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a DB subnet group. | On the [Amazon RDS console](https://console.aws.amazon.com/rds/), in the navigation pane, choose **Subnet groups**, and then create an Amazon RDS DB subnet group with subnets in multiple Availability Zones. This is required for the Amazon RDS database to run in a Multi-AZ configuration. | Cloud administrator |
| Create the Amazon RDS database. | Create an Amazon RDS database in an Availability Zone of the AWS Region you selected for the PeopleSoft HA environment. When you create the Amazon RDS database, make sure to select the Multi-AZ option (**Create a standby instance**) and the database subnet group you created in the previous step. For more information, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html). | Cloud administrator, Oracle database administrator |
| Migrate your PeopleSoft database to Amazon RDS. | Migrate your existing PeopleSoft database into the Amazon RDS database by using AWS Database Migration Service (AWS DMS). For more information, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html) and the AWS blog post [Migrating Oracle databases with near-zero downtime using AWS DMS](https://aws.amazon.com/blogs/database/migrating-oracle-databases-with-near-zero-downtime-using-aws-dms/). | Cloud administrator, PeopleSoft DBA |

### Set up your Amazon EFS file system
<a name="set-up-your-amazon-efs-file-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a file system. | On the [Amazon EFS console](https://console.aws.amazon.com/efs/), create a file system and mount targets for each Availability Zone. For instructions, see the [Amazon EFS documentation](https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html#creating-using-fs-part1-console). When the file system has been created, note its DNS name. You will use this information when you mount the file system. | Cloud administrator |

### Set up your PeopleSoft application and file system
<a name="set-up-your-peoplesoft-application-and-file-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch an EC2 instance. | Launch an EC2 instance for your PeopleSoft application. For instructions, see the [Amazon EC2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html#liw-quickly-launch-instance).+ For **Name**, enter `APP_TEMPLATE`.<br />+ For **OS images**, choose **Red Hat**.<br />+ For **Instance type**, choose the instance type that’s appropriate for your PeopleSoft application. For more information, see *Architecture details* in the [Architecture](#set-up-a-highly-available-peoplesoft-architecture-on-aws-architecture) section. | Cloud administrator, PeopleSoft administrator |
| Install PeopleSoft on the instance. | Install your PeopleSoft application and PeopleTools on the EC2 instance you created. For instructions, see the [Oracle documentation](https://docs.oracle.com). | Cloud administrator, PeopleSoft administrator |
| Create the application server. | Create the application server for the AMI template and make sure that it connects successfully to the Amazon RDS database. | Cloud administrator, PeopleSoft administrator |
| Mount the Amazon EFS file system. | Log in to the EC2 instance as the root user and run the following commands to mount the Amazon EFS file system to a folder called `PSFTMNT` on the server.<pre>sudo su –<br />mkdir /psftmnt<br />cat /etc/fstab</pre><br />Append the following line to the `/etc/fstab` file. Use the DNS name you noted when you created the file system.<pre>fs-09e064308f1145388.efs.us-east-1.amazonaws.com:/ /psftmnt nfs4 nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport,_netdev 0 0<br />mount -a</pre> | Cloud administrator, PeopleSoft administrator |
| Check permissions. | Make sure that the `PSFTMNT` folder has the proper permissions so that the PeopleSoft user can access it properly. | Cloud administrator, PeopleSoft administrator |
| Create additional instances. | Repeat the previous steps in this epic to create template instances for the process scheduler, web server, and Elasticsearch server. Name these instances `PRCS_TEMPLATE`, `WEB_TEMPLATE`, and `SRCH_TEMPLATE`. For the web server, set `joltPooling=true`** **and `DynamicConfigReload=1`. | Cloud administrator, PeopleSoft administrator |

### Create scripts to set up servers
<a name="create-scripts-to-set-up-servers"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a script to install the application server. | In the Amazon EC2 `APP_TEMPLATE` instance, as the PeopleSoft user, create the following script. Name it `appstart.sh` and place it in the `PS_HOME` directory. You will use this script to bring up the application server and also record the server name on the Amazon EFS mount.<pre>#!/bin/ksh<br />. /usr/homes/hcmdemo/.profile.<br />psadmin -c configure -d HCMDEMO<br />psadmin -c parallelboot -d HCMDEMO<br />touch /psftmnt/`echo $HOSTNAME`</pre> | PeopleSoft administrator |
| Create a script to install the process scheduler server. | In the Amazon EC2 `PRCS_TEMPLATE` instance, as the PeopleSoft user, create the following script. Name it `prcsstart.sh` and place it in the `PS_HOME` directory. You will use this script to bring up the process scheduler server.<pre>#!/bin/ksh<br />. /usr/homes/hcmdemo/. profile<br />/* The following line ensures that the process scheduler always has a unique name during replacement or scaling activity. */ <br />sed -i "s/.*PrcsServerName.*/`hostname -I | awk -F. '{print "PrcsServerName=PSUNX"$3$4}'`/" $HOME/appserv/prcs/*/psprcs.cfg<br />psadmin -p configure -d HCMDEMO<br />psadmin -p start -d HCMDEMO</pre> | PeopleSoft administrator |
| Create a script to install the Elasticsearch server. | In the Amazon EC2 `SRCH_TEMPLATE` instance, as the Elasticsearch user, create the following script. Name it `srchstart.sh` and place it in the `HOME` directory.<pre>#!/bin/ksh<br />/* The following line ensures that the correct IP is indicated in the elasticsearch.yaml file. */<br />sed -i "s/.*network.host.*/`hostname  -I | awk '{print "host:"$0}'`/" $ES_HOME_DIR/config/elasticsearch.yaml<br />nohup $ES_HOME_DIR/bin/elasticsearch &</pre> | PeopleSoft administrator |
| Create a script to install the web server. | In the Amazon EC2 `WEB_TEMPLATE` instance, as the web server user, create the following scripts in the `HOME` directory.<br />`renip.sh`: This script ensures that the web server has the correct IP when cloned from the AMI.<pre>#!/bin/ksh<br />hn=`hostname`<br />/* On the following line, change the IP with the hostname with the hostname of the web template. */<br />for text_file in `find  *  -type f -exec grep -l '<hostname-of-the-web-template>' {} \;`<br />do<br />sed -e 's/<hostname-of-the-web-template>/'$hn'/g' $text_file > temp<br />mv -f temp $text_file<br />done</pre><br />`psstrsetup.sh`: This script ensures that the web server uses the correct application server IPs that are currently running. It tries to connect to each application server on the jolt port and adds it to the configuration file.<pre>#!/bin/ksh<br />c2=""<br />for ctr in `ls -1 /psftmnt/*.internal`<br />do<br />c1=`echo $ctr | awk -F "/" '{print $3}'`<br />/* In the following lines, 9000 is the jolt port. Change it if necessary. */<br />if nc -z $c1 9000 2> /dev/null; then<br />if [[ $c2 = "" ]]; then<br />c2="psserver="`echo $c1`":9000"<br />else<br />c2=`echo $c2`","`echo $c1`":9000"<br />fi<br />fi<br />done</pre><br />`webstart.sh`: This script runs the two previous scripts and starts the web servers.<pre>#!/bin/ksh<br />/* Change the path in the following if necessary. */<br />cd  /usr/homes/hcmdemo <br />./renip.sh<br />./psstrsetup.sh<br />webserv/peoplesoft/bin/startPIA.sh</pre> | PeopleSoft administrator |
| Add a crontab entry. | In the Amazon EC2 `WEB_TEMPLATE` instance, as the web server user, add the following line to **crontab**. Change the time and path to reflect the values you need. This entry ensures that your web server always has the correct application server entries in the `configuration.properties` file.<pre>* * * * * /usr/homes/hcmdemo/psstrsetup.sh</pre> | PeopleSoft administrator |

### Create AMIs and Auto Scaling group templates
<a name="create-amis-and-auto-scaling-group-templates"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AMI for the application server template. | On the Amazon EC2 console, create an AMI image of the Amazon EC2 `APP_TEMPLATE` instance. Name the AMI `PSAPPSRV-SCG-VER1`. For instructions, see the [Amazon EC2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html). | Cloud administrator, PeopleSoft administrator |
| Create AMIs for the other servers. | Repeat the previous step to create AMIs for the process scheduler, Elasticsearch server, and web server. | Cloud administrator, PeopleSoft administrator |
| Create a launch template for the application server Auto Scaling group. | Create a launch template for the application server Auto Scaling group. Name the template `PSAPPSRV_TEMPLATE.` In the template, choose the AMI you created for the `APP_TEMPLATE` instance. For instructions, see the [Amazon EC2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#create-launch-template-from-instance).+ In the launch template, select the instance type based on your requirements.<br />+ In the **User data** field of the **Advanced details** section, add the following entries. Make sure that the path and user information are correct. You created the `appstart.sh` script in a previous step.<pre>#! /bin/ksh<br />su -c "/usr/homes/hcmdemo/appstart.sh" - hcmdemo</pre> | Cloud administrator, PeopleSoft administrator |
| Create a launch template for the process scheduler server Auto Scaling group. | Repeat the previous step to create a launch template for the process scheduler server Auto Scaling group. Name the template `PSPRCS_TEMPLATE`. In the template, choose the AMI you created for the process scheduler.+ In the **User data** field of the **Advanced details** section, add the following entries. Make sure that the path and user information are correct. You created the `prcsstart.sh` script in a previous step.<pre>#! /bin/ksh<br />su -c "/usr/homes/hcmdemo/prcsstart.sh" - hcmdemo</pre> | Cloud administrator, PeopleSoft administrator |
| Create a launch template for the Elasticsearch server Auto Scaling group. | Repeat the previous steps to create a launch template for the Elasticsearch server Auto Scaling group. Name the template `SRCH_TEMPLATE`. In the template, choose the AMI you created for the search server.+ In the **User data** field of the **Advanced details** section, add the following entries. Make sure that the path and user information are correct. You created the `srchstart.sh` script in a previous step.<pre>#! /bin/ksh<br />su -c "/usr/homes/essearch/srchstart.sh" - essearch</pre> | Cloud administrator, PeopleSoft administrator |
| Create a launch template for the web server Auto Scaling group. | Repeat the previous steps to create a launch template for the web server Auto Scaling group. Name the template `WEB_TEMPLATE`. In the template, choose the AMI you created for the web server.+ In the **User data** field of the **Advanced details** section, add the following entries. Make sure that the path and user information are correct. You created the `webstart.sh` script in a previous step.<pre>#! /bin/ksh<br />su -c "/usr/homes/hcmdemo/webstart.sh" - hcmdemo</pre> | Cloud administrator, PeopleSoft administrator |

### Create Auto Scaling groups
<a name="create-auto-scaling-groups"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Auto Scaling group for the application server. | On the Amazon EC2 console, create an Auto Scaling group called `PSAPPSRV_ASG` for the application server by using the `PSAPPSRV_TEMPLATE` template. For instructions, see the [Amazon EC2 documentation](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html).+ On the **Choose instance launch options** page, select the correct VPC and then select multiple subnets from different Availability Zones.<br />+ On the **Configure advanced options** page, do not select a load balancer.<br />+ On the **Configure group size and scaling policies** page, choose settings depending on how much load you want to architect your system for and whether you want to use a scaling policy. We recommend that you set the desired and minimum capacity to 2 at a minimum so that at least one instance is available to service the traffic at any point in time. For more information about Auto Scaling policies, see the [Amazon EC2 documentation](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-your-group.html). | Cloud administrator, PeopleSoft administrator |
| Create Auto Scaling groups for the other servers. | Repeat the previous step to create Auto Scaling groups for the process scheduler, Elasticsearch server, and web server. | Cloud administrator, PeopleSoft administrator |

### Create and configure target groups
<a name="create-and-configure-target-groups"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a target group for the web server. | On the Amazon EC2 console, create a target group for the web server. For instructions, see the [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-target-group.html). Set the port to the port that the web server is listening on. | Cloud administrator |
| Configure health checks. | Confirm that the health checks have the correct values to reflect your business requirements. For more information, see the [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html). | Cloud administrator |
| Create a target group for the Elasticsearch server. | Repeat the previous steps to create a target group called `PSFTSRCH` for the Elasticsearch server, and set the correct Elasticsearch port. | Cloud administrator |
| Add target groups to Auto Scaling groups. | Open the web server Auto Scaling group called `PSPIA_ASG` that you created earlier. On the **Load balancing** tab, choose **Edit** and then add the `PSFTWEB` target group to the Auto Scaling group.<br />Repeat this step for the Elasticsearch Auto Scaling group `PSSRCH_ASG` to add the target group `PSFTSRCH` you created earlier. | Cloud administrator |
| Set session stickiness. | In the target group `PSFTWEB`, choose the **Attributes** tab, choose **Edit**, and set the session stickiness. For stickiness type, choose **Load balancer generated cookie**, and set the duration to 1. For more information, see the [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/sticky-sessions.html).<br />Repeat this step for the target group `PSFTSRCH`. | Cloud administrator |

### Create and configure application load balancers
<a name="create-and-configure-application-load-balancers"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a load balancer for the web servers. | Create an Application Load Balancer named `PSFTLB` to load-balance traffic to the web servers. For instructions, see the [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html#configure-load-balancer).+ Provide the load balancer name.<br />+ For **Scheme**, choose **Internet-facing**.<br />+ In the **Network mapping** section, select the correct VPC and at least two public subnets from different Availability Zones.<br />+ In the **Listeners and routing** section, select the target group `PSFTWEB` and specify the correct protocol and port number. | Cloud administrator |
| Create a load balancer for the Elasticsearch servers. | Create an Application Load Balancer named `PSFTSCH` to load-balance traffic to the Elasticsearch servers.+ Provide the load balancer name.<br />+ For **Scheme**, choose **Internal**.<br />+ In the **Network mapping** section, select the correct VPC and private subnets.<br />+ In the **Listeners and routing** section, select the target group `PSFTSRCH` and specify the correct protocol and port number. | Cloud administrator |
| Configure Route 53. | On the [Amazon Route 53 console](https://console.aws.amazon.com/route53/), create a record in the hosted zone that will service the PeopleSoft application. For instructions, see the [Amazon Route 53 documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html). This ensures that all the traffic passes through the `PSFTLB` load balancer. | Cloud administrator |

## Related resources
<a name="set-up-a-highly-available-peoplesoft-architecture-on-aws-resources"></a>
+ [Oracle PeopleSoft website](https://www.oracle.com/applications/peoplesoft/)
+ [AWS documentation](https://docs.aws.amazon.com)
