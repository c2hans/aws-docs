---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/website-scenario-with-api-engine-and-database-management-system-in-an-on-premises-data-center.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 2.4 Website scenario with API engine and Database Management System in an on-premises data center
<a name="website-scenario-with-api-engine-and-database-management-system-in-an-on-premises-data-center"></a>

 Requirements addressed:
+  **REQ1** (data residency)
+  **REQ4** (availability and durability)

 AWS services – [Amazon Route 53](https://aws.amazon.com/route53/), [Amazon CloudFront](https://aws.amazon.com/cloudfront/), [Amazon API Gateway](https://aws.amazon.com/api-gateway/), [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/), [Amazon S3](https://aws.amazon.com/s3/), [Amazon RDS](https://aws.amazon.com/rds/), and [Amazon VPC](https://aws.amazon.com/vpc/)

![Website scenario with API engine and Database Management System in on-premises](https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/images/website-scenario-with-api-engine.png)

 Website scenario with API engine and Database Management System in on-premises

 Requirements **REQ2** (data protection) and **Customer-REQ1** (reliable connectivity) can be met through complimentary use of Architecture 1.1: [Hybrid network connectivity from a data center to the AWS Cloud](hybrid-network-connectivity-from-a-data-center-to-the-aws-cloud.md).

 Highly available and scalable cloud Domain Name System (DNS) web service Amazon Route 53, as well as Amazon API Gateway and [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS), allow many AWS customers to create web applications with separated data flow scenarios for regulated and unregulated workloads. Sensitive data can stored and processed in an on-premises data center, while other data stored and processed in Web application, hosted in the AWS Cloud. In this example:

1.  The mobile application sends requests to different URLs, depending on regulation requirements (regulated and non-regulated) and content types (static and dynamic). The requests, based on regulatory requirements and content types, are forwarded using a Simple Routing Policy to an on-premises data center in case of regulated workload or dynamic web application content. In any other cases, traffic is routed to the AWS Cloud.

1.  In the on-premises data center, the local API gateway forwards non-regulated data API requests to Amazon API Gateway using a VPC endpoint in the cloud for further processing, or forward the workload to the application, storing and processing data according to regulated rules.

1.  The application processes data and stores it in a local relational database to address data residence requirement **REQ1**.

1.  All database and website data is backed up locally and synced with AWS Region location for failover and durability requirements **REQ4**. For details about database backup and restore, refer to in Architecture 3.2: [Read-replicas in Amazon RDS from on-premises databases](read-replicas-in-amazon-rds-from-on-premises-databases.md).

1.  Non-regulated workloads are handled by Amazon API Gateway and transferred to classic two- or three-layer web applications in public or private VPC subnets through a secured VPC endpoint interface. Static content data requests are processed by Amazon CloudFront and forward to an Amazon S3 bucket, which stores static web application content if needed.

1.  In the case of an unavailable on-premises data center, to address failover and durability requirements **REQ4,** all local data center incoming traffic is forwarded by Amazon Route 53 to Amazon API Gateway, which process requests in read-only mode to address residence requirement **REQ1.**

 This web-oriented architecture could satisfy the following use cases:
+  You need to distribute your web content across Regions to satisfy data locality or data residency requirements.
+  You need to maintain the write/read API part of the web application in a local data center for regulated workload or dynamic content.

 The major benefit of this approach is that the clients can continue to communicate to the back-end over a single endpoint and API.
