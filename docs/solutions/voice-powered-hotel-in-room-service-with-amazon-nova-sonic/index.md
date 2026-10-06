---
source_url: https://docs.aws.amazon.com/solutions/voice-powered-hotel-in-room-service-with-amazon-nova-sonic/index.html
---

---
title: 'Guidance for Voice-Powered Hotel In-Room Service with Amazon Nova Sonic'
canonical_url: https://docs.aws.amazon.com/solutions/voice-powered-hotel-in-room-service-with-amazon-nova-sonic/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Voice-Powered Hotel In-Room Service with Amazon Nova Sonic

## Overview

This Guidance helps hotels modernize guest experiences by enabling voice-based room service ordering and requests through AI-powered conversations with Amazon Nova Sonic. Guests speak naturally to an in-room interface that streams audio to Amazon Nova Sonic, which processes requests and triggers actions like adding items to a cart, placing orders, or scheduling housekeeping. The system handles menu browsing, loyalty program queries, and service requests through real-time voice interaction, with all data securely managed through Amazon DynamoDB and encrypted at rest. You can deliver seamless, hands-free guest services that reduce wait times and improve satisfaction while lowering operational overhead for your staff.

## Benefits

### Deliver hands-free guest experiences

Enable hotel guests to order services, request housekeeping, and manage bookings through natural voice conversations. Reduce front-desk call volume while improving guest satisfaction and response times.

### Scale without managing infrastructure

Deploy a fully serverless voice AI system that automatically scales with guest demand. Pay only for actual usage while eliminating idle compute costs during low-occupancy periods.

### Protect guest data by default

Secure sensitive guest information with encryption at rest, temporary scoped credentials, and web application firewall protections. Meet hospitality privacy expectations without custom security engineering.

## How it works

This architecture diagram shows how to build a voice-powered hotel in-room service system that enables guests to interact with hotel services through natural voice conversations powered by Amazon Nova Sonic. [Download the architecture diagram.](downloads/voice-powered-hotel-in-room-service-with-amazon-nova-sonic.pdf)

![Architecture diagram for Voice-Powered Hotel In-Room Service with Amazon Nova Sonic](/images/solutions/voice-powered-hotel-in-room-service-with-amazon-nova-sonic/images/voice-powered-hotel-in-room-service-with-amazon-nova-sonic-1.png)

1. **Step 1**: Hotel guests speak to an in-room voice interface, which captures audio and streams it to the backend through a WebSocket connection.
1. **Step 2**: Amazon Nova Sonic processes the audio stream in real time, understanding guest intent and generating natural conversational responses.
1. **Step 3**: AWS Lambda functions handle request orchestration, triggering actions such as adding items to cart, placing orders, or scheduling services.
1. **Step 4**: Amazon DynamoDB stores guest session data, menu information, order history, and loyalty program details with encryption at rest.
1. **Step 5**: AWS WAF protects the application from common web exploits, while temporary scoped credentials ensure secure access to backend resources.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/sample-voice-ai-powered-in-room-service-with-amazon-nova-sonic/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
