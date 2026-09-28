---
source_url: https://docs.aws.amazon.com/solutions/application-and-data-connectors-for-amazon-q-business/index.html
---

---
title: 'Guidance for Application and Data Connectors for Amazon Q Business'
canonical_url: https://docs.aws.amazon.com/solutions/application-and-data-connectors-for-amazon-q-business/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Application and Data Connectors for Amazon Q Business

## Overview

This Guidance demonstrates how businesses can rapidly deploy Amazon Q Business, integrating large language model (LLM) capabilities seamlessly with third-party data sources such as Microsoft Teams, Confluence, ServiceNow, and Jira. It demonstrates how businesses can accelerate their adoption of AI capabilities through an automated deployment process that prioritizes security and operational efficiency. The Guidance helps businesses of all sizes, particularly small- and medium-sized businesses, to quickly implement enterprise-grade LLM capabilities within their existing workflows. This approach enhances productivity and decision-making while minimizing operational costs and security risks.

## Benefits

### Accelerate enterprise knowledge discovery deployment

Deploy a complete Amazon Q Business environment in minutes using infrastructure as code. Reduce manual configuration while ensuring consistent, repeatable deployments across your organization.

### Strengthen security with integrated controls

Centralize access management through AWS IAM Identity Center integration and secure credential handling with AWS Secrets Manager. Maintain data security while enabling seamless user authentication.

### Simplify data source integration management

Connect multiple enterprise data sources through a single deployment process. Easily update and expand your knowledge base while preserving existing configurations and user access permissions.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/application-and-data-connectors-for-amazon-q-business.pdf)

![Architecture diagram](/images/solutions/application-and-data-connectors-for-amazon-q-business/images/application-and-data-connectors-for-amazon-q-business-1.png)

1. **Step 1**: The System administrator deploys the AWS CloudFormation stack to create an Amazon Q Business application.
1. **Step 2**: During deployment, the administrator selects one or more supported data sources: Atlassian Jira, Atlassian Confluence, Microsoft Teams, ServiceNow, or Amazon Simple Storage Service (Amazon S3). The stack provisions the Amazon Q index and the Amazon Q retriever and then configures the selected data sources. It also integrates with an existing AWS IAM Identity Center to provision users for Amazon Q Business and stores the data source secrets in AWS Secrets Manager.
1. **Step 3**: Once the setup is complete, the authenticated business user sends a query, such as a query on company policies, knowledge articles, customer or system incidents, or team chat to the Amazon Q application. The Amazon Q Business application retrieves the most relevant information to the business user's query from the ingested content, for which the business user has access permissions.
1. **Step 4**: Amazon Q returns a filtered response to the business user's query based on the ingested data and context, using responses from the underlying LLM in Amazon Q.
1. **Step 5**: After the initial deployment, the administrator can update the stack parameters to include additional data sources. The updated stack modifies the existing Amazon Q setup by integrating the new selections while preserving previously configured resources and settings.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-application-and-data-connectors-for-amazon-q-business)

[Read usage guidelines](/solutions/guidance-disclaimers/)
