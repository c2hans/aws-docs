---
source_url: https://docs.aws.amazon.com/solutions/open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws/index.html
---

---
title: 'Guidance for Open Source 3D Reconstruction Toolbox for Gaussian Splats on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Open Source 3D Reconstruction Toolbox for Gaussian Splats on AWS

## Overview

This Guidance demonstrates how to create high-quality 3D content from real-world objects and environments without requiring specialized 3D modeling expertise, expensive equipment, or time-consuming manual processes for photorealistic asset creation. Users upload input media to Amazon S3, which triggers an automated workflow orchestrated by AWS Step Functions that handles the entire 3D reconstruction pipeline. The process runs on GPU-based compute nodes using either Amazon SageMaker Training Jobs or AWS Batch Jobs with Spot Instances for cost efficiency, automatically selecting the appropriate instance type based on job requirements and notifying users via email when reconstruction completes. You can streamline 3D asset production for e-commerce, digital twins, virtual production, and immersive experiences while scaling to process large volumes of content with automated workflows that eliminate traditional technical and cost barriers.

## Benefits

### Reduce GPU compute costs

Choose between on-demand and spot instance compute paths for your 3D reconstruction jobs. Pay only for GPU resources during active training while serverless components eliminate idle infrastructure costs.

### Automate your 3D reconstruction pipeline

Submit media files and a JSON configuration to trigger a fully orchestrated workflow from input validation through Gaussian Splat generation. Receive email notifications when your 3D assets are ready.

### Deploy with flexible infrastructure tooling

Launch the complete event-driven architecture using AWS CDK or Terraform. Focus on generating 3D content while automated container builds and model deployment handle operational setup.

## How it works

### Event-driven serverless architecture

This Reference architecture shows automated deployment of guidance event-driven, serverless architecture to user accounts

[Download the architecture diagram](downloads/open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws.pdf)Step 1Administrator user deploys guidance to AWS account and Region using AWS Cloud Development Kit (CDK) or Terraform.Step 2The Base AWS Cloud Formation stack to deploy will create all of the AWS resources needed to host the guidance. This includes: Amazon Simple Storage Service (S3) bucket, AWS Lambda functions, an Amazon DynamoDB table, necessary AWS Identity and Access Management (IAM) permissions, Amazon Elastic Container Registry (ECR) image registry, AWS Step Functions State Machine resource ID in AWS Systems Manager Parameter Store, and an Amazon Simple Notification Service (SNS) topic created.Step 3Once the Base AWS Cloud Formation stack has been deployed, the Post Deploy AWS Cloud Formation stack should be deployed. That stack will build a Docker container either locally or using AWS CodeBuild, push it to the Amazon ECR registry, and build and push the preprocessing models used during training (such as for background removal) into Amazon S3 bucket using AWS Lambda.### GPU Accelerated Gaussian Splat Reconstruction

This event-driven, serverless Reference architecture enables the generation of realistic 3D content through cutting-edge, open-source rendering techniques [Download the architecture diagram](downloads/open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws.pdf)

Step 1User authenticates to AWS Identity and Access Management (IAM) via AWS Tools and SDKs.Step 2The input is uploaded to a dedicated Amazon Simple Storage Service (S3) job bucket location. This can be done using a Gradio interface and AWS Software Development Kit (SDK).Step 3Optionally, the solution supports external job submission by uploading a '.JSON' job configuration file and media files into a designated S3 job bucket location.Step 4The job JSON file uploaded to the S3 job bucket will trigger an Amazon Simple Notification Service (SNS) message that will invoke the initialization Job trigger AWS Lambda function.Step 5The Job trigger AWS Lambda function will perform input validation and set appropriate variables for the AWS Step Function State Machine.Step 6The workflow job record will be created in Amazon DynamoDB job table.Step 7The Job trigger AWS Lambda function will invoke an AWS Step Functions State Machine to handle the entire workflow job.Step 8Based on the JSON, the process will use either an Amazon SageMaker Training Job (On-Demand Instance) or AWS Batch Job (Spot Instance) that will be submitted synchronously using the state machine built-in wait until completion mechanism.Step 9The Amazon Elastic Container Registry (ECR) container image and S3 job bucket model artifacts will be used to deploy a new container on a Graphics Processing Unit (GPU) based compute node with an instance type determined by the job JSON configuration.Step 10The container will run the entire pipeline as an Amazon SageMaker training job or AWS Batch job on a GPU compute node.Step 11The Job completion AWS Lambda function will complete the workflow job by updating the job metadata in DynamoDB and notifying the user via email upon completion using Amazon SNS.Step 12Internal workflow parameters are stored in AWS System Manager Parameter Store during guidance deployment to decouple the Job trigger AWS Lambda function and the AWS Step Function State Machine.Step 13Amazon CloudWatch is used to log and monitor the training jobs, surfacing possible errors to the user.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/compute/open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-open-source-3d-reconstruction-toolbox-for-gaussian-splats-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
