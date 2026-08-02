---
source_url: https://docs.aws.amazon.com/solutions/battery-passport-on-aws/index.html
---

# Guidance for Battery Passport on AWS

## Overview

This Guidance demonstrates how to comply with the European Union Battery Regulation requirements for electronic battery records accessible via QR codes by February 2027. It utilizes AWS data processing and storage services to achieve this. The implementation involves ingesting battery data from multiple enterprise systems using AWS Glue for batch processing and Lambda for real time record retrieval. The processed data is then transformed into regulation compliant passport formats. Additionally, it showcases Amazon DataZone support for the OpenLineage-compatible feature, which tracks the flow, transformations, and dependencies of data assets across various data processing stages. This feature provides a visual graph that illustrates the chain of custody and traceability of data. Data integrity is maintained through blockchain verification using Ethereum nodes, while DynamoDB stores passport information with differentiated access controls for public and restricted stakeholders. You can ensure regulatory compliance while maintaining data transparency and authenticity across the entire battery lifecycle from manufacturing through second-life operations.

## Benefits

### Accelerate regulatory compliance

Maintain data transparency and chain of custody with Open lineage. Apply separation of concern for the regulatory calculations such as Product Carbon Footprint per kWh for four lifecycle stages or evolving requirement of Performance class.

### Ensure data integrity with blockchain verification

Leverage Ethereum blockchain integration to create tamper-proof battery records throughout the entire lifecycle. Build stakeholder trust with publicly verifiable data hashes while maintaining secure access controls for sensitive information.

### Enable seamless battery lifecycle management

Orchestrate second-life workflows for battery repurposing, reuse, and remanufacturing with automated data transfer to secondary operators.

## How it works

### Data Pipeline

This architecture diagram illustrates how to construct a data pipeline that captures all the necessary data required to create a Battery Passport.It demonstrates the key components and their interactions, offering a comprehensive overview of the architecture’s structure and functionality.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/battery-passport-on-aws.pdf)Step 1Battery Passport input data is stored in various systems across the enterprise, both within and outside of AWS. These systems contain raw data that needs to be first captured and transformed into the values required to showcase in a passport.Step 2AWS Glue is used to fetch batch data, AWS Lambda is used to retrieve records from data on AWS Cloud, and API Gateway access on-prem APIs and ingest data into Amazon Simple Storage Service (Amazon S3) buckets for staging.Step 3AWS Glue jobs validates the staging data and correlate the data coming from multiple sources. Amazon DataZone will contain the data lineage from source to processed data, while OpenLineage is used for data sourced from systems outside of AWS or not supported by default DataZoneStep 4The Regulation (EU) 2023/1542) has very specific requirements about the data unit (e.g., PCF should be per Kwh for four different lifecycle stages). AWS Glue jobs is used to batch calculations, AWS Lambda is used for complex and single-record calculations (e.g., Performance class), and Amazon S3 will store all the processed data.Step 5Passport data needs to be accessed through a QR code and has different access requirements. AWS Glue job will push the data into the passport data repository and maintain the transparency and authenticity of the data.Step 6Amazon Simple Storage Service (Amazon S3). will store all the processed data. This data accessed for other regulatory requirements (e.g.; CSRD)Step 7Regulation has certain milestones. Amazon QuickSight is used to analyze how the economic operator is performing against the milestones, e.g., Target material Rate of recoverability### Battery Passport

This architecture diagram illustrates how to build Battery Passport on AWS. It demonstrates the key components and their interactions, offeringa comprehensive overview of the architecture’s structure and functionality

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/battery-passport-on-aws.pdf)Step 1Passport data accessed through a QR code, and access requirements may vary depending on whether the user is internal, public or restricted stakeholders. Users access the data via a web interface hosted in Amazon S3 and accessed through Amazon CloudFront.Step 2Amazon S3 store various documents related to the Battery Passport, such as conformity results, certificates, etc. These documents get access through the web portal using a signed URL,Step 3Data Pipeline fetch data from various internal and external sources and and make it available for Data Consumers. AWS Glue push the data into the Passport data repository and maintain its transparency and authenticity by inserting a hash into the blockchain node.Step 4AWS DynamoDB stores passport data in different tables for public and restricted data.Step 5AWS Step Functions workflows manage the passport data update and 2nd life processes. AWS Lambda functions issue and verify credentials to access restricted passport data. When a battery is repurposed, re-used, or remanufactured, The data shared with the second-life operator.Step 6The data integrity of the Battery Passport is verified via a public blockchain. Ethereum nodes store the hash of the Battery Passport data. AWS Nitro Enclaves secure the signing of Ethereum transactions. The private key is stored in AWS Secrets Manager, and AWS KMS is used for signingStep 7AWS Lambda functions in the Step Functions workflow write a subset of battery data to one or more public blockchains using self-managed, or partner-managed blockchain nodes.Step 8AWS Fargate is used to run containerized event listener applications that subscribe to on chain events and trigger downstream actions.## Related content

- **Building a Battery Passport on AWS: Part 1**: This blog post demonstrates how to build a Battery Passport system on AWS to collect and manage supply chain data and carbon footprint information across the battery lifecycle.

[Learn more](https://aws.amazon.com/blogs/industries/building-a-battery-passport-on-aws-part-1/)

- **Building a Battery Passport on AWS: Part 2**: This blog post demonstrates how to implement the Aggregator and Passport components using AWS services to process battery performance data and ensure data authenticity through blockchain integration.

[Learn more](https://aws.amazon.com/blogs/industries/building-a-battery-passport-on-aws-part-2/)

- **Guidance for Product Traceability on AWS**: This Guidance helps to provide transparency and traceability of the supply chain network for a product.

[Learn more](https://aws.amazon.com/solutions/guidance/product-traceability-on-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
