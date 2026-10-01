---
source_url: https://docs.aws.amazon.com/solutions/optimizing-cost-of-amazon-rds-for-mysql/index.html
---

---
title: 'Guidance for Optimizing Cost of Amazon RDS for MySQL'
canonical_url: https://docs.aws.amazon.com/solutions/optimizing-cost-of-amazon-rds-for-mysql/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Optimizing Cost of Amazon RDS for MySQL

## Overview

This Guidance demonstrates how you can optimize costs for applications that access Amazon Relational Database Service (Amazon RDS) for MySQL databases. It uses an in-memory data store to reduce the database load for read-heavy workloads. By caching frequently accessed query results in this high-performance data store, your applications can retrieve data faster, allowing you to reduce the provisioned capacity needed for the Amazon RDS database instance, thereby lowering overall costs.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/optimizing-cost-of-amazon-rds-for-mysql.pdf)

![Architecture diagram](/images/solutions/optimizing-cost-of-amazon-rds-for-mysql/images/optimizing-cost-of-amazon-rds-for-mysql-1.png)

1. **Step 1**: The application, running on Amazon Elastic Compute Cloud (Amazon EC2), AWS Lambda, or Amazon Elastic Container Service (Amazon ECS), writes data to an Amazon Relational Database Service (Amazon RDS) for MySQL database. This approach can be used with any relational database, not just Amazon RDS for MySQL.
1. **Step 2**: Initially, the application reads data directly from the database.
1. **Step 3**: The database query response is then cached in Amazon ElastiCache.
1. **Step 4**: For subsequent read requests involving the same query, the application retrieves data from ElastiCache instead of the database.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/amazon-elasticache-caching-for-amazon-rds/tree/main/guidance)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

You can optimize your operations by taking advantage of the fast query retrieval capabilities and the in-memory data store of ElastiCache. Also, by offloading repetitive queries from Amazon RDS to ElastiCache, you can free up resources for additional workloads, allowing your applications to respond swiftly to user demands while delivering a seamless and responsive experience. This powerful combination of data retrieval for ElastiCache and the robust database capabilities of Amazon RDS helps ensure that your applications can handle high traffic and demanding workloads without compromising on performance or user experience. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Safeguard your data with ElastiCache and Amazon RDS for MySQL. These services offer robust security features, so your sensitive information remains protected. ElastiCache supports encryption in transit and at rest, with your data encrypted both during transmission and while stored. Additionally, ElastiCache is compliant with industry-leading security standards such as the Federal Risk and Authorization Management Program (FedRAMP), Service Organization Control (SOC), and the Health Insurance Portability and Accountability Act (HIPAA). [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

In the event of disruptions to Amazon RDS, ElastiCache can serve as an additional source of data, providing a reliable fallback until Amazon RDS resumes normal operations. Also, with the high-performance data retrieval capabilities of ElastiCache, your applications remain available and responsive, even during unexpected events. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

ElastiCache can serve query results in sub-millisecond timeframes, outperforming traditional database caching, making it the ideal choice for workloads where speed of data retrieval is paramount. Moreover, ElastiCache is highly scalable, allowing you to seamlessly scale your in-memory data store to handle increasing traffic and data volumes without compromising performance. It supports consistent low-latency data retrieval even under heavy loads, including large datasets. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

ElastiCache delivers a cost-effective caching solution by eliminating the need for additional hardware and storage resources, offering a significantly lower cost model compared to traditional database caching. By replacing Amazon RDS read replicas with ElastiCache, you can achieve substantial cost savings without compromising performance. Furthermore, ElastiCache provides flexible pricing options, including instance-based and serverless models, allowing you to align your costs with your evolving business requirements. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

ElastiCache and Amazon RDS for MySQL help you achieve high performance with an optimized hardware footprint, reducing energy consumption and environmental impact. These AWS services allow you to attain the same or better performance levels while utilizing fewer physical resources for powering and cooling your data storage environments. By minimizing the infrastructure overhead, you can contribute to a more sustainable future for your business and the planet without compromising on scalability or performance. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Blog**: Optimize cost and boost performance of RDS for MySQL using Amazon ElastiCache for RedisThis blog post demonstrates how you can optimize your relational database costs with in-memory caching using Amazon ElastiCache.

[Read usage guidelines](/solutions/guidance-disclaimers/)
