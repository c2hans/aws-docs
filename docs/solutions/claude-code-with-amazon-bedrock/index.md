---
source_url: https://docs.aws.amazon.com/solutions/claude-code-with-amazon-bedrock/index.html
---

# Guidance for Claude Code with Amazon Bedrock

## Overview

This Guidance demonstrates how organizations can implement Claude Code with secure enterprise authentication for Amazon Bedrock using industry-standard protocols and AWS services. It outlines a comprehensive authentication flow integrating OpenID Connect (OIDC) providers, such as Microsoft Entra ID and Okta to create a secure access management system for AI model interactions. The Guidance helps organizations deploy Claude Code, while maintaining strict control over AI resource access, seamlessly connecting to existing identity infrastructure and providing observability for developer productivity and usage patterns. By following the provided steps and best practices, organizations can establish a scalable, compliance-friendly approach to managing Claude Code deployments across large enterprises.

## Benefits

### Streamline enterprise AI access

Integrate Amazon Bedrock seamlessly with your existing identity provider through OIDC federation. Maintain consistent access controls while leveraging your established authentication systems.

### Secure AI access with temporary credentials

Replace long-term access keys with temporary, session-based credentials for your AI workloads. Maintain enterprise security through standardized federation protocols.

### Automate security management

Leverage AWS managed services to handle authentication and credential management. Focus on building AI solutions while AWS handles the security infrastructure.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/claude-code-with-amazon-bedrock.pdf)

![Architecture diagram](/images/solutions/claude-code-with-amazon-bedrock/images/claude-code-with-amazon-bedrock-1.png)

1. **Step 1**: The credential process initiates authentication with an OpenID Connect (OIDC) provider.
1. **Step 2**: The OIDC provider returns an ID token after user authentication.
1. **Step 3**: Submit the OIDC token to Amazon Cognito identity pool.
1. **Step 4**: Amazon Cognito calls AssumeRoleWithWebIdentity on AWS Identity Access Management (IAM) and AWS Security Token Service (AWS STS).
1. **Step 5**: IAM and AWS STS return temporary AWS credentials with session tags.
1. **Step 6**: Amazon Cognito returns credentials to the credential process.
1. **Step 7**: Claude Code uses temporary credentials to call Amazon Bedrock.
1. **Step 8**: Amazon Bedrock returns the AI model response to Claude Code.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock)

[Read usage guidelines](/solutions/guidance-disclaimers/)
