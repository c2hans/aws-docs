---
source_url: https://docs.aws.amazon.com/solutions/optimizing-deep-learning-workloads-for-sustainability-on-aws/index.html
---

---
title: 'Guidance for Optimizing Deep Learning Workloads for Sustainability on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/optimizing-deep-learning-workloads-for-sustainability-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Optimizing Deep Learning Workloads for Sustainability on AWS

## Overview

This Guidance applies principles and best practices from the Sustainability Pillar of the AWS Well-Architected Framework to reduce the carbon footprint of your deep learning workloads. From data processing to model building, training and inference, this Guidance demonstrates how to maximize utilization and minimize the total resources needed to support your workloads.

## How it works

### Data processing

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/optimizing-deep-learning-workloads-for-sustainability-on-aws.pdf?target=_blank)Step 1Select an AWS Region with sustainable energy sources. When regulations and legal aspects allow, choose Regions near Amazon renewable energy projects and Regions where the grid has low published carbon intensity to host your data and workloads. When selecting a Region, try to minimize data movement across networks; store your data close to your producers and train your models close to your data.Step 2Evaluate whether you can avoid data processing by using existing publicly available datasets such as AWS Data Exchange and Open Data on AWS, which includes the Amazon Sustainability Data Initiative (ASDI). They offer weather and climate datasets, satellite imagery, and air quality or energy data, among others. Using these curated datasets avoids duplicating the compute and storage resources needed to download the data from the providers, store it in the cloud, organize, and clean it.
For internal data, you can also reduce duplication and rerun of feature engineering code across teams and projects by using Amazon SageMaker Feature Store.Step 3Adopt a serverless architecture for your data pipeline so it only provisions resources when work needs to be done. Use AWS Glue and AWS Step Functions for data ingestion and preprocessing, so you are not maintaining compute infrastructure 24/7. Step Functions can orchestrate AWS Glue jobs to create event-based serverless Extract, Transform, Load/Extract, Load, and Transform (ETL/ELT) pipelines.Step 4Use the appropriate Amazon Simple Storage Service (Amazon S3) storage tier to reduce the carbon impact of your workload. Use energy-efficient, archival-class storage for infrequently accessed data. If you can easily recreate an infrequently accessed dataset, use the Amazon S3 One Zone-IA class to minimize the total data stored.Step 5Manage the lifecycle of all your data and automatically enforce deletion timelines to minimize the total storage requirements of your workload using Amazon S3 Lifecycle policies. The S3 Intelligent-Tiering storage class automatically moves your data to the most sustainable access tier when access patterns change. Define data retention periods that support your sustainability goals while meeting your business requirements, not exceeding them.### Model building

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/optimizing-deep-learning-workloads-for-sustainability-on-aws.pdf#page=2?target=_blank)Step 1Define acceptable performance criteria. When you build an ML model, you'll likely need to make trade-offs between your model's accuracy and its carbon footprint. Establish performance criteria that support your sustainability goals while meeting your business requirements, not exceeding them.Step 2Evaluate if you can use pre-existing datasets, algorithms, or models. AWS Marketplace offers over 1,400 ML-related assets that customers can subscribe to. You can also fine-tune an existing model such as those available on Hugging Face, or use a pre-trained model from SageMaker JumpStart. Using pre-trained models can reduce the resources you need for data preparation and model training.
Try to find simplified versions of algorithms. This will help you use less resources to achieve a similar outcome. For example, DistilBERT, a distilled version of BERT, has 40% fewer parameters, runs 60% faster, and preserves 97% of BERT's performance.
Consider techniques to avoid training a model from scratch. Transfer learning (use a pre-trained source model and reuse it as the starting point for a second task) or incremental training (use artifacts from an existing model on an expanded dataset to train a new model).Step 3Use Amazon SageMaker Training Compiler to compile your Deep Learning models from their high-level language representation to hardware-optimized instructions to reduce training time. This can speed up training of Deep Learning models by up to 50% by more efficiently using SageMaker graphics processing unit (GPU) instances.Step 4Automate the ML environment. When building your model, use Lifecycle Configuration Scripts to automatically stop idle SageMaker Notebook instances. If you are using SageMaker Studio, install the auto-shutdown Jupyter extension to detect and stop idle resources. Use the fully managed training process provided by SageMaker to automatically launch training instances and shut them down as soon as the training job is complete. This minimizes idle compute resources, and limits the environmental impact of your training job.### Model training

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/optimizing-deep-learning-workloads-for-sustainability-on-aws.pdf#page=3?target=_blank)Step 1Use SageMaker Debugger to identify training problems. With built-in rules such as system bottlenecks, overfitting, and saturated activation functions, SageMaker Debugger can monitor your training jobs and automatically stop them as soon as it detects a bug, which helps you avoid unnecessary carbon emissions.Step 2Right-size your training jobs with Amazon CloudWatch metrics that monitor the utilization of resources such as CPU, GPU, memory, and disk utilization. SageMaker Debugger also provides profiler capabilities to detect under-utilization of system resources and right-size your training environment. This helps avoid unnecessary carbon emissions.Step 3Use AWS Trainium to train your deep learning workloads. It is expected to be the most energy efficient processor offered by AWS for this purpose.Step 4Consider Managed Spot Training, which takes advantage of unused Amazon Elastic Compute Cloud (Amazon EC2) capacity and can save you up to 90% in cost compared to On-Demand instances. By shaping your demand for the existing supply of Amazon EC2 instance capacity, you will improve your overall resource efficiency and reduce idle capacity of the overall AWS Cloud.Step 5Reduce the volume of logs you keep. By default, CloudWatch retains logs indefinitely. By setting limited retention time for your notebooks and training logs, you'll avoid the carbon footprint of unnecessary log storage.
Adopt sustainable tuning job strategy. Prefer Bayesian search over random search (and avoid grid search). Bayesian search makes intelligent guesses about the next set of parameters to pick based on the prior set of trials. It typically requires ten times fewer jobs than random search, and therefore ten times less compute resources, to find the best hyperparameters.### Inference

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/optimizing-deep-learning-workloads-for-sustainability-on-aws.pdf#page=4?target=_blank)Step 1If your users can tolerate some latency, deploy your model on asynchronous endpoints to reduce resources that are idle between tasks and minimize the impact of load spikes.Step 2When you don't need real-time inference, use SageMaker batch transform. Unlike persistent endpoints, clusters are decommissioned when batch transform jobs finish.Step 3Amazon EC2 Inf1 instances (based on custom designed AWS Inferentia chips) have 50% higher performance per watt than g4dn.Step 4Improve efficiency of your models by compiling them into optimized forms with SageMaker Neo.Step 5Deploy multiple models behind a single endpoint. Sharing endpoint resources is more sustainable than deploying a single model behind one endpoint, and can help you cut up to 90 percent of your inference costs.Step 6Right-size your endpoints by using metrics from Amazon CloudWatch, or by using the Amazon SageMaker Inference Recommender. This tool can run load testing jobs and recommend the proper instance type to host your model.Step 7If your workload has intermittent or unpredictable traffic, configure autoscaling inference endpoints in SageMaker or use SageMaker Serverless Inference, which automatically launches compute resources and scales them in and out depending on traffic, which eliminates idle resources.Step 8When working on Internet of Things (IoT) use cases, evaluate if ML inference at the edge can reduce the carbon footprint of your workload. When deploying ML models to edge devices, use SageMaker Edge Manager, which integrates with SageMaker Neo and AWS IoT Greengrass, and compress the size of models for deployment with pruning and quantization.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as amany Well-Architected best practices as possible.

