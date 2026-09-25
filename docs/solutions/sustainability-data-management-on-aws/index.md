---
source_url: https://docs.aws.amazon.com//solutions/sustainability-data-management-on-aws/index.html
---

---
title: 'Guidance for Sustainability Data Management on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/sustainability-data-management-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Sustainability Data Management on AWS

## Overview

This Guidance demonstrates how you can manage and share data to help drive your organization's sustainability initiatives. With a growing number of data sources for tracking the environmental impact of your organization, it becomes challenging to discover, assess validity, and extract values from these assets across multiple teams. This Guidance provides a streamlined framework for enterprise data management. It takes into consideration data quality, security, cataloging, and lineage—allowing you to seamlessly share applicable datasets. With more reliable data, organizations can solve use cases such as more accurately calculating their estimated carbon emissions, assessing climate risk, or understanding the biodiversity impact of the organization. With centralized access to key data assets, you can make informed decisions to achieve your environmental goals more efficiently with proper data governance.

## How it works

### Overview

This architecture diagram illustrates how sustainability applications can both consume and produce data assets, incorporating key data management concepts to quickly share and extract trusted value from data across your organization.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sustainability-data-management-on-aws-guidance.pdf#page=1)Step 1Data is stored in various types of data stores, within and/or outside of AWS. These data stores contain data assets that represent a physical data object (such as a database table or a file). These data stores house both source and target datasets in the data fabric.

Step 2Technical metadata is automatically imported into the data catalog for data assets that existed before the implementation of the data fabric.

Step 3The data owners maintain business metadata for their data assets in the data catalog to enrich the data with business context. For example, business context for dataset columns, tags, domain- or enterprise-wide business glossary terms.

Step 4The data consumers search the data catalog for data assets using technical and/or business metadata. The metadata pertaining to data quality and data lineage establishes trust in how data assets can be used.

Step 5The data consumers request access to the relevant data assets from the data owner, who can either grant or deny the request.

Step 6The data products perform export, transform, and load (ETL), data profiling, and data quality operations to create new curated data assets to enable data-driven use cases for the data consumers.

Step 7Data assets created by the data products are registered in the data catalog with the corresponding metadata.

### User access

User access to the data catalog.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sustainability-data-management-on-aws-guidance.pdf#page=2)Step 1AWS IAM Identity Center manages all users for both Amazon DataZone and the other APIs.

Step 2Amazon API Gateway uses an Amazon Cognito authorizer. The corresponding user pool uses IAM Identity Center as its identity provider.

Step 3Amazon DataZone integrates directly with IAM Identity Center for user management.

### Data discovery

Search, discover, and request access to data assets in the data catalog.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sustainability-data-management-on-aws-guidance.pdf#page=3)Step 1Users explore the data catalog through the search functionality in Amazon DataZone. Assets can be searched for by their associated metadata.

Step 2Data lineage for each asset is stored in an instance of OpenLineage Marquez. Marquez is deployed on an Amazon Elastic Container Service (Amazon ECS) container fronted by an Application Load Balancer. Users can view the data lineage of assets through Marquez.

Step 3From the data catalog, the data consumer requests read-only access to a desired dataset from the data asset owner.

Step 4Asset owners approve or deny subscription requests to individual assets that they have published to the catalog.

Step 5Once an asset owner approves a user's subscription request, the user can access the asset through Amazon Athena, for assets registered as AWS Glue tables, or through the Amazon Redshift Data API for Amazon Redshift tables.

### Automated data asset registration

Data asset registration with profiling, transformation, quality assertion, and lineage tracking.

