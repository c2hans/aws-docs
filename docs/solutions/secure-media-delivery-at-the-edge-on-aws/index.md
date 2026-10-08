---
source_url: https://docs.aws.amazon.com/solutions/secure-media-delivery-at-the-edge-on-aws/index.html
---

---
title: 'Guidance for Secure Media Delivery at the Edge on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/secure-media-delivery-at-the-edge-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Secure Media Delivery at the Edge on AWS

## Overview

This Guidance demonstrates how to protect premium video content from unauthorized access when delivering through Amazon CloudFront by implementing token-based security at the edge. Amazon CloudFront functions validate secure tokens for each viewer request, permitting or denying access to video content based on individual authorization. The system uses AWS Secrets Manager for secure key storage and includes automatic key rotation through AWS Step Functions, while AWS WAF blocks compromised playback sessions for enhanced protection. You can maintain strict control over your valuable media assets while delivering high-performance streaming experiences to authorized viewers only.

## Benefits

### Strengthen content protection

Implement token-based authentication and automated session revocation to safeguard premium video content from unauthorized access. The solution helps protect your valuable media assets while maintaining seamless delivery to legitimate viewers.

### Accelerate threat response

Automatically identify and block compromised playback sessions through continuous log analysis and AWS WAF integration. Your content remains protected as the solution proactively detects suspicious patterns and revokes access without manual intervention.

### Simplify security operations

Deploy a comprehensive edge security solution with automated key rotation and centralized token management. Focus on your content strategy while the architecture handles complex security workflows through AWS Step Functions and serverless components.

## How it works

### Base Module

This architecture diagram illustrates how to effectively support the core components of Secure Media Delivery at the Edge on AWS. It shows the key components and their interactions, providing an overview of the architecture's structure and functionality.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/secure-media-delivery-at-the-edge-on-aws.pdf)Step 1A user makes a request to Amazon CloudFront for video manifests and segments.Step 2An Amazon CloudFront function validates secure tokens, permitting or denying access to video content.Step 3AWS Secrets Manager stores signing keys for viewer token generation and validation.Step 4An AWS Step Functions workflow coordinates key rotation.Step 5An AWS WAF rule group blocks compromised playback sessions identified by the solution.Step 6CloudFront delivers logs to Amazon Simple Storage Service (Amazon S3) for later analysis.Step 7Allowed requests are forwarded to origin for non-cached objects.### Auto Session-Revocation Module

This architecture diagram illustrates how to effectively support the Auto Session-Revocation components of Secure Media Delivery at the Edge on AWS. It shows the key components and their interactions, providing an overview of the architecture's structure and functionality.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/secure-media-delivery-at-the-edge-on-aws.pdf)Step 1An Amazon EventBridge rule runs periodically to invoke the session revocation workflow in Step Functions.Step 2A Lambda function generates SQL queries to Amazon Athena to obtain analysis and insights from the stored access logs.Step 3An Amazon DynamoDB table stores IDs and additional information associated with suspicious sessions to be revoked.Step 4A Lambda function compiles a final list of the playback sessions marked for blocking. It then updates the AWS WAF rule group with the appropriate rules matching selected sessions.### Website / API Demo Module

This architecture diagram illustrates how to effectively support the demo website and demo API components of Secure Media Delivery at the Edge on AWS. It shows the key components and their interactions, providing an overview of the architecture's structure and functionality.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/secure-media-delivery-at-the-edge-on-aws.pdf)Step 1A CloudFront distribution to deliver the traffic from Amazon API Gateway and deliver demo website (optionally, if enabled).Step 2A Lambda@Edge function that signs outgoing requests towards API Gateway according to SigV4 specification (for security).Step 3A demo website (when activated) with an embedded video player.Step 4An Amazon S3 bucket stores static assets for the demo website, and an auto session revocation module.Step 5A DynamoDB table stores metadata about video assets and corresponding parameters used to generate the tokens.Step 6An AWS Lambda function associated with API Gateway generates the token for video playback based on the retrieved metadata about the video assets and token parameters.Step 7The Lambda function leverages a solution-provided library containing the necessary methods to generate the tokens.Step 8An API Gateway public API processes requests to generate the tokens for video playback, and to manually revoke specified playback sessions.[Read usage guidelines](/solutions/guidance-disclaimers/)
