---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters deploys the following components in your AWS account.

![Graphic depicting Account Assessment for AWS Organizations architecture](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/account-assessment-for-aws-orgs-architecture-diagram.png)

1. Users access the solution by opening the [Amazon CloudFront url in their browser](https://aws.amazon.com/cloudfront/). CloudFront delivers the web UI content from an Amazon S3 bucket.

1. The Amazon S3 bucket hosts the web UI files and assets.

1. When the web UI is loaded, it redirects the user to the Amazon Cognito hosted login form. On successful login, Cognito grants a user access token that is stored on the client.

1. On the web UI an authenticated user can view the results of previous scans and a history of scans. To load this data or start scans, the web UI sends http requests to the solution’s API. An AWS Web Application Firewall (WAF) protects the application programming interfaces (APIs) from attacks. By default this solution uses AWS managed rule sets for the WAF. You can modify the firewall rules according to your needs via the AWS Console. The WAF also limits API access to a range of IP addresses that you define as a deployment parameter when deploying the solution.

1. An Amazon API Gateway provides the solution’s API layer.

1. The Cognito Authorizer attached to the API Gateway will validate the access token in each incoming request against Amazon Cognito.

1. The API Gateway routes each request to the responsible [AWS Lambda](https://aws.amazon.com/lambda/) function. The solution contains one Lambda function per read operation as well as one Lambda function to start Delegated Admin scans and Trusted Access scans respectively.

1. To serve the results of a scan to the web UI, a Lambda function loads the data from the DynamoDB.

1. To scan for Delegated Admin Accounts or Trusted access, a Lambda function assumes the IAM role deployed by the OrgManagement stack of this solution. Then it will call the AWS Organizations API in the organization management account. It stores the results in DynamoDB.

1. While Delegated Admin scans and trusted access scans are started on demand through the web UI and API Gateway, the scan for policies is supposed to run once per day. For that purpose, an Amazon EventBridge rule triggers the Policy Scan Lambda function on a daily schedule.

1. The Policy Scan lambda function registers the start of a scan by writing an IN\_PROGRESS record into DynamoDB, retrieves all active account ids from the AWS Organizations API, and passes the list of account ids to the Policy Scan Step Function.

1. The Step Function orchestrates the subtasks for a Policy scan:
   + It first verifies for each account id that the Spoke Role can be assumed in that account. (The Spoke Role is deployed by the spoke template of this solution.)
   + For each verified account, and for each of the AWS Services to be scanned, it calls another Lambda functions to scan the given account and service in each region.
   + Once all accounts have been iterated, the Step Function calls the Finish Job Lambda function to update the job record in DynamoDB to SUCCESS, FAILED or SUCCESS\_WITH\_FAILURES.

1. For each account and service, the Lambda function assumes the Spoke Role in the given account and calls the given service API once per region.

1. The Lambda function It stores a representation of the retrieved resource-based, identity-based or service control policy objects in DynamoDB. Should the call to a service API fail, it stores a "failed task" object instead. The user can now use the Policy Explorer search form on the web UI to browse all stored policies.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account Assessment for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
