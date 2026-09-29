---
source_url: https://docs.aws.amazon.com/solutions/environmental-impact-factor-mapping-on-aws/index.html
---

---
title: 'Guidance for Environmental Impact Factor Mapping on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/environmental-impact-factor-mapping-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Environmental Impact Factor Mapping on AWS

## Overview

This Guidance automates the selection of environmental impact factors (EIFs)—sometimes also referred to as emission factors—using foundation models with retrieval augmented generation (RAG) to scale product carbon footprint assessments. EIFs measure activities into metrics to assess potential environmental impacts, like carbon dioxide equivalent (CO2e). The Guidance takes in activity data descriptions (such as purchase orders) and parameters (such as regions), and returns a ranked list of EIFs with similarity scores. Human annotators, invoked by low similarity scores or random sampling, provide ongoing evaluation, improvement, and corrective annotations. The Guidance is based on using two algorithms published by Amazon: [CaML](https://www.amazon.science/publications/caml-carbon-footprinting-of-household-products-with-zero-shot-semantic-text-similarity) , an algorithm to automate Economic Input-Output based Life Cycle Assessment (EIOLCA) using semantic text similarity matching and [Flamingo](https://www.amazon.science/publications/flamingo-environmental-impact-factor-matching-for-life-cycle-assessment-with-zero-shot-machine-learning) , an algorithm for automatically identifies process-based LCA EIFs.

## How it works

### Option 1

This architecture diagram shows how to scale carbon footprint assessments using a knowledge store made up of Amazon S3 and Amazon Bedrock. For Option 2, open the other tab.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/environmental-impact-factor-mapping-on-aws.pdf)Step 1Collect business activity data and emission factors from appropriate sources.Step 2Index relevant activity category datasets using knowledge bases for Amazon Bedrock to build vector knowledge stores for searching during mapping.Step 3Ingest the activity data to Amazon Simple Storage Service (Amazon S3). AWS Glue cleans and formats incoming data for mapping activities to impact factors.Step 4AWS Step Functions iterates through the business activities. It calls large language models (LLMs) hosted by Amazon Bedrock to match the given activity to the most relevant emission factor category using RAG. Matches are stored in Amazon S3.Step 5AWS Glue combines the matched activity and category with its corresponding kg CO2e from relevant emission factor datasets. This combined dataset is registered in AWS Glue Data Catalog.Step 6Report on mapped emission factor data with Amazon QuickSight or Amazon Athena.### Option 2

This architecture diagram shows how to scale carbon footprint assessments using a knowledge store made up of Amazon OpenSearch Service Neural Search. For Option 1, open the other tab.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/environmental-impact-factor-mapping-on-aws.pdf)Step 1Collect business activity data and emission factors from appropriate sources.Step 2Use Amazon OpenSearch Service Neural Search feature to convert emission factor query text into vector embeddings, and return close matches.Step 3Ingest the activity data to Amazon S3. AWS Glue cleans and formats incoming data for mapping activities to impact factors.Step 4Step Functions iterates through the business activities. It calls large language models (LLMs) hosted by Amazon Bedrock to match the given activity to the most relevant emission factor category using RAG. Matches are stored in Amazon S3.Step 5AWS Glue combines the matched activity and category with its corresponding kg CO2e from relevant emission factor datasets. This combined dataset is registered in Data Catalog.Step 6Report on mapped emission factor data with QuickSight or Athena.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-environmental-impact-factor-mapping-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch provides centralized logging with metrics and alarms across all deployed services to raise alerts for operational anomalies. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Resources are protected using AWS Identity and Access Management (IAM) policies and principles. Use least-privilege access and role-based access to grant permissions to operators. Data at rest is encrypted using AWS Key Management Service (KMS). HTTPS endpoints with transport layer security (TLS) provide encryption in transit for service endpoints. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

These serverless services automatically adapt to demand changes. Amazon S3 is fully elastic, growing and shrinking as data is added or removed, providing durable cloud storage and industry-leading availability without overprovisioning. Step Functions offers serverless orchestration with built-in error handling for modern applications. As the application runs, it maintains state, tracks workflow steps, and stores an event log passed between components. If networks fail or components hang, the application can resume from the last checkpoint, ensuring a seamless workflow. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Bedrock allows developers to choose suitable foundation models from leading AI companies for their use cases. Amazon Bedrock is a fully managed service offering high-performing foundation models through a single API, along with capabilities for building secure, private, and responsible generative AI applications. AWS Glue enables quick data discovery and preparation for analytics, ML, and application development. AWS Glue is a serverless data integration service, eliminating infrastructure management through automatic provisioning and supporting various data processing frameworks and workloads. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance relies on serverless services such as Amazon S3, Athena, and AWS Glue. These services require no infrastructure setup or management and scale automatically to match demand, ensuring minimum resource utilization. Serverless scaling helps reduce overall resource usage and costs by adjusting to fluctuating demands. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Step Functions call Amazon Bedrock directly, eliminating the need for dedicated compute to process data. This approach reduces compute usage and, as a result, lowers carbon footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
