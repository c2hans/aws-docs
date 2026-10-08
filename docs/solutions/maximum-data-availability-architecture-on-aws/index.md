---
source_url: https://docs.aws.amazon.com/solutions/maximum-data-availability-architecture-on-aws/index.html
---

---
title: 'Guidance for Maximum Data Availability Architecture on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/maximum-data-availability-architecture-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Maximum Data Availability Architecture on AWS

## Overview

This Guidance demonstrates how to enhance database resiliency using a Maximum Data Availability Architecture (MD2A). It introduces MD2A, a data platform that uses APIs and SDKs to deliver full-stack resiliency from the user interface to the database layers. With advanced cloud database technologies, the platform is used to replicate data across multiple geographic locations for continuous operations with minimal downtime. High-performance storage engines provide low-latency, cross-regional availability, while modern NoSQL databases enable efficient data access worldwide. By automating database management tasks and eliminating administration needs, this approach significantly improves application responsiveness and the user experience for global applications. The MD2A can be extended to incorporate various cloud data products, making it a flexible solution for organizations seeking to build more resilient data architectures that support continuous operations and improve global application performance.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/maximum-data-availability-architecture-on-aws.pdf)

![Architecture diagram](/images/solutions/maximum-data-availability-architecture-on-aws/images/maximum-data-availability-architecture-on-aws-1.png)

1. **Step 1**: A consumer or API accesses the application, protected by AWS WAF and AWS WAF Bot Control rules.
1. **Step 2**: Amazon Aurora is deployed in multiple Availability Zones (Multi-AZ) or configured with an Amazon Aurora Global Database.
1. **Step 3**: Amazon DynamoDB provides a global table, replicated between two AWS Regions.
1. **Step 4**: The resilient data platform extends up the application stack. To use this resilient data platform, the application code must implement a capable and resilient connection pool.
1. **Step 5**: The Transaction Queue Code will automatically detect Aurora availability changes and process all cached transactions accordingly.
1. **Step 6**: The Maximum Data Availability Architecture (MD2A) Data Platform's Backend code intelligently redirects any failing transactions and stores them in the DynamoDB global table.
1. **Step 7**: The application code includes a segregated data access layer in the Application Code that isolates the application logic from the specifics of the various data sources.
1. **Step 8**: Aurora can be patched, upgraded, or completely rebuilt without causing application downtime or transactions loss.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-maximum-data-availability-architecture-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

MD2A uses Aurora Global Database, DynamoDB, Amazon S3 Intelligent-Tiering storage class, global traffic management, as well as an application firewall and balancing infrastructure. These services integrate with the MD2A Data Platform through APIs and SDKs, delivering full-stack resiliency across the user interface, services, and database layers. Aurora Global Database and DynamoDB replicate data across multiple Availability Zones and AWS Regions for continuous operations and minimal downtime. They automate database management tasks like backups, patching, and failover. The high-performance storage engine of Aurora provides low-latency, cross-Regional availability, improving application responsiveness. DynamoDB, a fully managed NoSQL database, eliminates administration needs. Its global tables feature enables low-latency data access from multiple Regions, enhancing the user experience for global applications. Together with MD2A, these services can be instrumented to track performance, usage, and effectiveness. They can also automate changes and deployments, reducing the risk of human error and accelerating delivery. Finally, MD2A can accommodate various security best practices and compliance standards while protecting sensitive data. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

MD2A, being a data-intensive platform, requires robust security measures to protect user data and ensure seamless operations. AWS WAF Bot Control and AWS Certificate Manager (ACM) play crucial roles in enhancing MD2A's user security for bot detection and mitigation, simplified certificate management, and user trust. Specifically, AWS WAF identifies and blocks malicious bots that could harm the platform or steal user data; it also protects against automated attacks like brute-force attacks, scraping, and distributed denial of service (DDoS) attacks. In addition, ACM reduces the risk of certificate expiration; by using valid Amazon issued and signed TLS certificates, MD2A can establish a trusted connection with users, supporting the security of their interactions with the platform. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Elastic Load Balancing (ELB) distributes incoming traffic across multiple instances, supporting high availability and fault tolerance while optimizing resource utilization. AWS Auto Scaling automatically adjusts the number of instances based on demand, preventing performance degradation during peak usage and maintaining cost-efficiency. Amazon CloudWatch provides near real-time insights and alerts for proactive issue resolution. For data management, Aurora Global Database replicates data across multiple Availability Zones and Regions for data durability and controlled low latency. Similarly, DynamoDB Global Tables enable globally distributed data access with low latency, replicating data across multiple Regions for high availability and data durability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Aurora Global Database provides low-latency access to relational data across Regions, reducing read latencies for global applications. DynamoDB Global Tables improve efficiency through rapid, consistent read and write operations across globally distributed data, minimizing latency for worldwide users. Amazon Global Accelerator, paired with ELB, improves performance by intelligently routing traffic to the nearest entry point, reducing network hops and latency. The global DNS infrastructure of Amazon Route 53 swiftly resolves domain names and routes users to the closest content servers. Together, these services optimize application responsiveness and resource utilization, supporting overall performance efficiency in global deployments. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The MD2A Data Platform uses several tools to optimize costs effectively. Auto Scaling automatically adjusts resources based on demand, minimizing waste and reducing expenses. AWS Budgets allows setting predefined spending limits and sends alerts to prevent cost overruns. For detailed financial analysis, AWS Cost Explorer provides in-depth visibility into usage patterns and expenditures, helping identify cost-saving opportunities. These tools work together to enable accurate cost forecasting, promote efficient resource utilization, and support informed decision-making for ongoing cost optimization. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

MD2A can help users significantly reduce their carbon footprint through cloud computing and AWS managed services. Specifically, AWS data centers employ highly energy-efficient practices, including advanced cooling technologies and renewable energy sources; the commitment to sustainability by AWS extends to waste reduction and resource optimization. AWS Managed Services were specifically chosen to support sustainability for three key reasons: First, they reduce the physical infrastructure footprint, minimizing the need for on-premises hardware. Second, these services provide scalability and efficiency through rightsizing so that resources are used optimally. Finally, the sustainable practices of AWS align with the MD2A Data Platform goal to minimize environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
