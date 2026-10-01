---
source_url: https://docs.aws.amazon.com//solutions/account-assessment-for-aws-organizations//index.html
---

---
title: 'Guidance for Account Assessment for AWS Organizations'
canonical_url: https://docs.aws.amazon.com/solutions/account-assessment-for-aws-organizations/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Account Assessment for AWS Organizations

## Overview

This Guidance helps organizations gain visibility into complex AWS Organizations dependencies by automatically discovering trusted access enabled services, delegated administrator accounts, and identity-based and resource-based policies across multiple accounts. The system provides a web-based interface where users can initiate scans and view historical results of their AWS Organizations configuration. On-demand scans identify delegated admin accounts and trusted access services, while daily automated scans discover policies across all active accounts and regions. The policy explorer allows teams to search and browse all discovered policies, making it easier to understand cross-account dependencies and service relationships within large, multi-account environments. You can reduce security risks, accelerate compliance audits, and simplify organizational governance by gaining complete visibility into policy dependencies and service configurations across your entire AWS Organizations structure.

## Benefits

### Gain cross-account policy visibility

Assess resource-based, identity-based, and service control policies across your entire AWS Organizations environment through a single web-based interface, eliminating manual account-by-account audits.

### Automate organization-wide security assessments

Run daily automated policy scans across all member accounts and regions using serverless orchestration, reducing manual effort and ensuring continuous governance without operational overhead.

### Centralize delegated access tracking

Identify delegated administrator configurations and trusted access settings across your organization in near real-time, helping you detect unexpected permissions and maintain least-privilege compliance.

## How it works

This architecture diagram illustrates how to effectively support Account Assessment for AWS Organizations. It shows the key components and their interactions, providing an overview of the architecture's structure and functionality. [Download the architecture diagram](downloads/account-assessment-for-aws-organizations.pdf)

![Architecture diagram for Account Assessment for AWS Organizations](/images/solutions/account-assessment-for-aws-organizations/images/account-assessment-for-aws-organizations.png)

1. **Step 1**: Users access the Guidance by opening the Amazon CloudFront URL in their browser. CloudFront delivers the web UI content from an Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 2**: The Amazon S3 bucket hosts the web UI files and assets.
1. **Step 3**: When the web UI is loaded, it redirects the user to the Amazon Cognito hosted login form. On successful login, Cognito grants a user access token that is stored on the client.
1. **Step 4**: On the web UI an authenticated user can view the results of previous scans and a history of scans. To load this data or start scans, the web UI sends http requests to the Guidance API. An AWS Web Application Firewall (WAF) protects the application programming interfaces (APIs) from attacks. By default this Guidance uses AWS managed rule sets for the WAF. You can modify the firewall rules according to your needs via the AWS Console. The WAF also limits API access to a range of IP addresses that you define as a deployment parameter when deploying the Guidance.
1. **Step 5**: An Amazon API Gateway provides the Guidance's API layer.
1. **Step 6**: The Cognito Authorizer attached to the API Gateway will validate the access token in each incoming request against Amazon Cognito.
1. **Step 7**: The API Gateway routes each request to the responsible AWS Lambda function. The Guidance contains one Lambda function per read operation as well as one Lambda function to start Delegated Admin scans and Trusted Access scans respectively.
1. **Step 8**: To serve the results of a scan to the web UI, a Lambda function loads the data from Amazon DynamoDB.
1. **Step 9**: To scan for Delegated Admin Accounts or Trusted access, a Lambda function assumes the IAM role deployed by the OrgManagement stack. Then it will call the AWS Organizations API in the organization management account. It stores the results in DynamoDB.
1. **Step 10**: While Delegated Admin scans and trusted access scans are started on demand through the web UI and API Gateway, the scan for policies is supposed to run once per day. For that purpose, an Amazon EventBridge rule triggers the Policy Scan Lambda function on a daily schedule.
1. **Step 11**: The Policy Scan Lambda function registers the start of a scan by writing an IN_PROGRESS record into DynamoDB, retrieves all active account ids from the AWS Organizations API, and passes the list of account ids to the Policy Scan Step Function.
1. **Step 12**: The Step Function orchestrates the subtasks for a Policy scan: - It first verifies for each account id that the Spoke Role can be assumed in that account. (The Spoke Role is deployed by the spoke template of this Guidance.) - For each verified account, and for each of the AWS Services to be scanned, it calls another Lambda function to scan the given account and service in each region. - Once all accounts have been iterated, the Step Function calls the Finish Job Lambda function to update the job record in DynamoDB to SUCCESS, FAILED, or SUCCESS_WITH_FAILURES.
1. **Step 13**: For each account and service, the Lambda function assumes the Spoke Role in the given account and calls the given service API once per region.
1. **Step 14**: The Lambda function stores a representation of the retrieved resource-based, identity-based or service control policy objects in DynamoDB. Should the call to a service API fail, it stores a "failed task" object instead. The user can now use the Policy Explorer search form on the web UI to browse all stored policies.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/account-assessment-for-aws-organizations)

## Related content

- **How do I move accounts between organizations in AWS Organizations?**: Identify some of the account, reporting, billing, and other considerations you will need to take when migrating accounts.

[Learn more](https://repost.aws/knowledge-center/organizations-move-accounts)

- **Migrating accounts between AWS Organizations with consolidated billing to all features**: Learn how to migrate our accounts configured with consolidated billing to a new organization that has all features.

[Learn more](https://aws.amazon.com/blogs/mt/migrating-accounts-between-aws-organizations-with-consolidated-billing-to-all-features/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
