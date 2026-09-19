---
source_url: https://docs.aws.amazon.com//solutions/product-attribution-and-personalization-using-amazon-bedrock//index.html
---

---
title: 'Guidance for Product Attribution and Personalization using Amazon Bedrock'
canonical_url: https://docs.aws.amazon.com/solutions/product-attribution-and-personalization-using-amazon-bedrock/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Product Attribution and Personalization using Amazon Bedrock

## Overview

This Guidance demonstrates how to address the challenge of enriching product catalogs with contextual attributes and personalized descriptions by using computer vision and AI to analyze product images and generate tailored content for different customer segments. Retailers can upload product images for multi-modal analysis that automatically identifies not just standard specifications, but also contextual attributes like occasion, style descriptors, and even colloquial terms such as "kicks" for shoes. The AI then categorizes products and creates personalized descriptions tailored to distinct shopper personas, transforming a single product into multiple compelling narratives. You can move beyond basic product specifications to deliver personalized, contextually rich content that resonates with each unique customer segment.

## Benefits

### Accelerate product catalog enrichment automatically

Deploy AI-powered image analysis to generate contextual product attributes and personalized descriptions at scale. Reduce manual content creation effort while improving product discoverability with modern, customer-relevant terminology.

### Enhance customer engagement with personalization

Leverage generative AI to create tailored product descriptions that resonate with individual shoppers. Transform static catalog data into dynamic, context-aware content that drives conversion and customer satisfaction.

### Scale seamlessly with serverless architecture

Build on fully managed AWS services that automatically handle variable workloads without infrastructure management. Focus your resources on customer experience while AWS manages the underlying compute, storage, and AI capabilities.

## How it works

This architecture diagram shows how to use computer vision and AI to assign rich attributes to products that go beyond basic specifications. AI adds contextual attributes like occasion, style descriptors, and even slang terms like "kicks" for shoes, then generates personalized product descriptions using the generated attributes combined with customer context. [Download the architecture diagram.](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/product-attribution-and-personalization-using-amazon-bedrock.pdf)

![Architecture diagram for Product Attribution and Personalization using Amazon Bedrock](/images/solutions/product-attribution-and-personalization-using-amazon-bedrock/images/product-attribution-and-personalization-using-amazon-bedrock.png)

1. **Step 1**: Users access the app via Amazon CloudFront with Lambda@Edge routing. They upload product images, search products, and receive personalized descriptions using data from Amazon DynamoDB.
1. **Step 2**: User authentication is handled by Amazon Cognito for secure session management.
1. **Step 3**: Amazon CloudFront serves the static web frontend assets from an Amazon S3 bucket.
1. **Step 4**: API requests route through Amazon API Gateway (REST API) to backend AWS Lambda functions.
1. **Step 5**: Six Lambda functions: options, session, generate (multi-modal image analysis via Bedrock), sku (product categorization via Bedrock), products (personalized descriptions via Bedrock), and chat (conversational AI via Bedrock).
1. **Step 6**: Each AWS Lambda function reads and writes to dedicated Amazon DynamoDB tables for sessions, options, prompts, and chat history.
1. **Step 7**: Product and input images are stored in dedicated Amazon S3 buckets accessed by the generate and products functions.
1. **Step 8**: The chat, generate, SKU, and products functions leverage Amazon Bedrock, a fully managed service that provides foundation models with security and responsible AI capabilities.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-product-attribution-and-personalization-using-amazon-bedrock)

[Read usage guidelines](/solutions/guidance-disclaimers/)
