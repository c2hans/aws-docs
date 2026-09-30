---
source_url: https://docs.aws.amazon.com/solutions/visual-search-on-aws/index.html
---

---
title: 'Guidance for Visual Search on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/visual-search-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Visual Search on AWS

Elevate your ecommerce experience with reverse image lookup

## Overview

This Guidance shows how to create a visual search capability for ecommerce websites, allowing users to upload product images to find visually similar items and improve product discovery. While typically complex, recent technological advancements have made it easier to develop accurate and scalable visual search algorithms. This Guidance explores these new technologies, such as multimodal embedding models, and shows how these technologies can be used to create intuitive visual search features. By generating embeddings from product images and text descriptions, you can add effective visual search functionality to your ecommerce platform.

## How it works

This architecture diagram helps build a simple visual search capability, allowing your users to upload a product image and discover similar looking products from the ecommerce website.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/visual-search-on-aws.pdf)

![Architecture diagram](/images/solutions/visual-search-on-aws/images/visual-search-on-aws-1.png)

1. **Step 1**: A time-based Amazon EventBridge scheduler invokes an AWS Lambda function to populate search indexes with multimodal embeddings and product meta-data.
1. **Step 2**: The Lambda function first retrieves product feed stored as a JSON file in Amazon Simple Storage Service (Amazon S3).
1. **Step 3**: The Lambda function then invokes the Amazon Titan Multimodal Embedding G1 model hosted on Amazon Bedrock to create vector embeddings for each product in the catalog. These embeddings are created based on the primary image and product description for each item in the product catalog.
1. **Step 4**: The Lambda function finally persists these vector embeddings as k-nearest neighbor (k-NN) vectors, along with product meta-data in the vector store, such as Amazon OpenSearch Service, Amazon DocumentDB, or Amazon Aurora. This index is used as the source for semantic image searches.
1. **Step 5**: The user initiates a visual search request through a frontend application by uploading a product image.
1. **Step 6**: The application uses the Amazon API Gateway REST API to invoke a pre-configured proxy Lambda function to process the visual search request.
1. **Step 7**: Optional step for better search results: The Lambda function first generates the caption for the input image using the Anthropic Claude 3.5 Sonnet model hosted on Amazon Bedrock.
1. **Step 8**: The Lambda function then invokes the Titan Multimodal Embeddings model. This model generates a multimodal embedding based on the input image uploaded by the user and the image caption, if one was generated in step 7.
1. **Step 9**: The Lambda function then performs a k-NN search on the vector store index to find semantically similar results for the embedding generated in step 8.
1. **Step 10**: The resultant semantic search results retrieved from the vector store are then filtered to eliminate any duplicate entries. The filtered results are then enriched with product metadata from the search index before being passed back to the API Gateway.
1. **Step 11**: Finally, the response from API Gateway is returned to the client application, which then displays the search results to the end user.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-simple-visual-search-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS X-Ray traces requests as they flow through API Gateway to underlying services such as Lambda and Amazon S3, providing valuable insights into the application's behavior. Simultaneously, Amazon CloudWatch captures metrics and logs from all services involved in the architecture. By visualizing and analyzing these components using X-Ray, along with the metrics and logs collected by CloudWatch, you can efficiently identify performance bottlenecks and troubleshoot requests. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance is configured with a multi-layered approach, combining tightly scoped AWS Identity and Access Management (IAM) policies with the access control of API Gateway and the threat mitigation of AWS WAF. This creates a robust security framework that safeguards the application and its underlying resources from potential security threats. Specifically, IAM policies are scoped down to the minimum permissions necessary for each service to function properly, effectively limiting unauthorized access to resources. Furthermore, API Gateway implements API key-based authorization to control API access and is integrated with AWS WAF for protection against web exploits. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The fully managed, serverless services offer high availability and automatic scaling to meet fluctuating traffic demands. For example, Lambda, Amazon OpenSearch Serverless, API Gateway, and Amazon S3 adjust their capacity dynamically, while Amazon Bedrock supports provisioned throughput, allowing you to select the appropriate model capacity units for your specific traffic volumes. This combination ensures that the application can handle varying loads without failure, minimizing downtime. The high availability and scalability of these services, coupled with the ability to fine-tune the capacity of Amazon Bedrock, create a robust, reliable architecture capable of consistently serving requests even under demanding conditions. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Bedrock and Lambda offer several features to optimize your workloads and enhance performance efficiency. With Amazon Bedrock, you can use provisioned throughput mode to meet high request volumes for real-time inference when on-demand capacity isn't sufficient. Additionally, Amazon Bedrock offers a batch inference capability that is ideal for initial and scheduled bulk embedding creation. Lambda provides provisioned concurrency, which pre-provisions Lambda execution environments for a configured number of instances. This can potentially reduce cold-start occurrences and improve Lambda execution timing, further boosting your application's performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon Bedrock, Amazon S3, and Lambda offer various features to optimize your costs. Amazon Bedrock, as a fully managed service, eliminates operational and management costs associated with deploying, scaling, and managing foundation models. It provides flexible pricing options with on-demand and provisioned throughput modes, allowing you to choose the most cost-effective plan. Amazon S3 offers different storage tiers and lifecycle policies, so you can automate data movement between tiers and optimize storage costs. For compute resources, Lambda is covered by Compute Savings Plans, offering discounted pricing for Lambda executions. You can further optimize Lambda costs by selecting suitable memory and processor configurations. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda, API Gateway, and Amazon S3 scale dynamically with your application's incoming traffic, maximizing resource utilization and limiting the environmental impact. These services are not pre-provisioned, allowing for efficient resource allocation. Lambda allows you to choose optimal memory, storage, and processor configurations, further maximizing resource efficiency. With Amazon S3, you can set lifecycle policies to automatically delete stale objects, reducing unnecessary data storage. The scalability and flexibility of these services help you minimize wasted resources and reduce your overall environmental footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
