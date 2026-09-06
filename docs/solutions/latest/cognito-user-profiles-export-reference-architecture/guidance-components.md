---
source_url: https://docs.aws.amazon.com/solutions/latest/cognito-user-profiles-export-reference-architecture/guidance-components.html
---

# Guidance components
<a name="guidance-components"></a>

## Export workflow
<a name="export-workflow"></a>

The `ExportWorkflow` AWS Step Functions workflow is invoked on a set schedule. This guidance includes a parameter to run the workflow daily, weekly, or every 30 days. If you prefer another schedule, you can modify the schedule in the Amazon CloudWatch console after launching this guidance.

The `ExportWorkflow` Step Functions workflow interrogates your primary user pool and performs the following actions:
+ Lists all users in the primary user pool and refreshes the `BackupTable` DynamoDB table with updated user profile information (such as standard and custom attributes, and the user enabled flag), and adds new users.
+ Lists all groups in the primary user pool and refreshes the `BackupTable` DynamoDB table with updated group information (such as group description and precedence value), and adds new groups.
+ Lists all users in each group to identify new group members, and users that are no longer members of a group, and updates the `BackupTable` DynamoDB table accordingly.
+ Checks the `BackupTable` DynamoDB table for records that were not updated during this run of `ExportWorkflow` Step Functions workflow. These records will be removed from the `BackupTable` DynamoDB table.

## Backup table
<a name="backup-table"></a>

The `BackupTable` DynamoDB table is a global table with a replica in your backup AWS Region. When data changes in the table, DynamoDB asynchronously replicates that data to the replica in your backup Region. The guidance exports the user profile, group, and group membership information to the backup Amazon DynamoDB table on a set schedule.

In the primary Region, the `BackupTable` DynamoDB table is configured to enable DynamoDB Point-in-Time Recovery, which enables you to restore the `BackupTable` DynamoDB table to any point in time during the last 35 days. For more information, refer to [Point-in-Time Recovery for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html).

## Import workflow
<a name="import-workflow"></a>

The `ImportWorkflow` Step Functions workflow populates an empty user pool with user profiles, groups, and group memberships from the DynamoDB global table. You must run the `ImportWorkflow` Step Functions workflow on demand in either the primary or backup Region. When starting the execution, you must supply a JSON object as input and supply the ID for the new user pool in the `NewUserPoolId` property.

![Amazon Cognito NewUserPoolId property](http://docs.aws.amazon.com/solutions/latest/cognito-user-profiles-export-reference-architecture/images/cognito-NewUserPoolId-property.png)

The `ImportWorkflow` Step Functions workflow first checks that the new user pool does not have any groups or users before proceeding. If the user pool is not empty, the `ImportWorkflow` Step Functions workflow will be halted.

 **Note:** When a user profile is created in the new user pool, it is assigned a new Amazon Cognito generated unique ID (the sub attribute). Additionally, user passwords are not replicated by this guidance. Refer to [Limitations](#limitations) for more details.

## Limitations
<a name="limitations"></a>

### Passwords
<a name="passwords"></a>

This guidance does not back up user passwords to DynamoDB. When signing in to the new user pool that was populated with the `ImportWorkflow` Step Functions workflow, users will be required to [reset their passwords](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool-password-reset.html).

### Multi-factor authentication
<a name="multi-factor-authentication"></a>

This guidance does not support user pools with multi-factor authentication (MFA) enabled. When this guidance is deployed, it checks the primary user pool’s MFA setting and, if the setting is either optional or required, this guidance will not launch. This guidance also performs this check every time the `ExportWorkflow` Step Functions workflow is run and, if MFA has been enabled, the workflow will terminate. MFA is not supported because this guidance is unable to replicate an end-user’s MFA token that is used to configure time-based one-time passwords (TOTP) as a second factor.

### Cognito sub attribute
<a name="cognito-sub-attribute"></a>

The `ImportWorkflow` Step Functions workflow will create new users in the empty user pool and synchronize their user profiles with the current state in the backup DynamoDB table. These new users will be assigned new Cognito-generated unique IDs (the `sub` attribute). If your application is using this value to uniquely identify a user, we recommend that you copy this value to a new custom attribute in the primary user pool. This attribute will be exported to DynamoDB and available in the new user pool when the `ImportWorkflow` Step Functions workflow runs.

### Federated users
<a name="federated-users"></a>

Users who have signed in to your user pool using a third-party identity provider will not have profiles exported to DynamoDB. These users will be created in the new user pool when they next log in through the third-party identity provider. This means that custom attributes for federated users will not be exported by this guidance, and the federated user will get a new value for the `sub` attribute when they log in to the new user pool.

### Cognito advanced security features
<a name="cognito-advanced-security-features"></a>

When evaluating users as part of Cognito’s [advanced security features](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html), the user history is not exported by this guidance and therefore will not be available in the new user pool.

### Username attributes
<a name="username-attributes"></a>

When a user pool is initially created, you can allow users the choice of using either an email address or a phone number as their username. However, this guidance does not support user pools that are configured to allow both email addresses and phone numbers.

### Group roles
<a name="group-roles"></a>

AWS Identity and Access Management (IAM) roles associated with groups are not exported by this guidance. If you have an IAM role attached to a group, you must create a similar role or associate that role with the group in the new user pool.

### Tracked devices
<a name="tracked-devices"></a>

This guidance does not export [tracked devices](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html) to the `BackupTable` DynamoDB table. As such, if you use the `ImportWorkflow` Step Functions workflow to populate a new user pool, there will be no tracked devices associated with the imported user profiles.
