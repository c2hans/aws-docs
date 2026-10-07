---
source_url: https://docs.aws.amazon.com//solutions/sustainability-insights-framework-on-aws/index.html
---

---
title: 'Guidance for Sustainability Insights Framework on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/sustainability-insights-framework-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Sustainability Insights Framework on AWS

## Overview

This Guidance demonstrates how you can automate your carbon footprint tracking with the Sustainability Insights Framework (SIF) on AWS. If you are looking to build a new carbon footprint tracking system or to improve an existing one, this Guidance will help you accelerate the design and automate tracking processes.

## How it works

### Overview

The SIF is composed of a suite of modules focusing on a specific set of features. This conceptual architecture shows these modules and their interactions.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sustainability-insights-framework-on-aws.pdf)Step 1Users interact with SIF through REST APIs.

Step 2The Access Management module is where users and permissions are managed and resources are separated by groups.

Step 3When performing data processing calculations, the Impacts module enables users to manage resources, such as impact factors, that can be referenced from within the Calculations and Pipelines modules.

Step 4The Reference Datasets module enables users to manage datasets, such as lookup tables. These datasets can be referenced from within the Calculations and Pipelines modules.

Step 5The Calculations module enables users to define and manage equations or functions which can be referenced in other modules to perform data processing calculations.

Step 6The Pipelines module enables users to configure data processing pipelines used to perform calculations.

Step 7The Pipeline Processor module is responsible for orchestrating pipelines and performing pipeline aggregations.

Step 8The Calculator module is a backend component that runs operations in a pipeline. This can include arithmetic or the lookup of resources.

### Access Management

The Access Management Module uses the concepts of users and groups to allow for permissions management and segregation of resources within SIF. SIF users can define users and groups through an external REST API.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sustainability-insights-framework-on-aws.pdf)Step 1Users of SIF interact with the Access Management module through an externally available API.

Step 2The externally available API consists of a REST API in **Amazon API Gateway**. The application logic is deployed in **AWS Lambda**.

Step 3User authentication is done through tokens received from **Amazon Cognito**.

Step 4The Access Management data is stored in an **Amazon DynamoDB** table.

Step 5Access Management resource changes emit events to a message bus in **Amazon EventBridge**. Events can be tracked to update other components of the framework.

### Impacts

The Impacts Module enables users to manage impact-related resources. These resources can be referenced from within the Calculations and Pipelines modules when performing data processing calculations, such as emissions.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sustainability-insights-framework-on-aws.pdf)Step 1Users of SIF interact with the Impacts module through an externally available API.

Step 2The externally available API consists of a REST API in **API Gateway**. The application logic is deployed in **Lambda**.

Step 3User authentication is done through tokens received from **Amazon Cognito**. Authorization is done through the Access Management module.

Step 4Impact data is stored in a **DynamoDB** table.

Step 5**Amazon Simple Queue Service (Amazon SQS)** is used along with a Lambda Impact Task Processor to orchestrate bulk Impact creation tasks.

Step 6Amazon SQS asynchronously processes metadata updates to resources, such as adding searchable tags.

Step 7Impacts resource changes emit events to a message bus in **EventBridge**. Events can be tracked to update other components of the framework.

### Reference Datasets

The Reference Datasets Module enables users to manage datasets, such as lookup tables. These datasets can be referenced from within the Calculations and Pipelines modules when performing data processing calculations, such as emissions.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sustainability-insights-framework-on-aws.pdf)Step 1Users of SIF interact with the Reference Datasets module through an externally available API and file uploads to **Amazon Simple Storage Service (Amazon S3)** through a pre-signed URL.

Step 2The externally available API consists of a REST API in **API Gateway**. The application logic is deployed in **Lambda**.

Step 3User authentication is done through tokens received from **Amazon Cognito**. Authorization is done through the Access Management module.

Step 4Data (such as dataset names) and metadata (such as tags) are stored in a **DynamoDB** table.

Step 5The dataset is stored in **Amazon S3**.

Step 6The dataset is indexed on Create/Update using **AWS Step Functions**.

Step 7Amazon SQS asynchronously processes metadata updates to resources, such as adding searchable tags.

Step 8Reference Dataset resource changes emit events to a message bus in **EventBridge**. Events can be tracked to update other components of the framework.

### Calculations

The Calculations Module enables users to define and manage equations or functions. These equations or functions can then be referenced in other Calculations or Pipelines modules when performing data processing calculations, such as emissions.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sustainability-insights-framework-on-aws.pdf)Step 1Users of SIF interact with the Calculations module through an externally available API.

Step 2The externally available API consists of a REST API in **API Gateway**. The application logic is deployed in **Lambda**.

Step 3User authentication is done through tokens received from **Amazon Cognito**. Authorization is done through the Access Management module.

Step 4Calculations data is stored in a **DynamoDB** table.

Step 5Amazon SQS asynchronously processes metadata updates to resources, such as adding searchable tags.

Step 6Calculations resource changes emit events to a message bus in **EventBridge**. Events can be tracked to update other components of the framework.

### Pipelines

The Pipelines Module enables users to manage Pipeline configurations. These configurations define data processing pipelines used to perform calculations, such as emissions. A Pipeline can be configured to aggregate outputs across executions and groups into metrics. Metrics capture key performance indicators (KPIs), such as total emissions over time.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sustainability-insights-framework-on-aws.pdf)Step 1Users of SIF interact with the Pipelines module through an externally available API.

Step 2The externally available API consists of a REST API in **API Gateway**. The application logic is deployed in **Lambda**.

Step 3User authentication is done through tokens received from **Amazon Cognito**. Authorization is done through the Access Management module.

Step 4Pipeline configuration is stored in a **DynamoDB** table.

