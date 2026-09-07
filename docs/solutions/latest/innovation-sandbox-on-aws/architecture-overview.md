---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters builds the following environment in your AWS account.

![Innovation Sandbox on AWS high-level architecture diagram](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/diagrams/high-level.drawio.png)

**Innovation Sandbox on AWS architecture**
The high-level process flow for the solution components deployed with the AWS CloudFormation templates is as follows:

1. Users sign in to the solution through an [Amazon Cognito](https://aws.amazon.com/cognito/) user pool that federates to [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) using SAML 2.0. You can configure IAM Identity Center to use its built-in user store or integrate it with an external identity provider such as Okta or Microsoft Entra ID.

1. The web User Interface (UI) is hosted in an [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution backed by an [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) bucket that serves the web frontend, including the HTML pages, CSS stylesheets, and JavaScript code. Amazon Cognito provides the authentication layer, issuing tokens that the web UI uses to obtain temporary IAM credentials.

1. The web UI signs each API request with AWS Signature Version 4 (SigV4) using credentials from the Amazon Cognito identity pool, then calls [Amazon API Gateway](https://aws.amazon.com/api-gateway/) REST API resources. [AWS WAF](https://aws.amazon.com/waf/) protects the API Gateway from common exploits, and API Gateway authorizes requests natively using IAM authorization. The backend [AWS Lambda](https://aws.amazon.com/lambda/) functions enforce role-based access based on identities assigned to user groups in IAM Identity Center.

1. AWS Lambda functions handle API requests by reading and writing status and configuration data to [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) tables. These tables store the solution’s global settings (lease preferences, account cleanup settings, email notification settings, maintenance mode) and all operational data (leases, accounts, templates, principals).

1. AWS Lambda functions manage the lifecycle of accounts using the [AWS Organizations](https://aws.amazon.com/organizations/) API, moving them between organizational units (OUs) based on account status. [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) attached to OUs restrict which services and resources sandbox users can access.

1. The solution’s backend includes an event-driven architecture built on [Amazon EventBridge](https://aws.amazon.com/eventbridge/) for routing domain events. The solution monitors sandbox account leases for breaches in configured budget and duration thresholds, and publishes events that trigger email notifications via [Amazon Simple Email Service](https://aws.amazon.com/ses/) and invoke Lambda functions responsible for lease and account lifecycle management.

1.  [AWS Step Functions](https://aws.amazon.com/step-functions/) orchestrates complex, multi-step workflows including blueprint deployment and assignment processing. Step Functions coordinates the sequencing, retries, and error handling for these long-running operations.

1. A durable AWS Lambda function orchestrates account cleanup by invoking an [AWS CodeBuild](https://aws.amazon.com/codebuild/) project that runs [AWS Nuke](https://aws-nuke.ekristen.dev/) to delete all user-created resources in sandbox accounts. After cleanup completes, the solution validates that the account is clean and either returns it to the available pool or moves it to quarantine for manual investigation.

1.  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) stores all compute logs with a 90-day retention. Logs are automatically archived to Amazon S3 for long-term retention following a multi-tier strategy (S3 Standard for one year, then S3 Glacier for additional years).

1.  [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) stores the account cleanup configuration, including the AWS Nuke resource filter that AWS CodeBuild reads at the start of each cleanup run, and the post-cleanup validation exclusion list. Administrators manage these configurations through the AWS AppConfig console.

1. Users access assigned sandbox accounts via the IAM Identity Center access portal console, or programmatically using credentials. The solution provides a direct link in the web UI to access the AWS account with Single Sign-On (SSO).
