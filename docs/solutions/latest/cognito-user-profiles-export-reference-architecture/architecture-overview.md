---
source_url: https://docs.aws.amazon.com/solutions/latest/cognito-user-profiles-export-reference-architecture/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

Deploying this guidance with the default parameters builds the following environment in the AWS Cloud.

 **Cognito User Profiles Export Reference Architecture architecture on AWS**

![user profiles export with amazon cognito](https://docs.aws.amazon.com/solutions/latest/cognito-user-profiles-export-reference-architecture/images/user-profiles-export-with-amazon-cognito.png)

1. In the primary AWS Region, an [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) scheduled [event](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) invokes the [AWS Step Functions](https://aws.amazon.com/step-functions/) export workflow, which examines the primary [Amazon Cognito](https://aws.amazon.com/cognito/) user pool. It stores user profiles, groups, and group membership information in the global table.

    *Note: This Guidance does not create the primary user pool.*

1. When the export workflow is complete, Step Functions sends a completion or error message to the [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/) topic for logging or troubleshooting.

1.  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) asynchronously replicates all data to the backup Region for added resiliency.

1. In your backup Region, use the same Step Functions import workflow as seen in Step 2 to import data from global table to populate a new, empty Amazon Cognito user pool. This enables you to easily recover user profiles, groups, and group memberships.

    *Note: This Guidance does not create the new user pool.*

1. A mapping comma-separated values (CSV) file uploads to the guidance’s [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) bucket. This CSV file maps the line number reported by Amazon Cognito to the subattribute of the corresponding users for inclusion in the troubleshooting error message.

1. When the import workflow is complete, Step Functions sends a completion or error message to an Amazon SNS topic for logging or troubleshooting.