Step 5The Pipelines module can directly invoke the Calculator module to dry run a pipeline configuration.

Step 6Amazon SQS asynchronously processes metadata updates to resources, such as adding searchable tags.

Step 7Pipelines resource changes emit events to a message bus in **EventBridge**. Events can be tracked to update other components of the framework.

### Pipeline Processor

The Pipeline Processor Module is responsible for the orchestration of Pipelines. This includes starting a pipeline execution in response to input files provided by a user and performing any aggregations defined in the pipeline configuration. The Pipeline Processor module also provides the status of pipeline executions.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sustainability-insights-framework-on-aws.pdf)Step 1Users of SIF interact with the Pipeline Processor module through an externally available API.

Step 2The externally available API consists of a REST API in **API Gateway**. The application logic is deployed in **Lambda**.

Step 3User authentication is done through tokens received from **Amazon Cognito**. Authorization is done through the Access Management module.

Step 4The REST API allows a user to query the execution status of a pipeline, query for activities processed by a pipeline, and query for metrics aggregated from activities.

Step 5Activity data processed by a pipeline is stored in an **Amazon Aurora** Serverless v2 database.

Step 6Metrics data processed by a pipeline are stored in a **DynamoDB** table.

Step 7Pipelines execution is done through tasks defined in **Step Functions**. This verifies a pipeline and input data, performs calculations by invoking the Calculator, performs aggregations on Calculator outputs, stores aggregations as metrics, and records the status of the execution.

### Calculator

The Calculator Module is a backend component which parses and executes the operations defined within a pipeline. This can include arithmetic operations or lookups of resources, such as Reference Datasets and Impacts.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sustainability-insights-framework-on-aws.pdf)Step 1The Calculator module is invoked through **Step Functions**, defined in the Pipeline Processor module.

Step 2The Calculator uses the Pipeline configuration to execute all of the operations in the configuration.

Step 3These operations may be lookups in Reference Datasets, retrieving Impacts, or retrieving functions defined in the Calculations module. This is done by invoking the Lambda APIs for each module. Retrieved resources can be cached to **DynamoDB**.

Step 4Outputs for each activity processed as part of a pipeline are written to the activity data in an **Aurora** v2 Serverless database.

Step 5Audit logs are written to an output location in **Amazon S3** through writes to **Amazon Kinesis Data Firehose**.

## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code: SIF](https://github.com/aws-solutions-library-samples/guidance-for-aws-sustainability-insights-framework)
[Go to sample code: SIF CLI](https://github.com/aws-solutions-library-samples/guidance-for-sustainability-data-fabric-on-aws/tree/main)

## Well-Architected Pillars

### Operational Excellence

Deployments for infrastructure and application code changes can be done through [AWS CloudFormation](https://aws.amazon.com/cloudformation/) and the [AWS Cloud Development Kit](https://aws.amazon.com/cdk/) (AWS CDK). Integration tests exist for all of the modules in addition to tests for end-to-end scenarios. These tests can be run to verify deployments. [Read the Operational Excellence whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The infrastructure components of this Guidance were selected to help secure your workloads and minimize your security maintenance tasks. **Amazon Cognito** and the Access Management module are utilized for user authentication and authorization, respectively. Database services use encryption at rest, where permissions are set between tenants and tenant data is separated. Both external and internal interfaces are implemented in services that require TLS (HTTPS/SSL) to enforce data encryption in transit. Customer managed keys in [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) are used to encrypt data in **Kinesis Data Firehose**. [Read the Security whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

For a workload to perform its intended function correctly and consistently, managed services including **Lambda** (for computing), **API Gateway** (for API), and **Amazon SQS** (for messaging) are used. This ensures that your core services are deployed across multiple Availability Zones. Key components in this Guidance are split into separate microservices with clear REST interfaces defined between the services. Retries with backoff limits are implemented in clients between services, allowing for reliable application-level architecture. Deployment of this Guidance can be done through infrastructure as code (IaC). This makes it possible to deploy one-off deployments and hooks in continuous integration and continuous deployment (CI/CD) pipelines. Parameters and environment variables for the applications are handled through standard mechanisms such as [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html). [Read the Reliability whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Database services in this Guidance were chosen based on the access patterns and use cases required. **DynamoDB** was chosen for the NoSQL datastore use cases, and **Aurora** Serverless v2 was chosen for the data layer requiring relational access patterns. Additionally, deployment of this Guidance can be done through IaC. Customers can quickly deploy and test this Guidance with their data and use case, and they can terminate services just as quickly when they are done. Customers are able to select their preferred AWS Region to deploy this Guidance using the provided IaC tooling. [Read the Performance Efficiency whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

To help you build and operate cost-aware workloads, this Guidance gives you the option to enable a flexible pricing model. [Compute Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/) can be enabled for **Lambda** to help reduce your costs. You can also assign cost-allocation tags to organize your resources and track your AWS costs on a detailed level. To help you scale using only the minimum resources, this Guidance utilizes services in layers. The compute layer uses **Lambda** while the data layer incorporates the auto scaling capabilities for **Aurora** and **DynamoDB**, ensuring resources are scaled based on demand. [Read the Cost Optimization whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Primary services within the architecture, such as **Lambda**, **DynamoDB**, and **Aurora**, offer automated scaling, which optimizes resource utilization. These services can scale from zero to peak demands to ensure the minimum provisioned capacity is used to meet demand. This Guidance also follows a serverless architecture, in which compute can be scaled up and down with demand. [Read the Sustainability whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Guidance for Carbon Accounting on AWS**: This Guidance helps customers calculate their carbon footprints, track their Greenhouse gas (GHG) emitting activities, and identify carbon hotspots.

[Learn more](https://aws.amazon.com/solutions/guidance/carbon-accounting-on-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
