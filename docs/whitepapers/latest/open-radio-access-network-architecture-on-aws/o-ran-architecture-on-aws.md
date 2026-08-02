---
source_url: https://docs.aws.amazon.com/whitepapers/latest/open-radio-access-network-architecture-on-aws/o-ran-architecture-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# O-RAN architecture on AWS
<a name="o-ran-architecture-on-aws"></a>

 As shown in the preceding figure, AWS can provide all required building blocks for O-RAN development and deployment. While non-RT RIC is located in the Region to use all the benefit of AWS data lakes and AI/ML gears, near-RT RIC and O-CU can be hosted at the edge site using the [AWS Outposts](https://aws.amazon.com/outposts/) and Amazon EKS services. At the far-edge site, O-DU can be placed on Amazon EKS Anywhere. Because this architecture is fully empowered by AWS services, service deployment and monitoring of each component can be done through AWS management and orchestration services such as [AWS Software Development Kits](https://aws.amazon.com/developer/tools/) (AWS SDKs), [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), and [AWS CloudFormation](https://aws.amazon.com/cloudformation/), which provide true single panes of glass for the entire RAN operation. The following figure shows a reference architecture of O-RAN on AWS infrastructure hosting the O-RAN components.

![A diagram depicting O-RAN reference architecture.](http://docs.aws.amazon.com/whitepapers/latest/open-radio-access-network-architecture-on-aws/images/o-ran-ra.png)

## O-RAN components on AWS
<a name="o-ran-components-on-aws"></a>

### RIC
<a name="ric"></a>

 Disintegration of RAN as defined by the O-RAN alliances provides an opportunity to use cloud concepts farther away from the radio stations. The RIC, near-RT and non-RT, provide mobility operators with the ability to customize their RAN network, automate their network operations and optimization, and use AI/ML capabilities. The following sections expand on how AWS services enable RIC architecture.

 Radio network conditions are constantly changing based on users’ behaviors, environmental changes, interferences, and more. The randomness of the radio channels’ characterization and the random nature of events impacting signal quality requires a RAN that reacts to these events to maximize the quality of its users’ experience. Traditionally, CSPs tackle this problem through centralized self-organizing network (SON) capabilities, and network equipment provider (NEP)s features delivery and densification. The latter is often limited to individual NEPs, resulting in CSPs choosing radio equipment vendors for entire countries (or Regions) rather than mixing and matching based on the localized environmental behaviors.

 This idea of customizing approaches based on localized environments is the foundational idea behind RIC. As such, the RIC architecture needs to support agility, innovation, and elasticity, while reducing the overall cost and complexity of managing a mobility network. These characteristics are aligned with cloud benefits enabled by AWS.

### Near-RT RIC
<a name="near-rt-ric"></a>

 The near-RT RIC has the following functions:
+  Mobility management.
+  Radio connection management.
+  Quality of Service (QoS) management.
+  Interference management.
+  Trained models.
+  Independent and extensible software plug-ins.

 All these functions interact with one another, and are enabled by a common radio network information base. The latter provides near-RT RIC functions with an overview of the network RIC supports. This is illustrated in the following figure.

![A document depicting near-RT RIC components.](http://docs.aws.amazon.com/whitepapers/latest/open-radio-access-network-architecture-on-aws/images/near-rt-ric.png)

 The near-RT RIC requires rapid low latency access to the network. This is enabled by AWS Outposts, which provides CSPs with a fully-managed service that offers the same AWS infrastructure, AWS services, APIs, and tools to their edge locations. AWS Outposts provides services such as Amazon EKS and Amazon ECS to support container-based applications, Amazon EMR clusters to support data analytics effort requiring immediate local processing, and Amazon RDS for relational databases.

 Near-RT RIC ISVs can use Amazon EKS on Outposts to deliver RIC functions such as QoS managements. Amazon EKS enables non-RT RIC to scale with network conditions, upgrades RIC functions independently from one another, supports canary deployment of the new RIC version, and supports third-party RAN applications.

![A diagram depicting near-RT RIC AWS architecture.](http://docs.aws.amazon.com/whitepapers/latest/open-radio-access-network-architecture-on-aws/images/near-rt-architecture.png)

 [Amazon ElastiCache](https://aws.amazon.com/elasticache/) provides a fully managed Redis database, simplifying the hosting of RIC Shared Data Storage in support of the O-RAN SDL libraries. It provides sub-millisecond latency to support near real-time RIC applications such as mobility management, and supports the scaling necessary to support the entire set of RIC applications.

 Amazon RDS provides a scalable, easy-to-set-up, and operationally efficient solution to support static and semi-static network configuration. Amazon RDS on Outposts supports mySQL and PostreSQL database engines.

### Non-RT RIC
<a name="non-rt-ric"></a>

 The non-RT RIC provides the required intelligence to perform optimization of the RAN networks, uses data from across the operation support system (OSS) stack, and has access to AI/ML resources to build a model that can be applied to a given near-RT RIC, or a set of near-RT RIC. As illustrated in the following figure, the non-RT RIC has three logical roles:
+  Ingestion of A1 messages.
+  Hosting of non-real time applications (R-APP).
+  Enrichment of A1 messages.

![A diagram depicting non-RT RIC functional view.](http://docs.aws.amazon.com/whitepapers/latest/open-radio-access-network-architecture-on-aws/images/non-rt-ric.png)

 To support operators that plan for a one-to-many relationship between non-RT RIC and near-RT-RIC, you can use AWS services such as Amazon API Gateway, AWS Lambda, AWS Step Functions, and [Amazon Simple Queue Service](https://aws.amazon.com/sqs/) (Amazon SQS).
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) provides you with scalable services that make it easy to publish, maintain, and monitor the A1 interfaces between non-RT and near-RT RIC.
+  [AWS Lambda](https://aws.amazon.com/lambda/), a serverless event-driven compute service, provides you with the ability to perform A1 enrichment without having to provision or manage dedicated servers.
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) provides you with a low-code visual workflow service that helps you orchestrate and automate A1 enrichment procedure.
+  [Amazon SQS](https://aws.amazon.com/sqs/) is a fully-managed queueing service that enables you to communicate between R-APP at scale, while allowing you to set different prioritization for given A1 messages, both native and enriched.

 The following figure illustrates a reference architecture for developing Non-RT RIC on AWS:

![A diagram depicting non-RT RIC on AWS.](http://docs.aws.amazon.com/whitepapers/latest/open-radio-access-network-architecture-on-aws/images/non-rt-ric2.png)

 The AWS Cloud enables you to host modern R-APP applications, specially designed to run on the Non-RT RIC as code by using AWS Lambda. Similarly, Amazon EKS provides you with a managed container service to run and scale your Kubernetes-based R-APP applications.

### SMO
<a name="smo"></a>

 Service Management and Orchestration (SMO) can be reduced to:
+  Ingestion of OAM data.
+  Applications hosting.
+  Inventory and configuration data storage.
+  API layer.

 This section discusses how AWS services help you develop SMOs that benefit from scalability, performance, and reliability, and deploy them in minutes across your entire network. The following figure illustrates an SMO architecture on AWS.

![A diagram depicting SMO architecture on AWS.](http://docs.aws.amazon.com/whitepapers/latest/open-radio-access-network-architecture-on-aws/images/smo-architecture.png)

 Ingestion of O1 messages is facilitated by [Amazon API Gateway](https://aws.amazon.com/api-gateway/), [Amazon Kinesis](https://aws.amazon.com/kinesis/), [Amazon MSK](https://aws.amazon.com/msk/), and [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/). For example, when an O-RAN network element (NE) has a large configuration change, a large log, or a large performance data available, Amazon API Gateway facilitates the implementation of a REST request to initiate a file retrieval from the NE. The data transfer is facilitated by the AWS Transfer Family. Similarly, Amazon Kinesis and Amazon MSK provide you with scalable, reliable, managed solutions to ingest near real-time network events and near real-time configuration messages. SMO functions and applications can subscribe to a fully scalable data bus, and provide the required RAN network management and orchestration.

 Use [Amazon EKS](https://aws.amazon.com/eks/) to run Kubernetes-compliant SMO applications on AWS without the need to install and operate your own Kubernetes control plane. [AWS Lambda](https://aws.amazon.com/lambda/) provides you with the ability to benefit from the event-driven nature of SMO OAM functions by building SMO applications that only use compute resources when needed. AWS Lambda is a serverless, event-driven compute service that lets you run code virtually without provisioning or managing servers.

 Use [AWS Step Functions](https://aws.amazon.com/step-functions/?step-functions.sort-by=item.additionalFields.postDateTime&step-functions.sort-order=desc) to build orchestration logic.

 Use [Amazon EventBridge](https://aws.amazon.com/eventbridge/) for event-driven integration with other Business Support Systems (BSS)/OSS/external applications, while Amazon SQS provides you with a fully-managed message queuing service that enables to decouple your SMO microservices and serverless applications.

 AWS purpose-built database services for [Graph DB](https://aws.amazon.com/neptune/), [NoSQL](https://aws.amazon.com/nosql/), and [RDBMS](https://aws.amazon.com/rds/) provide you with the ability to support inventory and configuration management use cases. They provide you with the scalability, reliability, and performance to decouple the database layer from your application to achieve a common data unification model shared with applications across the OSS stack.

 Amazon API Gateway enables you to integrate SMO with external applications. For example, a REST API can easily be exposed for a service orchestrator to initiate a configuration change. Amazon API Gateway, being a fully managed service, makes it easy for you to develop, create, publish, maintain, monitor, and scale the APIs required northbound and southbound of SMO.

### O-CU
<a name="o-cu"></a>

 The O-CU hosts Radio Resource Control (RRC), Service Data Adaptation Protocol (SDAP), and PDCP protocols, and consists of the O-CU control plane (O-CU-CP) and the O-CU user plane (O-CU-UP). Because O-CU communicates O-DU through the F1 interface and the Core Network through N2 (for Access and Mobility Management Function (AMF)) and N3 (for UPF) in a low latency, it should be located at the edge data center. [AWS Outposts](https://aws.amazon.com/outposts) provides a perfect option for building the edge data center of CSP, because it provides a fully-managed service that offers the same AWS infrastructure, AWS services, APIs, and tools to virtually any datacenter, co-location space, or on-premises facility for a truly consistent hybrid experience.

 From the perspective of protocol stack, the O-Ran Central Unit control plane

 (O-CU-CP) hosts the RRC and the control plane part of the PDCP protocol, while O-CU-UP hosts the user plane part of the PDCP protocol and the SDAP protocol. O-CU deals with upper layer protocol stacks, unlike O-DU and O-RU, which make it independent of the complex physical layer. This aspect enables you to virtualize and containerize O-CU easily, as you can with 5G Core Network function components.

 Because O-CU has to cover an aggregated set of O-DUs, the scalability, elasticity, and flexibility of using compute and storage resources would bring a huge benefit in terms of efficiency for resource utilization and cost optimization. To maximize this benefit from the software architecture, people often choose container-based implementation. For the orchestration of containers, Kubernetes is often selected, not only for 5G Core Network providers, but also O-RAN SW providers. AWS provides [Amazon EKS](https://aws.amazon.com/eks/) as a managed Kubernetes service with the control plane or primary nodes functionality. Worker nodes under the EKS cluster are created using [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) in cases of [EKS managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html) and [self-managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/worker.html).

 As with Core Network functions, O-CU is often required to support [network segmentation](https://en.wikipedia.org/wiki/Network_segmentation) such as having separate OAM, control plane, and user plane sub-networks. The best practice for having this network separation at the Kubernetes environment is using the [Multus meta CNI Plugin](https://github.com/k8snetworkplumbingwg/multus-cni). Amazon EKS now supports Multus CNI as an [add-on package of EKS](https://aws.amazon.com/blogs/containers/amazon-eks-now-supports-multus-cni/). As illustrated in the [AWS official GitHub](https://github.com/aws-samples/eks-install-guide-for-multus), creation of Multus-ready worker node groups can be automated with CloudFormation or CDK using a Lambda function and CloudWatch Event rule. Mostly O-CU-UP requires packet processing acceleration, generally using [SR-IOV DPDK](https://doc.dpdk.org/guides/nics/intel_vf.html). Because of this, the best practice for selecting an instance type for a worker node group of O-CU-CP is using the latest generation of [ENA](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)-available instances, such as the C6 and M5 instance families.

 For the container storage, the [Amazon EBS CSI driver](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html) provides a container storage interface (CSI) interface that allows Amazon EKS clusters to manage the lifecycle of Amazon EBS volumes for persistent volumes. In the AWS environment, the O-CU container image and helm chart can be stored and managed in [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) (Amazon ECR). For the collection of KPI and metric for O-CU, you can use [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/) and [Amazon Managed Grafana](https://aws.amazon.com/grafana/).

 This full stack of AWS tools for building O-CU on AWS from the bottom layer (through AWS Outposts) to the top of O-CU application and additional monitoring and orchestration layers (through CloudFormation, CloudWatch) are shown in the following figure in a high-level view.

![A diagram depicting full-stack view for O-CU design in AWS.](http://docs.aws.amazon.com/whitepapers/latest/open-radio-access-network-architecture-on-aws/images/full-stack-view.png)

### O-DU and O-RU
<a name="o-du-and-o-ru"></a>

 The O-DU performs the Radio Link Control (RLC), Medium Access Control (MAC), and physical layer in the 3GPP specifications. The RLC builds information packets and recovers transmission losses by retransmitting lost packets. The MAC layer controls the physical layer, and allocates radio resources to transmit and receive packets over the air. The physical layer in the O-DU is responsible for link connectivity. The performance of physical layer dominates wireless link throughput and coverage where user experience would be mostly affected. The physical layer consumes heavy computational power for complex channel estimation and interference cancelling to improve the performance. To relieve its computational complexity, hardware acceleration techniques are commonly used in the O-DU.

 AWS infrastructure and services bring significant advantages and benefits to CSPs. AWS provides tightly integrated hardware infrastructure and platform software by working with multiple hardware and RAN vendors. AWS management control, programmable APIs, and tools and services such as [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) improves operation efficiency and relieves undifferentiated heavy lifting of infrastructure management. AWS automation services, CI/CD with [AWS CodePipeline](https://aws.amazon.com/codepipeline/), and automated life cycle management will speed up time to market and enhance operational resiliency. With the cost savings by AWS, total cost of ownership (TCO) benefits will come in the form of enhanced staff productivity, less management efforts, and flexible payment like pay-as-you-go.

The O-DU can run on Amazon EKS Anywhere. AWS provides [Amazon EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere/) for CSPs who want to keep the existing Commercial-Off-The-Shelf (COTS) hardware, but build an end-to-end platform and management framework from cell sites to an AWS Region cloud. As a CaaS layer, EKS Anywhere runs on bare metal servers and operates clusters on the CSPs on-premises data centers with fully managed Kubernetes services. EKS Anywhere can support customer designated devices such as L1 accelerators and network interfaces supporting Precision Time Protocol (PTP), and enable low-latency access to the devices by Single Root I/O Virtualization Container Network Interface (SR-IOV CNI) and Data Plane Development Kit (DPDK). CSPs can use the EKS console to view all the Kubernetes clusters running on cell sites, in AWS Outposts, Local Zones, and Regions. This enables customers to have a single pane of glass and build an end-to-end management framework to deploy 5G CNFs from O-DU to 5G Core Network functions.
