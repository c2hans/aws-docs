---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/infrastructure-description-and-controls.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Infrastructure Description and Controls
<a name="infrastructure-description-and-controls"></a>

## Cloud Models (Nature of the Cloud)
<a name="cloud-models-nature-of-the-cloud"></a>

 Cloud computing is the on-demand delivery of compute power, database storage, applications, and other IT resources through a cloud services platform via the Internet with pay-as-you-go pricing. As cloud computing has grown in popularity, several different models and deployment strategies have emerged to help meet specific needs of different users. Each type of cloud service and deployment method provides you with different levels of control, flexibility, and management.

### Cloud Computing Models
<a name="cloud-computing-models"></a>

 *Infrastructure as a Service (IaaS)*

 Infrastructure as a Service (IaaS) contains the basic building blocks for cloud IT and typically provides access to networking features, computers (virtual or on dedicated hardware), and data storage space. IaaS provides you with the highest level of flexibility and management control over your IT resources and is most similar to existing IT resources that many IT departments and developers are familiar with today (e.g. Amazon Elastic Compute Cloud (Amazon EC2)).

 *Platform as a Service (PaaS)*

 Platform as a Service (PaaS) removes the need for organizations to manage the underlying infrastructure (usually hardware and operating systems) and allows you to focus on the deployment and management of your applications (e.g. AWS Elastic Beanstalk). This helps you be more efficient as you don’t need to worry about resource procurement, capacity planning, software maintenance, patching, or any of the other undifferentiated heavy lifting involved in running your application.

 *Software as a Service (SaaS)*

 Software as a Service (SaaS) provides you with a completed product that is run and managed by the service provider. In most cases, people referring to Software as a Service are referring to end-user applications (e.g. Amazon Connect). With a SaaS offering you do not have to think about how the service is maintained or how the underlying infrastructure is managed; you only need to think about how you will use that particular piece of software. A common example of a SaaS application is web-based email which can be used to send and receive email without having to manage feature additions to the email product or maintain the servers and operating systems on which the email program is running.

