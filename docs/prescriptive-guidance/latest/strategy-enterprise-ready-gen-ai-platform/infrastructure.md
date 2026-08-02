---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/infrastructure.html
---

# Layer 1: Building reliable data and compute infrastructure for generative AI
<a name="infrastructure"></a>

For developing generative AI applications, particularly if training or fine-tuning a foundation model is necessary, a robust data foundation and compute infrastructure is critical. As enterprises embark on their generative AI journey, they need infrastructure that can support the entire machine learning lifecycle. They also need to strike the right balance between performance, cost, and operational efficiency.

Reliable generative AI infrastructure should offer the following three key components: the foundational infrastructure, the vector storage and retrieval infrastructure, and the compute infrastructure. Together, these components provide the flexibility to serve the needs of any project, regardless of its scale, requirements, or environment.

**This section contains the following topics:**
+ [Foundation infrastructure for API-based implementations](#infrastructure-foundation)
+ [Vector storage and retrieval infrastructure](#infrastructure-storage)
+ [High-performance compute infrastructure for model training and fine-tuning](#infrastructure-compute)
+ [Implementation recommendations](#infrastructure-implementation-recs)

## Foundation infrastructure for API-based implementations
<a name="infrastructure-foundation"></a>

Most organizations begin their generative AI journey by using pretrained foundation models through APIs. [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) provides serverless access to leading foundation models through a unified API. This helps you experiment and deploy generative AI applications without managing complex infrastructure. For these implementations, you need the following:
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) general-purpose instances for running your applications.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) for storing application data and outputs.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) for monitoring and logging your application's performance and usage.
+ (Optional) [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) for serverless compute when building event-driven generative AI applications.

## Vector storage and retrieval infrastructure
<a name="infrastructure-storage"></a>

As your generative AI applications mature, you'll likely need to enhance them with domain-specific knowledge and context. With Retrieval Augmented Generation (RAG), the foundation model references an authoritative data source that is outside of its training data sources, such as your organization's data or documents, before generating a response. For more information, see [Retrieval Augmented Generation options and architectures on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/introduction.html).

[Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) provides a fully managed solution for building RAG applications. It helps you to securely connect your enterprise data with foundation models. For additional flexibility, you can use [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) with vector search capabilities, or you can use [Amazon Relational Database Service (Amazon RDS) for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) with the [pgvector](https://github.com/pgvector/pgvector) extension to store vector embeddings.

For efficient vector operations, consider using Amazon EC2 compute-optimized instances for embedding generation. Also consider caching frequently accessed embeddings by using [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html) to optimize performance and reduce costs.

For more information about vector databases and caching, see [What is a vector database?](https://aws.amazon.com/what-is/vector-databases/) and [Choosing an AWS vector database for RAG use cases](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/introduction.html).

## High-performance compute infrastructure for model training and fine-tuning
<a name="infrastructure-compute"></a>

For organizations that are ready to customize foundation models, AWS offers comprehensive infrastructure for model training and fine-tuning. You can use Amazon Simple Storage Service (Amazon S3) as low cost, scalable, and highly durable object storage for building data platforms and for storing training data and trained models. In addition, [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a serverless data integration service that can help you prepare data for model training.

For the training infrastructure, [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) offers a fully managed machine-learning environment with the tools and workflows that you need to build, train, and deploy models. Using SageMaker AI can significantly reduce your operational overhead. Consider using [accelerated computing instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html#ac_hardware), such as the G and P instance families. These instance families provide access to the latest GPUs from NVIDIA for machine learning training and inference. You can also use [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/), a purpose-built machine learning accelerator that speeds up training times by up to 50%, while lowering costs.

For truly large projects, you can use [Amazon EC2 UltraClusters](https://aws.amazon.com/ec2/ultraclusters/). UltraClusters consist of thousands of accelerated Amazon EC2 instances that are co-located in a given AWS Availability Zone and interconnected. UltraClusters can scale to thousands of GPUs or machine learning accelerators. They deliver exa-floating point operations per second (exaflops) of aggregate compute capacity, which reduces training times and can reduce time-to-solution from weeks to a few days.

## Implementation recommendations
<a name="infrastructure-implementation-recs"></a>

Consider the following recommendations for setting up a scalable and cost-effective infrastructure for your generative AI projects:
+ For quick experimentation and initial deployments, start with Amazon Bedrock and use general-purpose compute instances for your applications.
+ As your needs evolve, implement vector storage solutions by using Amazon Bedrock Knowledge Bases or Amazon OpenSearch Service. Scale your infrastructure accordingly.
+ For advanced customization, standardize and automate the provisioning of secure and governed machine learning environments to support the requirements of distributed teams. For more information, see [Setting up secure, well-governed machine learning environments on AWS](https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws/) (AWS blog post).
+ Adopt machine learning operations (MLOps) to automate and standardize processes across the machine learning lifecycle. These processes include model development, testing, integration, release, and infrastructure management. For more information, see [What is MLOps?](https://aws.amazon.com/what-is/mlops/)
+ For small-scale experiments or proof of concepts, start with Amazon SageMaker AI and general-purpose compute instances. As you scale to large production deployments, consider Amazon EC2 accelerated computing instances for maximum performance.
+ Use [managed spot training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html) in SageMaker AI to optimize the cost of training models by up to 90% compared to on-demand instances. SageMaker AI manages the spot interruptions on your behalf.
