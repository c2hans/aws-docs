---
source_url: https://docs.aws.amazon.com/solutions/integrating-an-industrial-data-fabric-with-litmus-edge-on-aws/index.html
---

---
title: 'Guidance for Integrating an Industrial Data Fabric with Litmus Edge on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/integrating-an-industrial-data-fabric-with-litmus-edge-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Integrating an Industrial Data Fabric with Litmus Edge on AWS

## Overview

This Guidance shows how Litmus Edge can ingest near real-time data from edge data sources into AWS IoT SiteWise. As an industrial Internet of Things (IoT) platform, Litmus Edge helps users collect, process, and analyze data from industrial devices through a tight integration with AWS IoT SiteWise Edge, seamless deployment and management of Litmus Edge’s protocol support, data processing and enrichment at edge. Litmus Edge collects data from programmable logic controllers (PLCs), Supervisory Control and Data Acquisition (SCADA), and industrial historians. By adding it as a data source, users can initiate a seamless flow of sensor data for visualization, empowering real-time decision-making on the factory floor.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/integrating-an-industrial-data-fabric-with-litmus-edge-on-aws.pdf)

![Architecture diagram](/images/solutions/integrating-an-industrial-data-fabric-with-litmus-edge-on-aws/images/integrating-an-industrial-data-fabric-with-litmus-edge-on-aws-1.png)

1. **Step 1**: Litmus Edge is an industrial IoT platform that helps users collect, process, and analyze data from industrial devices. Using the Litmus Edge management software console, users can add Litmus software as a data source on AWS IoT SiteWise Edge gateway by the Litmus Edge container. This enables users to configure the protocols, data flows, and data conditioning.
1. **Step 2**: After the configurations are deployed, the sensor data flows to AWS IoT SiteWise Edge for local monitoring, storage, and access at the edge. Data from programmable logic controllers (PLCs), Supervisory Control and Data Acquisition (SCADA), and industrial historians is collected by Litmus Edge and published as MQTT messages to the MQTT broker running on AWS IoT SiteWise Edge.
1. **Step 3**: The publisher component on the AWS IoT SiteWise Edge gateway listens to all MQTT topics. It then securely publishes data to AWS IoT SiteWise in the cloud. In case of network disruption, it also addresses local buffering, storing, and forwarding of the event to AWS IoT SiteWise. To support decision-making on the factory floor, users can create local applications that use MQTT connectivity to visualize and monitor data in real-time at the edge.
1. **Step 4**: Published data is correlated with corresponding assets and populated on AWS IoT SiteWise in the cloud, where users can visualize it either with the AWS IoT SiteWise Monitor or with Amazon Managed Grafana.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS IoT SiteWise integrates with Amazon CloudWatch logs and metrics and AWS CloudTrail auditing. This enables users to monitor their industrial assets and their data collection, processing, and storage at the edge and in the cloud. Additionally, by using the metadata bulk operations capability of AWS IoT SiteWise, users can change their information model to adapt to changing plant operations. Further, users can take advantage of the component-based architecture of AWS IoT Greengrass to seamlessly extend their edge applications. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses AWS Identity and Access Management (IAM) policies scoped for the minimum required permissions for users, adhering to the principle of least privilege. AWS IoT Core and AWS IoT Greengrass policies allow only authorized smart industrial assets to connect and publish data to AWS. Additionally, by using AWS IoT SiteWise and Amazon Simple Storage Service (Amazon S3), this Guidance encrypts all data at rest. For example, edge processing for AWS IoT SiteWise relies on file-system encryption for the security of credentials. Exposed APIs (hosted within AWS IoT SiteWise Edge gateways and accessible over the local network) use a TLS connection backed by a server-certificate private key and use an access-control password for client authentication. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS IoT Greengrass and AWS IoT SiteWise operate across multiple Availability Zones within the AWS global infrastructure to maintain low-latency, high-throughput, and highly redundant networking. AWS IoT Greengrass can handle intermittent internet connectivity and supports data resiliency and backup needs. Users can store and process data at the edge, reducing their dependence on cloud connectivity and facilitating smooth plant operations. Additionally, AWS IoT SiteWise provides throttling limits for cloud data ingress and egress. By buffering data at the edge before sending it to the AWS Cloud, it reduces the risk of data loss during connection outages. It also enables users to back up asset metadata and telemetry data in an Amazon S3 cold storage tier. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses fully managed services that automatically scale up or down for optimal performance without risking over- or underprovisioning. It includes services purpose built for industrial settings—for example, it uses AWS IoT SiteWise, AWS IoT Events, and AWS IoT TwinMaker. AWS IoT SiteWise provides flexible options for ingesting telemetry data into the AWS Cloud. For example, users can choose real-time data ingestion for operations monitoring or buffered ingestion for advanced analytics. This service also offers three storage tiers (hot, warm, and cold) to optimize data storage based on performance requirements. Further, AWS IoT SiteWise Edge enables users to store and process data locally, facilitating low-latency data access for edge applications. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

AWS IoT SiteWise provides cost-optimized ingestion methods and different storage tiers (hot, warm, and cold) so users can optimize storage costs based on data access patterns. It also lets users buffer data at the edge before ingesting it to the cloud, helping to reduce ingestion costs by up to 90 percent for analytics data. Additionally, AWS IoT SiteWise Edge enables users to collect, store, and process data on local devices. Likewise, AWS IoT Greengrass lets users filter, aggregate, and process data at the edge before sending it to the cloud. Both services reduce the amount of data that users need to store and process in the cloud, helping users lower data transfer costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses fully managed services, which support sustainability by optimizing resource usage and avoiding the need for overprovisioning. These services reduce the need for on-premises infrastructure, instead using energy-efficient AWS data centers that are increasingly powered by renewable energy. Additionally, AWS IoT SiteWise Edge enables users to filter incoming data at the edge, and AWS IoT Core rules let users filter data in the cloud. This helps reduce the storage and processing resources needed in the cloud, effectively minimizing a workload’s environmental impact. Finally, by configuring the retention-period setting, users can remove unneeded data from the hot and warm storage tiers to further optimize energy use. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