### Cloud Computing Deployment Models
<a name="cloud-computing-deployment-models"></a>

 *Cloud*

 A cloud-based application is fully deployed in the cloud and all parts of the application run in the cloud. Applications in the cloud have either been created in the cloud or have been migrated from an existing infrastructure to take advantage of the benefits of cloud computing ([https://aws.amazon.com/what-is-cloud-computing/](https://aws.amazon.com/what-is-cloud-computing/)). Cloud-based applications can be built on low-level infrastructure pieces or can use higher level services that provide abstraction from the management, architecting, and scaling requirements of core infrastructure.

 *Hybrid*

 A hybrid deployment is a way to connect infrastructure and applications between cloud-based resources and existing resources that are not located in the cloud. The most common method of hybrid deployment is between the cloud and existing on-premises infrastructure to extend, and grow, an organization's infrastructure into the cloud while connecting cloud resources to the internal system. For more information on how AWS can help you with hybrid deployment, visit the AWS hybrid page ([https://aws.amazon.com/hybrid/](https://aws.amazon.com/hybrid/)).

 *On-premises*

 The deployment of resources on-premises, using virtualization and resource management tools, is sometimes sought for its ability to provide dedicated resources ([https://aws.amazon.com/hybrid/](https://aws.amazon.com/hybrid/)). In most cases this deployment model is the same as legacy IT infrastructure while using application management and virtualization technologies to try and increase resource utilization.

## Security
<a name="security"></a>

### Physical Security
<a name="physical-security"></a>

 Amazon has many years of experience in designing, constructing, and operating large-scale data centers. This experience has been applied to the AWS platform and infrastructure. AWS data centers are housed in facilities that are not branded as AWS facilities. Physical access is strictly controlled both at the perimeter and at building ingress points by professional security staff utilizing video surveillance, intrusion detection systems, and other electronic means. Authorized staff must pass two-factor authentication a minimum of two times to access data center floors. All visitors are required to present identification and are signed in and continually escorted by authorized staff. AWS only provides data center access and information to employees and contractors who have a legitimate business need for such privileges. When an employee no longer has a business need for these privileges, his or her access is immediately revoked, even if they continue to be an employee of Amazon or Amazon Web Services. All physical access to data centers by AWS employees is logged and audited routinely.

 Additional information on infrastructure security may be found on the webpage on [AWS Data Center controls](https://aws.amazon.com/compliance/data-center/controls/) .

 *Single or Multi-Tenant Environments*

 As cloud technology has rapidly evolved over the past decade, one fundamental technique used to maximize physical resources as well as lower customer costs has been to offer multi-tenant services to cloud customers. To facilitate this architecture, AWS has developed and implemented powerful and flexible logical security controls to create strong isolation boundaries between customers. Security is job zero at AWS and you will find a rich history of AWS steadily enhancing its features and controls to help customers achieve their security posture requirements such as GxP. Coming from operating an on-premises environment, you will often find that CSPs like AWS enable you to effectively optimize your security configurations in the cloud compared to your on-premises solutions.

 The AWS logical security capabilities as well as security controls in place address the concerns driving physical separation to protect your data. The provided isolation combined with the automation and flexibility added offers a security posture that matches or bests the security controls seen in traditional, physically separated environments.

 Additional detailed information on logical separation on AWS may be found in the [Logical Separation on AWS](https://d1.awsstatic.com/whitepapers/compliance/AWS_Logical_Separation_Handbook.pdf) whitepaper.

## Cloud Infrastructure Qualification Activities
<a name="cloud-infrastructure-qualification-activities"></a>

### Geography
<a name="geography"></a>

 AWS serves over a million active customers in more than 200 countries. As customers grow their businesses, AWS will continue to provide infrastructure that meets their global requirements.

 The AWS Cloud infrastructure is built around AWS Regions and Availability Zones. An AWS Region is a physical location in the world which has multiple Availability Zones. Availability Zones consist of one or more discrete data centers, each with redundant power, networking, and connectivity, housed in separate facilities. These Availability Zones offer you the ability to operate production applications and databases that are more highly available, fault tolerant, and scalable than would be possible from a single data center. The AWS Cloud operates in over 70 Availability Zones within over 20 geographic Regions around the world, with announced plans for more Availability Zones and Regions. For more information on the AWS Cloud Availability Zones and AWS Regions, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure).

 Each Amazon Region is designed to be completely isolated from the other Amazon Regions. This achieves the greatest possible fault tolerance and stability. Each Availability Zone is isolated, but the Availability Zones in a Region are connected through low-latency links. AWS provides customers with the flexibility to place instances and store data within multiple geographic regions as well as across multiple Availability Zones within each AWS Region. Each Availability Zone is designed as an independent failure zone. This means that Availability Zones are physically separated within a typical metropolitan region and are located in lower risk flood plains (specific flood zone categorization varies by AWS Region). In addition to discrete uninterruptable power supply (UPS) and onsite backup generation facilities, they are each fed via different grids from independent utilities to further reduce single points of failure. Availability Zones are all redundantly connected to multiple tier-1 transit providers.

### Data Locations
<a name="data-locations"></a>

 Where geographic limitations apply, unlike other cloud providers, who often define a region as a single data center, the multiple Availability Zone (AZ) design of every AWS Region offers you advantages. If you are focused on high availability, you can design your applications to run in multiple AZ's to achieve even greater fault-tolerance. AWS infrastructure Regions meet the highest levels of security, compliance, and data protection. If you have data residency requirements, you can [choose the AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) that is in close proximity to your desired location. You retain complete control and ownership over the region in which your data is physically located, making it easy to meet regional compliance and data residency requirements.

 In addition, for moving on-premises data to AWS for migrations or ongoing workflows, the following [AWS website on Cloud Data Migration](https://aws.amazon.com/cloud-data-migration/) describes the various tools and services that you may use to ensure data onshoring compliance, including:
+  Hybrid cloud storage (AWS Storage Gateway, AWS Direct Connect)
+  Online data transfer (AWS DataSync, AWS Transfer Family, Amazon S3 Transfer Acceleration, AWS Snowcone, Amazon Data Firehose, APN Partner Products)
+  Offline data transfer (AWS Snowcone, AWS Snowball Edge, AWS Snowmobile)

### Capacity
<a name="capacity"></a>

 When it comes to capacity planning, AWS examines capacity at both a service and rack usage level. The AWS capacity planning process also automatically triggers the procurement process for approval so that AWS doesn’t have additional lag time to account for, and AWS relies on capacity planning models, which are informed in part by customer demand, to trigger new data center builds. AWS enables you to reserve instances so that space is guaranteed in the region(s) of your choice. AWS uses the number of reserved instances to inform planning for FOOB (future out of bound).

### Uptime
<a name="uptime"></a>

 AWS maintains SLAs (Service Level Agreements) for various services across the platform, which, at the time of this writing, includes a guaranteed monthly uptime percentage of at least 99.99% for Amazon EC2 and Amazon EBS within a Region. A full list of AWS SLAs can be found at [https://aws.amazon.com/legal/service-level-agreements/](https://aws.amazon.com/legal/service-level-agreements/). In addition, Amazon Web Services publishes the most up-to-the-minute information on service availability in the AWS Service Health Dashboard ([https://status.aws.amazon.com/](https://status.aws.amazon.com/)). It is important to note that as part of the shared security responsibility model, it is your responsibility to architect your application for resilience based on your organization’s requirements.
