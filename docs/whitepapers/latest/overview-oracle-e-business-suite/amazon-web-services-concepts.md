---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-oracle-e-business-suite/amazon-web-services-concepts.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon Web Services concepts
<a name="amazon-web-services-concepts"></a>

 This section describes the AWS infrastructure and services that are part of the reference architecture for running Oracle E-Business Suite on AWS.

## Regions and Availability Zones
<a name="regions-and-availability-zones"></a>

 Each [Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) is a separate geographic area isolated from the other Regions. Regions provide you the ability to place resources, such as Amazon Elastic Compute Cloud (Amazon EC2) instances, and data in multiple locations. Resources aren't replicated across Regions unless you do so specifically.

 An AWS account provides multiple Regions so you can launch your application in locations that meet your requirements. For example, you might want to launch your application in Europe to be closer to your European customers, or to meet legal requirements.

 Each Region has multiple, isolated locations known as Availability Zones. Each Availability Zone runs on its own physically distinct, independent infrastructure, and is engineered to be highly reliable. Common points of failure, such as generators and cooling equipment, are not shared across Availability Zones. Because Availability Zones are physically separate, even extremely uncommon disasters such as fires, tornados or flooding would only affect a single Availability Zone. Each Availability Zone is isolated, but the Availability Zones in a Region are connected through low-latency links. The following figure illustrates the relationship between Regions and Availability Zones.

![Diagram showing the relationship between AWS Regions and Availability Zones](https://docs.aws.amazon.com/whitepapers/latest/overview-oracle-e-business-suite/images/regions-and-avaliability-zones.png)

 The following figure shows the Regions and the number of Availability Zones in each Region provided by an AWS account at the time of this publication. For the most current list of Regions and Availability Zones, see [Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

**Note**
You can’t describe or access additional Regions from the AWS GovCloud (US) Region or China (Beijing) Region.

![Map of AWS Regions and Availability Zones](https://docs.aws.amazon.com/whitepapers/latest/overview-oracle-e-business-suite/images/map-of-regions-and-availability-zones.png)

## Amazon Elastic Compute Cloud (Amazon EC2)
<a name="amazon-elastic-compute-cloud-amazon-ec2"></a>

 [Amazon EC2](https://aws.amazon.com/ec2/) is a web service that provides resizable compute capacity in the cloud, billed by the hour or second (minimum of 60 seconds). You can run virtual machines (EC2 instances) ranging in size from one vCPU and 0.5 GB memory, to 448 vCPU and 24 TB memory. You have a choice of operating systems including Windows Server 2008/2012/2016/2019, Oracle Linux, Red Hat Enterprise Linux, and SUSE Linux.

## Amazon RDS Custom for Oracle
<a name="amazon-rds-custom-for-oracle"></a>

 [Amazon RDS Custom](https://aws.amazon.com/rds/custom/) brings the benefits of Amazon RDS to a market that can't easily move to a fully managed service because of customizations that are required with third-party applications. Amazon RDS Custom for Oracle automates setup, operation, and scaling of databases in the cloud while granting access to the database and underlying operating system to configure settings, install patches, and enable native features to meet the dependent application's requirements. Through the time-saving benefits of a managed service, Amazon RDS Custom for Oracle allows valuable resources to focus on more important business-impacting, strategic activities.

## Elastic Load Balancing
<a name="elastic-load-balancing"></a>

 [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) automatically distributes incoming application traffic across multiple Amazon EC2 instances, containers, and IP addresses, in one or more Availability Zones on AWS Cloud. It enables you to achieve greater levels of fault tolerance in your applications, seamlessly providing the required amount of load balancing capacity needed to distribute application traffic. Elastic Load Balancing can be used for load balancing web server traffic.

## Amazon Elastic Block Store (Amazon EBS)
<a name="amazon-elastic-block-store-amazon-ebs"></a>

 [Amazon EBS](https://aws.amazon.com/ebs/) provides persistent block level storage volumes for use with EC2 instances in the AWS Cloud. Each Amazon EBS volume is automatically replicated within its Availability Zone to protect you from component failure, offering high availability and durability. EBS volumes offer the consistent and low-latency performance needed to run your workloads.

## Amazon Machine Image (AMI)
<a name="amazon-machine-image-ami"></a>

 An [Amazon Machine Image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (AMI) is simply a packaged-up environment that includes all the necessary bits to set up and boot your instance. Your AMIs are your unit of deployment. Amazon EC2 uses Amazon EBS and Amazon Simple Storage Service (Amazon S3) to provide reliable, scalable storage of your AMIs so they can boot when you need them.

## Amazon Simple Storage Service (Amazon S3)
<a name="amazon-simple-storage-service-amazon-s3"></a>

 [Amazon S3](https://aws.amazon.com/s3/) provides developers and IT teams with secure, durable, highly scalable object storage. Amazon S3 is easy to use. It provides a simple web services interface you can use to store and retrieve any amount of data from anywhere on the web. With Amazon S3, you pay only for the storage you actually use. There is no minimum fee and no setup cost.

## Amazon Route 53
<a name="amazon-route-53"></a>

 [Amazon Route 53](https://aws.amazon.com/route53/) is a highly available and scalable cloud Domain Name System (DNS) web service. It is designed to give developers and businesses an extremely reliable and cost-effective way to route end users to internet applications by translating names like www.example.com into the numeric IP address.

## Amazon Virtual Private Cloud (Amazon VPC)
<a name="amazon-virtual-private-cloud-amazon-vpc"></a>

 [Amazon VPC](https://aws.amazon.com/vpc/) enables you to provision a logically isolated section of the AWS Cloud, in which you can launch AWS resources in a virtual network that you define. You have complete control over your virtual networking environment, including selection of your own private IP address range, creation of subnets, and configuration of route tables and network gateways.

 You can use multiple layers of security, including security groups and network access control lists, to help control access to EC2 instances in each subnet. Additionally, you can create a Hardware Virtual Private Network (VPN) connection between your corporate data center and your VPC and use the AWS Cloud as an extension of your corporate data center.

## Amazon Elastic File System (Amazon EFS)
<a name="amazon-elastic-file-system-amazon-efs"></a>

 [Amazon EFS](https://aws.amazon.com/efs/) is a file storage service for EC2 instances. Amazon EFS supports the NFS v4 protocol, so the applications and tools that you use today work seamlessly with Amazon EFS. Multiple EC2 instances can access an Amazon EFS file system at the same time, providing a common data source for workloads and applications running on more than one instance. With Amazon EFS, storage capacity is elastic, growing and shrinking automatically as you add and remove files, so your applications have the storage they need, when they need it.

## AWS security and compliance
<a name="aws-security-and-compliance"></a>

 The AWS Cloud security infrastructure has been architected to be one of the most flexible and secure cloud computing environments available today. Security on AWS is very similar to security in your on-premises data center—but without the costs and complexities involved in protecting facilities and hardware. AWS provides a secure global infrastructure, plus a range of features that you can use to help secure your systems and data in the cloud. To learn more, see [AWS Cloud Security](https://aws.amazon.com/security/).

 AWS compliance enables customers to understand the robust controls in place at AWS to maintain security and data protection in the cloud. AWS engages with external certifying bodies and independent auditors to provide customers with extensive information regarding the policies, processes, and controls established and operated by AWS.

 To learn more, see [AWS Compliance](https://aws.amazon.com/compliance/).
