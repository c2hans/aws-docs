---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/migrating-oracle-workloads-to-outposts-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migrating Oracle workloads to AWS Outposts
<a name="migrating-oracle-workloads-to-outposts-on-aws"></a>

 Customers with physical infrastructure investments like factories, manufacturing plants, warehouses and fulfillment centers often require ultra-low latency and high bandwidth between their local equipment and the ERP modules to ensure business continuity. Running Oracle E-Business Suite on [AWS Outposts](https://aws.amazon.com/outposts/) provides a viable hybrid cloud solution for ERP customers with ultra-low latency requirements, strict data residency requirements, or where there are no in-country regions. Using AWS Outposts, customers have the benefit of a fully-managed infrastructure with many core AWS services available in your data center, with seamless connection to a nearby AWS Region.

 AWS Outposts are a family of fully managed solutions delivering AWS infrastructure and native services to on-premises or edge locations while providing a consistent hybrid cloud experience. AWS Outposts are available in a variety of form factors, from 1U and 2U Outposts servers to 42U Outposts racks, and multiple rack deployments.

![Graphic showing the steps for using AWS Outposts](http://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/outposts-overview.png)

Many AWS services are locally available on Outposts, several of which (Amazon EC2, Amazon EBS, Application Load Balancer, and Amazon S3) are used in the following reference architecture for Oracle ERP on AWS Outposts. Outposts offers any-use EC2 instances for both database and application tier workloads.

![Diagram showing using AWS services on AWS Outposts.](http://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/outposts-local-services.png)

 In addition to the locally offered services, because of the unique network model, EC2 instances on your Outpost can easily access in-region AWS services since the VPC spans both the region and Outpost. It may be convenient to visualize your Outpost as an additional AZ in your Region. Technically, the Outpost will be *attached* to one of the AZs and shares the VPC of the region. EC2 instances on your Outpost uses AWS Nitro-based hardware virtualization that is consistent with in-region virtualization.

![Reference architecture diagram showing deploying Oracle ERP on a single Outpost rack](http://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/deploy-erp-single-outpost-rack.png)

 The Oracle ERP on AWS Outposts reference architecture illustrates a deployment on a single Outpost rack. By using Placement Groups, EC2 instances for both the Application and Database tier reside on separate physical hardware hosts within the rack to protect against node failure.

 The architecture can be enhanced to protect against rack failure by adding additional Outposts. These might be in the same on-premises DC or a nearby collocated facility. Uniquely, an HA or DR environment can be configured to run in-region on AWS.

 An ALB (Application Load Balancer) fronts two application servers. An on-premises load-balancer might also be used to connect to the App tier through the local gateway. The database is protected with Data Guard (Max Protection mode). Synchronous replication to the standby database on the Outpost is viable due to ultra-low latencies ensuring zero data loss in the event of a node failure. Cascading standby databases to in-region EC2 instances are possible and indeed recommended. Backups to Amazon EBS, local Amazon S3 or in-region Amazon S3 are recommended to augment the DR configuration.

![Reference architecture diagram showing using Application Load Balancers](http://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/outposts-with-albs.png)

 The migration methodologies to EC2 instances discussed previously are applicable to AWS Outposts. Due to the likely physical proximity to the current on-premises Oracle E-Business Suite environments, the migration will likely be accelerated due to higher data transfer bandwidth available on the local network.
