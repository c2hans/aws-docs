---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/aws-for-data.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS for data
<a name="aws-for-data"></a>

 There are three different stages to building a modern data strategy. These stages are not sequential, and you can start at any stage, depending on your data journey.
+  **Modernize** — You can modernize your data infrastructure with the most scalable, trusted, and secure cloud provider.
+  **Unify** — You can unify your data by putting it to work in the best data lakes and purpose-built data stores.
+  **Innovate** — You can create new experiences and reimagine old processes with AI and ML.

 These three stages in turn lead to the development of a modern data strategy on AWS, as illustrated in the following figure. This strategy gives you the best of both data lakes and purpose-built stores. It enables you to store any amount of data at a low cost, and in open-standards data formats. This helps you avoid the risks of getting locked into a proprietary format. It helps you break down data silos and empower your teams to run analytics or ML at scale, using your preferred tools and techniques.

![A diagram depicting modern data strategy on AWS .](http://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/images/modern-data-strategy.png)

## Modern data architecture
<a name="modern-data-architecture"></a>

 AWS modern data architecture connects your data lake, your data warehouse, and all other purpose-built stores into a coherent whole. The following figure depicts a modern data architecture on AWS.

![A diagram depicting modern data architecture on AWS.](http://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/images/modern-data-architecture.png)

 **Key:**

1.  Store data in a purpose-built database that can support a modern application and its different features. It no longer needs to be a single type of relational database, but could be a NoSQL database, cache store, or anything else which works for the application. The focus is on application empowerment, not analytics.

1.  Use the data lake, which uses a storage service such as [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3), to store data from all those purpose-built databases and native open-file formats. Open formats give more power to organizations to use the data however they need to.

1.  Once the data lake is hydrated with data, you can build analytics of any kind easily, and use any technology customers want to use for their use cases. This can range from traditional data warehousing and batch reporting to more near real-time alerting and reporting. This can even be ad-hoc querying of data, or more advanced ML-based analytics use cases. Data is now stored in a layer that’s more open and provides more freedom of analytics choices.

1.  ML and AI are also critical for a modern data strategy, to help you predict what will happen in the future, and to build intelligence into your systems and applications. Customers have varied needs when it comes to AI/ML, and require a broad set of AI/ML services. This is true for expert ML practitioners, for everyday developers, and for customers who don’t want to build and train models.

1.  Finally, data governance is a critical element to combining and sharing data from different sources so you can put data in the hands of people at all levels of your organization. There are data residency compliance needs which come with globalization. There is need for granular control over who has permission to access data, and standard security needs such as encryption, auditability, monitoring, alerting, and so on.

## Purpose-built databases
<a name="purpose-built-databases"></a>

 Organizations are breaking free from legacy databases. They are moving to fully managed databases and analytics, modernizing data warehouse databases, and building modern applications with purpose-built databases to get more out of their data. Organizations want to move away from old-guard databases because they are expensive, proprietary, lock you in, offer punitive licensing terms, and come with frequent audits from their vendors. Organizations that are moving to open-source databases are looking for the performance of commercial-grade databases with the pricing, freedom, and flexibility of open-source databases.

 AWS provides purpose-built database services to overcome these challenges with on-premises database solutions. The most straightforward and simple solution for many organizations that are struggling to maintain their own relational databases at scale is a move to a managed database service, such as [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS). In most cases, these customers can migrate workloads and applications to a managed service without needing to re-architect their applications, and their teams can continue to use the same database skill sets. Organizations can lift and shift their self-managed databases such as Oracle, SQL Server, MySQL, PostgreSQL, and MariaDB to Amazon RDS. For organizations that are looking for better performance and availability, they can move their relational databases to MySQL and PostgreSQL to [Amazon Aurora](https://aws.amazon.com/elasticache/) and get [three to five times better throughput](https://aws.amazon.com/about-aws/whats-new/2021/01/amazon-aurora-supports-postgresql-12/).

 Many organizations also use non-relational databases such as MongoDB and Redis as document and in-memory databases for use cases such as content management, personalization, mobile apps, catalogs, and near real-time use cases such as caching, gaming leaderboards, and session stores. The most straightforward and simple solution for many organizations who are struggling to maintain their own non-relational databases at scale is a move to a managed database service (for example, moving self-managed MongoDB databases to Amazon DocumentDB or moving self-managed in-memory databases such as Redis and ElastiCache to [Amazon ElastiCache](https://aws.amazon.com/elasticache/)). In most cases, these organizations can migrate workloads and applications to a managed service without needing to re-architect their applications, and their teams can continue to use the same database skill sets.

![A diagram that shows purpose-built database services on AWS.](http://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/images/purpose-built-databases.png)

## Purpose-built data analytics services
<a name="purpose-built-data-analytics-services"></a>

 Purpose-built data analytics services enable you to use the right tool for the right job, and provides the agility to iteratively and incrementally build out the modern data architecture. You gain the flexibility to evolve the data lake house to meet current and future needs as you add new data sources, discover new use cases and their requirements, and develop newer analytics methods.

 AWS provides a portfolio of purpose-built data analytics services, which include [AWS Glue](https://aws.amazon.com/glue/), [Amazon EMR](https://aws.amazon.com/emr/), [Amazon Athena](https://aws.amazon.com/athena/), [Amazon Kinesis](https://aws.amazon.com/kinesis/), [Amazon Managed Streaming for Apache Kafka](https://aws.amazon.com/msk/) (Amazon MSK), [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/), [Amazon Redshift](https://aws.amazon.com/redshift/), and [Quick](https://aws.amazon.com/quicksight/) for various unique analytics use cases. These are managed services, so organizations don’t need to worry about administration tasks such as software provisioning, configuration, backups, patching, and recovery. Instead, organizations can focus on getting insights from their data and creating a business value, not managing the infrastructure. These purpose-built data analytics services are optimized for specific use cases, because one size solution doesn’t fit for all use cases and leads to compromises in analytics. The purpose-built-analytics capabilities are illustrated in the following figure.

![A diagram depicting purpose-built data analytics services on AWS .](http://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/images/purpose-built-analytics.png)

## ML and AI services
<a name="ml-and-ai-services"></a>

 In the past, ML technology was limited to a few major tech companies and hardcore academic researchers, but things began to change when cloud computing entered into the mainstream. Compute power and data became more available, and ML is now making an impact across almost every industry, including finance, retail, fashion, real estate, healthcare, and more. ML is moving from the peripheral to a core part of most every business and industry. In time, virtually every application will be infused with ML and AI.

 AWS provides the broadest and deepest set ML and AI services, in three different levels, for builders of all levels of expertise in their ML journey:
+  **For expert practitioners**, AWS supports all the major ML frameworks ,including TensorFlow, MXNet, PyTorch, Caffe 2, and so on. We offer the highest performance instances for ML training in the cloud with Amazon EC2 P4d instances, powered by the latest NVIDIA A100 Tensor Core GPUs, and coupled with first-in-the-cloud 400 Gbps instance networking. P4d instances are deployed in hyperscale clusters, called [EC2 UltraClusters](https://aws.amazon.com/getting-started/hands-on/deploy-a-p4d-ec2-ultracluster/), offering supercomputer-class performance for the most complex ML training jobs. For inference, which represents 90% of the cost of ML, we provide the lowest cost for ML inference in the cloud with [Amazon EC2 Inf1 instances](https://aws.amazon.com/ec2/instance-types/inf1/), powered by [AWS Inferentia chips](https://aws.amazon.com/machine-learning/inferentia/).
+  **For data scientists and ML developers**, AWS provides [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/). SageMaker AI was built from the ground up to simplify the process of ML with tools for every step of the ML development, including labeling, data preparation, feature engineering, statistical bias detection, auto-ML, training, tuning, hosting, explainability, monitoring, and workflows.
+  **For developers and business users**, AWS provides pre-trained AI services that provide ready-made intelligence for applications and workflows, and end-to-end solutions that can solve business needs right out of the box using [AutoML](https://docs.aws.amazon.com/sagemaker/latest/dg/use-auto-ml.html) technology. These services address common use cases such as personalized recommendations, contact center intelligence, document processing, intelligent search, business metrics analysis, and more. AWS also provides industry-specific AI services for both industrial and healthcare industries.

![A diagram describing AWS ML and AI services.](http://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/images/ml-ai-services.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
