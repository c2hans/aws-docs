---
source_url: https://docs.aws.amazon.com/solutions/retail-hyper-personalization-on-aws/index.html
---

# Guidance for Retail Hyper Personalization on AWS

## Overview

This Guidance helps retailers deliver individualized experiences to both identified and anonymous consumers by combining real-time behavioral signals with machine learning recommendations and generative AI. The system processes browsing events, transactions, and in-store interactions in real time through Amazon Kinesis Data Streams, feeding Amazon Personalize for tailored product recommendations and Amazon Bedrock for personalized content generation. An AI Shopping Assistant powered by Amazon Bedrock AgentCore enables conversational product discovery, while automated retraining workflows detect and respond to model drift to maintain recommendation quality. You can increase conversion rates and customer lifetime value by delivering relevant experiences across every touchpoint, regardless of whether shoppers are logged in or anonymous.

## Benefits

### Deliver individualized experiences at scale

Combine machine learning recommendations with generative AI to serve personalized product suggestions and content to each shopper across every channel in near real-time.

### Automate your personalization operations

Deploy self-healing ML pipelines that detect model drift and trigger retraining automatically. Reduce manual intervention while keeping recommendations accurate as customer behavior evolves.

### Unify omnichannel retail signals instantly

Ingest and act on data from e-commerce, in-store IoT, POS, and CRM systems through a single streaming pipeline. Update customer profiles in near real-time to power timely engagement.

## How it works

This architecture diagram shows how to build a retail hyper personalization platform that combines real-time data streaming, machine learning recommendations, and generative AI to deliver individualized shopping experiences. [Download the architecture diagram.](downloads/retail-hyper-personalization-on-aws.pdf)

![Architecture diagram for Retail Hyper Personalization on AWS](/images/solutions/retail-hyper-personalization-on-aws/images/retail-hyper-personalization-on-aws-1.png)

1. **Step 1**: Behavioral signals from e-commerce, in-store IoT, POS, and CRM systems are ingested in real time through Amazon Kinesis Data Streams.
1. **Step 2**: Stream processing updates customer profiles and enriches event data for downstream personalization services.
1. **Step 3**: Amazon Personalize generates tailored product recommendations based on individual customer behavior and interaction history.
1. **Step 4**: Amazon Bedrock generates personalized content including product descriptions and marketing copy tailored to each shopper segment.
1. **Step 5**: An AI Shopping Assistant powered by Amazon Bedrock AgentCore enables conversational product discovery through natural language interactions.
1. **Step 6**: Automated monitoring detects model drift and triggers retraining workflows to maintain recommendation accuracy as customer behavior evolves.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-retail-hyper-personalization-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
