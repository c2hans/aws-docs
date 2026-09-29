---
source_url: https://docs.aws.amazon.com//solutions/generative-ai-powered-visual-inspection-on-aws//index.html
---

---
title: 'Guidance for Generative AI-Powered Visual Inspection on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/generative-ai-powered-visual-inspection-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Generative AI-Powered Visual Inspection on AWS

## Overview

This Guidance shows how to automate equipment detection and installation verification tasks that traditionally require extensive manual effort by applying foundation models to on-site visual inspection workflows. When reference images and bill of materials are uploaded, foundation models generate detailed descriptions of each component and create module-specific detection rules. Field technicians then capture images during on-site inspections, and the system compares what appears in the photo against expected components for that module, identifying detected items and flagging anything missing in real time through a mobile interface. You can reduce inspection time, minimize human error in component validation, and ensure installation completeness without requiring technicians to manually cross-reference complex equipment lists.

## Benefits

### Reduce inspection errors with generative AI

Verify installed components against reference images and bill of materials data using Amazon Bedrock. Catch missing or incorrect items that manual checks routinely overlook.

### Accelerate field verification workflows

Enable technicians to photograph assemblies and receive near real-time detection results on mobile devices. Cut inspection cycle times while maintaining consistent quality standards across sites.

### Adapt detection rules without retraining models

Generate module-specific detection rules and false positive patterns automatically from your product data. Update inspection criteria as components change without custom model development.

## How it works

This architecture diagram illustrates how to effectively support on-site visual inspection and verification on AWS. It shows the key components and their interactions, providing an overview of the architecture's structure and functionality. [Download the architecture diagram.](downloads/generative-ai-powered-visual-inspection-on-aws.pdf)

![Architecture diagram for Generative AI-Powered Visual Inspection on AWS](/images/solutions/generative-ai-powered-visual-inspection-on-aws/images/generative-ai-powered-visual-inspection-on-aws.png)

1. **Step 1**: Admin uploads images of products and bill of material (BOM) to Amazon Simple Storage Service bucket.
1. **Step 2**: Item description generation pipeline AWS Lambda is triggered to process each reference image with Amazon Bedrock Claude Sonnet model and generates a reference rich and detailed description of the image.
1. **Step 3**: Descriptions are combined with BOM data to generate module specific detection rules. Additional rules for common false positive patterns are generated for improved accuracy.
1. **Step 4**: Descriptions and specific detection rules are stored in Amazon S3 and synced to Amazon DynamoDB table.
1. **Step 5**: The detection pipeline is triggered when a user uploads the image to Amazon S3 while performing an on-site visual inspection.
1. **Step 6**: A AWS Lambda function is triggered and prepares the context with the uploaded image and target module, retrieving relevant reference descriptions and detection rules from DynamoDB to provide context to the model (RAG approach).
1. **Step 7**: Amazon Bedrock Nova Pro performs the detection task and outputs results to Amazon S3 and DynamoDB.
1. **Step 8**: Detection results are retrieved by the mobile client through Amazon API Gateway, with all the items detected. User can move to next module for verification or restart the detection by taking a different picture to detect the missing items.
## Related content

- **How Amazon uses Amazon Nova models to automate operational readiness testing for new fulfillment centers**: Learn how Amazon uses Amazon Nova models to automate visual inspection and operational readiness testing.

[Read the blog](https://aws.amazon.com/blogs/machine-learning/how-amazon-uses-amazon-nova-models-to-automate-operational-readiness-testing-for-new-fulfillment-centers/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
