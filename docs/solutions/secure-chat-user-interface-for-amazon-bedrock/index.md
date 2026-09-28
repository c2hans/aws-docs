---
source_url: https://docs.aws.amazon.com/solutions/secure-chat-user-interface-for-amazon-bedrock/index.html
---

---
title: 'Guidance for Secure Chat User Interface for Amazon Bedrock'
canonical_url: https://docs.aws.amazon.com/solutions/secure-chat-user-interface-for-amazon-bedrock/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Secure Chat User Interface for Amazon Bedrock

## Overview

This Guidance demonstrates how to rapidly deploy secure, production-ready conversational AI applications using AWS Bedrock Agents with an intuitive chat interface. It helps organizations overcome common development hurdles by providing a pre-built, serverless framework featuring Cognito authentication, multi-agent support, and automated scaling capabilities. The solution shows how enterprises can accelerate their AI implementation timeline while maintaining robust security and scalability. By eliminating the complexity of frontend infrastructure development, organizations can focus on agent development and customization, enabling faster deployment of enterprise-grade conversational AI applications across various industries.

## Benefits

### Accelerate secure chat deployment

Deploy a configurable chat interface that supports multiple agent types without repeated UI deployments. Reduce time-to-market while maintaining enterprise-grade security controls.

### Simplify user authentication management

Leverage built-in authentication workflows with Amazon Cognito to secure user access. Focus on building chat experiences while AWS manages identity and access controls.

### Enable flexible agent integration

Configure your chat interface to work with Bedrock Agents, Strands Agents, or AgentCore Agents through a single UI. Adapt to changing requirements without rebuilding your application.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/secure-chat-user-interface-for-amazon-bedrock.pdf)

![Architecture diagram](/images/solutions/secure-chat-user-interface-for-amazon-bedrock/images/secure-chat-user-interface-for-amazon-bedrock-1.png)

1. **Step 1**: The user navigates to the Secure Chat UI URL.
1. **Step 2**: The Secure Chat UI makes a request to AWS Amplify.
1. **Step 3**: Amplify returns a page with HTML, CSS, and JavaScript. The user inputs the configuration details for Amazon Cognito and Amazon Bedrock Agents, Strands Agents, or Amazon Bedrock AgentCore Agents. The user configures each Agent through a configuration interface, eliminating the need for repeated UI deployments.
1. **Step 4**: Upon configuration completion, the user authenticates using Amazon Cognito with a username and password configured for them in the user pool.
1. **Step 5**: After successful authentication, Amazon Cognito Identity Pool exchanges authentication tokens for temporary AWS credentials through AWS Simple Token Service (AWS STS) using the appropriate AWS Identity and Access Management (IAM) Role.
1. **Step 6**: Amazon Cognito Identity Pool issues temporary AWS credentials to the Secure Chat UI.
1. **Step 7**: Once authenticated, the user sees the Secure Chat UI chat prompt.
1. **Step 8**: The user interacts with the configured Amazon Bedrock Agent, Strands Agent, or Amazon Bedrock AgentCore Agent.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-a-secure-chat-user-interface-for-amazon-bedrock)

[Read usage guidelines](/solutions/guidance-disclaimers/)
