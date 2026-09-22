---
source_url: https://docs.aws.amazon.com//solutions/intelligent-application-modernization-explorer-on-aws//index.html
---

---
title: 'Guidance for Intelligent Application Modernization Explorer on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/intelligent-application-modernization-explorer-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Intelligent Application Modernization Explorer on AWS

## Overview

This Guidance helps organizations evaluate their current application environments for modernization by using generative AI to analyze tech stacks, identify modernization opportunities, and generate cost estimates. Users upload application data through a web interface and receive AI-powered insights on tech stack similarities, modernization patterns, and planning recommendations. Amazon Bedrock foundation models process and normalize technology inventories, assess skill relevance, and identify pilot candidates for modernization initiatives. You can accelerate your modernization planning cycles and make data-driven decisions with AI-generated recommendations tailored to your specific application portfolio.

## Benefits

### Accelerate your modernization planning

Identify the right applications to modernize first using GenAI-powered analysis of your enterprise data, reducing planning time and helping your teams move from assessment to action faster.

### Reduce risk with data-driven insights

Prioritize modernization initiatives with confidence by generating automated similarity analysis, pilot identification, and TCO estimates before you commit resources to any workload.

### Build on a secure, scalable foundation

Deploy a serverless, multi-layered architecture that handles large-scale application portfolios in parallel, so your teams can focus on modernization outcomes rather than managing infrastructure.

## How it works

This architecture diagram shows how Applications Modernization Explorer uses GenAI to transform organizational data into actionable intelligence, enabling enterprises to reduce modernization risk by identifying the right applications to modernize first, providing modernization pathways, and generating cost estimates. [Download the architecture diagram.](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/intelligent-applications-modernization-explorer-on-aws.pdf)

![Architecture diagram for Intelligent Application Modernization Explorer on AWS](/images/solutions/intelligent-application-modernization-explorer-on-aws/images/intelligent-applications-modernization-explorer-on-aws.png)

1. **Step 1**: User logs in to the UI, uploads data and uses the UI to access Insights, Tech Stack Similarities, Planning, and Estimates.
1. **Step 2**: Amazon CloudFront caches and distributes content globally from edge locations, reducing latency for end users.
1. **Step 3**: Amazon Simple Storage Service serves as the origin storage for static assets like HTML, CSS, JavaScript, and images.
1. **Step 4**: Amazon Cognito manages user registration, authentication, and account recovery. It provides secure sign-in workflows and password policies. User Pool issues JWT tokens that authorize access to backend APIs and resources, eliminating the need for custom authentication infrastructure.
1. **Step 5**: AWS WAF protects web applications from common exploits and vulnerabilities. It filters malicious traffic using customizable rules to block SQL injection, cross-site scripting (XSS), bot attacks, and other threats. WAF inspects HTTP/HTTPS requests at the edge before they reach your application infrastructure.
1. **Step 6**: Amazon API Gateway manages all APIs at scale. It handles request routing, authentication, authorization, throttling, and monitoring.
1. **Step 7**: Several AWS Lambda functions run the code for all the APIs invoked by the frontend, and for the steps in AWS Step Functions.
1. **Step 8**: Amazon DynamoDB stores in various tables processed data for both global level (projects, projects share) and project specific level (application similarity, component similarity, pilot identification, TCO and Team estimates, and Process Tracking).
1. **Step 9**: Amazon Simple Queue Service decouples synchronous processes from background processes. For example, data normalization is triggered on successful upload and transformation of tech stack files.
1. **Step 10**: Amazon Q Developer in chat applications executes build commands defined in buildspec files to provision all the project specific infrastructure (Lambda functions, Step Functions, Amazon Athena tables, SQS queues, and more).
1. **Step 11**: Amazon S3 stores the artifacts required by Amazon Q Developer in chat applications when a new project is created.
1. **Step 12**: AWS CloudFormation automates resource creation and deletion invoked by Amazon Q Developer in chat applications when a project is created or deleted.
1. **Step 13**: Amazon Athena queries data directly in Amazon S3 (Skills, Technology Vision, Applications, Tech Stack, Infrastructure, Utilization, Skill Relevance, and normalized Tech Stack).
1. **Step 14**: Amazon S3 stores all the uploaded and transformed files, as well as the Athena query results.
1. **Step 15**: AWS Step Functions orchestrates multiple Lambda functions to parallel process large datasets for Tech Stack normalization, Skill relevance, Application Similarity, Component Similarity, Pilot Identification, and Project Exports.
1. **Step 16**: Amazon Bedrock provides access to high-performing foundation models that are in use by Tech Stack normalization, Skills Relevance, and Pilot Identification enhancement processes.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-intelligent-application-modernization-explorer)

[Read usage guidelines](/solutions/guidance-disclaimers/)