### Operational Excellence

CloudWatch is used to measure machine learning (ML) operations metrics to monitor the performance of the deployed environment. In the data processing phase, AWS Glue and Step Functions workflows are used to track the history of the data within the pipeline execution. In the model development phase, SageMaker Debugger provides near real-time monitoring of training jobs to detect issues and performance bottlenecks. In the deployment phase, the health of model endpoints deployed on SageMaker hosting options is monitored using CloudWatch metrics and alarms. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

All the proposed services support integration with AWS Identity and Access Management (IAM) that can be used to control access to resources and data. Data is stored in Amazon S3 and SageMaker Feature Store that support encryption at rest using AWS Key Management Service (AWS KMS). To reduce data exposure risks, data lifecycle plans are established to remove data automatically based on age, and store only the data that has business need. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The customer has the option to deploy SageMaker services in a highly available manner. AWS Glue Data Catalog is used to track the data assets that have been loaded into the ML workloads. Fault tolerant, repeatable, and highly available data processing is ensured thanks to data pipelines. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Training and inference instance types are optimized using CloudWatch metrics and SageMaker Inference Recommender. The use of simplified versions of algorithms, pruning, and quantization is recommended to achieve better performance. SageMaker Training Compiler can speed up training of deep learning models by up to 50%, and SageMaker Neo optimizes ML models to perform up to 25x faster. Instances based on Trainium and Inferentia offer higher performance compared to other Amazon EC2 instances. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

We encourage the use of existing publicly available datasets to avoid the cost of storing and processing data. Using the appropriate Amazon S3 storage tier, S3 Lifecycle policies, and S3 Intelligent-Tiering storage class help reduce storage cost. SageMaker Feature Store helps reduce the cost of storing and processing duplicated datasets. We recommend data and compute proximity to reduce transfer costs. Serverless data pipelines, asynchronous SageMaker endpoints, and SageMaker batch transform help avoid the cost of maintaining compute infrastructure 24/7. We encourage optimization techniques (compilation, pruning, quantization, use of simplified version of algorithms) as well as transfer learning and incremental training to reduce training and inference costs. Scripts are provided to automatically shutdown unused resources. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This reference architecture aligns with the goals of optimization for sustainability: Ensure elimination of idle resources by the use of serverless technologies (AWS Glue, Step Functions, SageMaker Serverless Inference Endpoint) and environment automation Achieve reduction of unnecessary data processing and data storage using Amazon S3 lifecycle policies, SageMaker Feature Store, and the use of existing, publicly available datasets and models Achieve maximization of the utilisation of provisioned resources by right-sizing the environments (using CloudWatch and SageMaker Inference Recommender) and asynchronous processing (SageMaker Asynchronous Endpoints) Achieve maximization of CPU efficiency using simplified versions of algorithms, models compilation (SageMaker Training compiler and SageMaker Neo), and compression techniques (pruning and quantization) [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Optimize AI/ML workloads for sustainability: Part 1**: Identify business goals, validate ML use, and process data

[Learn more](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/)

- **Optimize AI/ML workloads for sustainability: Part 2**: Model development

[Learn more](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/)

- **Optimize AI/ML workloads for sustainability: Part 3**: Deployment and monitoring

[Learn more](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/)

- **Part 1: How NatWest Group built a scalable, secure, and sustainable MLOps platform**: This is the first post of a four-part series detailing how NatWest Group, a major financial services institution, partnered with AWS to build a scalable, secure, and sustainable machine learning operations (MLOps) platform.

[Learn more](https://aws.amazon.com/blogs/machine-learning/part-1-how-natwest-group-built-a-scalable-secure-and-sustainable-mlops-platform/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
