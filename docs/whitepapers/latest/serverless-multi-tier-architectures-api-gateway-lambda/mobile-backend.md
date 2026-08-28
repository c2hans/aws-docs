---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/mobile-backend.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Mobile backend
<a name="mobile-backend"></a>

![Architectural pattern for serverless mobile backend](http://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/images/arch-pattern-serverless-mobile-backend.png)

* Architectural pattern for serverless mobile backend *

* Table 1 - Mobile backend tier components *

|  Tier  |  Components  |
| --- | --- |
|  Presentation  |  Mobile application running on a user device.  |
|  Logic  |  Amazon API Gateway with AWS Lambda. <br /> This architecture shows three exposed services (`/tickets`, `/shows`, and `/info`). API Gateway endpoints are secured by [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) In this method, users sign in to Amazon Cognito user pools (using a federated third-party if necessary), and receive access and ID tokens that are used to authorize API Gateway calls. <br /> Each Lambda function is assigned its own Identity and Access Management (IAM) role to provide access to the appropriate data source.  |
|  Data  |  DynamoDB is used for the `/tickets` and `/shows` services. <br /> Amazon RDS is used for the `/info` service. This Lambda function retrieves Amazon RDS credentials from AWS Secrets Manager and uses an elastic network interface to access the private subnet.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
