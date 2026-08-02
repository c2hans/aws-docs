---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/MCP-Server.html
---

# MCP Server
<a name="MCP-Server"></a>

The optional Model Context Protocol (MCP) Server integration enables AI agents to programmatically access and analyze your load testing data through natural language interactions. This component is only deployed if you select the MCP Server option during solution deployment.

The MCP Server acts as a bridge between AI development tools and your DLT deployment, providing a standardized interface for intelligent analysis of performance testing results. The architecture integrates several AWS services to create a secure, scalable interface for AI agent interactions:

## Amazon Bedrock AgentCore Gateway
<a name="agentcore-gateway"></a>

Amazon Bedrock AgentCore Gateway is a fully managed service that provides standardized hosting and protocol management for MCP servers. In this solution, AgentCore Gateway serves as the public endpoint that AI agents connect to when requesting access to your load testing data.

The service handles all MCP protocol communication, including tool discovery, authentication token validation, and request routing. AgentCore Gateway operates as a multi-tenant service with built-in security protections against common threats to public endpoints, while validating Cognito token signatures and claims for each request.

## DLT MCP Server Lambda
<a name="MCP-Server-Lambda"></a>

The DLT MCP Server Lambda function is a custom serverless component that processes MCP requests from AI agents and translates them into queries against your DLT resources.

This Lambda function acts as the intelligence layer of the MCP integration, retrieving test results from DynamoDB tables, accessing performance artifacts stored in S3 buckets, and querying CloudWatch logs for detailed execution information. The Lambda function implements read-only access patterns and transforms raw DLT data into structured, AI-friendly formats that agents can easily interpret and analyze.

## Authentication integration
<a name="MCP-Auth-Integration"></a>

The authentication system leverages your existing Cognito user pool infrastructure to maintain consistent access controls across both the web console and MCP Server interfaces.

This integration uses OAuth 2.0 token-based authentication. Users authenticate once through the Cognito login process and receive tokens that work for both UI interactions and MCP Server access. The system maintains the same permission boundaries and access controls as the web interface, ensuring that users can only access through AI agents the same load testing data they can access through the console.
