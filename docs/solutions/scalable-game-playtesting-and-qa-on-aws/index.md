---
source_url: https://docs.aws.amazon.com/solutions/scalable-game-playtesting-and-qa-on-aws/index.html
---

# Guidance for Scalable Game Playtesting and QA on AWS

## Overview

This Guidance helps game developers securely manage and scale their quality assurance (QA) and playtesting efforts using an AWS-based solution. This Guidance provides a web-based console for uploading game builds, configuring testing campaigns, inviting and managing testers, and reviewing session data and tester feedback powered by Amazon Bedrock for summarization and sentiment analysis. It integrates with AWS services like Amazon GameLift Streams and Amazon CloudFront to streamline the distribution of game content and sharing of client builds via streaming technology. With this Guidance, developers can scale their testing efforts anywhere in the world on-demand, increase testing frequency with no locally installed builds, protect intellectual property by reducing the risk of pre-release content leaks, and accelerate game improvements with GenAI player feedback and sentiment summaries.

## Benefits

### Streamline playtester onboarding and management

Reduce operational overhead with self-service registration and automated session management through Discord integration. Enable testers to instantly access games through browser-based streaming.

### Scale playtesting operations effortlessly

Leverage serverless architecture to automatically handle varying playtest demands without infrastructure management. Pay only for actual testing sessions while maintaining consistent performance.

### Accelerate feedback insights with AI-powered analysis

Transform playtesting feedback into actionable insights using GenAI summarization and sentiment analysis. Make informed decisions faster with automated analysis of player responses and structured data management.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/scalable-game-playtesting-and-qa-on-aws.pdf)

![Architecture diagram](/images/solutions/scalable-game-playtesting-and-qa-on-aws/images/scalable-game-playtesting-and-qa-on-aws-1.png)

1. **Step 1**: Users manage playtests through Single Page Application (SPA) hosted within Amazon Simple Storage Service (Amazon S3). Management functions included (orchestrating playtest sessions, organizing playtesters, etc.) All authentication is handled by Amazon Cognito.
1. **Step 2**: Managed Amazon CloudFront website utilizes Amazon API Gateway and AWS Lambda to call Amazon GameLift Streams to create new streaming client. Amazon S3 is used to store game builds for GameLift Streams.
1. **Step 3**: AWS Step Functions are used to manage the various states of setting up new GameLift Streams.
1. **Step 4**: Playtesting information (Observations, Observation Results, Playtesters, Playtest sessions, Studio, and Publisher) will be stored and retrieved from Amazon DynamoDB.
1. **Step 5**: Users can leverage foundation models available through Amazon Bedrock to automatically summarize hundreds of playtester's feedback, derive sentiment and generate actionable insights from gameplay sessions
1. **Step 6**: Play Testers interact with Discord via bot to receive playtesting URL's and to play test games. Players are able to self-register and initialize their playtest sessions without leaving discord.
1. **Step 7**: Play Testers may receive playtesting URL outside of Discord where pixel streaming can be done within a browser.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-scalable-game-playtesting-and-qa-on-aws/tree/main)

[Read usage guidelines](/solutions/guidance-disclaimers/)
