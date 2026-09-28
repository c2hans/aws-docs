---
source_url: https://docs.aws.amazon.com/solutions/personalized-retail-seller-listings-on-aws/index.html
---

---
title: 'Guidance for Personalized Retail Seller Listings on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/personalized-retail-seller-listings-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Personalized Retail Seller Listings on AWS

## Overview

This Guidance helps retail sellers accelerate product listing creation and management on e-commerce platforms by automating the extraction and generation of product information from PDF manuals and images using AI. Sellers upload product manuals and images through a web interface, and Amazon Bedrock Data Automation extracts structured data such as specifications, features, warranty information, and visual descriptions from these files. An Amazon Bedrock LLM then merges the extracted information to generate compelling product descriptions, create highlights, and produce optimized search keywords, with real-time job status tracking throughout the entire process. You improve customer experience and drive sales through high-quality, consistent product listings while dramatically reducing the manual effort required to create and optimize product content for search engine visibility.

## Benefits

### Accelerate time-to-market for listings

Automate extraction of product specifications, features, and visuals from technical documents and images. Reduce hours of manual copywriting to minutes with AI-powered content generation.

### Improve product discoverability at scale

Generate SEO-optimized descriptions, highlights, and search keywords consistently across your entire catalog. Enable your marketing teams to focus on strategy instead of manual content creation.

### Scale without infrastructure management

Process varying volumes of product listings with an event-driven, pay-per-use architecture that scales to zero when idle. Eliminate fixed infrastructure costs while maintaining near real-time processing.

## How it works

This architecture diagram illustrates how e-commerce and marketing teams can automate extracting information from technical documents and product images to generate optimized product descriptions and listings for search. [Download the architecture diagram.](downloads/personalized-retail-seller-listings-on-aws.pdf)

![Architecture diagram for Personalized Retail Seller Listings on AWS](/images/solutions/personalized-retail-seller-listings-on-aws/images/personalized-retail-seller-listings-on-aws.png)

1. **Step 1**: You authenticate through Amazon Cognito User Pool via Amazon CloudFront, then select PDF manuals and product images to upload through the web interface, with static assets in Amazon Simple Storage Service.
1. **Step 2**: Amazon API Gateway routes your request to upload-handler AWS Lambda, which creates a job record in Amazon DynamoDB and returns pre-signed S3 URLs for direct file upload.
1. **Step 3**: You upload files directly to S3 raw bucket. Amazon EventBridge captures ObjectCreated events and triggers queue-processor Lambda, which verifies uploads and sends messages to Amazon Simple Queue Service.
1. **Step 4**: Extract-product-info Lambda (triggered by Amazon SQS) invokes Amazon Bedrock Data Automation to extract structured data from PDFs (specifications, features, instructions, warranty) and images (visual features, descriptions, brand information).
1. **Step 5**: Extraction results are saved to S3 processed bucket with metadata in DynamoDB. EventBridge receives ExtractionComplete event and triggers merge-product-data Lambda.
1. **Step 6**: Merge-product-data Lambda retrieves extracted JSON files from Amazon S3 and job details from DynamoDB, then invokes Amazon Bedrock LLM to merge information, generate descriptions, create highlights, and generate search keywords.
1. **Step 7**: Unified product data is saved to S3 merged bucket and DynamoDB products table with complete information and images.
1. **Step 8**: You monitor job status (PENDING, PROCESSING, EXTRACTING, MERGING, COMPLETED, FAILED) through API Gateway polling DynamoDB, then view product lists and details retrieved from Amazon S3 and DynamoDB.
1. **Step 9**: For each product image, API Gateway routes requests to product-image Lambda, which generates pre-signed S3 URLs for secure carousel display.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-personalized-retail-seller-listings-on-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
