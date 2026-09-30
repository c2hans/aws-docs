---
source_url: https://docs.aws.amazon.com/solutions/deploying-enterprise-apps-with-netapp-bluexp-workload-factory-for-aws-and-amazon-fsx-for-netapp-ontap/index.html
---

---
title: 'Guidance for Deploying Enterprise Apps with NetApp BlueXP Workload Factory for AWS and Amazon FSx for NetApp ONTAP'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-enterprise-apps-with-netapp-bluexp-workload-factory-for-aws-and-amazon-fsx-for-netapp-ontap/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Deploying Enterprise Apps with NetApp BlueXP Workload Factory for AWS and Amazon FSx for NetApp ONTAP

## Overview

This Guidance demonstrates how to use NetApp BlueXP Workload Factory for AWS, a software as a service (SaaS) framework that connects Amazon FSx for NetApp ONTAP data volumes with Amazon Bedrock. It provides step-by-step instructions for implementing Retrieval-Augmented Generation (RAG) workflows, allowing AWS customers to create chatbots that deliver customized responses based on their knowledge base. Users can also embed data into a vector database that integrates with Amazon Bedrock to reveal valuable insights from unstructured enterprise data. This Guidance offers a secure, efficient path to optimizing the capabilities of generative artificial intelligence (AI) for various applications, including RAG chatbots and SQL deployment assistants.

## How it works

This architecture diagram shows how to connect your Amazon FSx for NetApp ONTAP data with Amazon Bedrock to provide your team access to your knowledge base.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-enterprise-apps-with-netapp-bluexp-workload-factory-for-aws-and-amazon-fsx-for-netapp-ontap.pdf)

![Architecture diagram](/images/solutions/deploying-enterprise-apps-with-netapp-bluexp-workload-factory-for-aws-and-amazon-fsx-for-netapp-ontap/images/deploying-enterprise-apps-with-netapp-bluexp-workload-factory-for-aws-and-amazon-fsx-for-netapp-ontap-1.png)

1. **Step 1**: The user deploys the NetApp BlueXP Workload Factory for AWS application into their AWS account, running on an Amazon Elastic Compute Cloud (Amazon EC2) instance.
1. **Step 2**: The NetApp BlueXP Workload Factory for AWS connects to specified source data volumes (Data 1, Data 2) residing in Amazon FSx for NetApp ONTAP. This data can originate from on-premises or the AWS Cloud. The NetApp BlueXP Workload Factory for AWS monitors for source data updates, such as new files added, and ingests those data changes.
1. **Step 3**: The user selects an available Large Language Model (LLM) supported by the NetApp BlueXP Workload Factory for AWS to be used by Amazon Bedrock for response generation.
1. **Step 4**: The NetApp BlueXP Workload Factory for AWS initiates the embedding process using the Amazon Titan in Amazon Bedrock LLM.
1. **Step 5**: The NetApp BlueXP Workload Factory for AWS Lance DB open source vector database (DB) component runs on Amazon EC2. This component stores the vector embeddings received from Amazon Bedrock in the vector DB storage within FSx for ONTAP.
1. **Step 6**: The user authenticates through the NetApp BlueXP Workload Factory for AWS application user interface (UI) to Microsoft Active Directory Domain Services using Auth0.
1. **Step 7**: The user sends a text prompt to the NetApp BlueXP Workload Factory for AWS chatbot application.
1. **Step 8**: Based on the user's prompt, the NetApp BlueXP Workload Factory for AWS chatbot retrieves Retrieval-Augmented Generation (RAG) vector data from the documents stored in the accessible data volumes (Data1, Data2).
1. **Step 9**: The NetApp BlueXP Workload Factory for AWS component uses Amazon Bedrock to generate a response based on results from the associated LLM combined with RAG. It then displays the response to the user through its user interface.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

FSx for ONTAP offers resilient, high-performance storage with enterprise features like data replication from on-premises arrays, supporting data integrity and availability. Amazon Bedrock accelerates generative AI application development by providing access to pre-trained models, while Amazon EC2 delivers secure cloud compute capacity. This integration allows for data replication from on-premises to AWS using NetAPP SnapMirror, a software that can quickly replicate snapshot data to one or more storage systems. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

FSx for ONTAP, Amazon Bedrock, and AWS Identity and Access Management (IAM) provide comprehensive security and enhanced user management capabilities. FSx for ONTAP is a managed-file storage service, providing encryption at rest and in transit, along with compliance certifications like HIPAA and FedRAMP. Amazon Bedrock integrates with various AWS security services to secure the use of foundation models within applications; it also supports data encryption in transit and gives users full control over their data. IAM enforces fine-grained access controls, allowing administrators to implement the principle of least privilege. Finally, as an independent software vendor (ISV) application running within the user's account, this Guidance prevents data leakage from the user's environment. The combination of these services, along with the identity-based policies of IAM, provides comprehensive security measures and enhanced user management capabilities. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

FSx for ONTAP supports high availability through multiple Availability Zone (AZ) deployment options and offers robust data protection features, including NetApp ONTAP snapshots and integration with AWS Backup, supporting data durability and availability. Amazon Bedrock, as a managed AWS service, reduces downtime risk and maintains consistent performance by using the expertise of AWS in managing complex AI infrastructure. This Guidance, installed on Amazon EC2, allows for easy system restarts or rebuilds during instance maintenance. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

FSx for ONTAP delivers high performance with solid state drive (SSD) support for active data and uses SnapMirror and FlexCache to improve data mobility between on-premises and AWS environments. Amazon Bedrock gives users access to foundation models without having to manage complex infrastructure. This Guidance, installed on Amazon EC2, integrates with AWS Nitro System, a lightweight hypervisor supporting high performance for workloads. This combination of services provides performance efficiency from experimentation to full-scale production deployment. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

FSx for ONTAP offers data efficiency features like deduplication, compression, and compaction, while tiering colder data into a capacity pool reduces storage costs. Amazon Bedrock helps users avoid the expensive process of building and training custom models, significantly reducing development costs. This Guidance also fully utilizes hardware resources for computing, networking, and I/O acceleration, passing savings to users. The efficiency features of FSx for ONTAP directly lower storage costs, often a significant portion of generative AI application expenses. Amazon Bedrock, as a managed service, simplifies AI model development and deployment processes, further reducing associated costs. Lastly, the flexible pricing options of Amazon EC2, including Savings Plans, On-Demand, and Reserved Instances, provide additional avenues for cost optimization. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The services selected for this Guidance were chosen as optimal services for their respective workloads, balancing efficiency and sustainability. By using native AWS managed services, users can benefit from the ongoing commitment to sustainability of AWS, which includes investments in renewable energy and efficient data center designs. This approach allows organizations to reduce their carbon footprint compared to running similar workloads on-premises or with less optimized cloud solutions. The use of these managed services also means that resources are more efficiently shared and utilized across multiple customers, potentially leading to overall energy savings and a more sustainable IT infrastructure. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
