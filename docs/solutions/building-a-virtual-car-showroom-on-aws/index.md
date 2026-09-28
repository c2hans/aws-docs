---
source_url: https://docs.aws.amazon.com/solutions/building-a-virtual-car-showroom-on-aws/index.html
---

---
title: 'Guidance for Building a Virtual Car Showroom on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-virtual-car-showroom-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Building a Virtual Car Showroom on AWS

## Overview

This Guidance demonstrates how to create an immersive virtual car showroom experience that transforms traditional automotive retail through cutting-edge AI technologies. By leveraging Large Language Models (LLM), voice agents, and advanced speech technologies, businesses can deliver personalized, interactive vehicle exploration experiences that increase customer engagement and streamline the purchasing journey. The solution helps dealerships expand their market reach beyond physical locations while reducing operational costs. It shows how integrating conversational AI and voice interfaces can create more natural, accessible shopping experiences that meet modern consumers' expectations for convenient, on-demand service - ultimately driving higher conversion rates and customer satisfaction.

## Benefits

### Deliver personalized car shopping experiences

Enable natural conversations between customers and AI voice agents to explore vehicle inventory and specifications. Enhance customer engagement through interactive voice and visual interactions that feel natural and responsive.

### Scale customer service automatically

Automatically adjust AI agent capacity based on customer demand using container-based architecture. Optimize costs by paying only for the resources needed to handle current customer interactions.

### Ensure reliable customer experiences

Maintain consistent performance through automated monitoring and scaling of AI voice agents. Deliver uninterrupted service by detecting and responding to changes in customer demand patterns.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-a-virtual-car-showroom-on-aws.pdf)

![Architecture diagram](/images/solutions/building-a-virtual-car-showroom-on-aws/images/building-a-virtual-car-showroom-on-aws-1.png)

1. **Step 1**: A car shopper starts by talking with their web or mobile app that is served via AWS Amplify.
1. **Step 2**: The app connects to a WebRTC provider to start a user session.
1. **Step 3**: The user session connects with an AI Voice Agent running as a Task in Amazon Elastic Container Service (Amazon ECS) based on a published container from Amazon Elastic Container Registry (Amazon ECR).
1. **Step 4**: The AI Voice Agent uses Amazon Transcribe to convert speech to text to be then processed, by a foundation model of your choice through Amazon Bedrock.
1. **Step 5**: Your LLM from Amazon Bedrock responds to the prompt and utilises function calls to interact with external tools.
1. **Step 6**: The function call initiates additional agents and LLMs to query Amazon Aurora and pull the car inventory via text-to-sql chaining.
1. **Step 7**: The car images referenced in the data retrieved through RAG (Retrieval-Augmented Generation) in the previous steps are then pulled from Amazon Simple Storage Service (Amazon S3) and presented to the LLM to further enhance the context for describing the data set.
1. **Step 8**: The text response from the LLM is then handed over to Amazon Polly to generate the response in natural language.
1. **Step 9**: The generated voice and text are then transported back to the WebRTC layer.
1. **Step 10**: The client app then relays the audio and visual content in the web or mobile app.
1. **Step 11**: The user continues further interaction and Q&A via voice and visual displays as inputs.
[Read usage guidelines](/solutions/guidance-disclaimers/)
