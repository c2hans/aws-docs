---
source_url: https://docs.aws.amazon.com/solutions/persistent-world-game-hosting-on-aws/index.html
---

---
title: 'Guidance for Persistent World Game Hosting on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/persistent-world-game-hosting-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Persistent World Game Hosting on AWS

## Overview

This Guidance helps game developers build persistent world games and host virtual worlds on AWS using Amazon GameLift and serverless backend components. The architecture uses managed and serverless components to reduce operational effort and scale based on player demand. Developers can use this architecture to get started with persistent virtual world game development on MacOS and Windows. This Guidance includes infrastructure as code (IaC) automation, configuration scripts for setting up dependencies, and a sample Unity client/server implementation.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/persistent-world-game-hosting-on-aws.pdf)

![Architecture diagram](/images/solutions/persistent-world-game-hosting-on-aws/images/persistent-world-game-hosting-on-aws-1.png)

1. **Step A**: Amazon EventBridge triggers WorldManager AWS Lambda function every one minute. The function checks existing worlds' status through the Amazon GameLift API.
1. **Step B**: WorldManager Lambda function stores the current state of the sessions and worlds to Amazon DynamoDB for faster back end access.
1. **Step C**: WorldManager queries configured worlds from DynamoDB and creates any worlds that are not running by calling the Amazon GameLift API CreateGameSession.
1. **Step 1**: Game client request an identity and credentials from Amazon Cognito Identity Pool to sign authorized API requests.
1. **Step 2**: Game client requests the world list through Amazon API Gateway. API Gateway triggers ListWorlds Lambda function that checks game session information in the defined Region from DynamoDB.
1. **Step 3**: Game client requests to join a specific world in a specific Region by calling JoinWorld Lambda function through API Gateway.
1. **Step 4**: Lambda function creates a player session for the player, increases the amount of players for that world in DynamoDB, and sends the connection information to the game client.
1. **Step 5**: Client connects to the Amazon GameLift session directly over transmission control protocol (TCP) and sends the player session ID.
1. **Step 6**: Amazon GameLift session validates the player session ID with the Amazon GameLift server software development kit (SDK).
1. **Step 7**: Amazon GameLift checks for world-specific player data and updates the player data as needed. It will store the latest player location after the player leaves.
1. **Step 8**: Amazon GameLift session checks DynamoDB for scheduled termination and terminates if requested.
1. **Step 9**: Game server sends logs and metrics to Amazon CloudWatch using the CloudWatch Agent.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-persistent-world-game-hosting-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS Cloud Development Kit (AWS CDK) handles deployments and updates by using AWS CloudFormation to control resource updates and rollbacks. This reduces errors caused by manual configuration changes. For Amazon GameLift fleet updates, CloudFormation will create a replacement fleet. It will wait for the replacement to become fully active to accept traffic before terminating the old fleet. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The game client uses Amazon Cognito Identity Pool identities to secure access to the back end services. This is achieved by signing the requests with AWS Identity and Access Management (IAM) credentials provided by the Identity Pool. Only authenticated requests are allowed to the provided APIs hosted on API Gateway. Additionally, game clients are allowed to access only the data of their own account. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

In case the game server (and consequently the game world) crashes, the architecture will automatically replace the world with a new one, which will have access to the same persisted data of that specific world. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon GameLift allows direct client to server communication to optimize near real time performance. The architecture allows developers to host game servers across multiple AWS Regions, reducing the latency between the game client and the server. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The architecture leverages serverless components including API Gateway, Lambda and DynamoDB, which allow you to reduce costs by paying for the exact amount of resources based on player traffic. Additionally, Amazon GameLift can be configured to scale based on demand so you have a minimal set of unused resources running at any given time. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This architecture uses managed and serverless services to run only the resources required for the current player load, reducing your individual impact on the environment. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
