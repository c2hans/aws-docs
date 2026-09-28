---
source_url: https://docs.aws.amazon.com/solutions/product-catalog-enhancement-with-generative-ai-on-aws/index.html
---

---
title: 'Guidance for Product Catalog Enhancement with Generative AI on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/product-catalog-enhancement-with-generative-ai-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Product Catalog Enhancement with Generative AI on AWS

## Overview

This Guidance demonstrates how retailers can use generative AI to improve their product catalog management process. By automating the traditionally manual task of processing and standardizing product data from manufacturers, retailers can significantly enhance their operational efficiency. The Guidance addresses the common challenge of handling diverse data formats from multiple manufacturers, transforming this time-consuming process into a streamlined, automated workflow. This approach not only enhances productivity but also helps ensure more consistent and higher-quality product catalog entries, enabling retailers to maintain accurate and up-to-date product information more effectively.

## Benefits

### Accelerate product listing creation

Deploy a serverless workflow that automatically generates SEO-optimized titles, descriptions, and features from raw product data. Focus on product strategy while AI handles content enrichment.

### Enhance customer search experience

Improve product discoverability with AI-enriched catalog data in OpenSearch Serverless. Drive higher conversion rates through more relevant search results and detailed product information.

### Scale catalog operations cost-effectively

Leverage serverless architecture that adapts to your business demand with pay-as-you-go pricing. Eliminate infrastructure management overhead while maintaining high performance during peak periods.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/product-catalog-enhancement-with-generative-ai-on-aws.pdf)

![Architecture diagram](/images/solutions/product-catalog-enhancement-with-generative-ai-on-aws/images/product-catalog-enhancement-with-generative-ai-on-aws-1.png)

1. **Step 1**: The product's raw data, which was created or integrated from your marketplace, is sent individually in a JSON format using Amazon API Gateway.
1. **Step 2**: API Gateway calls an AWS Step Functions workflow, which then invokes four AWS Lambda functions in sequence, using the raw data as parameter. Each function will enrich the data.
1. **Step 3**: The first Lambda function uses the raw data to invoke Amazon Bedrock to generate an improved title.
1. **Step 4**: The second Lambda function uses the raw data to generate an enriched description, considering best practices in search engine optimization and highlighting the product's benefits.
1. **Step 5**: The third Lambda function extracts features commonly used by ecommerce companies. These might include relevant characteristics like material, color, size, weight, dimensions, capacity, compatibility, or functionality.
1. **Step 6**: The last Lambda function creates a JSON file with the product's title, description, and feature list. It then inserts the data into Amazon OpenSearch Serverless.
1. **Step 7**: OpenSearch Serverless acts as an enhanced product catalog for ecommerce. It applies generative AI to its listings to enhanced search results and improve the customer experience.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-product-catalog-enhancement-with-generative-ai-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
