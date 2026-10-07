---
source_url: https://docs.aws.amazon.com/solutions/vibe-coding-with-aws-mcp-servers/index.html
---

---
title: 'Guidance for Vibe Coding with AWS MCP servers'
canonical_url: https://docs.aws.amazon.com/solutions/vibe-coding-with-aws-mcp-servers/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Vibe Coding with AWS MCP servers

## Overview

This guidance demonstrates how to accelerate AWS application development using AI coding assistants powered by AWS Model Context Protocol (MCP) Servers. By integrating specialized MCP servers for AWS documentation, architecture visualization, React component generation, cost analysis, and security assessment, developers can streamline cloud development workflows through natural language interactions. The solution reduces time spent on manual tasks like documentation research and architecture design while ensuring adherence to AWS best practices, enabling teams to focus on business logic rather than infrastructure complexity, ultimately accelerating time-to-market and improving development efficiency.

## Benefits

### Accelerate AWS development velocity

Ship production-ready applications faster with AI-powered coding assistance and pre-built AWS integrations. Reduce development cycles while maintaining security and cost optimization best practices.

### Minimize AWS learning curve

Enable developers to build complex AWS architectures without deep expertise through intelligent documentation access and visual diagram generation. Transform natural language requests into working AWS solutions.

### Streamline production deployment decisions

Assess cost implications and security compliance before deployment with integrated pricing analysis and CDK security evaluation. Make data-driven decisions that optimize both performance and budget.

## How it works

### Overview

This architecture diagram illustrates how to effectively develop AWS applications using AI assistants enhanced with AWS MCP Servers, demonstrated through a sample hotel booking application built on Amazon Bedrock AgentCore.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/vibe-coding-with-aws-mcp-servers.pdf)Step 1Developers install an AI coding assistant that supports the Model Context Protocol (MCP), such as Amazon Q Developer, Kiro, or compatible alternatives. MCP enables AI assistants to access structured, domain-specific capabilities through standardized server integrations.Step 2Developers configure AWS MCP Servers in their development environment, enabling AI assistants to access AWS-specific capabilities. This guidance showcases six essential servers, with additional specialized servers available in the complete AWS MCP collection.Step 3This guidance includes a comprehensive, real-world hotel booking application. Developers can deploy this reference implementation to their AWS account using the provided AWS CDK infrastructure, creating a working example for exploring vibe coding techniques with AWS MCP Servers.Step 4The reference implementation runs on Amazon Bedrock AgentCore, where both the hotel booking agent and custom MCP server operate within the Amazon Bedrock AgentCore runtime, integrating with mock APIs for property resolution, reservations, and content moderation. See next slide for detailed architecture.Step 5When exploring AWS services and architectures, developers leverage their AI assistant's integration with AWS Knowledge MCP Server to access official documentation and best practices. AWS Diagram MCP Server generates architecture visualizations, accelerating understanding of complex distributed systems.Step 6Developers accelerate frontend development using AWS Frontend MCP Server to generate React components with AWS integration, while Nova Canvas MCP Server creates custom graphics and visual elements.Step 7Production readiness assessment leverages AWS Pricing MCP Server for cost analysis and AWS CDK MCP Server for security evaluation through CDK Nag rules and AWS Solutions Constructs patterns, enabling data-driven deployment decisions.### Hotel Booking System – Sample Application

This complete hotel booking system is provided as a realistic, hands-on example of Amazon Bedrock AgentCore in action. It demonstrateshow AI agents and custom MCP servers orchestrate complex AWS services through natural language interactions.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/vibe-coding-with-aws-mcp-servers.pdf)Step 1A user, authenticated by Amazon Cognito, submits a request (e.g., "Find me a hotel in Seattle for next weekend") by invoking the Hotel Booking Agent. The agent is deployed on Amazon Bedrock AgentCore. Amazon Bedrock AgentCore Runtime provides a secure, serverless and purpose-built hosting environment for deploying and running AI agents or tools.Step 2The agent, built using the Strands Agents SDK, invokes an Amazon Bedrock model to leverage LLM capabilities for natural language understanding.Step 3The agent retrieves historical data about previous interactions with a user. Amazon Bedrock AgentCore Memory manages conversation context for the agent.Step 4The agent connects to the Hotel Booking MCP Server, which is also deployed on Amazon Bedrock AgentCore, to discover and invoke tools required to complete the user's request.Step 5Once a tool is selected, the agent calls it through its MCP Server. The MCP Server routes requests to Amazon API Gateway.Step 6Amazon API Gateway exposes 3 different APIs that represent the tools of the MCP Server: Property Resolution, Reservations, and Toxicity Detection via corresponding AWS Lambda functions.Step 7AWS Lambda functions process the requests: Property Resolution Lambda: Performs fuzzy matching against hotel records and uses Amazon Location Service to search properties not in Amazon DynamoDB. It returns top 5 matching hotels with details like location, amenities, and pricing. Reservations Lambda: Executes CRUD operations on reservation data, validates booking parameters (dates, guest count, room availability), generates confirmation numbers, and manages reservation status transitions (Booked → Confirmed → Cancelled). Toxicity Detection Lambda: Analyzes user input text using Amazon Comprehend for inappropriate content, applies allow list filtering, scores toxicity levels, and returns safety assessment results.Step 8API Responses are passed back to the MCP Server, so that the server can process them as tool results. The MCP Server transforms API responses into structured tool results, handles error conditions, formats data for agent consumption, and maintains request/response correlation for multi-step booking workflows.Step 9The MCP Server tool results are sent back to the Hotel Booking agent for processing. The agent determines next steps, leveraging Amazon Bedrock foundation models to interpret the tool results, and decide the best course of action.Step 10The final response (search results, booking confirmation, or error messages) are delivered back as a response to the User.Step 11AWS Identity and Access Management (AWS IAM) secures the system with dedicated execution roles for the hotel booking agent, MCP server, and AWS Lambda functions. Each role implements least-privilege access to required AWS services including Amazon Bedrock models, Amazon Bedrock AgentCore Memory, and API resources.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-vibe-coding-with-aws-mcp-servers)

[Read usage guidelines](/solutions/guidance-disclaimers/)
