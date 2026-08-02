---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/data-eng.html
---

# Data engineering
<a name="data-eng"></a>

**Automate and orchestrate data flows across your organization. **

Use metadata to automate [pipelines](https://aws.amazon.com/glue/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc) that process raw data and generate optimized outputs. Leverage existing architectural guardrails and security controls as defined across the AWS CAF platform architecture and platform engineering capabilities, as well as the Operations perspective. Work with the platform engineering enablement team to develop reusable [blueprints](https://aws.amazon.com/blogs/big-data/simplify-data-integration-pipeline-development-using-aws-glue-custom-blueprints/) for common patterns that simplify pipeline deployment.

## Start
<a name="data-eng-start"></a>

### Deploy a data lake
<a name="deploy-a-data-lake.57048c19-595b-5922-8f9d-3076364f3ae7"></a>

Establish foundational data storage capabilities by using suitable storage solutions for structured and unstructured data. This enables you to collect and store data from various sources, and makes the data accessible for further processing and analysis. Data storage is a critical component of a data engineering strategy. A well-designed data storage architecture allows organizations to store, manage, and access their data efficiently and cost-effectively. AWS offers a variety of data storage services to meet specific business needs.

For example, you can establish foundational data storage capabilities by using [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) for object storage, [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) for relational databases, and [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html) for data warehousing. These services help you store data securely and cost-effectively, and make the data easily accessible for further processing and analysis. We recommend that you also implement data storage best practices, such as data partitioning and compression, to improve performance and reduce costs.

### Develop data ingestion patterns
<a name="develop-data-ingestion-patterns.654e2dce-c7eb-5eae-bc4d-4f626284fcc8"></a>

To automate and orchestrate data flows, establish data ingestion processes to gather data from diverse sources, including databases, files, and APIs. Your data ingestion processes should support business agility and take governance controls into account.

The orchestrator should be capable of running cloud-based services and provide a automated scheduling mechanism. It should offer options for conditional links and dependencies among tasks, along with polling and error-handling capabilities. Additionally, it should seamlessly integrate with alerting and monitoring systems to ensure that pipelines run smoothly.

A few popular orchestration mechanisms include:
+ *Time-based orchestration* starts a workflow on a recursive interval and at a defined frequency.
+ *Event-based orchestration* starts a workflow based on the occurrence of an event such as creation of a file or an API request.
+ *Polling* implements a mechanism in which a task or workflow calls a service (for example, through an API) and waits for a defined response before proceeding to the next step.

Modern architecture design emphasizes taking advantage of managed services that simplify infrastructure management in the cloud and reduce the burden on developers and infrastructure teams. This approach also applies to data engineering. We recommend that you use managed services where applicable to build data ingestion pipelines to accelerate your data engineering processes. Two examples of these types of services are Amazon Managed Workflows for Apache Airflow (Amazon MWAA)and AWS Step Functions:
+ **Apache Airflow** is a popular orchestration tool for programmatically authoring, scheduling, and monitoring workflows. AWS offers [Amazon Managed Workflows for Apache Airflow (Amazon MWAA)](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html) as a managed service that enables developers to focus on building rather than managing infrastructure for the orchestration tool. Amazon MWAA makes it easy to author workflows by using Python scripts. A directed acyclic graph (DAG) represents a workflow as a collection of tasks in a way that shows each task's relationships and dependencies. You can have as many DAGs as you want, and Apache Airflow will run them according to each task's relationships and dependencies.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) helps developers build a low-code visual workflow for automating IT and business processes. The workflows that you build with Step Functions are called *state machines*, and each step of your workflow is called a *state*. You can use Step Functions to create workflows for built-in error handling, parameter passing, recommended security settings, and state management. These reduce the amount of code you have to write and maintain. Tasks perform work by coordinating with another AWS service or an application that you host either on premises or in a cloud environment.

### Accelerate data processing
<a name="accelerate-data-processing.8d87ac38-933d-5ca7-98a3-c3712b58b1df"></a>

Data processing is a crucial step in making sense of the vast amounts of data collected by modern organizations. To get started with data processing, AWS offers managed services such as [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) or [AWS Data Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/what-is-datapipeline.html), which provide powerful extract, transform, and load (ETL) capabilities. Organizations can use these services to start processing and transforming raw data, including cleaning, normalizing, and aggregating data to prepare it for analysis.

Data processing starts with simple techniques such as aggregation and filtering to perform initial data transformations. As data processing needs evolve, you can implement more advanced ETL processes that enable you to extract data from various sources, transform it to fit your specific needs, and load it into a centralized data warehouse or database for unified analysis. This approach ensures that data is accurate, complete, and available for analysis in a timely manner.

By using AWS managed services for data processing, organizations can benefit from a higher level of automation, scalability, and cost-effectiveness. These services automate many routine data processing tasks, such as schema discovery, data profiling, and data transformation, and free up valuable resources for more strategic activities. Additionally, these services scale automatically to support growing data volumes.

### Provide data visualization services
<a name="provide-data-visualization-services.7bad93b3-c67b-55cb-8bb1-70f877286c14"></a>

Find ways to make data available to decision-makers who use data visualization to interpret data meaningfully and quickly. Through visualizations you can interpret patterns and increase engagement across a diverse set of stakeholders, regardless of their technical skills. A good platform enables data engineering teams to provision resources that provide data visualization rapidly and with little overhead. You can also provide self-service capabilities by using tools that can easily query data stores without the need for engineering expertise. Consider using built-in tooling that can provide serverless business intelligence through data visuals and interactive dashboards, and that can use natural language to query back-end data.

