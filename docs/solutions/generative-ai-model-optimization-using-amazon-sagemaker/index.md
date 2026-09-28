---
source_url: https://docs.aws.amazon.com/solutions/generative-ai-model-optimization-using-amazon-sagemaker/index.html
---

---
title: 'Guidance for Generative AI Model Optimization Using Amazon SageMaker'
canonical_url: https://docs.aws.amazon.com/solutions/generative-ai-model-optimization-using-amazon-sagemaker/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Generative AI Model Optimization Using Amazon SageMaker

Optimizing generative AI models for speed and efficiency

## Overview

This Guidance shows how you can optimize your generative AI models using Amazon SageMaker, a service where you can build, train, and deploy large language models (LLMs) at scale. By using advanced optimization techniques like speculative decoding, quantization, and compilation, you can achieve significant performance improvements. These optimizations can deliver higher throughput, lower latency, and reduced inference costs. The streamlined interface in SageMaker abstracts away the complex research and experimentation normally required to optimize generative AI models, allowing you to rapidly develop and deploy high-performing, cost-effective generative AI applications. The provided diagrams illustrate the steps required to configure this application. The first diagram demonstrates how data scientists can optimize large language models (LLMs) within SageMaker. The second diagram outlines the deployment of those optimized LLMs.

## How it works

### Optimization for data scientists

This architecture diagram shows how data scientists can optimize Large Language Models (LLMs) within Amazon SageMaker to deliver responses that are not only faster, but also more accurate and cost-effective. The subsequent tab outlines the deployment of the optimized LLMs in Amazon SageMaker.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/generative-ai-model-optimization-using-amazon-sagemaker.pdf#page=1)Step 1Deploy the optimization toolkit with the AWS CloudFormation template to your AWS account.Step 2Run each of the four Python-based Jupyter notebooks within Amazon SageMaker Studio to configure, optimize, and test the selected foundation model. Host the models and the training data in the Amazon Simple Storage Service (Amazon S3), which serves as the default hosting location.Step 3Fine-tune pre-optimized models in Amazon SageMaker using the Speculative Decoding Model notebook. This model accelerates inference on ml.p4d.24xlarge instances using a faster draft model to predict candidate outputs in parallel.Step 4Improve inference speed by deploying a custom speculative decoding model using the Custom Speculative Decoding Model notebook on ml.p4d.24xlarge instances. Access draft models from the Hugging Face model hub or your own Amazon S3 bucket.Step 5Reduce model memory requirements through quantization, using the Quantized Model notebook on the ml.g5.12xlarge instance. This uses Activation-Aware Weight Quantization (AWQ) to shrink the memory footprint while maintaining quality, enhancing throughput, and reducing latency.Step 6Compile and deploy your tuned models on performance-optimized AWS Inferentia hardware (ml.inf2.48xlarge instances) with the Compiled Model for Inferentia 2 notebook.Step 7Deploy SageMaker endpoints to access your models from applications.### LLM deployment in applications

This architecture diagram shows how to deploy the optimized LLMs in SageMaker, including using AWS CloudFormation to provision all the necessary application resources.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/generative-ai-model-optimization-using-amazon-sagemaker.pdf#page=2)Step 1Deploy all application resources using CloudFormation, including SageMaker endpoints for interacting with optimized large language models (LLMs).Step 2Log in through the application interface.Step 3Host web UI content in Amazon S3. Deliver that content quickly to users in any location through Amazon CloudFront.Step 4Provide a persistent WebSocket connection to the application with Amazon API Gateway.Step 5Authenticate users through Amazon Cognito for every transaction conducted through CloudFront and API Gateway.Step 6Implement business logic through LangChain Orchestrator functions in AWS Lambda to fulfill requests. The Orchestrator retrieves configured LLM options and session information from the Parameter Store, a capability of AWS Systems Manager and Amazon DynamoDB.Step 7Using the chat history and query, the LangChain Orchestrator creates the final prompt and sends the request to the LLM hosted on SageMaker using Amazon SageMaker Jumpstarts.Step 8Send the LLM response back to the user through API Gateway.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-generative-ai-model-optimization-using-amazon-sagemaker)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The use of managed services provides scalable and reliable infrastructure to handle fluctuating user loads with high availability. For example, Amazon CloudWatch offers centralized logging and monitoring for all services involved for efficient operations. SageMaker offers standard logging and metrics for monitoring and analyzing the performance of deployed machine learning models, helping you gain insights into operational health and make data-driven decisions for continuous improvement. Lastly, Lambda provides built-in logging and metrics capabilities, and when coupled with CloudWatch, you get consistent logging for the Lambda functions. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Cognito delivers robust user authentication and authorization capabilities, preventing unauthorized access to the application. Concurrently, the Parameter Store secures storage of sensitive configuration data, thereby reducing the risk of data breaches. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

