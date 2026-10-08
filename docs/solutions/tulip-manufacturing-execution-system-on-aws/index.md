---
source_url: https://docs.aws.amazon.com/solutions/tulip-manufacturing-execution-system-on-aws/index.html
---

---
title: 'Guidance for Tulip Manufacturing Execution System (MES) on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/tulip-manufacturing-execution-system-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Tulip Manufacturing Execution System (MES) on AWS

## Overview

This Guidance illustrates how to build seamless data flows between the Tulip Frontline Operations Platform and an Amazon Virtual Private Cloud (Amazon VPC). This integration helps manufacturers digitize operator workflows, automate data collection, and gain real-time visibility into shop floor operations. The Tulip Manufacturing Execution System (MES) provides a user-friendly, no-code environment where users can create functional applications that replace manual, paper-based processes. Through Tulip Connectors, users can seamlessly ingest data into their applications and store it in Tulip Tables, transforming fragmented systems into a unified digital solution for manufacturing operations.

## How it works

This architecture diagram showcases comprehensive data flows between a Tulip Manufacturing Execution System (MES) and AWS. The Tulip MES is offered as a software as a service (SaaS) on AWS, enabling data transparency and generating actionable insights.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/tulip-manufacturing-execution-system-on-aws.pdf?target=_blank)

![Architecture diagram](/images/solutions/tulip-manufacturing-execution-system-on-aws/images/tulip-manufacturing-execution-system-on-aws-1.png)

1. **Step 1**: Tulip MES on AWS is designed to be a highly scalable, multi-tenant SaaS solution. At the core is an Amazon Elastic Kubernetes Service (Amazon EKS) cluster, deployed across multiple Availability Zones for high availability. Amazon RDS for PostgreSQL, in a high availability configuration, is used to store application data. The Application Load Balancer (ALB) serves as an entry point for the application, forwarding the requests to the appropriate Kubernetes service with the right tenant context. A NAT gateway in the public subnet allows application and database servers to reach the internet.
1. **Step 2**: Amazon Simple Storage Service (Amazon S3) is used to store customer specific files with each customer having their own set of AWS Identity and Access Management (IAM) credentials to access their isolated Amazon S3 buckets. Amazon OpenSearch Service is used for log aggregation and analysis.
1. **Step 3**: Operators at customer sites access Tulip through an application known as the Tulip Player. The Tulip platform also supports connectivity between select industrial devices, such as sensors, actuators, and cameras directly through Tulip edge device(s). Additionally, industrial assets, Programmable Logic Controllers (PLCs), and other external systems can be integrated with the Tulip platform using the Tulip Connector Host.
1. **Step 4**: AWS IoT Greengrass can also connect in parallel to industrial assets, Programmable Logic Controllers (PLCs), and historian systems to collect and store time series industrial data to AWS IoT SiteWise.
1. **Step 5**: AWS customers can integrate their Enterprise Resource Planning (ERP) application to Tulip using REST API.
1. **Step 6**: Customers can also create an Amazon S3 data lake in their own account for data analytics. Data from the Tulip application can be extracted and transferred to the Amazon S3 data lake using AWS Lambda to call Tulip's REST API. Time series data from AWS IoT SiteWise can also be exported to the Amazon S3 data lake.
1. **Step 7**: Customers can extract value from industrial data stored in the Amazon S3 data lake using various AWS analytics services. For data warehousing, they can use Amazon Redshift. To manage the data catalog, they can use AWS Glue. And for business intelligence capabilities, they can take advantage of Amazon QuickSight.
1. **Step 8**: Customers can use the data stored in the Amazon S3 data lake to build, train, and deploy machine learning models using Amazon SageMaker. They can also use Amazon Bedrock to develop generative artificial intelligence (AI) applications. Amazon Q Business can be configured to obtain relevant answers to pressing questions, solve problems, generate content, and take action on the user's behalf.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon EKS and the ALB automate critical infrastructure management tasks. Specifically, Amazon EKS provisions and maintains control plane nodes across multiple Availability Zones (AZs), delivering high availability for the Kubernetes environment. The service handles Kubernetes version upgrades, security patches, and bug fixes, eliminating manual maintenance overhead. ALB complements this automation by monitoring target health and routing traffic away from unhealthy instances, maintaining application reliability across AZs. The integrated monitoring, security, and compliance features provide comprehensive operational visibility, allowing teams to focus on application development rather than infrastructure management. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Multiple layers of security are implemented through three core AWS services: Amazon S3, ALB, and Amazon EKS. Amazon S3 enforces data isolation by assigning dedicated IAM credentials and isolated buckets to each customer, preventing unauthorized cross-tenant access. ALB secures application communication through SSL/TLS termination and client authentication, protecting data in transit between clients and services. Within Amazon EKS, Kubernetes namespaces create logical boundaries that isolate customer workloads so that resources remain separate and secure. This multi-layered security approach delivers a robust multi-tenant environment with clear security boundaries and access controls. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Within this architectural framework, Tulip MES deploys multiple AWS services across application, data, and monitoring layers. At the application layer, Amazon EKS hosts core services while ALB distributes traffic across AZs, maintaining service availability during zone failures. The data layer combines Amazon RDS for PostgreSQL and Amazon S3, providing automated backups, replication, and failover capabilities for structured data, while offering durable object storage for customer files. To maintain platform stability, Tulip MES monitors infrastructure health through integrated open-source tools—Prometheus, Grafana, and ClusterFlow—deployed within their Amazon EKS cluster. This comprehensive approach enables rapid issue detection and resolution for consistent platform availability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The Tulip MES architecture optimizes performance efficiency through integrated AWS services. Amazon EKS automatically scales application components based on demand, while Amazon RDS for PostgreSQL adjusts compute, memory, and storage resources to match database workload requirements. Amazon S3 provides consistent performance for file operations regardless of storage volume, handling concurrent access without degradation. OpenSearch Service processes log data and analytics queries at scale, enabling rapid search and visualization of operational data. These services work together to maintain performance as workloads grow, reducing infrastructure bottlenecks and delivering responsive experiences across a multi-tenant platform. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Tulip optimizes costs through the flexible pricing models of AWS and automated resource management. Amazon EKS and Amazon RDS for PostgreSQL implement demand-based autoscaling, preventing resource waste by matching capacity to actual usage. For predictable workloads, Tulip reduces costs through Amazon EC2 Reserved Instances and Savings Plans, applying discounted rates to steady-state Amazon Elastic Compute Cloud (Amazon EC2) and Amazon RDS for PostgreSQL usage. This combination of automated scaling and strategic pricing commitments minimizes operational overhead while maintaining optimal resource utilization. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By using managed AWS services like Amazon EKS, Amazon RDS for PostgreSQL, and Amazon S3, Tulip can reduce the energy and resources required to provision, operate, and maintain their own infrastructure. Managed services often have a higher degree of efficiency and optimization compared to self-managed infrastructure. By using the autoscaling features in services like Amazon EKS and Amazon RDS for PostgreSQL, Tulip automatically scales resources up and down based on demand. This can help minimize resource waste and improve energy efficiency by only using the necessary compute and storage capacity at any given time. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
