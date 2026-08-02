---
source_url: https://docs.aws.amazon.com/solutions/latest/cognito-user-profiles-export-reference-architecture/overview.html
---

# Build a framework for exporting user profile and group information from your Amazon Cognito user pools
<a name="overview"></a>

This implementation guide discusses architectural considerations and configuration steps for deploying the Cognito User Profiles Export Reference Architecture Guidance in the Amazon Web Services (AWS) Cloud.

The guide is intended for IT infrastructure architects, administrators, and DevOps professionals who have practical experience architecting in the AWS Cloud.

Many Amazon Web Services (AWS) customers use [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) to provide a scalable and secure user directory for their applications. [Amazon Cognito](https://aws.amazon.com/cognito/) customers often need to export their users to facilitate more complex user queries, or to provide resiliency in case of regional failure or accidental deletion of their users. To assist with this, AWS offers the Cognito User Profiles Export Reference Architecture Guidance. This Guidance is designed to provide a framework for exporting user profile and group information from your user pool, allowing you to focus on extending this guidance’s functionality rather than managing the underlying infrastructure operation.

This guidance uses an `ExportWorkflow` [AWS Step Functions](https://aws.amazon.com/step-functions/) workflow to periodically export user profiles, groups, and group membership details from your user pool to an [Amazon DynamoDB global table](https://aws.amazon.com/dynamodb/global-tables/) with automatic, asynchronous replication to a backup Region for added resiliency.

This guidance’s `ImportWorkflow` Step Functions workflow can be used to populate a new, empty user pool with data from the global table, allowing you to easily recover user profiles, groups, and group memberships. The `ImportWorkflow` Step Functions workflow can be run in either the primary or backup Region.

Customers interested in using this guidance for both backup and recovery should be comfortable with a Recovery Time Objective (RTO) measured in hours rather than minutes since the guidance requires the `ImportWorkflow` Step Functions workflow to run in a recovery scenario. Refer to [Cognito transactions per second (TPS)](design-considerations.md#cognito-transactions-per-second-tps) for performance benchmarks for different sized user pools.

The Recovery point objective (RPO) is determined by the time the `ExportWorkflow` Step Functions workflow runs in the primary Region. You will lose any updates made after the last `ExportWorkflow` Step Functions workflow run.

## Limitations
<a name="limitations1"></a>

Customers interested in using this guidance should be aware that it does not export sensitive information, such as user passwords; that user pools with multi-factor authentication (MFA) enabled are not supported; and that advanced security features are not supported. For a full list of limitations, refer to [Limitations](guidance-components.md#limitations) in the guidance components section.
