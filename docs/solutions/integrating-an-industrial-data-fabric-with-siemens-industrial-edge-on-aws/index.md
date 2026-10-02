---
source_url: https://docs.aws.amazon.com/solutions/integrating-an-industrial-data-fabric-with-siemens-industrial-edge-on-aws/index.html
---

---
title: 'Guidance for Integrating an Industrial Data Fabric with Siemens Industrial Edge on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/integrating-an-industrial-data-fabric-with-siemens-industrial-edge-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Integrating an Industrial Data Fabric with Siemens Industrial Edge on AWS

## Overview

This Guidance shows how to integrate your industrial data fabric with Siemens Industrial Edge and AWS to analyze industrial asset data at scale. Industrial Edge is an open, ready-to-use edge computing platform that features a centralized management system for many Industrial Edge apps and a variety of devices. Using AWS IoT SiteWise Edge to integrate AWS with Industrial Edge, you can use preprocessed operational data with Industrial Edge apps and AWS services. This enables you to promote industrial connectivity, contextualization, analytics, AI, automation, and more, empowering data-driven decision-making.

## How it works

This architecture diagram shows how to ingest near real-time data at scale from edge data sources into AWS IoT SiteWise by using AWS IoT SiteWise Edge and Siemens Industrial Edge.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/integrating-an-industrial-data-fabric-with-siemens-industrial-edge-on-aws.pdf?target=_blank)

![Architecture diagram](/images/solutions/integrating-an-industrial-data-fabric-with-siemens-industrial-edge-on-aws/images/integrating-an-industrial-data-fabric-with-siemens-industrial-edge-on-aws-1.png)