[Download the architecture diagram.](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sustainability-data-management-on-aws-guidance.pdf#page=4)Step 1Data is placed into Amazon Simple Storage Service (Amazon S3) or Amazon Redshift.

Step 2A data owner or data product invokes an API Gateway API backed by AWS Lambda in the Hub account. The API body includes information on the data location, transformation logic, profiling specifications, and data quality assertions required in future steps. The API writes an event to an Amazon EventBridge event bus, which replicates it to an event bus in the spoke account.

Step 3The event in the spoke account invokes an AWS Step Functions workflow. The workflow creates an AWS Glue connection to the Amazon Redshift or Amazon S3 data source.

Step 4AWS Glue DataBrew performs data transformations through a recipe job.

Step 5An AWS Glue crawler infers the schema of the resulting dataset and creates an AWS Glue table.

Step 6An AWS Glue DataBrew profile job derives profile statistics against the table.

Step 7AWS Glue evaluates the data quality with user-defined assertions.

Step 8The resulting data lineage is summarized in the event and sent back to the hub account through EventBridge.

Step 9The EventBridge event bus in the hub account invokes another Step Functions workflow.

Step 10The new asset is imported into Amazon DataZone by creating and running a data source.

Step 11The lineage for the asset is published to EventBridge, which invokes an Amazon ECS deployment to register the lineage in a deployment of OpenLineage Marquez.

## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Try out this Guidance**: Explore an interactive demo for a sneak peak at how this Guidance functions.

[Explore interactive demo](https://demos.awsplayer.com/guidance/sustainability-data-fabric/index.html?target=_blank)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code: Data Management Core](https://github.com/aws-solutions-library-samples/guidance-for-data-fabric-on-aws)
[Go to sample code: Sustainability Data Management](https://github.com/aws-solutions-library-samples/guidance-for-sustainability-data-fabric-on-aws/tree/main)

## Well-Architected Pillars

### Operational Excellence

[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) provides centralized monitoring and observability, which tracks operational metrics and logs across services. This integrated visibility into your workload health and performance helps you identify issues and troubleshoot problems, allowing you to continuously improve processes and procedures for efficient operations. [Read the Operational Excellence whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

**Amazon Cognito**, [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM), and **IAM Identity Center** help you implement secure authentication and authorization mechanisms. **Amazon Cognito** provides user authentication and authorization for the application APIs, while **IAM** policies and roles control access to resources based on the principle of least privilege. **IAM Identity Center** simplifies managing user identities across the components of this Guidance, enabling centralized identity management. [Read the Security whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

An **Application Load Balancer**, **Lambda**, **EventBridge**, and **Amazon S3** work in tandem so that your workloads perform their intended functions correctly and consistently. For example, the **Application Load Balancer** distributes traffic to the application containers, providing high availability. **EventBridge** replicates events across accounts for reliable event delivery, while the automatic scaling of **Lambda** handles varying workloads without disruption. And as the root data source, **Amazon S3** provides highly durable and available storage. [Read the Reliability whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services selected for this Guidance are optimal services to help you both monitor performance and maintain efficient workloads. Specifically, **Athena** and the **Amazon Redshift** Data API provide efficient querying of data assets. **AWS Glue DataBrew** and [crawlers](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) automate data transformation and cataloging, improving overall efficiency. [Amazon Redshift Serverless](https://aws.amazon.com/redshift/redshift-serverless/) scales compute resources elastically, allowing high-performance data processing without over-provisioning resources. Lastly, **Amazon S3** offers high data throughput for efficient querying. [Read the Performance Efficiency whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

To optimize costs, this Guidance uses serverless services that automatically scale based on demand, ensuring that you only pay for the resources you use. For example, **EventBridge** eliminates the need for polling-based architectures, reducing compute costs, and **Amazon Redshift Serverless** automatically scales compute based on demand, charging only for resources consumed during processing. [Read the Cost Optimization whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The serverless services of this Guidance work together to reduce the need for always-on infrastructure, lowering the overall environmental impact of the workload. For example, **Amazon Redshift Serverless** automatically scales to the required demand, provisioning only the necessary compute resources and minimizing idle resources and their associated energy usage. [Read the Sustainability whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
