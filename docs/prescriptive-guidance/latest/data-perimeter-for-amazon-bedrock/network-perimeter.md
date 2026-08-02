---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/network-perimeter.html
---

# Network perimeter
<a name="network-perimeter"></a>

The network perimeter for Amazon Bedrock addresses the unique challenges of AI workloads where prompts and responses contain sensitive data that must be protected in transit. Unlike traditional API calls with predictable payloads, AI interactions involve variable-length content that might inadvertently contain confidential information.

This diagram is a high level illustration of a network perimeter.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/images/guide-img/4f7d8782-326c-45ca-95dd-0c4e97e42271/images/eb548adf-bae9-4725-ad50-3ad5d54ec150.png)

Figure 3.3 High level illustration of a network perimeter

1. SCP denies Amazon Bedrock, Amazon S3, OpenSearch and other operations not originating from VPC endpoint

1. Using Amazon VPC endpoints denies access to external untrusted resources

1. SCP denies Amazon Bedrock operations outside approved regions

1. Resource policies allow access only from known Amazon VPC endpoints

1. AWS security groups isolate AI workloads in dedicated subnets with HTTPS-only access to Amazon VPC endpoints

This section covers the essential network security controls for Amazon Bedrock:
+ VPC endpoint enforcement - Implementing SCP controls to enforce private connectivity
+ Network segmentation for AI workloads - Isolating AI processing from other network traffic
+ Regional boundary enforcement - Implementing data residency and geographic restrictions
+ Monitoring network access patterns - Detecting anomalous network behavior in AI workloads
+ Network access control lists - Subnet-level network filtering for AI workloads
+ Knowledge base network controls - Network access controls for knowledge base resources
+ VPC endpoint network controls - Network-based Amazon VPC endpoint access restrictions
+ Best practices - Network perimeter implementation recommendations and guidelines

Each subsection provides practical implementation guidance for securing AI workloads at the network level.

**Note**
These network security configurations provide baseline patterns but may not suit all infrastructure architectures or compliance requirements. Adapt the examples to your specific network topology, traffic patterns, and data residency obligations. Validate that network controls don't disrupt legitimate AI operations and consult Amazon VPC and networking documentation for the latest features and best practices.
