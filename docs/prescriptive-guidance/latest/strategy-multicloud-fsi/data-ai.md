---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud-fsi/data-ai.html
---

# Establish a modern multicloud data and AI strategy
<a name="data-ai"></a>

A robust multicloud data strategy is essential for ensuring seamless data integration, stringent governance for compliance and resilience, and adherence to data sovereignty laws. It should include a cost-management framework that supports flexible scalability in line with organizational growth. By addressing these critical areas—integration, governance, resilience, sovereignty, and scalability—you can effectively optimize data assets across platforms. This ensures security and compliance, and enhances decision-making and operational efficiency.

When you build your multicloud data strategy, you should recognize that data management is the foundation of successful AI and generative AI applications. High-quality, well-managed data is both a differentiator and the cornerstone of innovative AI technologies. AI systems require diverse, accurate, and comprehensive datasets to train effectively. These systems can then create insights and generate value that would be impossible with traditional analytics. Working with data across multiple cloud service environments introduces additional considerations that are discussed in the following sections.

## Integration and accessibility
<a name="accessibility"></a>

The guiding principle of a multicloud data strategy is managing data that's spread across various platforms without sacrificing integrity and accessibility. You must develop a strategy that prioritizes interoperability and consistency. This includes implementing integration tools that connect disparate cloud services and provide a unified data view across clouds. A unified view facilitates an AI model's access to data, and ensures that teams and applications can easily find and use the data they need. We recommend that you create a unified data catalog that identifies data owners, custodians, and governance requirements while enabling a self-service experience for your data customers across your organization. AWS Partners such as Databricks, Snowflake, and Colibra have proven track records in successful data integration.

## Data lineage
<a name="data-lineage"></a>

When you use multiple CSPs, you must have a complete understanding of your data lineage, that is, where your data comes from. You must document the sources and owners of your data, the results they produced, and how these were applied, especially if you're using generative AI. A data lineage strategy shows you and third parties what data you have and how it is used. For multicloud customers, we recommend  that you focus on a federated governance model that includes automated lineage collection and data quality measures that cross all your cloud environments.

## Governance and compliance
<a name="government"></a>

A comprehensive multicloud data strategy must enforce stringent data protection policies, privacy controls, and legal compliance across all cloud environments. This includes the application of consistent data encryption, anonymization, and adherence to regulations such as General Data Protection Regulation (GDPR) and PCI DSS. This governance supports AI systems by ensuring that the data they use is both secure and compliant, and by maintaining trust and integrity in AI outputs. We recommend that you set up proactive alarms for compliance violations by using automated tooling. This *continual compliance* approach should use cloud-native and ISV solutions to remove manual efforts from detective controls. These controls must operate in every cloud environment that you host sensitive data in.

## Centralizing and analyzing security data
<a name="security-data"></a>

In a multicloud environment, security management is complex because of the variety of systems and data sources that are involved. Centralizing security data across multiple clouds helps enable better security by providing real-time analysis and response. This centralized approach requires tools that aggregate security alerts and automate the analysis of security data across CSPs. It simplifies the management of security alerts and helps enhance the detection of potential threats by applying consistent security policies and procedures across all cloud platforms.

## Centralizing application monitoring
<a name="monitoring"></a>

Central application monitoring in a multicloud environment is essential for maintaining performance and availability. It requires gathering and analyzing performance data from applications that are deployed across various cloud platforms. These solutions typically feature unified dashboards that display a wide range of operational metrics, logs, traces, and alarms. Centralized visibility enables administrators to monitor application health comprehensively and respond swiftly to any issues, and ensures consistent performance across all cloud environments. We recommend that you create centralized monitoring that includes cloud-native sources instead of relying exclusively on telemetry from your applications.

## Performance optimization
<a name="performance"></a>

Minimizing latency is essential to maintaining the performance of cloud-based applications and AI models. Optimizing data storage locations and employing edge computing are strategies for reducing latency. Implementing data caching strategies and choosing the appropriate data storage technologies significantly boost overall system performance, and facilitate quicker AI processing and real-time analytics. We recommend that you maintain training data close to your ML workloads. You can exfiltrate trained models to other environments and operate them with lower latency for customer-facing workloads. Organizations typically use [Retrieval Augmented Generation (RAG)](https://aws.amazon.com/what-is/retrieval-augmented-generation/) to gain better AI insights from custom data sources, which must also be colocated with low-latency networks to their trained models.

## Providing choices in AI/ML strategy
<a name="ai-ml-choices"></a>

FIs often give their teams the flexibility to choose from a diverse array of machine learning (ML) tools and platforms. This choice gives organizations the ability to adopt the best technology that aligns with each project's specific requirements, whether they involve complex datasets, require real-time processing, or necessitate highly scalable solutions. For multicloud enterprises, we recommend that you let your teams self-select AI models and managed services that best meet their business goals from each CSP, instead of offering a single AI service on one cloud that is a suboptimal fit for the workload.

## Optimizing multicloud operations with DataOps and MLOps
<a name="dataops-mlops"></a>

In multicloud operations, the challenges of managing cloud services require a strategic implementation of automation, data operations (DataOps), and machine learning operations (MLOps). These technologies and methodologies are essential for streamlining workflows, reducing complexity, and optimizing the management and operationalization of data and ML models.

DataOps improves the integration and collaboration of data flows between data managers and consumers. Implementing DataOps involves setting up agile data management processes that are similar to the agile methodologies in software development. This includes infrastructure as code (IaC), continuous integration and continuous delivery (CI/CD) pipelines for data, automated testing for data validity, and rapid iteration of data models. To improve your DataOps processes, we recommend that you create cross-functional teams that include data scientists, data engineers, and operations staff.

MLOps focuses on the lifecycle management of ML models to ensure scalability, reproducibility, and maintainability. To implement MLOps, organizations adopt version control systems for models and datasets, automate model training and deployment processes, and continuously monitor the performance of deployed models to detect model and data drift. If performance degrades, they initiate model retraining. Tools, such as MLflow for model lifecycle management, TensorFlow Extended (TFX) for end-to-end ML pipelines, and Kubeflow for orchestrating scalable ML models on Kubernetes, help implement MLOps practices across environments.

We recommend that you prioritize both DataOps and MLOps for all flows between CSPs, and use automated pipelines that proactively deploy, monitor, and generate alerts when data quality is endangered. Do not rely on human intervention, and engineer solutions that scale through automation at every opportunity.

## Data pipeline cost management
<a name="zero-etl"></a>

Managing costs effectively in a multicloud environment involves choosing the right mix of cloud services and pricing models. Using tools for monitoring and managing resource usage helps you allocate resources cost-effectively when you run cost-intensive AI computations and data storage across multiple clouds.

Adopt a strategy for [zero-ETL](https://aws.amazon.com/what-is/zero-etl/), which is a set of integrations that eliminates the need to build extract, transform, and load (ETL) data pipelines, wherever possible. Traditionally, ETL is a major driver of data pipeline cost, because it often loads data that might not be required for all ML workloads. Zero-ETL features support a more cost-efficient multicloud strategy, and enable organizations to optimize their investments while using powerful AI and data analytics capabilities.
