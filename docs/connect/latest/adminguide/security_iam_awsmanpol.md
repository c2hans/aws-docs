---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html
---

# AWS managed policies for Connect Customer
<a name="security_iam_awsmanpol"></a>

To add permissions to users, groups, and roles, it is more efficient to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) policies that provide your team with only the permissions that they need. To get started quickly, you can use AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the ReadOnlyAccess AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AmazonConnect\_FullAccess
<a name="AmazonConnect_FullAccess-policy"></a>

To allow full read/write access to Connect Customer, you must attach two policies to your IAM users, groups, or roles. Attach the `AmazonConnect_FullAccess` policy and a custom policy to have full access to Connect Customer.

To view the permissions for the `AmazonConnect_FullAccess` policy, see [AmazonConnect\_FullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonConnect_FullAccess.html) in the *AWS Managed Policy Reference*.

**Custom Policy**

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AttachAnyPolicyToAmazonConnectRole",
            "Effect": "Allow",
            "Action": "iam:PutRolePolicy",
            "Resource": "arn:aws:iam::*:role/aws-service-role/connect.amazonaws.com/AWSServiceRoleForAmazonConnect*"
        }
    ]
}
```

------

To allow a user to create an instance, ensure that they have the permissions granted by the `AmazonConnect_FullAccess` policy.

When you use `AmazonConnect_FullAccess` policy, note the following:
+ The custom policy that contains the `iam:PutRolePolicy` action, allows the user with this policy assigned to configure any resource in the account to work with an Connect Customer instance. Since this added action grants such broad permissions, only assign it when necessary. As an alternative, you can create the service-linked role with access to the necessary resources and let the user have access to pass the service-linked role to Connect Customer (which is granted by the `AmazonConnect_FullAccess` policy).
+ Additional privileges are required to create a Amazon S3 bucket with a name of your choosing, or use an existing bucket while creating or updating an instance from the Connect Customer admin website. If you choose default storage locations for your call recordings, chat transcripts, call transcripts, and other data, the system prepends "amazon-connect-" to the names of those objects.
+ The aws/connect KMS key is available to use as a default encryption option. To use a custom encryption key, assign users additional KMS privileges.
+ Assign users additional privileges to attach other AWS resources like Amazon Polly, Live Media Streaming, Data Streaming, and Lex bots to their Connect Customer instances.

For more information and detailed permissions, see [Required permissions for using custom IAM policies to manage access to the Connect Customer console](security-iam-amazon-connect-permissions.md).

## AWS managed policy: AmazonConnectReadOnlyAccess
<a name="amazonconnectreadonlyaccess-policy"></a>

To allow read-only access, you can attach the `AmazonConnectReadOnlyAccess` policy.

To view the permissions for this policy, see [AmazonConnectReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonConnectReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonConnectServiceLinkedRolePolicy
<a name="amazonconnectservicelinkedrolepolicy"></a>

This policy is attached to the service-linked role named `AWSServiceRoleForAmazonConnect` to allow Connect Customer to perform various actions on specified resources. As you enable additional features in Connect Customer, additional permissions are added for the [AWSServiceRoleForAmazonConnect](https://docs.aws.amazon.com/connect/latest/adminguide/connect-slr.html#slr-permissions) service-linked role to access the resources associated with those features.

To view the permissions for this policy, see [AmazonConnectServiceLinkedRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonConnectServiceLinkedRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonConnectCampaignsServiceLinkedRolePolicy
<a name="amazonconnectcampaignsservicelinkedrolepolicy"></a>

The `AmazonConnectCampaignsServiceLinkedRolePolicy` role permissions policy allows Connect Customer outbound campaigns to perform various actions on specified resources. As you enable additional features in Connect Customer, additional permissions are added for the [AWSServiceRoleForConnectCampaigns](https://docs.aws.amazon.com/connect/latest/adminguide/connect-slr-outbound.html#slr-permissions-outbound) service-linked role to access the resources associated with those features.

To view the permissions for this policy, see [AmazonConnectCampaignsServiceLinkedRolePolicy ](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonConnectCampaignsServiceLinkedRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonConnectVoiceIDFullAccess
<a name="amazonconnectvoiceidfullaccesspolicy"></a>

To allow full access to Connect Customer Voice ID, you must attach two policies to your users, groups, or roles. Attach the `AmazonConnectVoiceIDFullAccess` policy and a custom policy to access Voice ID through the Connect Customer admin website.

To view the permissions for the `AmazonConnectVoiceIDFullAccess` policy, see [AmazonConnectVoiceIDFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonConnectVoiceIDFullAccess.html) in the *AWS Managed Policy Reference*.

**Custom policy**

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AttachAnyPolicyToAmazonConnectRole",
            "Effect": "Allow",
            "Action": "iam:PutRolePolicy",
            "Resource": "arn:aws:iam::*:role/aws-service-role/connect.amazonaws.com/AWSServiceRoleForAmazonConnect*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "connect:CreateIntegrationAssociation",
                "connect:DeleteIntegrationAssociation",
                "connect:ListIntegrationAssociations"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "events:DeleteRule",
                "events:PutRule",
                "events:PutTargets",
                "events:RemoveTargets"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "events:ManagedBy": "connect.amazonaws.com"
                }
            }
        }
    ]
}
```

