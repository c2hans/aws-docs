---
source_url: https://docs.aws.amazon.com/solutions/multiplayer-session-based-game-hosting-on-aws/index.html
---

---
title: 'Guidance for Multiplayer Session-Based Game Hosting on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/multiplayer-session-based-game-hosting-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Multiplayer Session-Based Game Hosting on AWS

## Overview

This Guidance helps game developers get started with multiplayer game development by using Amazon GameLift for low-latency global game server hosting and matchmaking. It supports Unity, Unreal, and Godot game engines on the client side and provides sample integrations with Amazon GameLift for multiple game server implementation options, including C++, Go, Unity, and Unreal. This Guidance also implements best practices for integrating your game backend with Amazon GameLift in addition to observability with Amazon CloudWatch through near real-time game server logs, process-level game server metrics, and distributed tracing for backend APIs.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/multiplayer-session-based-game-hosting-on-aws.pdf)

![Architecture diagram](/images/solutions/multiplayer-session-based-game-hosting-on-aws/images/multiplayer-session-based-game-hosting-on-aws-1.png)

1. **Step 1**: Game client measures TCP latency to AWS Regions by calling Amazon DynamoDB endpoints.
1. **Step 2**: Game client uses the AWS Game SDK to make an authenticated POST request to Amazon API Gateway with the latency data in the request body.
1. **Step 3**: API Gateway validates client JSON Web Token with the Custom Identity Component public keys.
1. **Step 4**: API Gateway calls request-matchmaking AWS Lambda function, which sends a StartMatchmaking request to Amazon GameLift FlexMatch with the latency data.
1. **Step 5**: Amazon GameLift FlexMatch matches the player with other players and calls the Amazon GameLift queue to request a placement in case of a new match. It can also backfill players to existing matches.
1. **Step 6**: The Amazon GameLift queue finds a placement based on player latencies in one of the Amazon GameLift fleet locations.
1. **Step 7**: Once the placement is done and session started, Amazon GameLift FlexMatch sends a MatchmakingSucceeded event to an Amazon Simple Notification Service (Amazon SNS) topic. It also sends all intermediate events such as MatchmakingSearching.
1. **Step 8**: Amazon SNS invokes process-matchmaking Lambda function, which updates all match status changes to a DynamoDB table.
1. **Step 9**: Game client polls match status with a GET request containing the matchmaking ticket ID.
1. **Step 10**: Get-match-status Lambda function gets the latest match info from DynamoDB and sends it back to the game client. When matchmaking is done, it also sends the IP, port, and player session ID to the client.
1. **Step 11**: Game client connects with TCP (often UDP in real-time games) to the game session and sends the player session ID that the game server validates.
1. **Step 12**: The instances send logs and metrics to Amazon CloudWatch using the CloudWatch agent.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-custom-game-backend-hosting-on-aws/tree/main/BackendFeatures/AmazonGameLiftIntegration)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon GameLift manages game server fleets globally with a highly available configuration in each location, allowing you to configure how you want the game server fleet to scale and operate. Serverless services such as API Gateway, Lambda, and DynamoDB reduce the operational effort by managing underlying infrastructure on your behalf, so you can focus on code and configuration. By using CloudWatch to monitor all the components of the Guidance through metrics and logs, you can investigate bottlenecks or errors in near real time. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

API Gateway supports authentication of requests to validate user identities with the JSON Web Token provided by the game client and the public keys provided by the Custom Identity component. Authentication helps ensure players are who they claim to be when accessing their data on the backend Lambda functions. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon GameLift provides high availability in all Regions through hosting the game server instances in multiple Availability Zones (AZs). It will also automatically replace any failed game server processes or instances. The DynamoDB table for matchmaking tickets allows automatic horizontal scaling as the player load increases. DynamoDB also hosts in multiple AZs within the Region. The matchmaking tickets are considered ephemeral (and are also automatically deleted after 3 hours), so you don’t need to do backups on the table. For notifications on any availability issues, we recommend implementing CloudWatch alarms on appropriate metrics from Amazon GameLift for game servers in addition to any errors on the API Gateway and Lambda layers. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon GameLift allows direct client-to-server communication to optimize near real-time performance. This architecture diagram allows developers to host game servers using Amazon GameLift across multiple Regions, reducing the latency between the game client and the server. DynamoDB stores the matchmaking results and allows you to retrieve them with single-digit millisecond response times at scale. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The DynamoDB Time to Live (TTL) feature deletes items from your table after 3 hours without consuming any write throughput. This provides enough time for you to have the items available when you need them, but minimizes overall cost for unnecessary storage. Amazon GameLift allows you to use a combination of Amazon Elastic Compute Cloud (Amazon EC2) On-Demand and Spot instances. Configuring an On-Demand fleet and Spot fleet behind the same Amazon GameLift queue can help reduce cost through a built-in Spot optimization algorithm of Amazon GameLift, which uses Spot as the preferred choice when available. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon GameLift requires at least a single instance per Region to allow appropriate response times and to initiate scaling of the service, but the locations can be scaled to 1 at times of low traffic and to 0 for development and test environments. Additionally, the serverless services used by the backend, including DynamoDB, Lambda, and API Gateway scale based on demand to match the required capacity, reducing the compute footprint of this Guidance. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
