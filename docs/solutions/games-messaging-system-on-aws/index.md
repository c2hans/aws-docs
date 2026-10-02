---
source_url: https://docs.aws.amazon.com/solutions/games-messaging-system-on-aws/index.html
---

---
title: 'Guidance for Games Messaging System on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/games-messaging-system-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Games Messaging System on AWS

## Overview

This Guidance helps game developers build a scalable, serverless push notification system that addresses the challenge of delivering timely, targeted messages to players across different game events and campaigns. The system connects through WebSocket API Gateway to handle game events in real-time, storing player data securely in DynamoDB. When important player activities occur, automated processes instantly prepare and deliver notifications through Amazon SES, while also supporting targeted messaging to specific player segments based on custom queries. You can notify players about friend activities and in-game events while maintaining message records to meet your regulatory requirements.

## Benefits

### Optimize player engagement

Deploy a serverless messaging system that automatically delivers real-time notifications for friend activities and game events. Keep players connected to your game through timely, relevant communications that drive retention and session frequency.

### Scale messaging effortlessly

Implement a flexible architecture that automatically scales to handle varying message volumes without manual intervention. Focus on creating compelling player communications while AWS services manage the underlying infrastructure to match your game's growth.

### Target communications precisely

Leverage analytics capabilities to segment your player base and deliver personalized marketing campaigns to specific audience groups. Increase conversion rates by sending the right message to the right players at the right time.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/games-messaging-system-on-aws.pdf)

![Architecture diagram](/images/solutions/games-messaging-system-on-aws/images/games-messaging-system-on-aws-1.png)

1. **Step 1**: First, you'll connect through Amazon API Gateway WebSocket - this triggers an AWS Lambda function to handle your game events.
1. **Step 2**: When you need to handle player data, a Lambda function takes your game and user information and stores it safely in an Amazon DynamoDB table.
1. **Step 3**: You'll see your data being processed automatically by DynamoDB Streams triggering Lambda as soon as it arrives. This means when your players do something important (like friend login), you can notify them right away.
1. **Step 4**: To keep track of all your messages, you'll store them in a Message table in Amazon DynamoDB. This way, you can see what you've sent and check if it was delivered successfully.
1. **Step 5**: When DynamoDB Streams detect new message content in your DynamoDB table, a Lambda function automatically prepares it for sending through Amazon Simple Email Service(Amazon SES).
1. **Step 6**: Amazon SES then handles delivering your notifications - making sure they reach your players' devices exactly when you want them to.
1. **Step 7**: When you need to send messages to specific groups of players (like "all players active in last 30 days"), you'll use DynamoDB Zero-ETL and AWS Glue to organize your player data.
1. **Step 8**: You can then run your custom queries in Amazon Athena to find exactly which players should get your messages and save your results to an Amazon S3 bucket.
1. **Step 9**: A Lambda function will then take these results, add them to the Message table in DynamoDB, and start your notification process automatically.
1. **Step 10**: Throughout all of this, you can monitor your system's performance through Amazon CloudWatch dashboards, seeing exactly how your messages are being delivered.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-of-gaming-messaging-system-with-amazon-dynamoDB)

[Read usage guidelines](/solutions/guidance-disclaimers/)
