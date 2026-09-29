---
source_url: https://docs.aws.amazon.com/solutions/building-a-poc-for-amazon-fsx-for-lustre/index.html
---

---
title: 'Deploy a PoC for Amazon FSx for Lustre'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-poc-for-amazon-fsx-for-lustre/
source: aws-documentation
generated_on: 2026-09-29
---

# Deploy a PoC for Amazon FSx for Lustre

## Overview

This Guidance helps users deploy and configure optimal proof-of-concept (PoC) deployments of Amazon FSx for Lustre through deployment and configuration recommendations in addition to AWS CloudFormation templates. Using this Guidance, users can quickly and easily deploy a PoC environment that allows them to test a high-performance FSx for Lustre file system and Amazon Elastic Compute Cloud (Amazon EC2) instances. This approach helps users evaluate suitability for their workloads across performance, scale, integration, and functional testing, whether they’re using their own applications or the example tools provided.

## Benefits

### Accelerate PoCs of FSx for Lustre

Deploy and evaluate FSx for Lustre capabilities within hours using automated templates. Quickly assess performance benchmarks for your specific workload requirements.

### Simplify the storage evaluation process

Test FSx for Lustre with pre-configured tools or your applications through a streamlined deployment framework. Reduce PoC setup time from weeks to hours.

### Optimize storage costs confidently

Use the templates to evaluate different FSx deployment types (SCRATCH and PERSISTENT-SSD storage, along with standalone or s3-linked FSx file systems) to align with your performance and budget needs. Test actual workloads before full-scale deployment.

## How it works

This architecture diagram illustrates how customers can quickly deploy a proof-of-concept (PoC) environment, allowing them to test Amazon FSx for Lustre with their workload.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-a-poc-for-amazon-fsx-for-lustre.pdf?target=_blank)

![Architecture diagram](/images/solutions/building-a-poc-for-amazon-fsx-for-lustre/images/building-a-poc-for-amazon-fsx-for-lustre-1.png)

1. **Step 1**: The user logs into the AWS Management Console and deploys the proof-of-concept (PoC) template provided in this Guidance, using AWS CloudFormation to create a new stack.
1. **Step 2**: CloudFormation deploys an Amazon Virtual Private Cloud (Amazon VPC).
1. **Step 3**: CloudFormation deploys an Amazon Elastic Compute Cloud (Amazon EC2) instance compute node. This compute node will be used as part of this Guidance to conduct performance, functional, and integration testing with the deployed Amazon FSx for Lustre file system.
1. **Step 4**: CloudFormation configures the EC2 instance with AWS Systems Manager, allowing for Session Manager, a capability of Systems Manager, to secure CLI access to the EC2 instance.
1. **Step 5**: CloudFormation deploys an FSx for Lustre file system.
1. **Step 6**: (Optional) CloudFormation creates an Amazon Simple Storage Service (Amazon S3) bucket and an FSx for Lustre file system configuration to link the S3 bucket as a data repository for automatic import and export of data.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-deploying-a-poc-for-amazon-fsx-for-lustre)

[Read usage guidelines](/solutions/guidance-disclaimers/)
