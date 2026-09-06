---
source_url: https://docs.aws.amazon.com/whitepapers/latest/open-radio-access-network-architecture-on-aws/open-radio-access-network-architecture-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Open Radio Access Network Architecture on AWS
<a name="open-radio-access-network-architecture-on-aws"></a>

Publication date: **December 02, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 The Open Radio Access Network, or O-RAN, is an approach to transform the radio access network to a disaggregated, open, virtualized, and fully inter-operable mobile network. The O-RAN uses cloud technologies as its foundation to achieve the architecture goals and provide low-cost and fully automated 5G networks. AWS is an ideal cloud platform for the O-RAN network innovation, with more than 200 featured services and globally adopted infrastructure for telecom customers. This whitepaper explores the concept of the O-RAN, offers a reference architecture for the O-RAN on AWS, and presents best practices on Amazon Web Services (AWS) for key features of the O-RAN.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 Communication service providers (CSPs) are embarking on a digital transformation journey, supporting a new wave of services enabled by 5G technologies. These consist of [millimeter wave spectrum](https://en.wikipedia.org/wiki/Extremely_high_frequency) (mmWave) for better throughput and a reduced latency in the radio technology side, rearchitecting of the core network based on service-based architecture and Control-User Plane Separation (CUPS) to maximize the utilization, agility, and efficiency of 5G network for network slicing use cases, and, as a final frontier, the opening of the Radio Access Network (RAN) to enable an intelligent and fully interoperable RAN.

 The last part has been a key objective of the O-RAN alliance, with the intent to use the modern innovations of cloud-native software technologies such as microservices, containerized, service-based, and stateless architecture. Among those key components, the O-RAN initiative is expected to bring a significant change to the telecom industry, because it causes a decomposed and software-driven RAN architecture.

 For the RAN Network to be open, the following must occur:
+  Decomposition of the Central Unit (CU) and Distributed Unit (DU).
+  The use of enhanced Common Public Radio Interface (eCPRI).
+  The disaggregation of RAN software such as Radio Connection Management and Mobility Management from the CU and DU.
+  The use of artificial intelligence (AI) to support resource discovery and self-optimization.
+  The use of cloud concepts to increase innovation and reduce time to market.

 As described in the whitepaper *[5G Network Evolution with AWS](https://d1.awsstatic.com/whitepapers/5g-network-evolution-with-aws.pdf)*, AWS can provide an ideal platform for building O-RAN components, along with other 5G innovation. Because RAN has to be placed at the edge (CU) and far-edge (DU) sites, it requires various options and form-factors of edge deployment, which can be met with [AWS Outposts](https://aws.amazon.com/outposts/) and [Amazon EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere/).

 For the microservice-based RAN implementation, various options for the container service such as [Amazon Elastic Container Service](https://aws.amazon.com/ecs) (Amazon ECS), [Elastic Kubernetes Service](https://aws.amazon.com/eks) (Amazon EKS), [Amazon EKS Distro](https://aws.amazon.com/eks/eks-distro), and [Amazon EKS Anywhere](https://aws.amazon.com/eks/eks-anywhere) can be a hosting platform for DU and CU software, using the advantage of container orchestration. More importantly, as the O-RAN architecture intends to, using the artificial intelligence/[machine learning](https://aws.amazon.com/ai) (AI/ML) and [data lakes](https://aws.amazon.com/big-data/datalakes-and-analytics) services of AWS in the architecture contributes to the telecom industry and CSPs’ ability to advance to the next level of innovation.

### AWS and O-RAN
<a name="aws-and-o-ran"></a>

 To realize the O-RAN vision, the industry expects not only the creation of an open ecosystem for the RAN, but also ways to build digital transformation frameworks on top of the RAN. AWS is an ideal cloud platform to achieve these goals, because AWS provides a breadth and depth of digital components, from [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) (flexible compute capacity) to [Amazon SageMaker AI](https://aws.amazon.com/pm/sagemaker/) (the ML platform for industry-wide use cases). Many CSPs think of potential pain points such as:
+  Data Lifecycle Management (LCM) is additional overhead and requires huge investment and operation teams, if CSPs build the RAN Intelligent Controller (RIC) by themselves.
+  Scalability, elasticity, and reliability of RAN are the keys to sustain the business and improve the experience of end-customers.
+  Data analytics and ML is a differentiator for RIC.

 In this sense, this whitepaper describes the reference architecture of O-RAN implementation on AWS and its benefits, in relation to relevant services of AWS. This paper provides an O-RAN reference architecture, an overview of O-RAN components and their characteristics, use cases, and best practices for architecting O-RAN on AWS. Best practices include high-availability, scalability, security, performance, and operational excellence. Use the information in this paper to develop O-RAN solutions on AWS, providing a cost-efficient and agile path to CSPs so they can achieve an end-to-end malleable network, enabling a multitude of 5G services.
