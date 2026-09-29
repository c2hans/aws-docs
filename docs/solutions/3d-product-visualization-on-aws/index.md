---
source_url: https://docs.aws.amazon.com/solutions/3d-product-visualization-on-aws/index.html
---

---
title: 'Guidance for 3D Product Visualization on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/3d-product-visualization-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for 3D Product Visualization on AWS

## Overview

This guidance demonstrates how to integrate real-time 3D product visualization capabilities into websites using Amazon GameLift Streams, enabling businesses to create immersive digital experiences where customers can explore, customize, and interact with products in real-time. The implementation leverages AWS CodePipeline to manage the application build process, while AWS Lambda@Edge acts as an intermediary between the website frontend and streaming services. Website visitors access high-fidelity, scalable 3D experiences through Amazon CloudFront, which efficiently delivers cached files or retrieves them from Amazon S3 as needed. This comprehensive solution works across devices without requiring specialized hardware, resulting in more confident purchasing decisions, reduced return rates, and typically 30-40% higher conversion rates compared to static images. By implementing this guidance, you can create compelling product experiences that enhance customer engagement, transform online shopping into an interactive process, and boost conversion rates on your website while leveraging AWS's robust infrastructure that automatically scales during traffic fluctuations.

## Benefits

### Enhance customer engagement

Embed interactive 3D product visualizations directly into your website, allowing customers to explore products from every angle. This immersive experience helps increase conversion rates by giving customers confidence in their purchase decisions.

### Streamline development workflows

Deploy a fully automated CI/CD pipeline using AWS CodePipeline and CodeBuild to simplify application updates and maintenance. Your team can focus on creating compelling 3D experiences while AWS services handle the infrastructure management and deployment processes.

### Scale visualization capabilities

Meet varying demand with Amazon GameLift Streams' ability to automatically scale rendering resources as website traffic fluctuates. Your customers receive consistent, high-quality 3D visualization experiences even during peak traffic periods without requiring powerful client hardware.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/3d-product-visualization-on-aws.pdf)

![Architecture diagram](/images/solutions/3d-product-visualization-on-aws/images/3d-product-visualization-on-aws-1.png)

1. **Step 1**: Download the source code to start the application build.
1. **Step 2**: AWS CodePipeline orchestrates the download and AWS CodeBuild build invocations.
1. **Step 3**: AWS CodeBuild environments reside in Amazon Elastic Container Registry.
1. **Step 4**: AWS CodeBuild stores the compiled application in Amazon Simple Storage Service (Amazon S3) and updates streaming configuration files for Amazon GameLift Streams.
1. **Step 5**: Visitors access the website through the Amazon CloudFront distribution URL.
1. **Step 6**: Amazon CloudFront returns the cached website (which is or includes the build output of the application) or retrieves the files from Amazon S3.
1. **Step 7**: AWS Lambda@Edge serves as middleware between the website front end and Amazon GameLift Streams.
1. **Step 8**: Product visualizer application initializes after all the website files have loaded. The Amazon GameLift Streams session starts at the behest of the application's business logic.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-realtime-3d-product-visualization-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
