---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters builds the following environment in your AWS account.

![high level.drawio](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/high-level.drawio.png)

**Innovation Sandbox on AWS architecture**
The high-level process flow for the solution components deployed with the AWS CloudFormation templates is as follows:

1. Users access the solution (SAML2.0 application) using [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) authentication. You can configure IAM Identity Center to use its own internal user store, or integrate it with an external identity provider such as Okta or Microsoft Entra ID.

1. The web User Interface (UI) is hosted in an [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution. It uses an [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) bucket to host and serve the web frontend, including the HTML pages, CSS stylesheets, and the JavaScript code.

1. The web UI calls [Amazon API Gateway](https://aws.amazon.com/api-gateway/) REST API resources (resource, method, model) to fetch and mutate the solution data. [AWS Lambda](https://aws.amazon.com/lambda/) functions authorize the requests using role-based access, based on identities assigned by solution administrators to user groups in IAM Identity Center. [AWS WAF](https://aws.amazon.com/waf/) protects the Amazon API Gateway from common exploits and bots that can affect availability, compromise security, or consume excessive resources.

1. AWS Lambda functions handle the API requests by reading, and writing status and configuration data to an [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) table. These Lambda functions also fetch global configurations from [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) to manage solution parameters including lease preferences, account cleanup setting, customer worded "terms of service", and auth configurations.

1. AWS Lambda functions manage the lifecycle of accounts using the [AWS Organizations](https://aws.amazon.com/organizations/) API, and move them between organizational units (OUs) based on the account status. [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) attached to OUs prevent sensitive, expensive, or difficult to clean up services and resources from being used by sandbox users.

1. The solution’s backend includes an event-based architecture built on [Amazon EventBridge](https://aws.amazon.com/eventbridge/) for routing events. The solution monitors sandbox account leases using AWS Lambda for breaches in configured lease budget and duration thresholds and creates events that produce email notifications via [Amazon Simple Email Service](https://aws.amazon.com/ses/) and invoke Lambda functions that are responsible for the management of lease and account lifecycle.

1. Accounts going through the onboarding process or leases being terminated will invoke the account cleanup [AWS Step Functions](https://aws.amazon.com/step-functions/), which is responsible for recycling the accounts back into the account pool, ready for reuse.

1. AWS Step Functions run an [AWS CodeBuild](https://aws.amazon.com/codebuild/) project responible for deleting resources in the account. AWS Lambda functions monitor active account leases and issues actions such as moving an AWS account between Organizational Units (OUs), attaching/detaching an IAM Identity Center permission set to the account giving user access, or initiating the cleanup of an AWS account which deletes all user-created resources using [AWS Nuke](https://aws-nuke.ekristen.dev/).
   + If the clean up process is successful, the account is moved to the **available** account pool, or
   + If some resources cannot be deleted, the account is moved to a **quarantine** state, for manual investigation and remediation.

1. Users access assigned sandbox accounts via IAM Identity Center access portal console, or programmtically using credentials. The solution provides a link in the web UI to directly access the AWS account with Single Sign-On (SSO).