1. **Step 1**: Siemens Industrial Edge is an open software platform for simple, scalable, and manageable shop-floor IT. It provides decentralized and local data acquisition, storage, analytics, AI, and connectivity to AWS. The Industrial Edge Management application enables remote and central management of edge devices and applications.
1. **Step 2**: On Industrial Edge devices, southbound connector applications—such as Open Platform Communications Unified Architecture (OPC-UA), Modbus TCP, and Siemens SIMATIC S7 connectors, ethernet and IP connectors, and other off-the-shelf connectors—collect data from industrial assets for on-premises processing and analysis. This is done with Siemens apps such as Energy Manager and Performance Insight. You can create your own apps using the Mendix on Edge integration, Industrial Edge Flow Creator, or Docker apps.
1. **Step 3**: Industrial Edge Management can be deployed on-premises using a self-managed Kubernetes cluster or on AWS infrastructure using Amazon Elastic Kubernetes Service (Amazon EKS).
1. **Step 4**: AWS IoT SiteWise Edge, deployed on Industrial Edge devices, collects and aggregates data and sends it to AWS IoT SiteWise.
1. **Step 5**: AWS IoT SiteWise Monitor, AWS IoT TwinMaker, or Amazon Managed Grafana get data from AWS IoT SiteWise to create visualizations and get insights into collected industrial data.
1. **Step 6**: Amazon Athena enables you to query cold Internet of Things (IoT) data from Amazon Simple Storage Service (Amazon S3) for data analytics with Amazon Managed Grafana, Amazon QuickSight, or Mendix low-code apps.
1. **Step 7**: AWS artificial intelligence and machine learning (AI/ML) services, like Amazon SageMaker, use data from Amazon S3 to train ML models, then work with the Siemens AI Software Development Kit (SDK) to package and deploy ML models back to the edge.
1. **Step 8**: The Siemens AI Model Manager deploys and manages ML models on the edge, and the Siemens AI Inference Server implements the models. The Siemens AI Model Monitor then observes them and provides results for use in model improvement.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses various managed services that lower your operational overhead by letting you focus on your business instead of managing your IT infrastructure. For example, AWS IoT SiteWise, Amazon Managed Grafana, Amazon S3, and Athena help you avoid the heavy lifting of installing and maintaining operating systems and software. These services also integrate with Amazon CloudWatch or AWS CloudTrail to enhance observability. Additionally, AWS IoT SiteWise Edge, which is easily installable on Industrial Edge, gathers metrics to help you gain insights into your edge deployment. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses services that provide built-in security and support encryption in transit and at rest. CloudWatch and CloudTrail support traceability, and AWS Identity and Access Management (IAM) helps you implement a strong identity foundation. As part of the central system, Siemens Industrial Edge Management makes sure that only users with the right permissions can access and perform changes. It also enables you to remotely upgrade the full software stack of your devices, starting with the firmware. Certified by the Cloud Security Alliance, Industrial Edge Management encrypts communications to other systems and cloud services and securely stores credentials and secrets. Refer to Security Best Practices for Manufacturing OT for more information on designing, deploying, and securing distributed manufacturing workloads and resources at the industrial edge. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance includes AWS managed services like AWS IoT Core, AWS IoT SiteWise, Amazon S3, and Athena, which are scalable and highly available by design. They run on the AWS global infrastructure, which is designed to provide low-latency, high-throughput, and highly redundant networking. You can monitor your service quotas and ask for an increase if needed to match demand. Additionally, AWS IoT SiteWise Edge on Industrial Edge buffers data before it is ingested into AWS, helping resolve intermittent connectivity issues. As the central system, Industrial Edge enables you to easily manage remote backup-and-restore operations of your edge deployments. Additionally, Siemens Industrial Edge Management does not require uninterrupted internet connectivity, and you can deploy it in a highly available Kubernetes infrastructure. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AWS IoT SiteWise provides hot, warm, and cold storage tiers so that it can support both real-time and batch processing. AWS IoT TwinMaker and AWS Managed Grafana provide real-time data visualization, while Amazon QuickSight, Athena, and Amazon S3 support batch processing. Finally, SageMaker enables you to automatically scale and adjust the compute resources used for your ML workloads based on demand. Industrial Edge provides real-time data processing at the edge, reducing latency and facilitating timely decision-making. Additionally, it lets you centralize the management of connected devices and software. This makes deployment and application updates easier and more efficient across multiple machines and plants. Finally, Industrial Edge employs a microservice approach, so you only need to deploy the services or applications required for the task at hand while having the flexibility to deploy further functionality to the same devices later. This enables you to rightsize your devices, enhancing performance efficiency. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses managed services that reduce the cost of infrastructure management and provisioning. These services also only charge based on the resources you use, with no upfront costs or long-term usage commitments. SageMaker also automatically scales resources up and down based on demand. Additionally, you can use AWS Organizations and AWS Budgets to measure overall cost efficiency and learn how to use AWS services more cost efficiently. For example, Athena supports data partitioning, which enables you to reduce costs by scanning only a subset of your data. And Amazon S3 Intelligent-Tiering and AWS IoT SiteWise provide different storage tiers so that you can store data cost effectively based on access patterns. AWS IoT SiteWise also lets you ingest multiple properties in one API call, lowering data ingestion costs. Additionally, Industrial Edge lets you define a use case once and deploy it across multiple devices, avoiding the cost of individual device setup. This approach also enables centralized management and updates, reducing the time and effort required for maintenance. And by supporting local data processing at the edge—closer to data sources—Industrial Edge helps you significantly reduce data transfer and cloud storage costs. This helps you run computational resources more efficiently and avoid the need for extensive IT infrastructure, minimizing engineering efforts and ultimately lowering expenses. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses managed AWS services to maximize resource utilization and avoid overprovisioning. Through the scale and efficiency of the AWS global infrastructure compared to on-premises data centers, you can greatly reduce your carbon footprint and energy consumption. Additionally, many AWS services are designed for sustainability, incorporating features like energy-efficient hardware, renewable energy sources, and efficient resource utilization to minimize the environmental impact. You can use the Customer Carbon Footprint Tool to track, measure, review, and forecast the carbon emissions generated from your AWS usage so that you can optimize your energy use. Industrial Edge also significantly contributes to sustainability through its energy efficiency and resource optimization. By processing data locally at the edge, it avoids extensive data transmission to central servers, lowering your energy consumption and reducing your carbon footprint. It also enables real-time monitoring and optimization of industrial processes, leading to more efficient use of resources such as water, raw materials, and energy. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