CloudFront, API Gateway, Lambda, and DynamoDB are managed services that handle the underlying infrastructure complexity. The capabilities of these services include high availability, scalability, and fault tolerance for the application. Specifically, CloudFront and API Gateway provide reliable and scalable infrastructure to handle fluctuating user loads, while Lambda and DynamoDB offer inherent reliability and durability, reducing the risk of downtime or data loss. The combination of these managed services allows the chat application to withstand failures and handle increased user traffic. Finally, Amazon S3 is designed to provide 99.999999999% (11 nines) durability and 99.99% availability of objects over a given year. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

SageMaker and Lambda together facilitate two key advantages for this application: improved speed and scalability. First, the optimization techniques in SageMaker help deliver faster responses from the LLM while reducing the compute resources and costs required to run it. Second, the serverless nature of Lambda offers efficient use of compute resources, scaling up or down as needed to maintain high performance. The combined capabilities of these services enable the application to handle increasing user loads and adapt to evolving performance requirements without compromising efficiency. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

SageMaker helps you achieve cost optimization in several ways. One, the optimized models require fewer compute resources to deliver the same or better performance, leading to lower overall infrastructure costs. Two, the ability to deploy the models on different hardware configurations, including Inferentia-based instances, allows for better hardware utilization and cost savings. And three, the faster responses from the optimized LLM can lead to reduced costs associated with cloud resources and data transfer. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The primary reason for using SageMaker is to support more sustainable workloads. This is because the inherent capabilities of SageMaker enable your team to reduce the compute resources and energy consumption required to run the LLM, minimizing the environmental impact of the application. By deploying the optimized models on hardware configurations that offer better energy efficiency, the application can further contribute to sustainability goals. Additionally, the cost-effectiveness of the optimized models is a key factor in the long-term viability and scalability of the application. By significantly reducing the inference costs through techniques like quantization and compilation, the application can be operated in a more sustainable manner, even as user demand and computational requirements scale over time. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Achieve up to ~2x higher throughput while reducing costs by up to ~50% for generative AI inference on Amazon SageMaker with the new inference optimization toolkit – Part 1**: This blog post demonstrates the benefits of the new inference optimization toolkit and the use cases it unlocks.

[Learn more](https://aws.amazon.com/blogs/machine-learning/achieve-up-to-2x-higher-throughput-while-reducing-costs-by-50-for-generative-ai-inference-on-amazon-sagemaker-with-the-new-inference-optimization-toolkit-part-1/?target=_blank)

- **Achieve up to ~2x higher throughput while reducing costs by up to ~50% for generative AI inference on Amazon SageMaker with the new inference optimization toolkit – Part 2**: This blog post demonstrates how to get started with the inference optimization toolkit for supported models in Amazon SageMaker JumpStart and the Amazon SageMaker Python SDK.

[Learn more](https://aws.amazon.com/blogs/machine-learning/achieve-up-to-2x-higher-throughput-while-reducing-costs-by-up-to-50-for-generative-ai-inference-on-amazon-sagemaker-with-the-new-inference-optimization-toolkit-part-2/?target=_blank)

[Read usage guidelines](/solutions/guidance-disclaimers/)
