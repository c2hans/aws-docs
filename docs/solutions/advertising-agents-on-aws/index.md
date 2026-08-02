---
source_url: https://docs.aws.amazon.com/solutions/advertising-agents-on-aws/index.html
---

# Guidance for Advertising Agents on AWS

## Overview

This Guidance demonstrates how to transform advertising operations through AI-powered automation and multi-agent collaboration systems on Amazon Bedrock. It shows organizations how to streamline complex AdTech workflows, from campaign optimization to brand safety monitoring, using sophisticated AI agents working in concert. The solution helps marketing teams and advertising technology companies accelerate their digital transformation by providing a production-ready framework for automated decision-making in programmatic advertising. By implementing comprehensive knowledge bases and interactive simulation capabilities, this guidance enables teams to optimize campaign performance, improve ad yield, and make data-driven creative decisions while maintaining brand safety standards.

## Benefits

### Accelerate campaign planning decisions

Deploy specialized AI agents that collaborate to transform complex advertising workflows into actionable insights. Business users can interact naturally with media planning, inventory optimization, and ad load optimization agents to receive comprehensive campaign strategies in real time.

### Enhance advertising revenue potential

Leverage AI-powered analysis of campaign intelligence, performance analytics, and viewer monetization data to identify optimal audience segments and ad formats. The collaborative agent system delivers interactive visualizations with revenue projections to help maximize advertising yield.

### Streamline complex advertising workflows

Implement a secure, scalable architecture where business users can engage with specialized advertising agents through natural language conversations. The solution reduces manual effort by automating campaign planning tasks while maintaining governance through fine-grained IAM permissions.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/advertising-agents-on-aws.pdf)

![Architecture diagram](/images/solutions/advertising-agents-on-aws/images/advertising-agents-on-aws-1.png)

1. **Step 1**: Business Users securely authenticate through Amazon Cognito user pools. The AngularJS UI application, hosted in Amazon Simple Storage Service (Amazon S3) and distributed via Amazon CloudFront for low-latency global access, validates these Amazon Cognito tokens to authorize user sessions.
1. **Step 2**: User asks for Agent help in complex topics like planning a premium product campaign or optimizing inventory yield in natural language using chat interface, calling out the agent's name using @<agent> prefix.
1. **Step 3**: The query is passed to an Intelligent Orchestrator Strands Agent deployed in Amazon Bedrock AgentCore Runtime. Based on the input one of the Orchestrator agents, with agent depending on the invocation prompt, Media Planner, Inventory Optimizer, or Ad Load Optimizer handles the query.
1. **Step 4**: On initialization, the Orchestrator agent uses an agent config file packaged in the Agent Core run time to identify other specialized agents it needs to collaborate with. The specialized agents are then configured using Strands agent as a tool framework. The Orchestrator offers dual interaction modes - users can engage with the orchestration agents for comprehensive response, or directly chat with specialized agents for quick, focused answers.
1. **Step 5**: The Orchestrator agent uses Amazon Bedrock Knowledge Base indexed with campaign intelligence, performance analytics, content safety, and viewer monetization data stored in Amazon S3.
1. **Step 6**: The orchestrator agents and specialized agents collaboratively work together in natural language conversation, each focusing on areas like audience strategy, inventory optimization, ad format selection, and campaign timing.
1. **Step 7**: The agents use visualization template files stored in Amazon S3 to transform complex data to assist rendering of visual elements.
1. **Step 8**: The inter-agent conversations and the final response is streamed back to the user in real time. The final response contains integrated campaign strategies with interactive visualizations, including audience segments insights and revenue projections.
1. **Step 9**: The conversation history between the user and agents is stored in Amazon Bedrock AgentCore Memory.
1. **Step 10**: Amazon CloudWatch collects performance metrics and operational data from Amazon Bedrock AgentCore observability features, including session information and conversation traces.
1. **Step 11**: AWS Identity and Access Management (AWS IAM) implements fine-grained permissions for service-to-service communication and Amazon Bedrock AgentCore access following a least-privilege access model.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-advertising-agents-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
