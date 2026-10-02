---
source_url: https://docs.aws.amazon.com/solutions/user-profiles-export-with-amazon-cognito/index.html
---

---
title: 'Guidance for User Profiles Export with Amazon Cognito'
canonical_url: https://docs.aws.amazon.com/solutions/user-profiles-export-with-amazon-cognito/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for User Profiles Export with Amazon Cognito

## Overview

This Guidance demonstrates how to export Amazon Cognito user information efficiently, enabling advanced queries and enhancing data resiliency. It provides a robust framework for extracting user profile and group details from an Amazon Cognito user pool, safeguarding against regional failures or accidental deletions. The Guidance automates the export process, allowing you to focus on extending functionality rather than managing infrastructure. With a scalable and secure approach to backing up critical user data, you can enable business continuity and compliance while also optimizing user management strategies and maintaining control over Amazon Cognito user data.

## Benefits

### Ensure business continuity with user data resilience

Protect your application's user base with automated backup and recovery capabilities across AWS Regions. Maintain seamless access to user profiles even during regional disruptions.

### Streamline user profile management operations

Automate the export and synchronization of user profiles, groups, and memberships using serverless workflows. Reduce operational overhead while maintaining data consistency across regions.

### Enhance troubleshooting with detailed insights

Leverage comprehensive logging and notification systems to quickly identify and resolve user profile management issues. Maintain operational excellence with automated error tracking and reporting.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/user-profiles-export-with-amazon-cognito.pdf)

![Architecture diagram](/images/solutions/user-profiles-export-with-amazon-cognito/images/user-profiles-export-with-amazon-cognito-1.png)

1. **Step 1**: In the primary AWS Region, an Amazon CloudWatch scheduled event invokes the AWS Step Functions export workflow, which examines the primary Amazon Cognito user pool. It stores user profiles, groups, and group membership information in the global table. Note: This Guidance does not create the primary user pool.
1. **Step 2**: When the export workflow is complete, Step Functions sends a completion or error message to the Amazon Simple Notification Service (Amazon SNS) topic for logging or troubleshooting.
1. **Step 3**: Amazon DynamoDB asynchronously replicates all data to the backup Region for added resiliency.
1. **Step 4**: In your backup Region, use the same Step Functions import workflow as seen in Step 2 to import data from global table to populate a new, empty Amazon Cognito user pool. This enables you to easily recover user profiles, groups, and group memberships. Note: This Guidance does not create the new user pool.
1. **Step 5**: A mapping comma-separated values (CSV) file uploads to the solution's Amazon Simple Storage Service (Amazon S3) bucket. This CSV file maps the line number reported by Amazon Cognito to the subattribute of the corresponding users for inclusion in the troubleshooting error message.
1. **Step 6**: When the import workflow is complete, Step Functions sends a completion or error message to an Amazon SNS topic for logging or troubleshooting.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](/solutions/latest/cognito-user-profiles-export-reference-architecture/overview.html)

## Related content

- **Sample code**: This sample code shows how to export user profile and group information from your Amazon Cognito user pool.

[Learn more](https://github.com/aws-samples/sample-cognito-user-profiles-export-reference-architecture)

[Read usage guidelines](/solutions/guidance-disclaimers/)
