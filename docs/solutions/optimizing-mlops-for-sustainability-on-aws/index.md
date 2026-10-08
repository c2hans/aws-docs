---
source_url: https://docs.aws.amazon.com/solutions/optimizing-mlops-for-sustainability-on-aws/index.html
---

---
title: 'Guidance for Optimizing MLOps for Sustainability on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/optimizing-mlops-for-sustainability-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Optimizing MLOps for Sustainability on AWS

## Overview

This Guidance demonstrates how to implement environmentally sustainable MLOps practices across the entire machine learning lifecycle. It helps organizations optimize their ML workflows for both performance and energy efficiency, addressing the growing environmental impact of increasingly complex ML models. The solution shows how to reduce carbon emissions at every phase, from data collection and storage to model training and inference, while maintaining operational excellence. Furthermore, it demonstrates how organizations can align their MLOps practices with net-zero goals through practical best practices, enabling them to achieve both their ML objectives and sustainability targets without compromising on model performance.

## Benefits

### Reduce ML carbon footprint significantly

Optimize your machine learning operations to achieve up to 52% lower energy consumption using purpose-built infrastructure. Track and minimize environmental impact while maintaining model performance.

### Accelerate sustainable model development

Deploy automated MLOps pipelines that eliminate redundant training runs and optimize resource utilization. Reduce time-to-market while minimizing computational waste through intelligent experiment tracking.

### Cut storage costs intelligently

Implement automated data lifecycle management that moves ML artifacts between storage tiers based on access patterns. Reduce unnecessary storage consumption while ensuring data availability.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/optimizing-mlops-for-sustainability-on-aws.pdf)

![Architecture diagram](/images/solutions/optimizing-mlops-for-sustainability-on-aws/images/optimizing-mlops-for-sustainability-on-aws-1.png)

1. **Step 1**: Strategic Region Selection optimizes performance and sustainability, as different AWS Regions have varying carbon footprints based on their energy sources. - Use the AWS Customer Carbon Footprint Tool to evaluate regional carbon impacts. - Consider regions powered by AWS renewable energy projects. - Implement data locality principles by co-locating data processing with storage and minimizing cross-region data transfer.
1. **Step 2**: Serverless Architecture optimizes resource utilization and reduces idle computing capacity. - Deploy Amazon SageMaker Pipelines for automated ML workflows. - Use SageMaker Projects for MLOps automation. - Implement SageMaker Model Monitor for production monitoring. - Consider SageMaker Serverless Inference for auto-scaling endpoints.
1. **Step 3**: Reduce Duplication and rerun of feature engineering code across teams and projects by using Amazon SageMaker Feature Store.
1. **Step 4**: Optimizing Storage Strategy reduces the environmental impact of cloud workloads. - Through intelligent use of Amazon Simple Storage Service (Amazon S3) Storage Classes, organizations can significantly reduce their carbon footprint while maintaining operational efficiency. - Amazon S3 Intelligent-Tiering automatically moves data between access tiers based on usage patterns. - Organizations can further optimize their storage footprint using Amazon S3 Storage Lens to identify opportunities for improved storage efficiency and reduced environmental impact.
1. **Step 5**: Data Storage Archives - Amazon S3 Glacier storage classes provide sustainable storage for rarely accessed data. - Implementing Amazon S3 Lifecycle policies ensures automated data management through proper retention and deletion schedules, reducing unnecessary storage consumption.
1. **Step 6**: Hardware Optimization maximizes computational efficiency while minimizing energy consumption. - Leveraging purpose-built infrastructure like AWS Trainium, which offers up to 52% lower energy consumption compared to traditional Amazon Elastic Compute Cloud (Amazon EC2) instances, organizations can significantly reduce their carbon footprint during model training. - Managed Spot Training in Amazon SageMaker AI takes advantage of unused Amazon EC2 capacity, further enhancing resource efficiency and reducing idle infrastructure, making it a crucial component in sustainable ML practices.
1. **Step 7**: Model Training using Amazon SageMaker AI Model Parallelism enables efficient distribution of large models across multiple GPUs, optimizing resource utilization.
1. **Step 8**: Resource Optimization provides critical insights into resource utilization and opportunities for environmental impact reduction. - Amazon SageMaker AI Debugger plays a pivotal role by automatically detecting resource underutilization and training inefficiencies, enabling real-time interventions that prevent waste. - Integration with Amazon CloudWatch provides comprehensive metrics for right-sizing training jobs and optimizing resource allocation.
1. **Step 9**: Training Optimization Strategies minimize the environmental impact of machine learning. - Amazon SageMaker AI Automatic Model Tuning with Bayesian optimization significantly reduces the number of experimental training runs. - Utilizing Amazon SageMaker AI Processing for efficient model evaluation and implementing systematic performance criteria, organizations can make informed trade-offs between model accuracy and carbon footprint.
1. **Step 10**: Documentation through Amazon SageMaker AI Model Cards enables tracking of environmental impact metrics, promoting transparency and accountability in sustainable ML practices.
1. **Step 11**: Automated Deployment Infrastructure optimizes resource utilization and reduces manual intervention. - By implementing Amazon SageMaker AI Model Registry alongside AWS CodePipeline and Amazon SageMaker AI Pipelines, organizations can create efficient, repeatable deployment processes that minimize resource waste and operational overhead.
1. **Step 12**: Energy-efficient Deployment options reduce the environmental impact of machine learning inference workloads. - AWS designed AWS Inferentia chips to deliver high performance at the lowest cost in Amazon EC2 for deep learning (DL) and generative AI inference applications.
1. **Step 13**: Scalable Endpoint Solutions optimize resource utilization and minimize environmental impact in machine learning deployments. - Amazon SageMaker AI Serverless Inference automatically manages compute resources based on workload demands, eliminating idle resource waste for intermittent traffic patterns. - Amazon Asynchronous Endpoints optimize resource usage for latency-tolerant applications. - For batch processing needs, Amazon SageMaker AI Batch Transform provides resource-efficient inference by automatically decommissioning clusters upon job completion.
1. **Step 14**: Production Monitoring ensures optimal resource utilization and model performance over time. - Amazon SageMaker AI Model Monitor provides comprehensive monitoring capabilities that detect model drift, assess data quality, and track resource utilization, enabling organizations to make data-driven decisions about model retraining and resource allocation.
## Related content

- **Optimizing MLOps for Sustainability**: This blog post demonstrates how to optimize MLOps for sustainability on AWS, focusing on efficient practices in data preparation, model training, and deployment.

[Optimizing MLOps for Sustainability](https://aws.amazon.com/blogs/machine-learning/optimizing-mlops-for-sustainability/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
