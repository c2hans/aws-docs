---
source_url: https://docs.aws.amazon.com//solutions/account-assessment-for-aws-organizations//index.html
---

# Account Assessment for AWS Organizations

Investigate resource-based policy dependencies for your AWS Organizations accounts

- **Version**: 1.1.12
- **Released**: 7/2026
- **Author**: AWS
- **Est. deployment time**: 30 mins
- **Estimated cost**: [See details](/solutions/latest/account-assessment-for-aws-organizations/plan-your-deployment.html)

## Overview

Account Assessment for AWS Organizations allows you to centrally manage and evaluate all AWS accounts within your AWS Organizations, helping you to better understand and navigate the dependencies of AWS Organizations. The process to manually evaluate AWS Organizations dependencies can be time consuming—potentially involving reviews of tens or even hundreds of AWS resources of individual accounts. Now, you can run three types of scans to find delegated administrator accounts, identity-based and resource-based policies, and AWS services that have trusted access enabled for your AWS Organizations—all from a simple UI.

## Benefits

### Intuitive web UI

View, examine, and troubleshoot your scan results in an intuitive web UI.

### Compatible with over 25 AWS services

Use more than 25 AWS services enabled with trusted access to perform operations across all of the AWS accounts in your AWS Organizations.

### Three types of scans

Scan for resource-based policies, delegated admin accounts, and trusted access with the web UI.

## How it works

You can automatically deploy this architecture using the implementation guide and the accompanying AWS CloudFormation template.

[View implementation guide](/solutions/latest/account-assessment-for-aws-organizations/solution-overview.html)

![Architecture diagram](/images/solutions/account-assessment-for-aws-organizations/images/account-assessment-for-aws-organizations-1.png)

1. **Step 1**: Users access the solution by opening the Amazon CloudFront url in their browser . CloudFront delivers the web UI content from an Amazon S3 bucket.
1. **Step 2**: The Amazon S3 bucket hosts the web UI files and assets.
1. **Step 3**: When the web UI is loaded, it redirects the user to the Amazon Cognito hosted login form. On successful login, Cognito grants a user access token that is stored on the client.
1. **Step 4**: On the web UI an authenticated user can view the results of previous scans and a history of scans. To load this data or start scans, the web UI sends http requests to the solution’s API. An AWS Web Application Firewall (WAF) protects the application programming interfaces (APIs) from attacks. By default this solution uses AWS managed rule sets for the WAF. You can modify the firewall rules according to your needs via the AWS Console. The WAF also limits API access to a range of IP addresses that you define as a deployment parameter when deploying the solution.
1. **Step 5**: An Amazon API Gateway provides the solution’s API layer.
1. **Step 6**: The Cognito Authorizer attached to the API Gateway will validate the access token in each incoming request against Amazon Cognito.
1. **Step 7**: The API Gateway routes each request to the responsible AWS Lambda function. The solution contains one Lambda function per read operation as well as one Lambda function to start Delegated Admin scans and Trusted Access scans respectively.
1. **Step 8**: To serve the results of a scan to the web UI, a Lambda function loads the data from the DynamoDB.
1. **Step 9**: To scan for Delegated Admin Accounts or Trusted access, a Lambda function assumes the IAM role deployed by the OrgManagement stack of this solution. Then it will call the AWS Organizations API in the organization management account. It stores the results in DynamoDB.
1. **Step 10**: While Delegated Admin scans and trusted access scans are started on demand through the web UI and API Gateway, the scan for policies is supposed to run once per day. For that purpose, an Amazon EventBridge rule triggers the Policy Scan Lambda function on a daily schedule.
1. **Step 11**: The Policy Scan lambda function registers the start of a scan by writing an IN_PROGRESS record into DynamoDB, retrieves all active account ids from the AWS Organizations API, and passes the list of account ids to the Policy Scan Step Function.
1. **Step 12**: The Step Function orchestrates the subtasks for a Policy scan: - It first verifies for each account id that the Spoke Role can be assumed in that account. (The Spoke Role is deployed by the spoke template of this solution.) - For each verified account, and for each of the AWS Services to be scanned, it calls another Lambda functions to scan the given account and service in each region. - Once all accounts have been iterated, the Step Function calls the Finish Job Lambda function to update the job record in DynamoDB to SUCCESS, FAILED or SUCCESS_WITH_FAILURES.
1. **Step 13**: For each account and service, the Lambda function assumes the Spoke Role in the given account and calls the given service API once per region.
1. **Step 14**: The Lambda function It stores a representation of the retrieved resource-based, identity-based or service control policy objects in DynamoDB. Should the call to a service API fail, it stores a "failed task" object instead. The user can now use the Policy Explorer search form on the web UI to browse all stored policies.
## Deploy with confidence

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](/solutions/latest/account-assessment-for-aws-organizations/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Open the CloudFormation template in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.

[Launch in the AWS Console](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/account-assessment-for-aws-organizations/latest/account-assessment-for-aws-organizations-hub.template&redirectId=SolutionWeb)

## Deployment options

- **Implementation guide**: Follow the implementation guide for step-by-step actions to deploy this AWS Solution.

[Download guide](/pdfs/solutions/latest/account-assessment-for-aws-organizations/account-assessment-for-aws-organizations.pdf#solution-overview)

- **Source code**: The source code for this AWS Solution is available in GitHub.

[Go to GitHub](https://github.com/aws-solutions/account-assessment-for-aws-organizations)

- **CloudFormation template**: View or modify the CloudFormation template to customize your deployment.

[Download template](/solutions/latest/account-assessment-for-aws-organizations/deploy-the-solution.html)

## Related content

- **How do I move accounts between organizations in AWS Organizations?**: Identify some of the account, reporting, billing, and other considerations you will need to take when migrating accounts.

[Learn more](https://repost.aws/knowledge-center/organizations-move-accounts)

- **Migrating accounts between AWS Organizations with consolidated billing to all features**: Learn how to migrate our accounts configured with consolidated billing to a new organization that has all features.

[Learn more](https://aws.amazon.com/blogs/mt/migrating-accounts-between-aws-organizations-with-consolidated-billing-to-all-features/)

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/account-assessment-for-aws-organizations/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/account-assessment-for-aws-organizations/latest/rss.xml)