------

The custom policy configures the following:
+ The `iam:PutRolePolicy` allows the user who gets that policy to configure any resource in the account to work with the Connect Customer instance. Due to its broad scope, grant this permission only when absolutely necessary.
+ Attaching a Voice ID domain to an Connect Customer instance requires additional Connect Customer and Amazon EventBridge permissions. You need permissions to call Connect Customer APIs for creating, deleting, and listing integration associations. Additionally, EventBridge permissions are required to create and delete rules that provide contact records related to Voice ID.

Connect Customer Voice ID does not have a default encryption option, so you must allow the following API operations in the key policy to use your customer-managed key. Additionally, you need to grant these permissions on the relevant key, as they are not included in the managed policy.
+ `kms:Decrypt` - to access or store encrypted data.
+ `kms:CreateGrant` – when creating or updating a domain, used to create a grant to the customer managed key for the Voice ID domain. The grant controls access to the specified KMS key which allows access to [grant operations](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#terms-grant-operations) Connect Customer Voice ID requires. For more information about using grants, see [Using grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) in the *AWS Key Management Service Developer Guide*.
+ `kms:DescribeKey` – when creating or updating a domain, allows determining the ARN for KMS key you provided.

For more about creating domains and KMS keys, see [Get started enabling Voice ID in Connect Customer](enable-voiceid.md) and [Encryption at rest in Connect Customer](encryption-at-rest.md).

## AWS managed policy: CustomerProfilesServiceLinkedRolePolicy
<a name="customerprofilesservicelinkedrolepolicy"></a>

The `CustomerProfilesServiceLinkedRolePolicy` role permissions policy allows Connect Customer to perform various actions on specified resources. As you enable additional features in Amazon Connect, additional permissions are added for the [AWSServiceRoleForProfile](customerprofiles-slr.md#slr-permissions-customerprofiles) service-linked role to access the resources associated with those features.

To view the permissions for this policy, see [CustomerProfilesServiceLinkedRolePolicy ](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CustomerProfilesServiceLinkedRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AmazonConnectSynchronizationServiceRolePolicy
<a name="amazonconnectsynchronizationservicerolepolicy"></a>

The `AmazonConnectSynchronizationServiceRolePolicy` permissions policy allows Connect Customer Managed Synchronization to perform various actions on specified resources. As resource synchronization is enabled for more resources, additional permissions are added to the [AWSServiceRoleForAmazonConnectSynchronization](managed-synchronization-slr.md#slr-permissions-managed-synchronization) service-linked role to access these resources.

To view the permissions for this policy, see [AmazonConnectSynchronizationServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonConnectSynchronizationServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## Connect Customer updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Connect Customer since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Connect Customer Document history](doc-history.md) page.

| Change | Description | Date |
| --- | --- | --- |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Updated actions for Connect Customer Customer Profiles | Updated the Connect Customer Customer Profiles permissions in the service-linked role policy to `profile:*` on all Connect Customer Customer Profiles resources with the `amazon-connect-` domain prefix and template resources, with an explicit deny for the following actions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html)<br />Additionally, the following actions are allowed on all resources: `profile:ListRecommenderRecipes`, `profile:ListAccountIntegrations`, and `profile:ListDomains`. | May 20, 2026 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Updated actions for Connect AI agents | Updated the Connect AI agents permissions in the service-linked role policy to `wisdom:*` on all Connect Customer Connect AI agents resources with resource tag `'AmazonConnectEnabled':'True'`, with an explicit deny for the following actions:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | May 18, 2026 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect AI agents | Added the following Connect AI agents actions to the service-linked role policy:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | November 18, 2025 |
|  [AmazonConnectSynchronizationServiceRolePolicy](#amazonconnectsynchronizationservicerolepolicy) – Added actions for Managed Synchronization | Modified the allowed actions by adding batch and import wildcards. The following actions were added:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | November 21, 2025 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for AWS End User Messaging Social | Added AWS End User Messaging Social actions to allow the listing of WhatsApp business accounts and the retrieval of a business account's WhatsApp message templates. The following actions were added:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html)<br />The AWS End User Messaging Social template APIs are restricted to WhatsApp business accounts that are tagged `AmazonConnectEnabled : True`. | October 20, 2025 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect Customer Customer Profiles | Added the following Connect Customer Customer Profiles actions to the service-linked role policy below the **AllowCustomerProfilesForConnectDomain** Sid. Also, added support for profile UploadJobs on all amazon-connect-\* resources, and not just “upload-jobs” resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | July 25, 2025 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon Polly | Added the following Amazon Polly actions to the service-linked role policy:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | July 9, 2025 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect Customer Customer Profiles | Added the following Connect Customer Customer Profiles actions to the service-linked role policy:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | June 30, 2025 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect Customer Customer Profiles | Added the following Customer Profiles actions to the service-linked role policy:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | June 9, 2025 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect AI agents, to support messaging | Added the following Connect AI agents actions to the service-linked role policy to support messaging. These actions allow Connect Customer to send, list, and get the next message by using the Connect AI agents API:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | March 14, 2025 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect AI agents | Added the following Connect AI agents actions to the service-linked role policy:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | December 31, 2024 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added action for Amazon Pinpoint, to support push notifications | Added the following Amazon Pinpoint action to the service-linked role policy to support push notifications. This action allows Connect Customer to send push notifications by using the Amazon Pinpoint API:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | December 10, 2024 |
| [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for integration with AWS End User Messaging Social | Added the following AWS End User Messaging Social actions to the service-linked role policy. The actions allow Connect Customer to invoke these APIs on End User Messaging Social phone numbers that have the `'AmazonConnectEnabled':'True'` resource tag.[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | December 2, 2024 |
| [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon SES, to support the email channel | Added the following Amazon SES actions to the service-linked role policy to support the email channel. These actions allow Connect Customer send, receive, and manage emails by using the Amazon SES APIs:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | November 22, 2024 |
|  [AmazonConnectServiceLinkedRolePolicy](#amazonconnectservicelinkedrolepolicy) – Added Actions for Connect Customer Customer Profiles | Added the following actions to manage Connect Customer Customer Profiles resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | November 18, 2024 |
|  [CustomerProfilesServiceLinkedRolePolicy](#customerprofilesservicelinkedrolepolicy) – Added permissions for managing outbound campaigns | Added the following actions to retrieving profile information and triggering a campaign.[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | December 1, 2024 |
|  [AmazonConnectServiceLinkedRolePolicy](#amazonconnectservicelinkedrolepolicy) – Added Actions for Connect Customer Customer Profiles and Connect AI agents | Added the following actions to manage Connect Customer Customer Profiles resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html)<br />Added the following actions to manage Connect AI agents resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | November 18, 2024 |
|  [AmazonConnectCampaignsServiceLinkedRolePolicy](#amazonconnectcampaignsservicelinkedrolepolicy) – Added Actions for Connect Customer Customer Profiles and Connect AI agents | Added the following actions to manage Connect Customer resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html)<br />Added the following actions to manage EventBridge resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html)<br />Added the following actions to manage Connect AI agents resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | November 18, 2024 |
|  [AmazonConnectSynchronizationServiceRolePolicy](#amazonconnectsynchronizationservicerolepolicy) – Consolidated allowed actions and added a deny-list of actions for Managed Synchronization | Modified the allowed actions by using wildcards and added an explicit deny-list of actions. | November 12, 2024 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon Chime SDK Voice Connector | Added the following Amazon Chime SDK Voice Connector actions to the service-linked role policy. These actions allow Connect Customer to obtain Amazon Chime Voice Connector information by using get and list Amazon Chime SDK Voice Connector APIs:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | October 25, 2024 |
|  [AmazonConnectSynchronizationServiceRolePolicy](#amazonconnectsynchronizationservicerolepolicy) – Added for Managed Synchronization | Added the following actions to the service-linked role managed policy to support the launch of the `HoursOfOperationOverride` attribute.[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | September 25, 2024 |
|  [AmazonConnectSynchronizationServiceRolePolicy](#amazonconnectsynchronizationservicerolepolicy) – Added for Managed Synchronization | Added the following actions to the service-linked role managed policy for managed synchronization:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | July 5, 2024 |
|  [AmazonConnectReadOnlyAccess](#amazonconnectreadonlyaccess-policy) – Renamed action `connect:GetFederationTokens` and changed to `connect:AdminGetEmergencyAccessToken` | The AmazonConnectReadOnlyAccess managed policy has been updated due to the renaming of the Connect Customer action `connect:GetFederationTokens` to `connect:AdminGetEmergencyAccessToken`. This change is backwards compatible and the `connect:AdminGetEmergencyAccessToken` action will function in the same way as the `connect:GetFederationTokens` action. If you leave the previously named `connect:GetFederationTokens` action in your policies, they will continue to function as expected. | June 15, 2024 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon Cognito user pools and Connect Customer Customer Profiles | Added the following Amazon Cognito user pools actions to the service-linked role policy to allow select read operations on Cognito User Pool User Pool resources that have an `AmazonConnectEnabled` resource tag. This tag is put on the resource when the `CreateIntegrationAssociations` API is called:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html)<br />Added the following Connect Customer Customer Profiles action to the service-linked role policy to allow permissions to put data into the Connect-adjacent service, Customer Profiles:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | May 23, 2024 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect AI agents | The following action is allowed to be performed on Connect AI agents resources that have the resource tag `'AmazonConnectEnabled':'True'` on Connect AI agents Knowledge Base:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | May 20, 2024 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon Pinpoint | Added the following actions to the service-linked role policy to use Amazon Pinpoint phone numbers to allow Connect Customer to send SMS:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | November 17, 2023 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect AI agents | The following action is allowed to be performed on Connect AI agents resources that have the resource tag `'AmazonConnectEnabled':'True'` on Connect AI agents Knowledge Base:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | November 15, 2023 |
|  [AmazonConnectCampaignsServiceLinkedRolePolicy](connect-slr-outbound.md#slr-permissions-outbound) – Added actions for Connect Customer | Connect Customer added new actions to retrieve outbound campaigns:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | November 8, 2023 |
|  [AmazonConnectSynchronizationServiceRolePolicy](#amazonconnectsynchronizationservicerolepolicy) – Added new AWS managed policy | Added a new service-linked role managed policy for managed synchronization.<br />The policy provides access to read, create, update, and delete Connect Customer resources and is used to automatically synchronize AWS resources across AWS regions. | November 3, 2023 |
|  [AmazonConnectServiceLinkedRolePolicy](#amazonconnectservicelinkedrolepolicy) – Added actions for Customer Profiles | Added the following action to manage Connect Customer Customer Profiles Service Linked Roles:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | October 30, 2023 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect AI agents | The following actions are allowed to be performed on Connect AI agents resources that have the resource tag `'AmazonConnectEnabled':'True'` on Connect AI agents Knowledge Base:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | October 25, 2023 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Customer Profiles | Added the following action to manage Connect Customer Customer Profiles Service Linked Roles:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | October 6, 2023 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect AI agents | The following actions are allowed to be performed on Connect AI agents resources that have the resource tag `'AmazonConnectEnabled':'True'` on Connect AI agents knowledge bases and assistants:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html)<br />The following `List` actions are allowed to be performed on all Connect AI agents resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | September 29, 2023 |
|  [CustomerProfilesServiceLinkedRolePolicy](#customerprofilesservicelinkedrolepolicy) – Added CustomerProfilesServiceLinkedRolePolicy | New managed policy. | March 7, 2023 |
|  [AmazonConnect\_FullAccess](#AmazonConnect_FullAccess-policy) – Added permission for managing Connect Customer Customer Profiles Service Linked Roles | Added the following action to manage Connect Customer Customer Profiles Service Linked Roles.[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | January 26, 2023 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon CloudWatch | Added the following action to publish usage Connect Customer metrics for an instance to your account.[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | Februrary 22, 2022 |
|  [AmazonConnect\_FullAccess](#AmazonConnect_FullAccess-policy) – Added permissions for managing Connect Customer Customer Profiles domains | Added all permissions for managing Connect Customer Customer Profiles domains that are created for new Connect Customer instances.[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html)<br />The following permissions are allowed to be performed on domains with a name that is prefixed with `amazon-connect-`:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | November 12, 2021 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Connect Customer Customer Profiles | Added the following actions so Connect Customer flows and the agent experience can interact with the profiles in your default Customer Profiles domain:[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html)<br />Added the following action so Connect Customer flows and the agent experience can interact with the profile objects in your default Customer Profiles domain: [See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html)<br />Added the following action so Connect Customer flows and the agent experience can determine whether Customer Profiles is enabled for your Connect Customer instance: [See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | November 12, 2021 |
|  [AmazonConnectVoiceIDFullAccess](#amazonconnectvoiceidfullaccesspolicy) – Added new AWS managed policy | Added a new AWS managed policy so you can set up your users to use Connect Customer Voice ID.<br />This policy provides full access to Connect Customer Voice ID through the AWS console, SDK, or other means. | September 27, 2021 |
|  [AmazonConnectCampaignsServiceLinkedRolePolicy](connect-slr-outbound.md#slr-permissions-outbound) – Added new service-linked role policy | Added a new service-linked role policy for outbound campaigns.<br />The policy provides access to retrieve all the outbound campaigns. | September 27, 2021 |
|  [AmazonConnectServiceLinkedRolePolicy](connect-slr.md) – Added actions for Amazon Lex | Added the following actions for the all bots created in the account across all Regions. These actions were added to support integration with Amazon Lex. [See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | June 15, 2021 |
| [AmazonConnect\_FullAccess](security-iam-amazon-connect-permissions.md) – Added actions for Amazon Lex  | Added the following actions for the all bots created in the account across all Regions. These actions were added to support integration with Amazon Lex. [See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/security_iam_awsmanpol.html) | June 15, 2021 |
| Connect Customer started tracking changes | Connect Customer started tracking changes for its AWS managed policies. | June 15, 2021 |
