---
source_url: https://docs.aws.amazon.com/solutions/patient-and-clinical-data-insights-with-datavant-and-aws-clean-rooms/index.html
---

---
title: 'Guidance for Patient and Clinical Data Insights with Datavant and AWS Clean Rooms'
canonical_url: https://docs.aws.amazon.com/solutions/patient-and-clinical-data-insights-with-datavant-and-aws-clean-rooms/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Patient and Clinical Data Insights with Datavant and AWS Clean Rooms

## Overview

This Guidance shows how to use Datavant’s data deidentification and tokenization tools on AWS Clean Rooms to protect private patient information while gaining important insights. Using these tools, you can replace private information with encrypted tokens that cannot be reverse engineered to reveal the original information. You and collaborators can then work in AWS Clean Rooms to analyze collective datasets without sharing or moving the underlying data sources. By seamlessly deidentifying, linking, and collaborating on data while retaining fine-grained control, your healthcare and life sciences organization can accelerate and improve insights.

## How it works

This architecture diagram shows how to use Datavant’s data deidentification and tokenization tools on AWS Clean Rooms to protect your healthcare and life sciences organization’s private patient information. It also shows how to gain insights by replacing the data with encrypted tokens that cannot be reverse engineered.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/patient-and-clinical-data-insights-with-datavant-and-aws-clean-rooms.pdf)

![Architecture diagram](/images/solutions/patient-and-clinical-data-insights-with-datavant-and-aws-clean-rooms/images/patient-and-clinical-data-insights-with-datavant-and-aws-clean-rooms-1.png)

1. **Step 1**: Deidentify or tokenize data in an Amazon Simple Storage Service (Amazon S3) bucket using Datavant Switchboard (container). The container is deployed through supported container deployment methods, as detailed in Step 7.
1. **Step 2**: Link the tokenized data with your fellow collaborators using the Datavant Switchboard (container) and store the output in an Amazon S3 bucket.
1. **Step 3**: Use an AWS Glue crawler to crawl the linked, tokenized data. Prepare the data source for collaboration with AWS Glue Data Catalog.
1. **Step 4**: Instantiate AWS Clean Rooms and invite the member(s) to the collaboration to align on and implement analysis rules. Members can then associate configured tables from Data Catalog and use an AWS Clean Rooms service role to access their AWS Glue tables.
1. **Step 5**: The member who is allowed to query uses Aggregate and List functions across tables in the collaboration. Results can be exported to Amazon S3 for the member who is allowed to receive query results.
1. **Step 6**: The member who receives query results can use analytics services, including Amazon Redshift, Amazon Athena, Amazon EMR, and Amazon SageMaker, to derive insights from the newly enriched dataset.
1. **Step 7**: Datavant Switchboard container deployment methods include using AWS Fargate, Amazon Elastic Kubernetes Service (Amazon EKS), and Amazon Elastic Container Service (Amazon ECS).
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon Elastic Container Registry (Amazon ECR) prepares and builds container images, integrating with existing continuous integration and delivery build processes and supporting multistage-build and package-management deployment modalities. As two supported deployment methods, Amazon EKS monitors the health of container applications through liveliness probes, and Amazon ECS monitors it through health checks. Both methods support logging by writing to standard out (stdout) and standard error (stderr) streams. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon ECR statically scans images, dependencies, and libraries for common vulnerabilities and exposures. Additionally, Snyk is enabled for real-time container security, and Amazon Cognito generates JSON web tokens that enable secure communication to functions that require internet access. Amazon Cognito and AWS Identity and Access Management (IAM) support the principle of least privilege and enable you to avoid hard coding anything. Aside from the static and dynamic scanning completed by Amazon ECR and Snyk respectively, the container image is hardened with software built with trusted and verified signatures. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS Clean Rooms is a regional serverless service. This service runs on the AWS global infrastructure, which is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected through low-latency, high-throughput, and highly redundant networking. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AWS Clean Rooms offers optimized scalability, allowing you to seamlessly adjust your data analysis capacity based on your needs. You can automatically scale compute resources up or down depending on query workload demands. This helps ensure efficient utilization and cost optimization while maintaining data privacy and security within the collaborative environment. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon ECS and Amazon EKS scale automatically to meet demand, helping you optimize your costs based on load. Containers listen for a SIGTERM signal to scale down, and a container’s application startup time is optimized to enable cost savings when invoking the application from a cold start. Additionally, Amazon ECR lets you set up lifecycle policies to further reduce costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon ECR lets you right-size containers, and it regularly updates parent and base images and purges unused or obsolete container images. Additionally, Amazon EKS and Amazon ECS scale down when resources are not needed, and they support optimal architectures for container image builds. By removing unused images, scaling down when unused, and enabling you to optimize hardware for performance, these services reduce energy consumption, supporting sustainability. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
