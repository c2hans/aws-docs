---
source_url: https://docs.aws.amazon.com//solutions/dynamic-image-transformation-for-amazon-cloudfront//index.html
---

# Dynamic Image Transformation for Amazon CloudFront

Transform, optimize, and deliver images in real time at a fraction of the cost

- **Version**: 8.1.0
- **Released**: 8/2026
- **Author**: AWS
- **Est. deployment time**: 15 mins
- **Estimated cost**: [See details](/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/cost.html)

## Overview

Dynamic Image Transformation for Amazon CloudFront (formerly Serverless Image Handler) enables real-time image processing through the global content delivery network (CDN) of Amazon CloudFront. This AWS Solution helps you automatically optimize visual content delivery while significantly reducing operational costs and complexity. By dynamically transforming a single source image on-demand, it eliminates the need to store multiple versions of the same image, resulting in substantial storage savings. This solution also enhances the user experience through faster load times with improved caching, while providing robust security controls to protect against inappropriate content, including URL signing, request validation, and content moderation features.

## Benefits

### Streamlined image optimization

Transform and optimize images in real-time through simple API requests or pre-defined transformation policies.

### Cost-effective storage management

Automatically serve the most efficient image size and format based on device type and browser capabilities, helping ensure optimal file size and quality, and eliminating the need to manage and store multiple versions of the same image.

### Advanced security controls

Protect visual assets with URL signing, request validation, and content moderation features while maintaining granular access controls over your image delivery.

### Scalable architecture

Automatically handle varying loads with serverless architecture, enabling consistent performance during traffic spikes without managing infrastructure.

## How it works

### ECS Architecture

This solution provides secure, scalable, dynamic image transformation capabilities using a serverless containerized AWS architecture. It leverages a Amazon CloudFront Functions for request and response normalization, with requests routed through Application Load Balancer to Amazon ECS Fargate containers that perform the image processing. The containerized workload pulls the source images from Amazon S3 or external origins and integrates with Amazon Rekognition for AI-powered transformations like smart-cropping. The architecture includes a comprehensive management interface built on AWS Amplify and secured by Amazon Cognito, with API Gateway, Lambda, and DynamoDB for configuration management. Amazon CloudFront provides edge caching for optimized delivery.

[Open implementation guide](/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/solution-overview.html)Step 1An Amazon CloudFront distribution provides global caching and content delivery.

Step 2An Application Load Balancer (ALB) distributes incoming requests across multiple ECS tasks for high availability and scalability.

Step 3Amazon Elastic Container Service (ECS) tasks running on AWS Fargate process image transformation requests using containerized applications.

Step 4ECS tasks maintain in-memory caches of transformation policies and origin mappings for fast request resolution and reduced latency.

Step 5Images are retrieved from multiple origin types: Amazon S3 buckets or external HTTP-accessible domains based on configured origin mappings.

Step 6An administrative interface built with AWS Amplify provides policy and origin management capabilities through a secure web interface.

Step 7Amazon DynamoDB stores transformation policies, origin configurations, and mapping rules with high availability and performance.

Step 8Amazon Cognito provides authentication and authorization for the administrative interface.

Step 9(Optional) Amazon Rekognition integration for smart cropping and content moderation features.

### Lambda Architecture

This solution enables secure, scalable, dynamic image transformations using a serverless AWS architecture. It starts with CloudFront Functions for request and response normalization, uses API Gateway and Lambda for image processing, integrates with Rekognition for AI-powered features, and stores images in S3. Request signing validation is handled through Secrets Manager, while CloudFront provides edge caching for optimized delivery.

[Open implementation guide](/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/solution-overview.html)Step 1An Amazon CloudFront distribution provides a caching layer to reduce the cost of image processing and the latency of subsequent image delivery.

Step 2Amazon API Gateway provides endpoint resources and initiates the AWS Lambda function.

Step 3A Lambda function retrieves the image from a customer’s existing Amazon S3 bucket and uses `sharp` to return a modified version of the image to the API Gateway.

Step 4A solution-created S3 bucket provides log storage, separate from your customer-created S3 bucket for storing images.

Step 5(Optional) If you enter `Yes` for the **Enable Signature** template parameter, the Lambda function retrieves the secret value from your existing AWS Secrets Manager secret to validate the signature.

