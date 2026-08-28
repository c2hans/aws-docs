---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/analytics-on-aws-how-to-choose.html
---

# Choosing an AWS analytics service
<a name="analytics-on-aws-how-to-choose"></a>

**Taking the first step**

|  |  |
| --- |--- |
| **Purpose** | Help determine which AWS analytics services are the best fit for your organization. |
| **Last updated** | September 24, 2025 |
| **Covered services** |  +  [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) <br />+  [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html#first-time-user) <br />+   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) <br />+  [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/getting-started.html) <br />+  [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html) <br />+  [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/setting-up.html) <br />+  [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/examples.html) <br />+  [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html) <br />+  [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html) <br />+  [Amazon Managed Workflows for Apache Airflow](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html) <br />+  [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html) <br />+  [Quick](https://docs.aws.amazon.com/quicksight/latest/user/getting-started.html) <br />+  [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/new-user.html) <br />+  [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) <br />+  [Amazon SageMaker](https://docs.aws.amazon.com/next-generation-sagemaker/)   |

## Introduction
<a name="intro"></a>

Data is foundational to modern business. People and applications need to securely access and analyze data, which comes from new and diverse sources. The volume of data is also constantly increasing, which can cause organizations to struggle with capturing, storing, and analyzing all the necessary data.

Meeting these challenges means building a modern data architecture that breaks down all of your data silos for analytics and insights--including third-party data--and makes it accessible to everyone in the organization, in one place, with end-to-end governance. It's also increasingly important to connect your analytics and machine learning (ML) systems to enable predictive analytics.

This decision guide helps you ask the right questions to build your modern data architecture on AWS services. It explains how to break down your data silos (by connecting your data lake and data warehouses), your system silos (by connecting ML and analytics), and your people silos (by putting data in the hands of everyone in your organization).

[![AWS Videos](http://img.youtube.com/vi/9Y1bwAmx0Do?start=397&end=848/0.jpg)](http://www.youtube.com/watch?v=9Y1bwAmx0Do?start=397&end=848)

## Understand AWS analytics services
<a name="understand"></a>

A modern data strategy is built with a set of technology building blocks that help you manage, access, analyze, and act on data. It also gives you multiple options to connect to data sources. A modern data strategy should empower your teams to:
+ Use your preferred tools or techniques
+ Use artificial intelligence (AI) to assist with finding answers to specific questions about your data
+ Manage who has access to data with the proper security and data governance controls
+ Break down data silos to give you the best of both data lakes and purpose-built data stores
+ Store any amount of data, at low-cost, and in open, standards-based data formats
+ Connect your data lakes, data warehouses, operational databases, applications, and federated data sources into a coherent whole

AWS offers a variety of services to help you achieve a modern data strategy. The following diagram depicts the AWS services for analytics that this guide covers. The tabs that follow provide additional details.

![Diagram showing the AWS analytics services](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/analytics-services.png)

------
#### [ Unified analytics and AI ]

The next generation of [Amazon SageMaker](https://aws.amazon.com/sagemaker/) combines widely adopted AWS machine learning (ML) and analytics capabilities to deliver an integrated experience for analytics and AI, providing unified access to all your data. Using [Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/getting-started.html), you can collaborate and build faster with familiar AWS tools for model development, generative AI application development, data processing, and SQL analytics, all accelerated by Amazon Q Developer, our generative AI assistant for software development. Access your data from data lakes, data warehouses, or third-party and federated sources, with built-in governance to meet enterprise security requirements.

------
#### [ Data processing ]
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) helps you analyze unstructured, semi-structured, and structured data stored in Amazon S3. Examples include CSV, JSON, or columnar data formats such as Apache Parquet and Apache ORC. You can use Athena to run ad-hoc queries using ANSI SQL, without the need to aggregate or load the data into Athena. Athena integrates with Quick, AWS Glue Data Catalog, and [other AWS services](https://docs.aws.amazon.com/athena/latest/ug/athena-aws-service-integrations.html). You can also analyze data at scale with [Trino](https://trino.io/), without needing to manage infrastructure, and build real-time analytics using Apache Flink and Apache Spark.
+ [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html) is a managed cluster platform that simplifies running big data frameworks, such as Apache Hadoop and Apache Spark, on AWS to process and analyze vast amounts of data. Using these frameworks and related open-source projects, you can process data for analytics purposes and business intelligence workloads. Amazon EMR also lets you transform and move large amounts of data into and out of other AWS data stores and databases, such as Amazon S3.
+ With [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/setting-up.html), you can discover and connect to more than 100 diverse data sources and manage your data in a centralized data catalog. You can visually create, run, and monitor ETL pipelines to load data into your data lakes. Also, you can immediately search and query cataloged data using Athena, Amazon EMR, and Amazon Redshift Spectrum.
+ [Amazon Managed Workflows for Apache Airflow](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html) (MWAA) is a fully managed implementation of Apache Airflow that makes it easier to create, schedule, and monitor data workflows in the cloud. MWAA automatically scales workflow capacity to meet your needs and integrates with AWS security services. You can use MWAA to orchestrate workflows across your analytics services, including data processing, ETL jobs, and machine learning pipelines.

------
#### [ Data streaming ]
+ With [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html) (Amazon MSK), you can build and run applications that use Apache Kafka to process streaming data. Amazon MSK provides the control-plane operations, such as those for creating, updating, and deleting clusters. It lets you use Apache Kafka data-plane operations, such as those for producing and consuming data.
+ With [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/examples.html), you can collect and process large streams of data records in real time. The type of data used can include IT infrastructure log data, application logs, social media, market data feeds, and web clickstream data.
+ [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) is a fully managed service for delivering real-time streaming data to destinations such as Amazon S3, Amazon Redshift, Amazon OpenSearch Service, Splunk, and Apache Iceberg Tables. You can also send data to any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, Dynatrace, LogicMonitor, MongoDB, New Relic, Coralogix, and Elastic.
+  With [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html), you can use Java, Scala, Python, or SQL to process and analyze streaming data. You can author and run code against streaming sources and static sources to perform time-series analytics, feed real-time dashboards, and metrics.

------
#### [ Business intelligence ]

[Quick](https://docs.aws.amazon.com/quicksight/latest/user/getting-started.html) gives decision-makers the opportunity to explore and interpret information in an interactive visual environment. In a single data dashboard, Quick can include AWS data, third-party data, big data, spreadsheet data, SaaS data, B2B data, and more. With Quick Q, you can use natural language to ask questions about your data and receive a response. For example, "What are the top-selling categories in California?"

------
#### [ Search analytics ]

[Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html) provisions all the resources for your OpenSearch cluster and launches it. It also automatically detects and replaces failed OpenSearch Service nodes, reducing the overhead associated with self-managed infrastructures. You can use OpenSearch Service direct query to analyze data in Amazon S3 and other AWS services.

------
#### [ Data governance ]

With [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/getting-started.html), you can manage and govern access to data by using fine-grained controls. These controls help ensure access with the right level of privileges and context. Amazon DataZone simplifies your architecture by integrating data management services, including Amazon Redshift, Athena, Quick, AWS Glue, on-premises sources, and third-party sources.

------
#### [ Data collaboration ]

[AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/setting-up.html) is a secure collaboration workspace where you can analyze collective datasets without providing access to the raw data. You can collaborate with other companies by choosing the partners with whom you want to collaborate, selecting their datasets, and configuring privacy-enhancing controls for those partners. When you run queries, AWS Clean Rooms reads data from that data's original location and applies built-in analysis rules to help you maintain control over that data.

------
#### [ Data lake and data warehouse ]
+ [The next generation of Amazon SageMaker](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/lakehouse-get-started.html) is fully compatible with Apache Iceberg, allowing you to unify data across Amazon Simple Storage Service (Amazon S3) data lakes and Amazon Redshift data warehouses. This enables building analytics and AI and machine learning (ML) applications on a single data copy. Through zero-ETL integrations, you can stream data from operational sources in near real-time, run federated queries across multiple sources, and access data with Apache Iceberg–compatible tools. You can secure your data by defining fine-grained permissions that are enforced across all your analytics and ML tools and engines.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) can store and protect virtually any amount and kind of data, which you can use for your data lake foundation. Amazon S3 provides management features so that you can optimize, organize, and configure access to your data to meet your specific business, organizational, and compliance requirements. Amazon S3 Tables provide S3 storage that’s optimized for analytics workloads. Using standard SQL statements, you can query your tables with query engines that support Iceberg, such as Athena, Amazon Redshift, and Apache Spark.
+ [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/new-user.html) is a fully managed, petabyte-scale data warehouse service. Amazon Redshift can be connected to a data lakehouse in Amazon SageMaker, allowing you to use its powerful SQL analytic capabilities on your unified data across Amazon Redshift data warehouses and Amazon S3 data lakes. You can also use Amazon Q in Amazon Redshift, which simplifies SQL authoring through natural language.

------

## Consider criteria for AWS analytics services
<a name="consider"></a>

There are many reasons for building data analytics on AWS. You might need to support a greenfield or pilot project as a first step in your cloud migration journey. Alternatively, you might be migrating an existing workload with as little disruption as possible. Whatever your goal, the following considerations can be useful in making your choice.

------
#### [ Assess data sources and data types ]

Analyze available data sources and data types to gain a comprehensive understanding of data diversity, frequency, and quality. Understand any potential challenges in processing and analyzing the data. This analysis is crucial because:
+ Data sources are diverse and come from various systems, applications, devices, and external platforms.
+ Data sources have unique structure, format, and frequency of data updates. Analyzing these sources helps in identifying suitable data collection methods and technologies.
+ Analyzing data types, such as structured, semi-structured, and unstructured data determines the appropriate data processing and storage approaches.
+ Analyzing data sources and types facilitates data quality assessment, helps you anticipate potential data quality issues—missing values, inconsistencies, or inaccuracies.

------
#### [ Data processing requirements ]

Determine data processing requirements for how data is ingested, transformed, cleansed, and prepared for analysis. Key considerations include:
+ **Data transformation:** Determine the specific transformations needed to make the raw data suitable for analysis. This involves tasks like data aggregation, normalization, filtering, and enrichment.
+ **Data cleansing:** Assess data quality and define processes to handle missing, inaccurate, or inconsistent data. Implement data cleansing techniques to ensure high-quality data for reliable insights.
+ **Processing frequency:** Determine whether real-time, near real-time, or batch processing is required based on the analytical needs. Real-time processing enables immediate insights, while batch processing may be sufficient for periodic analyses.
+ **Scalability and throughput:** Evaluate the scalability requirements for handling data volumes, processing speed, and the number of concurrent data requests. Ensure that the chosen processing approach can accommodate future growth.
+ **Latency:** Consider the acceptable latency for data processing and the time it takes from data ingestion to analysis results. This is particularly important for real-time or time-sensitive analytics.

------
#### [ Storage requirements ]

Determine storage needs by determining how and where data is stored throughout the analytics pipeline. Important considerations include:
+ **Data volume:** Assess the amount of data being generated and collected, and estimate future data growth to plan for sufficient storage capacity.
+ **Data retention:** Define the duration for which data should be retained for historical analysis or compliance purposes. Determine the appropriate data retention policies.
+ **Data access patterns:** Understand how data will be accessed and queried to choose the most suitable storage solution. Consider read and write operations, data access frequency, and data locality.
+ **Data security:** Prioritize data security by evaluating encryption options, access controls, and data protection mechanisms to safeguard sensitive information.
+ **Cost optimization:** Optimize storage costs by selecting the most cost-effective storage solutions based on data access patterns and usage.
+ **Integration with analytics services:** Ensure seamless integration between the chosen storage solution and the data processing and analytics tools in the pipeline.

------
#### [ Types of data ]

When deciding on analytics services for the collection and ingestion of data, consider various types of data that are relevant to your organization's needs and objectives. Common types of data that you might need to consider includes:
+ **Transactional data:** Includes information about individual interactions or transactions, such as customer purchases, financial transactions, online orders, and user activity logs.
+ **File-based data:** Refers to structured or unstructured data that is stored in files, such as log files, spreadsheets, documents, images, audio files, and video files. Analytics services should support the ingestion of different file formats.
+ **Event data:** Captures significant occurrences or incidents, such as user actions, system events, machine events, or business events. Events can include any data that is arriving in high velocity that is captured for onstream or downstream processing.

------
#### [ Operational considerations ]

Operational responsibility is shared between you, and AWS, with the division of responsibility varying across different levels of modernization. You have the option of self-managing your analytics infrastructure on AWS or leveraging the numerous serverless analytics services to lesson your infrastructure management burden.

Self-managed options grant users greater control over the infrastructure and configurations, but they require more operational effort.

Serverless options abstract away much of the operational burden, providing automatic scalability, high availability, and robust security features, allowing users to focus more on building analytical solutions and driving insights rather than managing infrastructure and operational tasks. Consider these benefits of serverless analytics solutions:
+ **Infrastructure abstraction:** Serverless services abstract infrastructure management, relieving users from provisioning, scaling, and maintenance tasks. AWS handles these operational aspects, reducing management overhead.
+ **Auto-scaling and performance:** Serverless services automatically scale resources based on workload demands, ensuring optimal performance without manual intervention.
+ **High availability and disaster recovery:** AWS provides high availability for serverless services. AWS manages data redundancy, replication, and disaster recovery to enhance data availability and reliability.
+ **Security and compliance:** AWS manages security measures, data encryption, and compliance for serverless services, adhering to industry standards and best practices.
+ **Monitoring and logging:** AWS offers built-in monitoring, logging, and alerting capabilities for serverless services. Users can access detailed metrics and logs through Amazon CloudWatch.

------
#### [ Type of workload ]

When building a modern analytics pipeline, deciding on the types of workload to support is crucial to meet different analytical needs effectively. Key decision points to consider for each type of workload includes:

**Batch workload**
+ **Data volume and frequency:** Batch processing is suitable for large volumes of data with periodic updates.
+  **Data latency:** Batch processing might introduce some delay in delivering insights compared to real-time processing.

**Interactive analysis**
+ **Data query complexity:** Interactive analysis requires low-latency responses for quick feedback.
+ **Data visualization:** Evaluate the need for interactive data visualization tools to enable business users to explore data visually.

**Streaming workloads**
+ **Data velocity and volume:** Streaming workloads require real-time processing to handle high-velocity data.
+ **Data windowing:** Define data windowing and time-based aggregations for streaming data to extract relevant insights.

------
#### [ Type of analysis needed ]

Clearly define the business objectives and the insights you aim to derive from the analytics. Different types of analytics serve different purposes. For example:
+ Descriptive analytics is ideal for gaining a historical overview
+ Diagnostic analytics helps understand the reasons behind past events
+ Predictive analytics forecasts future outcomes
+ Prescriptive analytics provides recommendations for optimal actions

Match your business goals with the relevant types of analytics. Here are some key decision criteria to help you choose the right types of analytics:
+ **Data availability and quality:** Descriptive and diagnostic analytics rely on historical data, while predictive and prescriptive analytics require sufficient historical data and high-quality data to build accurate models.
+ **Data volume and complexity:** Predictive and prescriptive analytics require substantial data processing and computational resources. Ensure that your infrastructure and tools can handle the data volume and complexity.
+ **Decision complexity:** If decisions involve multiple variables, constraints, and objectives, prescriptive analytics may be more suitable to guide optimal actions.
+ **Risk tolerance:** Prescriptive analytics may provide recommendations, but come with associated uncertainties. Ensure that decision-makers understand the risks associated with the analytics outputs.

------
#### [ Evaluate scalability and performance ]

Assess the scalability and performance needs of the architecture. The design must handle increasing data volumes, user demands, and analytical workloads. Key decision factors to consider includes:
+ **Data volume and growth:** Assess the current data volume and anticipate future growth.
+ **Data velocity and real-time requirements:** Determine if the data needs to be processed and analyzed in real-time or near real-time.
+ **Data processing complexity:** Analyze the complexity of your data processing and analysis tasks. For computationally intensive tasks, services such as Amazon EMR provide a scalable and managed environment for big data processing.
+ **Concurrency and user load:** Consider the number of concurrent users and the level of user load on the system.
+ **Auto-scaling capabilities:** Consider services that offer auto-scaling capabilities, allowing resources to automatically scale up or down based on demand. This ensures efficient resource utilization and cost optimization.
+ **Geographic distribution:** Consider services with global replication and low-latency data access if your data architecture needs to be distributed across multiple regions or locations.
+ **Cost-performance trade-off:** Balance the performance needs with cost considerations. Services with high performance may come at a higher cost.
+ **Service-level agreements (SLAs):** Check the SLAs provided by AWS services to ensure they meet your scalability and performance expectations.

------
#### [ Data governance ]

Data governance is the set of processes, policies, and controls you need to implement to ensure effective management, quality, security, and compliance of your data assets. Key decision points to consider includes:
+ **Data retention policies:** Define data retention policies based on regulatory requirements and business needs and establish processes for secure data disposal when it is no longer needed.
+ **Audit trail and logging:** Decide on the logging and auditing mechanisms to monitor data access and usage. Implement comprehensive audit trails to track data changes, access attempts, and user activities for compliance and security monitoring.
+ **Compliance requirements:** Understand the industry-specific and geographic data compliance regulations that apply to your organization. Ensure that the data architecture aligns with these regulations and guidelines.
+ **Data classification:** Classify data based on its sensitivity and define appropriate security controls for each data class.
+ **Disaster recovery and business continuity:** Plan for disaster recovery and business continuity to ensure data availability and resilience in case of unexpected events or system failures.
+ **Third-party data sharing:** If sharing data with third-party entities, implement secure data sharing protocols and agreements to protect data confidentiality and prevent data misuse.

------
#### [ Security ]

The security of data in the analytics pipeline involves protecting data at every stage of the pipeline to ensure its confidentiality, integrity, and availability. Key decision points to consider includes:
+ **Access control and authorization:** Implement robust authentication and authorization protocols to ensure that only authorized users can access specific data resources.
+ **Data encryption:** Choose appropriate encryption methods for data stored in databases, data lakes, and during data movement between different components of the architecture.
+ **Data masking and anonymization:** Consider the need for data masking or anonymization to protect sensitive data, such as PII or sensitive business data, while allowing certain analytical processes to continue.
+ **Secure data integration:** Establish secure data integration practices to ensure that data flows securely between different components of the architecture, avoiding data leaks or unauthorized access during data movement.
+ **Network isolation:** Consider services that support [Amazon VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html) to avoid exposing resources to the public internet.

------
#### [ Plan for integration and data flows ]

Define the integration points and data flows between various components of the analytics pipeline to ensure seamless data flow and interoperability. Key decision points to consider includes:
+ **Data source integration:** Identify the data sources from which data will be collected, such as databases, applications, files, or external APIs. Decide on the data ingestion methods (batch, real-time, event-based) to bring data into the pipeline efficiently and with minimal latency.
+ **Data transformation:** Determine the transformations required to prepare data for analysis. Decide on the tools and processes to clean, aggregate, normalize, or enrich the data as it moves through the pipeline.
+ **Data movement architecture:** Choose the appropriate architecture for data movement between pipeline components. Consider batch processing, stream processing, or a combination of both based on the real-time requirements and data volume.
+ **Data replication and sync:** Decide on data replication and synchronization mechanisms to keep data up-to-date across all components. Consider real-time replication solutions or periodic data syncs depending on data freshness requirements.
+ **Data quality and validation:** Implement data quality checks and validation steps to ensure the integrity of data as it moves through the pipeline. Decide on the actions to be taken when data fails validation, such as alerting or error handling.
+ **Data security and encryption:** Determine how data will be secured during transit and at rest. Decide on the encryption methods to protect sensitive data throughout the pipeline, considering the level of security required based on data sensitivity.
+ **Scalability and resilience:** Ensure that the data flow design allows for horizontal scalability and can handle increased data volumes and traffic.

------
#### [ Architect for cost optimization ]

Building your analytics pipeline on AWS provides various cost optimization opportunities. To ensure cost efficiency, consider the following strategies:
+ **Resource sizing and selection:** Right-size your resources based on actual workload requirements. Choose AWS services and instance types that match the workloads performance needs while avoiding overprovisioning.
+ **Auto-scaling:** Implement auto-scaling for services that experience varying workloads. Auto-scaling dynamically adjusts the number of instances based on demand, reducing costs during low-traffic periods.
+ **Spot Instances:** Use Amazon EC2 Spot Instances for non-critical and fault-tolerant workloads. Spot Instances can significantly reduce costs compared to on-demand instances.
+ **Reserved instances:** Consider purchasing AWS Reserved Instances to achieve significant cost savings over on-demand pricing for stable workloads with predictable usage.
+ **Data storage tiering:** Optimize data storage costs by using different storage classes based on data access frequency.
+ **Data lifecycle policies:** Establish data lifecycle policies to automatically move or delete data based on its age and usage patterns. This helps manage storage costs and keeps data storage aligned with its value.

------

## Choose AWS analytics services
<a name="choose"></a>

Now that you know the criteria to evaluate your analytics needs, you are ready to choose which AWS analytics services are right for your organizational needs. The following table aligns sets of services with common capabilities and business goals.

- ****Unified analytics and AI****
  - **What is it optimized for?:** **Analytics and AI development**<br />Optimized for using a single development environment, Amazon SageMaker Unified Studio, to access data, analytics, and AI capabilities.
  - **Services:** [Amazon SageMaker](https://docs.aws.amazon.com/next-generation-sagemaker)

- ** **Data processing** **
  - **What is it optimized for?:** **Interactive analytics**<br />Optimized for performing real-time data analysis and exploration, which allows users to interactively query and visualize data. / **Services:** [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
  - **What is it optimized for?:** **Big data processing**<br />Optimized for processing, moving, and transforming large amounts of data. / **Services:** [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html)
  - **What is it optimized for?:** **Data catalog**<br />Optimized for providing detailed information about the available data, its structure, characteristics, and relationships. / **Services:** [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
  - **What is it optimized for?:** **Workflow orchestration**<br />Optimized for creating, scheduling, and monitoring data workflows using Apache Airflow to coordinate analytics processes and ETL jobs. / **Services:** [Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html)

- ****Data streaming****
  - **What is it optimized for?:** **Apache Kafka processing of streaming data**<br />Optimized for using Apache Kafka data-plane operations and running open source versions of Apache Kafka.  / **Services:** [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html)
  - **What is it optimized for?:** **Real-time processing**<br />Optimized for rapid and continuous data intake and aggregation, including IT infrastructure log data, application logs, social media, market data feeds, and web clickstream data. / **Services:** [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
  - **What is it optimized for?:** **Real-time streaming data delivery**<br />Optimized for delivering real-time streaming data to destinations such as Amazon S3, Amazon Redshift, OpenSearch Service, Splunk, Apache Iceberg Tables, and any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers. / **Services:** [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
  - **What is it optimized for?:** **Building Apache Flink applications**<br />Optimized for using Java, Scala, Python, or SQL to process and analyze streaming data. / **Services:** [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html)

- ****Business intelligence****
  - **What is it optimized for?:** **Dashboards and visualizations**<br />Optimized for visually representing complex datasets, and providing natural language query of your data.
  - **Services:** [Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)

- ****Search analytics****
  - **What is it optimized for?:** **Managed OpenSearch clusters**<br />Optimized for log analytics, real-time application monitoring, and clickstream analysis.
  - **Services:** [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)

- ****Data governance****
  - **What is it optimized for?:** **Managing data access**<br />Optimized for setting up the proper management, availability, usability, integrity, and security of data throughout its lifecycle.
  - **Services:** [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/what-is-datazone.html)

- ****Data collaboration****
  - **What is it optimized for?:** **Secure data clean rooms**<br />Optimized for collaborating with other companies without sharing raw underlying data.
  - **Services:** [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html)

- ****Data lake and warehouse****
  - **What is it optimized for?:** **Unified access to data lakes and data warehouses**<br />Built on a lakehouse architecture to optimize for unifying data access across Amazon S3 data lakes, Amazon Redshift data warehouses, operational databases, and third-party and federated data sources. / **Services:** [Amazon SageMaker](https://docs.aws.amazon.com/next-generation-sagemaker)
  - **What is it optimized for?:** **Object storage for data lakes**<br />Optimized for providing a data lake foundation with virtually unlimited scalability and high durability.  / **Services:** [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
  - **What is it optimized for?:** **Data warehousing**<br />Optimized for centrally storing, organizing, and retrieving large volumes of structured and sometimes semi-structured data from various sources within an organization. / **Services:** [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)

## Use AWS analytics services
<a name="use"></a>

You should now have a clear understanding of your business objectives, and the volume and velocity of data you will be ingesting and analyzing to begin building your data pipelines.

To explore how to use and learn more about each of the available services—we have provided a pathway to explore how each of the services work. The following sections provides links to in-depth documentation, hands-on tutorials, and resources to get you started from basic usage to more advanced deep dives.

------
#### [ Amazon Athena ]
+ **Getting started with Amazon Athena**

  Learn how to use Amazon Athena to query data and create a table based on sample data stored in Amazon S3, query the table, and check the results of the query.

  [Get started with the tutorial](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html)
+ **Get started with Apache Spark on Athena**

  Use the simplified notebook experience in Athena console to develop Apache Spark applications using Python or Athena notebook APIs.

  [Get started with the tutorial](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark.html)
+ **Catalog and govern Athena federated queries with Amazon SageMaker lakehouse architecture**

  Learn how to connect to, govern, and run federated queries on data stored in Amazon Redshift, DynamoDB, and Snowflake via the data lakehouse in Amazon SageMaker.

  [Read the blog](https://aws.amazon.com/blogs/big-data/catalog-and-govern-amazon-athena-federated-queries-with-amazon-sagemaker-lakehouse/)
+ **Analyzing data in Amazon S3 using Athena**

  Explore how to use Athena on logs from Elastic Load Balancers, generated as text files in a pre-defined format. We show you how to create a table, partition the data in a format used by Athena, convert it to Parquet, and compare query performance.

  [Read the blog post](https://aws.amazon.com/blogs/big-data/analyzing-data-in-s3-using-amazon-athena/)

------
#### [ AWS Clean Rooms ]
+  **Setting up AWS Clean Rooms**

  Learn how to set up AWS Clean Rooms in your AWS acccount.

   [Read the guide](https://docs.aws.amazon.com/clean-rooms/latest/userguide/setting-up.html)
+  **Unlock data insights across multi-party datasets using AWS Entity Resolution on AWS Clean Rooms without sharing underlying data**

  Learn how to use preparation and matching to help improve data matching with collaborators.

   [Read the blog post](https://aws.amazon.com/blogs/industries/unlock-data-insights-across-multi-party-datasets-using-aws-entity-resolution-on-aws-clean-rooms-without-sharing-underlying-data/)
+  **How differential privacy helps unlock insights without revealing data at the individual-level**

  Learn how AWS Clean Rooms Differential Privacy simplifies applying differential privacy and helps protect the privacy of your users.

   [Read the blog](https://aws.amazon.com/blogs/industries/how-differential-privacy-helps-unlock-insights-without-revealing-data-at-the-individual-level/)

------
#### [ Amazon Data Firehose ]
+  **Tutorial: Create a Firehose stream from console**

  Learn how to use the AWS Management Console or an AWS SDK to create a Firehose stream to your chosen destination.

   [Read the guide](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html)
+  **Send data to a Firehose stream**

  Learn how to use different data sources to send data to your Firehose stream.

   [Read the guide](https://docs.aws.amazon.com/firehose/latest/dev/basic-write.html)
+  **Transform source data in Firehose**

  Learn how to invoke your Lambda function to transform incoming source data and deliver the transformed data to destinations.

   [Read the guide](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html)

------
#### [ Amazon DataZone ]
+ **Getting started with Amazon DataZone **

  Learn how to create the Amazon DataZone root domain, obtain the data portal URL, walk through the basic Amazon DataZone workflows for data producers and data consumers.

  [Get started with the tutorial](https://docs.aws.amazon.com/datazone/latest/userguide/getting-started.html)
+ **Announcing the general availability of data lineage in the next generation of Amazon SageMaker and Amazon DataZone **

  Learn how Amazon DataZone uses automated lineage capture to focus on automatically collecting and mapping lineage information from AWS Glue and Amazon Redshift.

  [Read the blog](https://aws.amazon.com/blogs/aws/announcing-the-general-availability-of-data-lineage-in-the-next-generation-of-amazon-sagemaker-and-amazon-datazone/)

------
#### [ Amazon EMR ]
+ **Getting started with Amazon EMR**

  Learn how to launch a sample cluster using Spark, and how to run a simple PySpark script stored in an Amazon S3 bucket.

  [Get started with the tutorial](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html)
+ **Getting started with Amazon EMR on Amazon EKS**

  We show you how to get started using Amazon EMR on Amazon EKS by deploying a Spark application on a virtual cluster.

  [Explore the guide](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/getting-started.html)
+ **Get started with EMR Serverless**

  Explore how Amazon EMR Serverless provides a serverless runtime environment that simplifies the operation of analytics applications that use the latest open source frameworks.

  [Get started with the tutorial](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/getting-started.html)

------
#### [ AWS Glue ]
+ **Getting started with AWS Glue DataBrew**

  Learn how to create your first DataBrew project. You load a sample dataset, run transformations on that dataset, build a recipe to capture those transformations, and run a job to write the transformed data to Amazon S3.

  [Get started with the tutorial](https://docs.aws.amazon.com/databrew/latest/dg/getting-started.html)
+ **Transform data with AWS Glue DataBrew**

  Learn about AWS Glue DataBrew, a visual data preparation tool that makes it easy for data analysts and data scientists to clean and normalize data to prepare it for analytics and machine learning. Learn how to construct an ETL process using AWS Glue DataBrew.

  [Get started with the lab](https://catalog.workshops.aws/introduction-to-analytics-on-aws/en-US/lab-guide/transform-glue-databrew)
+ **AWS Glue DataBrew immersion day**

  Explore how to use AWS Glue DataBrew to clean and normalize data for analytics and machine learning.

  [Get started with the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/6532bf37-3ad2-4844-bd26-d775a31ce1fa/en-US)
+ **Getting started with the AWS Glue Data Catalog**

  Learn how to create your first AWS Glue Data Catalog, which uses an Amazon S3 bucket as your data source.

  [Get started with the tutorial](https://docs.aws.amazon.com/glue/latest/dg/start-data-catalog.html)
+ **Data catalog and crawlers in AWS Glue**

  Discover how you can use the information in the Data Catalog to create and monitor your ETL jobs.

  [Explore the guide](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)

------
#### [ Amazon Kinesis Data Streams ]
+ **Getting started tutorials for Amazon Kinesis Data Streams**

  Learn how to process and analyze real-time stock data.

  [Get started with the tutorials](https://docs.aws.amazon.com/streams/latest/dev/examples.html)
+ **Architectural patterns for real-time analytics using Amazon Kinesis Data Streams, part 1**

  Learn about common architectural patterns of two use cases: time series data analysis and event driven microservices.

  [Read the blog](https://aws.amazon.com/blogs/big-data/architectural-patterns-for-real-time-analytics-using-amazon-kinesis-data-streams-part-1/)
+ **Architectural Patterns for real-time analytics using Amazon Kinesis Data Streams, part 2**

  Learn about AI applications with Kinesis Data Streams in three scenarios: real-time generative business intelligence, real-time recommendation systems, and Internet of Things data streaming and inferencing.

  [Read the blog](https://aws.amazon.com/blogs/big-data/architectural-patterns-for-real-time-analytics-using-amazon-kinesis-data-streams-part-2-ai-applications/)

------
#### [ Amazon Managed Service for Apache Flink ]
+ **What is Amazon Managed Service for Apache Flink?**

  Understand the fundamental concepts of Amazon Managed Service for Apache Flink.

  [Explore the guide](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html)
+ **Amazon Managed Service for Apache Flink Workshop**

  In this workshop, you will learn how to deploy, operate, and scale a Flink application with Amazon Managed Service for Apache Flink.

  [Attend the virtual workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/2437ee74-38ed-4817-94b9-45b920cb168a/en-US)

------
#### [ Amazon MSK ]
+ **Getting Started with Amazon MSK**

  Learn how to create an Amazon MSK cluster, produce and consume data, and monitor the health of your cluster using metrics.

  [Get started with the guide](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html)
+ **Amazon MSK Workshop**

  Go deep with this hands-on Amazon MSK workshop.

  [Get started with the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/c2b72b6f-666b-4596-b8bc-bafa5dcca741/en-US)

------
#### [ Amazon MWAA ]
+ **Getting started with Amazon MWAA**

  Learn how to create your first MWAA environment, upload a DAG to Amazon S3, and run your first workflow.

  [Get started with the tutorial](https://docs.aws.amazon.com/mwaa/latest/userguide/get-started.html)
+ **Building data pipelines with Amazon MWAA**

  Learn how to build end-to-end data pipelines that orchestrate other AWS analytics services like Glue, EMR, and Redshift. This blog post explores a streamlined, configuration-driven approach to orchestrating dbt Core jobs using MWAA and Cosmos, with jobs running transformations on Amazon Redshift.

  [Read the blog post](https://aws.amazon.com/blogs/big-data/build-data-pipelines-with-dbt-in-amazon-redshift-using-amazon-mwaa-and-cosmos/)
+ **Amazon MWAA workshop**

  Explore hands-on exercises to learn how to deploy, configure, and use Amazon MWAA for data workflow orchestration.

  [Get started with the workshop](https://catalog.workshops.aws/amazon-mwaa-for-analytics/en-US)
+ **Best practices for Amazon MWAA**

  Learn architectural patterns and best practices for using Amazon MWAA in your analytics workflows.

  [Read the guide](https://docs.aws.amazon.com/mwaa/latest/userguide/best-practices.html)

------
#### [ OpenSearch Service ]
+ **Getting started with OpenSearch Service **

  Learn how to use Amazon OpenSearch Service to create and configure a test domain.

  [Get started with the tutorial](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html)
+ **Visualizing customer support calls with OpenSearch Service and OpenSearch Dashboards**

  Discover a full walkthrough of the following situation: a business receives some number of customer support calls and wants to analyze them. What is the subject of each call? How many were positive? How many were negative? How can managers search or review the the transcripts of these calls?

  [Get started with the tutorial](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/walkthrough.html)
+ **Getting started with Amazon OpenSearch Serverless workshop**

  Learn how to set up a new Amazon OpenSearch Serverless domain in the AWS console. Explore the different types of search queries available, and design eye-catching visualizations, and learn how you can secure your domain and documents based on assigned user privileges.

  [Get started with the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/f8d2c175-634d-4c5d-94cb-d83bbc656c6a/en-US)
+ **Cost Optimized Vector Database: Introduction to Amazon OpenSearch Service quantization techniques**

  Learn how OpenSearch Service supports scalar and product quantization techniques to optimize memory usage and reduce operational costs.

  [Read the blog post](https://aws.amazon.com/blogs/big-data/cost-optimized-vector-database-introduction-to-amazon-opensearch-service-quantization-techniques/)

------
#### [ Quick ]
+ **Getting started with Quick data analysis**

  Learn how to create your first analysis. Use sample data to create either a simple or a more advanced analysis. Or you can connect to your own data to create an analysis.

  [Explore the guide](https://docs.aws.amazon.com/quicksight/latest/user/getting-started.html)
+ **Visualizing with Quick**

  Discover the technical side of business intelligence (BI) and data visualization with AWS. Learn how to embed dashboards into applications and websites, and securely manage access and permissions.

  [Get started with the course](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/41/visualizing-with-quicksight)
+ **Quick workshops**

  Get a head start on your Quick journey with workshops

  [Get started with the workshops](https://catalog.workshops.aws/quicksight/en-US)

------
#### [ Amazon Redshift ]
+ **Getting started with Amazon Redshift Serverless**

  Understand the basic flow of Amazon Redshift Serverless to create serverless resources, connect to Amazon Redshift Serverless, load sample data, and then run queries on the data.

  [Explore the guide](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html)
+ **Amazon Redshift deep dive workshop**

  Explore a series of exercises which help users get started using the Amazon Redshift platform.

  [Get started with the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/380e0b8a-5d4c-46e3-95a8-82d68cf5789a/en-US)

------
#### [ Amazon S3 ]
+ **Getting started with Amazon S3**

  Learn how to create your first DataBrew project. You load a sample dataset, run transformations on that dataset, build a recipe to capture those transformations, and run a job to write the transformed data to Amazon S3.

  [Get started with the guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)

------
#### [ Amazon SageMaker ]
+  **Getting started with SageMaker**

  Learn how to create a project, add members, and use the sample JupyterLab notebook to begin building.

   [Read the guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/getting-started.html)
+  **Introducing the next generation of Amazon SageMaker: The center for all your data, analytics, and AI**

  Learn how to get started with data processing, model development, and generative AI app development.

   [Read the blog](https://aws.amazon.com/blogs/aws/introducing-the-next-generation-of-amazon-sagemaker-the-center-for-all-your-data-analytics-and-ai/)
+  **What is SageMaker Unified Studio?**

  Learn about the capabilities of SageMaker Unified Studio and how to access them when you use Amazon SageMaker.

   [Read the guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/what-is-sagemaker-unified-studio.html)
+  **Getting started with the lakehouse architecture of Amazon SageMaker**

  Learn how to create a project and to browse, upload, and query data for your business use cases in Amazon SageMaker.

   [Read the guide](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-get-started.html)
+  **Data connections in the lakehouse architecture of Amazon SageMaker**

  Learn how the lakehouse architecture provides a unified approach to managing data connections across AWS services and enterprise applications.

   [Read the guide](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-data-connection.html)
+  **Catalog and govern Athena federated queries with the SageMaker lakehouse architecture**

  Learn how to connect to, govern, and run federated queries on data stored in Amazon Redshift, DynamoDB, and Snowflake for your Amazon SageMaker projects.

   [Read the blog](https://aws.amazon.com/blogs/big-data/catalog-and-govern-amazon-athena-federated-queries-with-amazon-sagemaker-lakehouse/)

------

## Explore ways to use AWS analytics services
<a name="explore"></a>

------
#### [ Editable architecture diagrams ]

**Reference architecture diagrams**

Explore architecture diagrams to help you develop, scale, and test your analytics solutions on AWS.

[ Explore analytics reference architectures](https://aws.amazon.com/architecture/reference-architecture-diagrams/?achp_navlib4&ams%23interactive-card-vertical%23pattern-data--366709333.filter=%257B%2522search%2522%253A%2522analytics%2522%257D)

------
#### [ Ready-to-use code ]

|  |  |
| --- |--- |
| *Featured solution*<br />**Scalable Analytics Using Apache Druid on AWS**<br />Deploy AWS-built code to help you set up, operate, and manage Apache Druid on AWS, a cost-effective, highly available, resilient, and fault tolerant hosting environment.<br />[Explore this solution](https://aws.amazon.com/solutions/implementations/scalable-analytics-using-apache-druid-on-aws/) | **AWS Solutions**<br />Explore pre-configured, deployable solutions and their implementation guides, built by AWS.<br />[Explore all AWS security, identity, and governance solutions](https://aws.amazon.com/architecture/?nc2=h_ql_le_arc&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23solution&awsf.methodology=*all&awsf.tech-category=tech-category%23analytics&awsf.industries=*all&awsf.business-category=*all) |

------
#### [ Documentation ]

|  |  |
| --- |--- |
| **Analytics whitepapers** <br />Explore whitepapers for further insights and best practices on choosing, implementing, and using the analytics services that best fit your organization. <br />[Explore analytics whitepapers ](https://aws.amazon.com/whitepapers/?ams%23interactive-card-vertical%23pattern-data-1858756679.filter=%257B%2522filters%2522%253A%255B%257B%2522id%2522%253A%2522GLOBAL%2523aws-tech-category.and%2522%252C%2522value%2522%253A%255B%2522analytics%2522%255D%257D%255D%257D) | **AWS Big Data Blog** <br />Explore blog posts that address specific big data use cases. <br /> [Explore the AWS Big Data blog](https://aws.amazon.com/blogs/big-data/)  |

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Decision Guides. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query decision-guides` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
