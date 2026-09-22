---
source_url: https://docs.aws.amazon.com/solutions/custom-game-backend-hosting-on-aws/index.html
---

---
title: 'Guidance for Custom Game Backend Hosting on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/custom-game-backend-hosting-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Custom Game Backend Hosting on AWS

## Overview

This Guidance demonstrates how to deploy a custom, lightweight cross-platform game identity system, in addition to game backend features such as game server hosting with Amazon GameLift, chat with WebSockets, and friends lists and recommendations with Amazon Neptune. The identity system supports a number of authentication options including guest, Amazon Cognito, Steam, Sign-in with Apple, Google Play, and Facebook. You can also easily customize the Guidance to support any additional platforms, such as consoles. The Guidance is designed to be easily extendable with custom backend features and includes templates for both serverless and containerized backend components. Additionally, this Guidance provides software development kits (SDKs) and sample code for [Unreal Engine 5](https://github.com/aws-solutions-library-samples/guidance-for-custom-game-backend-hosting-on-aws/tree/main/UnrealSample) , [Unity 2021](https://github.com/aws-solutions-library-samples/guidance-for-custom-game-backend-hosting-on-aws/tree/main/UnitySample) (and newer versions), and [Godot 4](https://github.com/aws-solutions-library-samples/guidance-for-custom-game-backend-hosting-on-aws/tree/main/GodotSample) game engines. The SDKs integrate with the identity component and the sample backend features.

## How it works

This architecture diagram illustrates how to deploy a custom, lightweight, and scalable cross-platform game identity component and how to use the identities to authenticate against custom game backend components on AWS

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/custom-game-backend-hosting-on-aws.pdf)

![Architecture diagram](/images/solutions/custom-game-backend-hosting-on-aws/images/custom-game-backend-hosting-on-aws-1.png)

1. **Step 1**: The AWS Lambda function generate-keys is invoked every 7 days.
1. **Step 2**: Generate-keys gets the latest public jwks.json file from Amazon Simple Storage Service (Amazon S3), generates new public keys (JSON Web Key Set (JWKS)), and private keys, and updates Amazon S3 with the new public key and the previous key.
1. **Step 3**: Generate-keys updates the private key that is used to generate JSON Web Tokens (JWT) to AWS Secrets Manager.
1. **Step 4**: The game client uses the software development kit (SDK) to request a new guest identity. Or, the game client can sign in with their existing guest identity by sending the guest_secret through Amazon API Gateway, which is protected by AWS WAF rules.
1. **Step 5**: The login-as-guest Lambda function validates the guest identity, or creates a new one to the UserTable in Amazon DynamoDB.
1. **Step 6**: The Lambda function requests the private key from Secrets Manager, generates a signed JWT token for the client, and sends it back.
1. **Step 7**: The game client can now call custom backend components by sending requests with the JWT token in the Authorization header using the SDK.
1. **Step 8**: The backend components validate the token by requesting the JWKS public keys from the public endpoint through Amazon CloudFront, which gets the file from Amazon S3.
1. **Step 9**: The SDK automatically refreshes the JWT access token by calling refresh-access-token Lambda function through API Gateway. The function generates a new token using the private key from Secrets Manager.
1. **Step 10**: Additionally, the game client can send access tokens from the game platform-specific identity provider to link to an existing account, or create a new account. This account can optionally be created in an Amazon Cognito user pool. The Lambda functions validate the tokens and create the link to the user account in a specific DynamoDB table. Then it generates a JWT token for the client using the private key from Secrets Manager.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-custom-game-backend-hosting-on-aws/tree/main)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The custom identity component in this Guidance utilizes AWS X-Ray that traces user requests, and leverages Lambda Powertools to provide detailed information from within the backend logic. In addition, all components of this Guidance use Amazon CloudWatch to track logs of virtual private cloud (VPC) flows, API Gateway access, Amazon S3 access, Lambda completions, and AWS Fargate tasks. Finally, AWS CDK allows for controlled changes and consistent configuration across environments, helping you to meet your security and compliance needs. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

To support robust identity management, the custom identity component of this Guidance manages player identities and authentication. All other features of this Guidance secure access by validating JSON Web Tokens against public keys provided by the identity component. The custom identity component is protected by AWS WAF, a web application firewall that protects applications against common web exploits. Also, all data is encrypted at rest, as well as in transit. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance mainly leverages fully managed services that are highly available by default across multiple Availability Zones (AZ) within an AWS Region. For Fargate, a multi-AZ configuration is utilized for high availability and all database tables in DynamoDB are protected with point-in-time recovery. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance combines a number of different approaches to allow for various features to improve performance. First, the services selected for this Guidance are designed to perform at scale for game launches and other spikes in traffic by leveraging the automatically scaling components of serverless services. Next, the X-Ray data provided from the custom identity component allows developers to find congestion and calibrate the Guidance to their needs to optimize performance. Finally, the public keys that validate the JSON Web Tokens are provided through CloudFront to optimize latency for backend components. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance leverages serverless components when possible, allowing you to pay only for the exact resources you use. To further help with cost, consider AWS Savings Plans that can be utilized to optimize the cost for both Lambda and Fargate. Also, moving from on-demand DynamoDB tables to auto-scaling provisioned capacity allows you to use DynamoDB reserved capacity to reduce costs when the baseline traffic is known. All services utilized in this Guidance are configured to scale based on demand, including API Gateway, Lambda, DynamoDB, Amazon S3, Fargate, Secrets Manager, and AWS WAF, ensuring that only the minimum resources are required. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The components of serverless services in this Guidance scale automatically, allowing the components to scale while continually matching the load with only the minimum resources needed. This reduces the environmental impact of the infrastructure by avoiding provisioning unused capacity. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Wicked Saints Studios integrates TikTok within World Reborn using AWS**: This blog demonstrates how Wicked Saints Studios overcame TikTok integration challenges in their mobile game World Reborn by leveraging AWS infrastructure to create a cost-effective, custom solution when faced with expensive or inadequate market alternati

[Learn more](https://aws.amazon.com/blogs/gametech/wicked-saints-studios-integrates-tiktok-within-world-reborn-using-aws/)

- **AWS Game Backend Framework Workshop**: This workshop demonstrates how to deploy and test the AWS Game Backend Framework, integrate it with popular game engines, and leverage Visual Studio Code server for AWS CDK infrastructure deployment.

[Learn more](https://catalog.workshops.aws/awsgamebackendframework/en-US)

- **Harmony Games Deploys a Fully Custom Game Backend Utilizing AWS Cloud Development Kit (AWS CDK)**: This blog post demonstrates how Harmony Games utilizes AWS CDK to deploy a fully custom game backend infrastructure on AWS, enabling efficient development and scaling of their multiplayer game services.

[Learn more](https://aws.amazon.com/blogs/gametech/harmony-games-deploys-a-fully-custom-game-backend-utilizing-aws-cloud-development-kit-aws-cdk/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
