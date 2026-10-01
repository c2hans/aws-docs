---
source_url: https://docs.aws.amazon.com/solutions/building-agentic-ai-powered-hyper-personalized-customer-experience-on-aws/index.html
---

---
title: 'Guidance for Building Agentic AI-Powered Hyper-Personalized Customer Experience on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-agentic-ai-powered-hyper-personalized-customer-experience-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Building Agentic AI-Powered Hyper-Personalized Customer Experience on AWS

## Overview

This guidance demonstrates how to build an AI-powered hyper-personalization platform that delivers tailored product recommendations based on customer profiles and unique individual attributes. The solution showcases multi-agent collaboration, combining general e-commerce agents with domain-specific agents to enable hyper-personalized 1:1 search experiences and to execute actions on behalf of users, such as purchasing products. Leveraging Amazon Bedrock and OpenSearch, the application demonstrates keyword search, semantic search, and intelligent product discovery. While designed for healthcare retail, this architecture can be adapted to all digital retail industries like Automotive and CPG, featuring near real-time AI chat assistance powered by coordinated AI agents.

## Benefits

### Deliver truly individualized customer experiences

Deploy multi-agent AI that continuously adapts recommendations, content, and interfaces in near real-time based on each customer's unique profile. Move beyond traditional collaborative filtering to create 1:1 personalized interactions that increase engagement and conversion rates.

### Scale effortlessly with serverless architecture

Launch your hyper-personalization platform without managing infrastructure or capacity planning. Automatically handle demand fluctuations while reducing operational complexity and lowering total cost of ownership through pay-per-use pricing.

### Extend personalization across multiple industries

Adapt specialized AI agents from healthcare retail to automotive, CPG, and other sectors requiring individualized recommendations. Leverage semantic search and contextual analysis to deliver relevant product suggestions tailored to each customer's specific needs.

## How it works

### Solution Overview

This architecture diagram illustrates an AI-powered product recommendation solution that provides personalized product suggestions based on customer profiles, hyper-personal customer data, and intelligent search capabilities.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-agentic-ai-powered-hyper-personalized-customer-experience-on-aws.pdf)Step 1Multiple users access the platform simultaneously, each receiving individualized product recommendations and health insights based on their unique profiles and preferences.Step 2Users engage with the system through a web application via token-based authentication.Step 3Strands Agents coordinates how various specialized AI agents initialize, cache information, stream responses, and adapt to task context while maintaining user sessions.Step 4The custom tools include a Buy Now agent, which can execute product purchases, as well as domain-specific agents. The Bloodwork Analyzer interprets laboratory results, identifies biomarker patterns, and correlates nutritional deficiencies with targeted supplement recommendations, and the Body Composition Analyzer evaluates fitness metrics, tracks body composition trends, and generates personalized nutrition and exercise plans aligned with individual health goals.Step 5The data sources layer includes structured databases for profile and catalog management and a search engine with semantic search capabilities that enable intelligent product discovery and contextual retrieval. Data is encrypted at rest and secure access patterns are used for queries.### Infrastructure Architecture

This architecture diagram illustrates the key infrastructure components for the web application and data sources used to deploy the solution on AWS.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-agentic-ai-powered-hyper-personalized-customer-experience-on-aws.pdf)Step 1Users access the platform through Amazon CloudFront, a global content delivery network that provides low-latency access to the application for users worldwide.Step 2The web application is served from Amazon Simple Storage Service (Amazon S3), that hosts product images and static assets for the application.Step 3The Application Load Balancer distributes incoming traffic across the instances of the frontend and Strands services.Step 4AWS Fargate runs the serverless frontend and backend containers that provide the web application user interface and backend functionality, enabling product search, chat interaction, and customer profile management.Step 5Amazon Elastic Container Registry (Amazon ECR) serves as the container registry that stores and manages Docker images.Step 6Amazon DynamoDB provides the database layer storing customer profiles, product catalog, search history, and application data with low-latency access for near real-time operations. Data is encrypted at rest and secure access patterns are maintained.Step 7Amazon OpenSearch Service powers the search and analytics engine that enables keyword search, semantic search with embeddings, and intelligent product discovery capabilities for personalized recommendations. Data is encrypted at rest and secure access patterns are maintained.### Agent Collaboration Framework

This architecture diagram illustrates the Amazon Bedrock multi-agent collaboration using the Strands Agents SDK for the entirecustomer experience workflow.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-agentic-ai-powered-hyper-personalized-customer-experience-on-aws.pdf)Step 1Users interact submitting health data, product queries, and receiving personalized recommendations based on their unique profiles and preferences.Step 2The Strands service coordinates how specialized AI agents initialize, cache information, stream responses, and adapt to both user tasks and context while maintaining user sessions throughout the interaction.Step 3The supervisor agent orchestrates the workflow by delegating tasks to specialized agents, coordinating their responses, and synthesizing insights to provide comprehensive personalized recommendations.Step 4The body composition agent gets user input and evaluates fitness metrics, tracks body composition trends, and generates personalized nutrition and exercise plans aligned with individual health goals.Step 5The bloodwork analyzer agent interprets laboratory results from user input, identifies biomarker patterns, and correlates nutritional deficiencies with targeted supplement recommendations.Step 6The search agent queries the product catalog, applies personalized filters based on user preferences and health data, and retrieves relevant products.Step 7Amazon OpenSearch Service serves as the data layer containing the product catalog with semantic search capabilities that enable intelligent product discovery and contextual retrieval.### AgentCore Implementation

This architecture diagram shows alternative agent hosting on Amazon Bedrock AgentCore. Deploy secure, scalable AI agents on AWS with Amazon Bedrock AgentCore's purpose-built infrastructure, enabling complex workflows across tools and data sources while eliminating infrastructure management overhead.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-agentic-ai-powered-hyper-personalized-customer-experience-on-aws.pdf)Step 1Users interact with the chat interface hosted on AWS Fargate.Step 2Execute agent code, tools, and instructions in Amazon Bedrock AgentCore Runtime's serverless environment, supporting multiple frameworks and 8-hour sessions.Step 3Secure agent operations with AgentCore Identity, managing authentication and access controls across all interactions.Step 4Build context-aware agents with AgentCore Memory, maintaining both short-term and long-term knowledge across interactions.Step 5Access Amazon Bedrock for foundation models, enabling flexible use of various LLMs through a unified API.Step 6Transform REST APIs into Model Context Protocol (MCP) servers through AgentCore Gateway, enabling reusable tool sharing across agents.Step 7Connect to AWS services like Amazon OpenSearch Service to enrich context and perform tasks.Step 8Monitor agent performance through AgentCore Observability, tracking key metrics and ensuring operational excellence.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-building-agentic-ai-powered-hyper-personalized-customer-experience-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
