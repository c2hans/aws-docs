---
source_url: https://docs.aws.amazon.com/solutions/multi-tenant-architectures-on-aws/index.html
---

---
title: 'Guidance for Multi-Tenant Architectures on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/multi-tenant-architectures-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Multi-Tenant Architectures on AWS

## Overview

This Guidance shows customers three different models for handling multi-tenancy in the database tier, each offering a trade-off between tenant isolation and cost and complexity. Tenant isolation is fundamental to the design and development of multi-tenancy applications, particularly software as a service (SaaS) applications. In a multi-tenant architecture, multiple instances of an application operate in a shared environment to achieve cost and operational efficiency. An application operator must safeguard tenant data by making sure it is accessible only to that particular tenant. By offering three models of tenant isolation at the database-level, this Guidance allows customers to choose the right architecture that meets their risk and cost requirements.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/multi-tenant-architectures-on-aws.pdf)

![Architecture diagram](/images/solutions/multi-tenant-architectures-on-aws/images/multi-tenant-architectures-on-aws-1.png)

1. **Step 1**: In the Silo Model, each tenant interacts with an entire application stack dedicated to that tenant. The application stack runs on Amazon Elastic Compute Cloud (Amazon EC2) compute instances. Traffic and data do not cross tenant boundaries.
1. **Step 2**: Each tenant's data is stored in an Amazon Relational Database Service (Amazon RDS) database instance dedicated to that tenant. A tenant's data does not mix with other tenants' data.
1. **Step 3**: In the Bridge Model, tenants share the complete application stack, reducing cost and complexity.
1. **Step 4**: Tenants share the same RDS instance, but each have a dedicated schema.
1. **Step 5**: In the Pool Model, tenants share the entire application stack, just as in the Bridge Model.
1. **Step 6**: Tenants share the same database instance and objects. Database tables contain data for multiple tenants. Tenant isolation is provided by row-level security features in the database.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon RDS emits performance and utilization metrics to Amazon CloudWatch. Amazon RDS Performance Insights provides additional visibility through database load data for performance monitoring. Amazon RDS Enhanced Monitoring provides metrics for the operating system of your database instance. » [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Tenant data is isolated from access by other tenants in the following ways: the Silo Model separates tenant data into a database instance per tenant; the Bridge Model isolates tenant data into a dedicated schema per tenant; the Pool Model uses the row-level security features of the database engine. » [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon RDS creates automated database backups daily and saves them for a defined retention period. You may also create your own database snapshots in Amazon RDS and manage the snapshot lifecycles. In addition, you can still create and manage backups using native and third-party database backup tools. Amazon Aurora, one of the database engines that Amazon RDS supports, stores six copies of data across three Availability Zones. In Aurora, compute is decoupled from storage. Aurora storage also identifies and repairs errors automatically. » [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

SaaS customers may employ a hybrid architecture, allocating siloed infrastructure to high-traffic customers while co-locating quieter customers in a Bridge or Pool Model. If you have a highly variable workload, you may use Aurora Serverless. Database instances are scaled-to-fit workloads and may be adjusted over time. You may also add read replicas to shift read traffic away from busy writer nodes. » [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Each of the architectural models presented in this Guidance offer a trade-off between tenant isolation and cost. The Silo Model, for example, provides the strongest tenant isolation but incurs the most cost and complexity. Inversely, the Pool Model offers the least tenant isolation but costs the least. SaaS providers may choose hybrid architectures to manage costs and may even offer end users service tiers to allow them to make their own trade-off decisions. » [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Tenants in the Silo Model with variable workloads can use Aurora Serverless so that hardware is only applied to their workload when query activity is occurring. Bridge Model and Pool Model tenants minimize hardware provisioning by sharing database instances across tenants, maximizing use of the compute resource. » [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
