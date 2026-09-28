---
source_url: https://docs.aws.amazon.com/solutions/processing-overhead-imagery-on-aws/index.html
---

---
title: 'Guidance for Processing Overhead Imagery on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/processing-overhead-imagery-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Processing Overhead Imagery on AWS

## Overview

This Guidance demonstrates how to process remote sensing imagery using machine learning models that automatically detect and identify objects collected from satellites, unmanned aerial vehicles, and other remote sensing devices. Satellite images are often significantly larger than standard media files. This Guidance deploys highly scalable and available image processing services that support images of this size. These services collect, process, and analyze the images efficiently, giving you more time to assess and respond to what you discovered in your imagery.

## How it works

This architecture diagram shows how to implement scalable image processing and object detection using machine learning for analysis of remote sensing imagery.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/processing-overhead-imagery-on-aws.pdf)

![Architecture diagram](/images/solutions/processing-overhead-imagery-on-aws/images/processing-overhead-imagery-on-aws-1.png)

1. **Step 1**: The AWS Cloud Development Kit (AWS CDK) enables the deployment and management of custom models into AWS customer environments through Amazon SageMaker hosted model endpoints.
1. **Step 2**: The AWS customer submits an image request to the image request queue with Amazon Simple Queue Service (Amazon SQS).
1. **Step 3**: The model runner task retrieves the image request from the image request queue.
1. **Step 4**: The model runner task queues image Regions into the Region request queue.
1. **Step 5**: The model runner task generates tiles, invokes models, and stores results in state tables in Amazon DynamoDB.
1. **Step 6**: The model runner task aggregates, encodes, and outputs results to Amazon Simple Storage Service (Amazon S3) and Amazon Kinesis.
1. **Step 7**: The AWS customer or data analysts can access and review the aggregated results, including those from Geographic Information Systems (GIS).
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-overhead-imagery-inference-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

We developed internal pipelines that allow you to deploy and validate the software in this Guidance across multiple Regions and stages, helping you to integrate and make changes as needed. This, coupled with our team of engineers specifically tasked with managing this Guidance and responding effectively to any incidents or events, ensures you're consistently well-architected. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

<p>Resources in this Guidance are configured following our Best Practices for Security, Identity & Compliance. It continually undergoes routine security-centric analysis from our own Application Security (AppSec) team.</p> <p>You should be aware that because this system depends on integration with your existing infrastructure and is not managed through a command line interface (CLI), the Guidance doesn’t specifically address authentication and authorization for people and machine access. Instead, it goes through rigorous reviews by our AppSec team to ensure you are not exposed to vulnerabilities when deploying the services as they are designed.</p> [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance is distributed across various Availability Zones and operates on a multi-node Amazon ECS cluster, managed by AWS Fargate, ensuring you have consistent availability. Amazon SQS queues and Amazon SNS topics disseminate job metadata for you to monitor. These provide you with the capability to track the status and progression of your submitted jobs. This Guidance is equipped with comprehensive embedded metrics and dashboards that are deployed standard with the services. A continuous integration/continuous deployment (CI/CD) pipeline is utilized, which consistently constructs, deploys, and authenticates the ongoing releases of this Guidance through internal Amazon procedures. Data persistence and backup can be configured with the AWS Cloud Development Kit (AWS CDK) for all deployed resources. We have incorporated retry policies within our job queues and integrated logic into the code to manage graceful failures or partial completions of job requests, while providing status updates for those requests. Additionally, our Amazon ECS cluster features node failover, enabling other nodes to retry any tasks should a failure occur. Finally, we utilize comprehensive integration and load testing methods to confirm the performance and dependability of this Guidance under a wide range of scenarios. There are constraints you need to be aware of that may affect reliability. When working with extremely slow models against extensive sets of imagery, some calibration is necessary to ensure the optimal performance of this Guidance. This includes managing the models, imagery size, training data, and data sets. Each of these variables dictates how well the model will run. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Default settings are in place to illustrate the basic capabilities for you. These policies enable the service to dynamically scale up or down, according to the influx and speed of incoming job demands. To meet varying workload requirements, from scaling to traffic, and data access patterns, we employ autoscaling constructs within the AWS CDK framework. This allows you to define and manage the application's autoscaling patterns. Importantly, these configurations and options are made readily accessible to you. The location of this Guidance can be selected to decrease latency and improve performance by always running from within a single virtual private cloud (VPC) infrastructure. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance assesses cost by analyzing the resources integral to the architectural framework. By employing load testing, repeated iterations, and data collection, we've chosen our services, along with their resource allotments, according to the demonstrated requirements from what we've heard from our customers. We determine cost based on performance needs and provide the option for you to tailor the service to accommodate your unique mission objectives. This flexibility empowers you to opt for more dynamic scaling policies and larger instance types to enhance performance at a higher cost, or alternatively, to choose less aggressive scaling for cost savings. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Through the use of autoscaling constructs within AWS CDK, we dynamically adjust to match load requirements and ensure efficient resource allocation, thus ensuring that only the necessary minimum resources are deployed at any given time in the Guidance’s framework. All data stores are configured with best practices and patterns abstracted through constructs in AWS CDK. For demonstrative or "test drive" use cases, this Guidance is designed to operate efficiently with minimal allocation of resources, thus reducing the amount of required hardware for provisioning. This is the only instance in which hardware is needed. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Processing Overhead Imagery Against Computer Vision Models**: This sample code orchestrates queue monitoring, tile decomposition, per-tile model invocation, and result aggregation for processing high-resolution satellite images.

[Learn more](https://github.com/aws-solutions-library-samples/osml-model-runner)

- **Tiling Overhead Imagery on AWS**: This sample code efficiently serves satellite imagery tiles for dynamic, high-resolution geographical data visualization.

[Learn more](https://github.com/aws-solutions-library-samples/osml-tile-server)

[Read usage guidelines](/solutions/guidance-disclaimers/)
