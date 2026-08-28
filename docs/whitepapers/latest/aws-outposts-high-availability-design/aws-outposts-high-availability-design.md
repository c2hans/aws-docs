---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/aws-outposts-high-availability-design.html
---

# AWS Outposts High Availability Design and Architecture Considerations
<a name="aws-outposts-high-availability-design"></a>

Publication date: **August 12, 2021** ([Document history](document-revisions.md))

 This whitepaper discusses architecture considerations and recommended practices that IT managers and system architects can apply to build highly available on-premises application environments with AWS Outposts.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 This paper is intended for IT managers and system architects looking to deploy, migrate, and operate applications using the AWS cloud platform and run those applications on premises with [AWS Outposts rack](https://aws.amazon.com/outposts/rack/), the 42U rack form factor of [AWS Outposts](https://aws.amazon.com/outposts/).

 It introduces the architecture patterns, anti-patterns, and recommended practices for building highly available systems that include AWS Outposts rack. You will learn how to manage your AWS Outposts rack capacity and use networking and data center facility services to set up highly available AWS Outposts rack infrastructure solutions.

 AWS Outposts rack is a fully managed service that provides a logical pool of cloud compute, storage, and networking capabilities. With Outposts racks, customers can use supported AWS managed services in their on-premises environments, including: [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2), [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS), [ Amazon S3 on Outposts](https://aws.amazon.com/s3/outposts/), [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts.html) (Amazon EKS), [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS), [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS), and other [AWS services on Outposts](https://aws.amazon.com/outposts/features/#AWS_services_on_Outposts). Services on Outposts are delivered on the same [AWS Nitro System](https://aws.amazon.com/ec2/nitro/) used in the AWS Regions.

 By leveraging AWS Outposts rack, you can build, manage, and scale highly available on-premises applications using familiar AWS cloud services and tools. AWS Outposts rack is ideal for workloads that require low latency access to on-premises systems, local data processing, data residency, and migration of applications with local system interdependencies.

### Extending AWS infrastructure and services to on-premises locations
<a name="extending-infrastructure"></a>

 The AWS Outposts service delivers AWS infrastructure and services to on-premises locations in [more than 50 countries and territories](https://aws.amazon.com/outposts/faqs/), giving customers the ability to deploy the same AWS infrastructure, AWS services, APIs, and tools to virtually any datacenter, co-location space, or on-premises facility for a truly consistent hybrid experience. To understand how to design with Outposts, you should understand the different tiers that make up the AWS cloud.

 An [AWS Region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions) is a geographical area of the world. Each AWS Region is a collection of data centers that are logically grouped into [Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) (AZs). AWS Regions provide multiple (at least two) physically separated and isolated Availability Zones which are connected with low latency, high throughput, and redundant network connectivity. Each AZ consists of one or more physical data centers.

 A logical [Outpost](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-outposts) (hereafter referred to as an Outpost) is a deployment of one or more physically connected AWS Outposts racks managed as a single entity. An Outpost provides a pool of AWS compute and storage capacity at one of your sites as a private extension of an AZ in an AWS Region.

 Perhaps the best conceptual model for AWS Outposts is to think of unplugging one or more racks from a data center in an AZ of an AWS Region, and installing it in your own data center or colocation facility. You roll the racks from the AZ data center to your data center. You then plug the racks into [anchor points](https://docs.aws.amazon.com/outposts/latest/userguide/region-connectivity.html) in the AZ data center with a (very) long cable so that the racks continue to function as a part of the AWS Region. You also plug them into your local network to provide low latency connectivity between your on-premises networks and the workloads running on those racks. This gives you the operational and API consistency of the AWS Cloud, while keeping your workload local.

![Diagram showing an Outpost deployed in a customer data center and connected back to its anchor AZ and parent Region](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/outpost-deployed-in-customer-data-center.png)

 The Outpost functions as an extension of the AZ where it is anchored. AWS operates, monitors, and manages AWS Outposts infrastructure as part of the AWS Region. Instead of a very long physical cable, an Outpost connects back to its parent Region through a set of encrypted VPN tunnels called the Service Link.

 The Service Link terminates on a set of anchor points in an Availability Zone (AZ) in the Outpost’s parent Region.

 You choose where your content is stored. You can replicate and back up your content to the AWS Region or other locations. Your content will not be moved or copied outside of your chosen locations without your agreement, except as necessary to comply with the law or a binding order of a governmental body. For more information, see [AWS Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).

 The workloads that you deploy on those racks run locally. And, while the compute and storage capacity available in those racks is finite and cannot accommodate running the cloud-scale services of an AWS Region, the resources deployed on the rack (your instances and their local storage) receive the benefits of running locally while the management plane continues to operate in the AWS Region.

 To deploy workloads on an Outpost, you add subnets to your Virtual Private Cloud (VPC) environments and specify an Outpost as the location for the subnets. Then, you select the desired subnet when deploying supported AWS resources through the AWS Management Console, CLI, APIs, CDK, or infrastructure as code (IaC) tools. Instances in Outpost subnets communicate with other instances on the Outpost or in the Region through VPC networking.

 The Outpost Service Link carries both Outpost management traffic and customer VPC traffic (VPC traffic between the subnets on the Outpost and the subnets in the Region).

#### Important terms:
<a name="important-terms"></a>
+  **AWS Outposts** – is a fully managed *service* that offers the same AWS infrastructure, AWS services, APIs, and tools to virtually any datacenter, co-location space, or on-premises facility for a truly consistent hybrid experience.
+  **Outpost** – is a *deployment* of one or more physically connected AWS Outposts racks that is managed as a single logical entity and pool of AWS compute, storage, and networking deployed at a customer site.
+  **Parent Region** – the AWS Region which provides the management, control plane services, and regional AWS services for an Outpost deployment.
+  **Anchor Availability Zone (anchor AZ)** – the Availability Zone in the parent Region that hosts the anchor points for an Outpost. An Outpost functions as an extension of its anchor AZ. The anchor AZ is chosen by the customer when the Outposts order is placed. After an anchor AZ is chosen, it cannot be changed for the duration of the AWS Outposts subscription term.
+  **Anchor Points** – endpoints in the anchor AZ that receive the connections from remotely deployed Outposts.
+  **Service Link** – a set of encrypted VPN tunnels that connect an Outpost to its anchor Availability Zone in its parent Region.
+  **Local Gateway (LGW)** – A logical interconnect virtual router that enables communication between your Outpost and your on-premises network.

### Understanding the AWS Outposts Shared Responsibility Model
<a name="shared-security-model"></a>

 When you deploy AWS Outposts infrastructure into your data centers or co-location facilities, you take on additional responsibilities in the [AWS Shared Responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/). For example, in the Region, AWS provides diverse power sources, redundant core networking, and resilient Wide Area Network (WAN) connectivity to ensure services are available in the event of one or more component failures.

 With Outposts, you are responsible for providing resilient power and network connectivity to the Outpost racks to meet your availability requirements for workloads running on Outposts.

![Diagram showing the AWS Shared Responsibility Model updated for AWS Outposts](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/aws-shared-responsibility-model.png)

 With AWS Outposts, you are responsible for the physical security and access controls of the data center environment. You must provide sufficient power, space, and cooling to keep the Outpost operational and network connections to connect the Outpost back to the Region.

 Since Outpost capacity is finite and determined by the size and number of racks AWS installs at your site, you must decide how much EC2, EBS, and S3 on Outposts capacity you need to run your initial workloads, accommodate future growth, and to provide extra capacity to mitigate server failures and maintenance events.

 AWS is responsible for the availability of the Outposts infrastructure including the power supplies, servers, and networking equipment within the AWS Outposts racks. AWS also manages the virtualization hypervisor, storage systems, and the AWS services that run on Outposts.

 A central power shelf in each Outposts rack converts from AC to DC power and supplies power to servers in the rack via a bus bar architecture. With the bus bar architecture, half the power supplies in the rack can fail and all the servers will continue to run uninterrupted.

![Photographs showing AWS Outposts AC-to-DC power supplies and bus bar power distribution](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/ac-dc-supplies-and-bus-bar-distribution1.png)![Photographs showing AWS Outposts AC-to-DC power supplies and bus bar power distribution](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/ac-dc-supplies-and-bus-bar-distribution2.png)

 The network switches and cabling within and between the Outposts racks are also fully redundant. A fiber patch panel provides connectivity between an Outpost rack and the on-premises network and serves as the demarcation point between the customer-managed data center environment and the managed AWS Outposts environment.

 Just like in the Region, AWS is responsible for the cloud services offered on Outposts and takes on additional responsibilities as you select and deploy higher-level managed services like Amazon RDS on Outposts. You should review the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) and the Frequently Asked Questions (FAQ) pages for individual services as you consider and select services to deploy on Outposts. These resources provide additional details on the division of responsibilities between you and AWS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