## Advance
<a name="data-eng-advance"></a>

### Implement near real-time data processing
<a name="implement-near-real-time-data-processing.91251ef3-3e06-5154-9da3-9b3654ec02bf"></a>

Data processing is an essential component of any data engineering pipeline, which enables organizations to transform raw data into meaningful insights. In addition to traditional batch processing, real-time data processing has become increasingly important in today's fast-paced business environment. Real-time data processing enables organizations to respond to events as they occur, and improves decision-making and operational efficiency.

### Validate data quality
<a name="validate-data-quality.89a6e2bd-9386-508f-a13f-6bd5c7ed5c4c"></a>

Data quality directly impacts the accuracy and reliability of insights and decisions that are derived from data. Implementing data validation and cleansing processes is essential to ensure that you use high-quality and trustworthy data for analysis.

Data validation involves verifying the accuracy, completeness, and consistency of the data by checking it against predefined rules and criteria. This helps identify any discrepancies or errors in the data, and ensures that it is fit for purpose. Data cleansing involves the identification and correction of any inaccuracies, inconsistencies, or duplications in the data.

By implementing data quality processes and tools, organizations can improve the accuracy and reliability of insights derived from the data, resulting in better decision-making and operational efficiency. This not only enhances the organization's performance but also increases stakeholder confidence and trust in the data and analysis produced.

### Prove data transformation services
<a name="prove-data-transformation-services.ef72d0ea-ea09-5fce-a87b-dfe3fed6c35b"></a>

Data transformation prepares data for advanced analytics and machine learning models. It involves using techniques such as data normalization, enrichment, and deduplication to ensure that the data is clean, consistent, and ready for analysis.
+ *Data normalization* involves organizing data into a standard format, eliminating redundancies, and ensuring that data is consistent across different sources. This makes it easier to analyze and compare data from multiple sources and enables organizations to gain a more comprehensive understanding of their operations.
+ *Data enrichment* involves enhancing existing data with additional information from external sources such as demographic data or market trends. This provides valuable insights into customer behavior or industry trends that might not be apparent from internal data sources alone.
+ *Deduplication* involves identifying and removing duplicate data entries, and ensuring that the data is accurate and free from errors. This is especially important when dealing with large datasets, where even a small percentage of duplication might skew the results of the analysis.

By using advanced data transformation techniques, organizations ensure that their data is of high quality, accurate, and ready for more complex analysis. This leads to better decision-making, increased operational efficiency, and a competitive advantage in the marketplace.

### Enable data democratization
<a name="enable-data-democratization.bb060159-9f38-5bb1-9300-f81d844bc756"></a>

Promote a culture of data democratization by making data accessible, understandable, and usable for all employees. Data democratization helps employees make data-driven decisions and contributes to the organization's data-driven culture. This means breaking down silos and creating a culture where data is shared and used by all employees to drive decision-making.

Overall, data democratization is about creating a culture where data is valued, accessible, and understandable by everyone in the organization. By enabling data democratization, organizations foster a data-driven culture that drives innovation, improves decision-making, and ultimately leads to business success.

## Excel
<a name="data-eng-excel"></a>

### Provide UI-based orchestration
<a name="provide-ui-based-orchestration.0cdba747-eff7-574c-b4b2-09ac5f2f25a8"></a>

To build organizations that are agile and use effective approaches, it is important to plan for a modern orchestration platform that is used by development and operations resources across lines of business. The goal is to develop, deploy, and share data pipelines and workflows without being dependent on a single team, technology, or support model. This is achieved through capabilities such as UI-based orchestrating. Features such as drag-and-drop interaction enables users who have little technical expertise to construct DAGs and state machine data flows. These components can then generate executable code that orchestrates data pipelines.

DataOps helps overcome the complexities of data management and ensures a seamless data flow across organizations. A metadata-driven approach ensures data quality and compliance in accordance with your organization's mandates. Investment in toolsets such as microservices, containerization, and serverless functions improves scalability and agility.

Relying on data engineering teams to generate value out of data and leaving day-to-day infrastructure tasks to automation enables organizations to achieve excellence in automation and orchestration. Near real-time monitoring and logging of data flow management tasks support immediate remediation actions and improve the performance and security of the data flow pipeline. These principles help achieve scalability and performance while ensuring a secure data-sharing model, and set organizations up for success in the future.

### Integrate DataOps
<a name="integrate-dataops.2f979505-07b3-5ada-a9b8-8755e9925f68"></a>

DataOps is a modern approach to data engineering that emphasizes the integration of development and operations processes to streamline data pipeline creation, testing, and deployment. To implement DataOps best practices, organizations use infrastructure as code (IaC) and continuous integration and continuous delivery (CI/CD) tools. These tools support automated pipeline creation, testing, and deployment, which significantly improve efficiency and reduce errors. DataOps teams work with platform engineering enablement teams to build these automations, so each team can focus on what they do best.

Implementing DataOps methodologies helps foster a collaborative environment for data engineers, data scientists, and business users, and enables rapid development, deployment, and monitoring of data pipelines and analytics solutions. This approach provides more seamless communication and collaboration across teams, which leads to faster innovation and better outcomes.

To take full advantage of the benefits of DataOps, it is important to streamline data engineering processes. This is achieved by using best practices from platform engineering teams, including code review, continuous integration, and automated testing. By implementing these practices, organizations ensure that data pipelines are reliable, scalable, and secure, and that they meet the needs of both business and technical stakeholders.