Step 6(Optional) If you use the smart crop or content moderation features, the Lambda function calls Amazon Rekognition to analyze your image and returns the results.

Step 7The viewer request is proxied through an Amazon CloudFront function to normalize headers and query parameters for improved cache hit rates.

## Deploy with confidence

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Follow a step-by-step guide in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.

[AWS Launch Wizard](https://us-east-1.console.aws.amazon.com/launchwizard/home?region=us-east-1&redirectId=SolutionWeb#/deployment/create/SO0023)

## Deployment options

- **Implementation guide**: Follow the implementation guide for step-by-step actions to deploy this AWS Solution.

[Download guide](/pdfs/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/Dynamic%20Image%20Transformation%20for%20Amazon%20CloudFront.pdf#solution-overview)

- **Source code**: The source code for this AWS Solution is available in GitHub.

[Go to GitHub](https://github.com/aws-solutions/dynamic-image-transformation-for-amazon-cloudfront/)

- **AWS Launch Wizard**: Use AWS Launch Wizard for step-by-step guided deployment.

[Go to Launch Wizard](https://us-east-1.console.aws.amazon.com/launchwizard/home?region=us-east-1#/deployment/create/SO0023)

- **CloudFormation template (ECS)**: View or modify the CloudFormation template to customize your deployment.

[Download template](https://solutions-reference.s3.amazonaws.com/dynamic-image-transformation-for-amazon-cloudfront/latest/dynamic-image-transformation-for-amazon-cloudfront-ecs.template)

- **CloudFormation template (Lambda)**: View or modify the CloudFormation template to customize your deployment.

[Download template](https://solutions-reference.s3.amazonaws.com/dynamic-image-transformation-for-amazon-cloudfront/latest/dynamic-image-transformation-for-amazon-cloudfront-lambda.template)

## Related content

- **Fast and Cost-Effective Image Manipulation**: This blog explores AWS EC2 instance storage, focusing on temporary block-level storage for instances, ideal for temporary data or caches.

[Learn more](https://aws.amazon.com/blogs/architecture/fast-and-cost-effective-image-manipulation-with-serverless-image-handler/)

- **Perpetual**: Find out how Perpetual delivered a simple, cost-effective approach to image optimization for its client by using an AWS Solution.

[Learn more](https://aws.amazon.com/solutions/case-studies/perpetual-simplifies-dynamic-image-optimization-using-solutions-on-aws/)

- **Solving with AWS Solutions**: This video discusses AWS services and Sharp for efficient, scalable, cost-effective image processing with Amazon CloudFront and S3 for global delivery and storage.

[Learn more](https://youtu.be/oVDh7qPTk18)

## Customer stories

### Fotaflo

"Getting a working test version only took a couple of days. Within 2 weeks we launched in production and had migrated 75% of our image transformations at roughly ¼ of the cost we were previously paying the third-party service. On top of that, we still don't need to worry about maintaining the pipeline infrastructure or scaling servers due to the Amazon CloudFront, Amazon S3, and AWS Lambda architecture. Now our product team can get back to thinking about what more we can do with photos rather than how we can reduce the costs associated with transforming them."

**Martin Eckart Systems Architect, Fotaflo**

### Map Your Show

"At Map Your Show we manage thousands of images across web-based exhibitor profiles and mobile apps. By using Dynamic Image Transformation for CloudFront, we've simplified our image collection process and improved exhibitor platform onboarding time by 37%. The solution has been instrumental in helping us deliver high-performance, dynamically transformed images at scale— all without the need to manage multiple variants or maintain additional infrastructure." **Drew Martin, VP of Technology, Map Your Show**

### Perpetual

“Dynamic Image Transformation for Amazon CloudFront has proven it can scale globally while keeping availability high and image delivery efficient. For us, it’s been a complete solution for handling image optimization and delivery.”

**Vishal Gandhi, CTO, Perpetual**

### Mwave

Since moving to Amazon CloudFront, Mwave has recorded a 15% improvement in website performance, with Dynamic Image Transformation (DIT) delivering smaller image sizes and higher cache hit ratios on image-heavy pages.

**[Mwave](https://aws.amazon.com/solutions/case-studies/mwave-case-study/)**

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/dynamic-image-transformation-for-amazon-cloudfront/latest/rss.xml)
