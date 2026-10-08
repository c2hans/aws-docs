---
source_url: https://docs.aws.amazon.com/solutions/deploying-ai-agents-to-device-fleets-using-aws-iot-greengrass/index.html
---

---
title: 'Guidance for Deploying AI Agents to Device Fleets by Using AWS IoT Greengrass'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-ai-agents-to-device-fleets-using-aws-iot-greengrass/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Deploying AI Agents to Device Fleets by Using AWS IoT Greengrass

## Overview

This Guidance demonstrates how to leverage AWS IoT Greengrass to deploy StrandsAgents with local Small Language Models (SLMs) at the edge, enabling robust agentic operations across distributed device fleets. It helps organizations achieve critical operational requirements including low-latency processing, offline capabilities, and enhanced data confidentiality. The solution is particularly valuable for industries with stringent edge computing needs, such as robotics, automotive, oil and gas, and smart home automation. By combining cloud support with edge processing through Ollama inference engine, businesses can maintain reliable operations even with intermittent connectivity while ensuring sensitive data remains secure and local.

## Benefits

### Enable intelligent edge operations

Deploy AI capabilities directly to your device fleet with locally running foundation models through Ollama. Your operations continue uninterrupted with local intelligence even when cloud connectivity is limited or unavailable.

### Streamline fleet-wide deployments

Manage AI model distribution to thousands of edge devices through a centralized workflow using AWS IoT Greengrass and S3. Focus on developing intelligent applications while AWS services handle secure model deployment and device management.

### Access comprehensive data insights

Empower edge devices to reason across multiple data sources including documentation and OPC-UA industrial systems. The orchestration capabilities of Amazon Strands Agents SDK intelligently coordinate specialized agents to deliver contextual responses to complex queries.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/deploying-ai-agents-to-device-fleets-using-aws-iot-greengrass.pdf)

![Architecture diagram](/images/solutions/deploying-ai-agents-to-device-fleets-using-aws-iot-greengrass/images/deploying-ai-agents-to-device-fleets-using-aws-iot-greengrass-1.png)

1. **Step 1**: The user uploads a model file in GPT-Generated Unified Format (GGUF) to an Amazon Simple Storage Service (Amazon S3) bucket which AWS IoT Greengrass devices have access for.
1. **Step 2**: The devices in the fleet receive a file download job. The S3FileDownloader component processes this job and downloads the model file to the device from the Amazon S3 bucket.
1. **Step 3**: The model file in GGUF format loads into Ollama when the StrandsAgents component makes the first call to Ollama. The model name is specified in the recipe.yaml file of the component.
1. **Step 4**: The user sends a query to the local agent by publishing a payload to a device-specific agent topic in AWS IoT Core MQTT broker.
1. **Step 5**: After receiving the query, the component leverages the Strands Agents SDK's model-agnostic orchestration capabilities. The Orchestrator Agent perceives the query, reasons about the required information sources, and acts by calling the appropriate specialized agents (Documentation Agent, OPC-UA Agent, or both) to gather comprehensive data before formulating a response.
1. **Step 6**: If the query is related to information that can be found in the documentation, Orchestrator Agent calls Documentation Agent.
1. **Step 7**: Documentation Agent finds the information from the provided documents and returns it to Orchestrator Agent.
1. **Step 8**: If the query is related to current or historical machine data, Orchestrator Agent will call OPC-UA Agent.
1. **Step 9**: OPC-UA Agent makes a query to the OPC-UA server depending on the user query and returns the data from server to Orchestrator Agent.
1. **Step 10**: Orchestrator Agent forms a response based on the collected information. The StrandsAgents component publishes the response to a device-specific agent response topic in the AWS IoT Core MQTT broker.
1. **Step 11**: The Strands Agents SDK enables the system to work with locally deployed foundation models through Ollama at the edge, while maintaining the option to switch to cloud-based models like those in Amazon Bedrock when connectivity is available.
1. **Step 12**: The AWS Identity and Access Management (IAM) Greengrass Service Role provides access to the Amazon S3 resource bucket to download models to the device.
1. **Step 13**: The IoT certificate attached to the IoT thing allows the StrandsAgents component to receive and publish MQTT payloads to AWS IoT Core.
1. **Step 14**: The IoT Greengrass component logs the component operation to the local file system. Optionally, AWS CloudWatch Logs can be enabled to monitor the component operation in the CloudWatch console.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-deploying-ai-agents-to-device-fleets-using-aws-iot-greengrass)

[Read usage guidelines](/solutions/guidance-disclaimers/)
