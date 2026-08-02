---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/aws-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Services
<a name="aws-services"></a>

 Amazon Web Services (AWS) delivers a scalable cloud computing platform with high availability and dependability, providing the tools that enable you to run a wide range of applications. Helping to protect the confidentiality, integrity, and availability of our customers’ systems and data is of the utmost importance to AWS, as is maintaining customer trust and confidence.

 Similar to other general-purpose IT products such as operating systems and database engines, AWS offers commercial off-the-shelf (COTS) IT services according to IT quality and security standards such as ISO, NIST, SOC and many others. For purposes of this paper, we will use the definition of COTS in accordance with the definition established by FedRAMP, a United States government-wide program for procurement and security assessment. FedRAMP references the US Federal Acquisition Regulation (FAR) for its definition of COTS, which outlines COTS items as:
+  Products or services that are offered and sold competitively in substantial quantities in the commercial marketplace based on an established catalog.
+  Offered without modification or customization.
+  Offered under standard commercial terms and conditions.

 Under GAMP guidelines (such as GAMP 5: A Risk-Based Approach to Compliant GxP Computerized Systems), organizations implementing GxP-compliant environments will need to categorize AWS services using respective GAMP software and hardware categories (e.g. Software Category 1 for Infrastructure Software, including operating systems, database managers and security software or Category 5 for custom or bespoke software). Most often, organizations utilizing AWS services for validated applications will categorize them under Software Category 1.

 AWS offers products falling into several categories. Below is a subset of those AWS offerings spanning Compute, Storage, Database, Networking & Content Delivery, and Security and Compliance. A later section of this whitepaper, [AWS Products in GxP Systems](aws-products-in-gxp-systems.md), will provide information to assist you in using AWS services to implement your GxP-compliant environments.

**Table : Subset of AWS offerings by group**

|  Group  |  AWS Products  |
| --- | --- |
|  Compute  |  Amazon EC2, Amazon EC2 Auto Scaling, Amazon Elastic Container Registry, Amazon Elastic Container Service, Amazon Elastic Kubernetes Service, Amazon Lightsail, AWS Batch, AWS Elastic Beanstalk, AWS Fargate, AWS Lambda, AWS Outposts, AWS Serverless Application Repository, AWS Wavelength, VMware Cloud on AWS  |
|  Storage  |  Amazon Simple Storage Service (Amazon S3), Amazon Elastic Block Store (Amazon EBS), Amazon Elastic File System (Amazon EFS), Amazon FSx for Lustre, Amazon FSx for Windows File Server, Amazon Glacier, AWS Backup, AWS Snow Family, AWS Storage Gateway, CloudEndure Disaster Recovery  |
|  Database  |  Amazon Aurora, Amazon DynamoDB, Amazon DocumentDB, Amazon ElastiCache, Amazon Keyspaces, Amazon Neptune, Amazon Quantum Ledger Database (Amazon QLDB), Amazon RDS, Amazon RDS on VMware, Amazon Redshift, Amazon Timestream, AWS Database Migration Service  |
|  Networking & Content Delivery  |  Amazon VPC, Amazon API Gateway, Amazon CloudFront, Amazon Route 53, AWS PrivateLink, AWS App Mesh, AWS Cloud Map, AWS Direct Connect, AWS Global Accelerator, AWS Transit Gateway, Elastic Load Balancing  |
|  Security, Identity, and Compliance  |  AWS Identity & Access Management (IAM), Amazon Cognito, Amazon Detective, Amazon GuardDuty, Amazon Inspector, Amazon Macie, AWS Artifact, AWS Certificate Manager, AWS CloudHSM, AWS Directory Service, AWS Firewall Manager, AWS Key Management Service, AWS Resource Access Manager, AWS Secrets Manager, AWS Security Hub CSPM, AWS Shield, AWS Single Sign-On, AWS WAF  |

 Details and specifications for the full portfolio of AWS products are available online at [https://aws.amazon.com/](https://aws.amazon.com/).
