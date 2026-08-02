---
source_url: https://docs.aws.amazon.com/solutions/gamelift-testing-on-aws/index.html
---

# Guidance for GameLift Testing on AWS

## Overview

This Guidance helps developers test, visualize, and optimize their multiplayer games using the Amazon GameLift Testing Toolkit. With the toolkit, developers can troubleshoot, debug, and tune their Amazon GameLift infrastructure. This Guidance offers an optional capability to use virtual players that run the same code as real players so developers can test the success of their game before launching it into production.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/gamelift-testing-on-aws.pdf)

![Architecture diagram](/images/solutions/gamelift-testing-on-aws/images/gamelift-testing-on-aws-1.png)

1. **Step 1**: Amazon CloudFront provides access to the toolkit web console, which is stored on Amazon Simple Storage Service (Amazon S3). Toolkit console users authenticate with Amazon Cognito user pools.
1. **Step 2**: The web console connects with an Amazon API Gateway WebSocket API, which calls an AWS Lambda function to process requests and store data in Amazon DynamoDB.
1. **Step 3**: The Lambda function can query and update Amazon GameLift infrastructure directly.
1. **Step 4**: The game listener receives GameLift events through Amazon EventBridge and uses AWS Step Functions to poll and receive infrastructure updates from GameLift and Amazon CloudWatch.
1. **Step 5**: The game listener dispatches aggregated event data over a custom EventBridge event bus. The events are received by a Lambda function which stores data in DynamoDB and calls API Gateway to send data to connected web console users for display.
1. **Step 6**: The web console user can also launch virtual player tasks on AWS Fargate to simulate real game clients.
1. **Step 7**: Each virtual player task requests an Amazon Cognito guest identity and connects into the game client services API Gateway to request matchmaking.
1. **Step 8**: The Lambda functions call GameLift FlexMatch to start the matchmaking process and place successful matches onto a fleet using game session queues.
1. **Step 9**: The virtual player tasks connect with GameLift fleet instances to start their game sessions.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/amazon-gamelift-testing-toolkit/)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Both the toolkit and the sample game are fully deployed with infrastructure as code, which reduces errors caused by manual processes and reduces the effort to deploy changes. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The serverless web console API on API Gateway is protected with AWS Identity and Access Management (IAM) based authentication against a Cognito User Pool. The serverless sample game backend on API Gateway is protected with IAM-based authentication for secure validation of the player's guest identity. Game servers on GameLift only allow access to the ports used for client-server communication. The backend Lambda functions only have access to the services they need. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Data is stored in DynamoDB tables, utilizing on-demand capacity allocation to automatically scale based on changes in demand. The solution backend services use Lambda, which scales instances automatically. The sample game backend supports GameLift Target-based auto-scaling to handle changes in demand. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

By utilizing managed, serverless technologies such as API Gateway, Lambda, DynamoDB, and Fargate, you only pay for the resources you use and reduce the operational effort required to maintain the solution. The solution can be deployed into a region of your choice, and utilizes CloudFront to reduce latency for the web console end user. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Virtual Player Tasks can be launched with Fargate Spot to reduce the cost of testing. The web console and sample game backends utilize serverless technologies so that you only pay for the resources you use. The web console backend utilizes the native scaling features of Lambda and API Gateway, with DynamoDB tables using on-demand capacity allocation to ensure the resources match the demand. The sample game backend supports GameLift Target-based auto-scaling to minimize the resources required. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance extensively uses managed services, which shifts responsibility for maintaining high-average utilization to AWS. The sample game backend supports GameLift Target-based auto-scaling to minimize the resources required. By packing game sessions onto the minimum number of server instances, resource utilization is kept consistently high. By widely utilizing managed services, this Guidance reduces your individual impact on the environment. You can further reduce the sustainability impact of unused resources by launching game servers onto Spot fleets, and launching Virtual Player tasks onto Fargate Spot. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
