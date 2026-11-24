---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/simplified-tip-iam-policies.html
---

# Use the identity context for IAM policies

When you turn on the simplified experience for trusted identity propagation, the identity context, including the user's username, is available in audit logs and for IAM policy evaluation. Because the identity context is carried in the user's SigV4 credentials, IAM can evaluate these context keys on any request signed with those credentials. You can use the keys in all IAM policy types: identity policies, resource policies, role trust policies, service control policies (SCPs), and resource control policies (RCPs). This includes resource policies such as Amazon S3 bucket policies, DynamoDB resource policies, and AWS Key Management Service key policies. For more information about IAM policy types, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*. For more information about AWS services that support these context keys, see [AWS services that support TIP](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_tip_services.html) in the *IAM User Guide*.

**Important**
If you use session-specific context keys, such as `aws:OriginIdentity/Subject`, in AWS Key Management Service key policies, services that cache data keys, such as Amazon S3 with S3 Bucket Keys enabled, might not call AWS Key Management Service for every request. To control access reliably, add the conditions to the policy of the integrated service, such as an Amazon S3 bucket policy. For more information, see [Using session-specific context with AWS services that cache data keys](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-aws.html#conditions-aws-session-data-key-caching) in the *AWS Key Management Service Developer Guide*.

To see where the username appears in CloudTrail events, see [Identity context fields in AWS CloudTrail (simplified experience)](sso-info-in-cloudtrail.md#sso-cloudtrail-simplified-tip-fields).

## Available context keys
<a name="simplified-tip-condition-keys"></a>

Sessions that come through IAM Identity Center carry the following context keys for IAM policies. The simplified experience adds three new keys, namely `aws:OriginIdentity/Subject`, `aws:OriginIdentity/SubjectType`, and `aws:OriginIdentity/Issuer`. The other keys in the table below are also available in the legacy experience. All of these keys are available for both organization and account instances of IAM Identity Center, except `aws:OriginIdentity/IdentityProviderAccount`, which is present only for account instances. If you use the keys in an SCP or RCP, the policy doesn't affect requests in your management account, because SCPs and RCPs don't apply to the management account.

| Context key | Value | New key with the simplified experience for trusted identity propagation (Yes/No) |
| --- | --- | --- |
| aws:OriginIdentity/Subject | A user's IAM Identity Center username | Yes |
| aws:OriginIdentity/SubjectType | The type of subject. For IAM Identity Center sessions, the value is always "user". | Yes |
| aws:OriginIdentity/Issuer | The issuer of your workforce users' identities. For IAM Identity Center sessions, the value is the ARN of your IAM Identity Center instance. | Yes |
| aws:OriginIdentity/IdentityProviderAccount | The ID of the AWS account that owns the IAM Identity Center instance that your workforce users federate from. This key is present only for account instances, not for organization instances. | No |
| aws:OriginIdentity/IdentityProviderOrgID | The ID of the AWS organization of the IAM Identity Center instance that your workforce users federate from. This key is not present if the account that owns the instance is not in an organization. | No |
| aws:IdentityStoreArn | ARN of the Identity Store that holds your workforce users | No |
| aws:IdentityCenterInstanceArn | ARN of the IAM Identity Center instance that your workforce users federate from | No |
| identitystore:UserId | A user's Identity Store user ID | No |
| identitystore:IdentityStoreArn | ARN of the Identity Store that holds your workforce users | No |

**Note**
For the Identity Store ARN, we recommend `aws:IdentityStoreArn` for new policies. It uses the global `aws:` prefix and is the same key as on the IAM federation path. The existing `identitystore:IdentityStoreArn` key carries the same value, and is retained for backward compatibility.

**Important**
A username is unique only within one IAM Identity Center instance. Another identity source can carry the same username, for example another organization's IAM Identity Center instance. To make sure usernames in your policies can only come from your IAM Identity Center instance, we recommend that you require `aws:OriginIdentity/Issuer` to equal your IAM Identity Center instance ARN in an SCP or RCP, rather than in each policy. If your identity source changes, you then update the condition in one place. See [Examples: limit access to your IAM Identity Center instance (SCPs and RCPs)](#simplified-tip-policy-example-scp-rcp).

## Choose context keys for common decisions
<a name="simplified-tip-policy-decisions"></a>

The following table shows which context keys to use for common authorization decisions.

| Authorization decision | Context keys |
| --- | --- |
| Identify a specific user | aws:OriginIdentity/Subject, with aws:OriginIdentity/Issuer required in an SCP or RCP |
| Allow only people, not workloads or automation | aws:OriginIdentity/SubjectType |
| Allow only users that federate from your IAM Identity Center instance | aws:OriginIdentity/Issuer |
| Allow only users that federate from IAM Identity Center instances in your AWS organization | aws:OriginIdentity/IdentityProviderOrgID |
| Allow only users that federate from account instances in specific AWS accounts | aws:OriginIdentity/IdentityProviderAccount |

Use `aws:OriginIdentity/Issuer` to allow only one specific IAM Identity Center instance. Use `aws:OriginIdentity/IdentityProviderOrgID` to allow users from any instance that is owned by an account in your AWS organization. This includes your organization instance and account instances in your member accounts, and it blocks identities from instances outside your organization. Because this key covers every instance in your organization, you can use it as a broad control, for example in an RCP that sets a data perimeter around your organization. If all the accounts that end users can federate into using an IAM Identity Center instance are in this same organization, `aws:OriginIdentity/IdentityProviderOrgID` is enough on its own. Use `aws:OriginIdentity/IdentityProviderAccount` to allow only account instances in specific accounts. Organization instances don't carry this key. This is useful when you want to trust an account instance in an account that isn't in an organization, or in an account outside your organization. AWS sets these keys when the session starts, so they identify where your IAM Identity Center instance is configured, not which account the request passes through. When a user in a session assumes another role, AWS STS propagates the identity context to the new session only to roles in accounts in the same organization as the account that owns your instance, or to roles in that same account if it isn't in an organization. For more information, see [Where the identity context propagates](simplified-tip-overview.md#simplified-tip-propagation).

## Handle requests that don't carry the context keys
<a name="simplified-tip-policy-null-guard"></a>

The IAM Identity Center context keys are included only when a user who signed in through IAM Identity Center makes the request. Sessions that users started before you turned on the simplified experience don't include them.

A Deny statement that uses a negated operator, such as `StringNotEquals`, also applies to requests that don't carry the key. To limit the Deny to requests that carry the key, add a `Null` condition. For more information, see [Condition operator to check existence of condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_Null) in the *IAM User Guide*.

## Ways to use these context keys
<a name="simplified-tip-policy-uses"></a>

The following table shows common goals and the type of policy that fits each one.

| Goal | Type of policy | How the policy works |
| --- | --- | --- |
| Allow only people who sign in through your IAM Identity Center instance to read your organization's data | Resource control policy (RCP) | Deny reads on your restricted resources unless aws:OriginIdentity/Issuer equals your IAM Identity Center instance ARN. Workforce identities from other identity sources are denied. |
| Block access through IAM Identity Center account instances created in member accounts | Service control policy (SCP) | Deny actions when aws:OriginIdentity/Issuer is present and doesn't equal your organization instance ARN. |
| Allow only users from IAM Identity Center instances in your AWS organization to access your resources | Resource control policy (RCP) | Deny requests that carry a user identity unless aws:OriginIdentity/IdentityProviderOrgID equals your organization ID. Users from instances outside your organization are denied. |
| Allow only users from account instances in specific AWS accounts to access your resources | Resource control policy (RCP) | Deny requests that carry a user identity unless aws:OriginIdentity/IdentityProviderAccount is one of the account IDs that you allow. Users from organization instances don't carry this key, so the Deny also applies to them. |
| Allow only named users to read a sensitive table, even though many people use the same role | Resource-based policy | Deny reads unless aws:OriginIdentity/Subject is one of the named usernames. See [Example: allow only named users to read a table (resource-based policy)](#simplified-tip-policy-example-named-table). |

For full examples of the SCP and RCP patterns, see [Examples: limit access to your IAM Identity Center instance (SCPs and RCPs)](#simplified-tip-policy-example-scp-rcp).

## Examples: limit access to your IAM Identity Center instance (SCPs and RCPs)
<a name="simplified-tip-policy-example-scp-rcp"></a>

Use SCPs and RCPs to apply the IAM Identity Center context keys across your organization. Test these policies from a member account, because SCPs and RCPs don't apply to the management account.

**RCP: allow only users from your IAM Identity Center instance to read restricted data**

A username is unique only within one IAM Identity Center instance, so another identity source can carry the same username. The following RCP denies reads on restricted resources unless the request comes from a user in your IAM Identity Center instance. Workforce identities from other identity sources are denied.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "OnlyOurInstanceCanReadRestricted",
            "Effect": "Deny",
            "Principal": "*",
            "Action": ["s3:GetObject", "secretsmanager:GetSecretValue"],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket/*",
                "arn:aws:secretsmanager:*:111122223333:secret:restricted/*"
            ],
            "Condition": {
                "Null": { "aws:OriginIdentity/Issuer": "false" },
                "StringNotEquals": {
                    "aws:OriginIdentity/Issuer": "arn:aws:sso:::instance/ssoins-1234567890abcdef"
                }
            }
        }
    ]
}
```

**RCP: block identities from outside your AWS organization**

The following RCP denies requests that carry a user identity from an IAM Identity Center instance outside your AWS organization. Requests that do not carry a user identity are not affected, because of the `Null` condition. An identity from an instance whose account is not in an organization is also denied. That identity carries a username, but it doesn't carry `aws:OriginIdentity/IdentityProviderOrgID`, because this key is present only when the account that owns the instance is in an organization.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyIdentitiesFromIdentityProvidersOutsideMyOrg",
            "Effect": "Deny",
            "Principal": "*",
            "Action": ["sts:AssumeRole", "sts:SetContext", "s3:*"],
            "Resource": "*",
            "Condition": {
                "Null": { "aws:OriginIdentity/Subject": "false" },
                "StringNotEquals": { "aws:OriginIdentity/IdentityProviderOrgID": "o-exampleorgid" }
            }
        }
    ]
}
```

**SCP: block access through other IAM Identity Center instances**

The following SCP denies actions when the request comes from an IAM Identity Center instance other than your organization instance, such as an account instance created in a member account.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyOtherIdentityCenterInstances",
            "Effect": "Deny",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "Null": { "aws:OriginIdentity/Issuer": "false" },
                "StringNotEquals": {
                    "aws:OriginIdentity/Issuer": "arn:aws:sso:::instance/ssoins-1234567890abcdef"
                }
            }
        }
    ]
}
```

## Example: allow only one user to access a bucket (bucket policy)
<a name="simplified-tip-policy-example-user-folder"></a>

The following bucket policy denies access to the `amzn-s3-demo-bucket` Amazon S3 bucket for every user who signed in through IAM Identity Center, except `example-user-1`. Attach the policy to the bucket.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyAllUsersExceptOne",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket",
                "arn:aws:s3:::amzn-s3-demo-bucket/*"
            ],
            "Condition": {
                "Null": { "aws:OriginIdentity/Subject": "false" },
                "StringNotEquals": { "aws:OriginIdentity/Subject": "example-user-1" }
            }
        }
    ]
}
```

The `Null` condition limits the Deny to requests that carry a username, so requests from IAM roles that don't come through IAM Identity Center aren't affected. The policy doesn't grant access. `example-user-1` still needs an Allow, for example in the policy of the IAM role that they use.

## Example: allow only named users to read a table (resource-based policy)
<a name="simplified-tip-policy-example-named-table"></a>

The `PayrollRecords` DynamoDB table should be readable only by two payroll administrators, `example-user-1` and `example-user-2`, even though everyone who uses the `FinanceAnalyst` permission set can read other tables. Attach the following resource-based policy to the table:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "OnlyPayrollAdminsCanRead",
            "Effect": "Deny",
            "Principal": "*",
            "Action": ["dynamodb:GetItem", "dynamodb:BatchGetItem", "dynamodb:Query", "dynamodb:Scan"],
            "Resource": "arn:aws:dynamodb:us-east-1:111122223333:table/PayrollRecords",
            "Condition": {
                "StringNotEquals": {
                    "aws:OriginIdentity/Subject": ["example-user-1", "example-user-2"]
                },
                "BoolIfExists": { "aws:PrincipalIsAWSService": "false" }
            }
        }
    ]
}
```

This statement denies anyone whose username isn't one of the two administrators. Requests that AWS services make on their own behalf, such as backups, are not affected, because of the `BoolIfExists` condition on `aws:PrincipalIsAWSService`. To make sure these usernames can only come from your IAM Identity Center instance, use an RCP that requires `aws:OriginIdentity/Issuer` to equal your IAM Identity Center instance ARN; see [Examples: limit access to your IAM Identity Center instance (SCPs and RCPs)](#simplified-tip-policy-example-scp-rcp).

Requests that don't carry a username at all, such as requests from IAM roles that don't come through IAM Identity Center, are also denied. Make sure that matches your intent before you apply it.

## Consideration: username changes
<a name="simplified-tip-username-changes"></a>

These context keys match the username exactly. If a username changes in your identity source, any policy that references the old value breaks. Allow statements stop granting access, and deny statements stop blocking it. Under the shared responsibility model, you are responsible for keeping policies in sync with your identity source. Before you rename a user, locate every policy that references the old username in an `aws:OriginIdentity/Subject` condition and update it to the new value. For the same reason, don't reassign a former user's username to a new employee. Any policy that still references it would apply to the new person. It could grant them the former user's access or block them in the former user's place.

## Verify and troubleshoot policy behavior
<a name="simplified-tip-policy-troubleshoot"></a>

The following table shows where to check each outcome, the value to expect, and what a missing or different value means.

| Outcome | Where to check | Expected value | Meaning of a missing or different value |
| --- | --- | --- | --- |
| The username appears in CloudTrail | The userIdentity.onBehalfOf element of the CloudTrail event for the request | subject is the user's username, and issuer is your IAM Identity Center instance ARN | The simplified experience isn't turned on, the session was created before you turned it on, or the service doesn't record the username yet. |
| A policy condition on the username matches | The aws:OriginIdentity/Subject value in the policy, compared with onBehalfOf.subject in CloudTrail | The two values match exactly | The policy uses a different format than your identity source, or the user was renamed. For more information, see [Consideration: username changes](#simplified-tip-username-changes). |
| Requests without the user's identity aren't denied | Each Deny statement that uses a negated operator with an IAM Identity Center context key | The statement includes a Null condition with the value false on the key, if the Deny should apply only when the key is present | Without the Null condition, the Deny also applies to requests that don't carry the key. For more information, see [Handle requests that don't carry the context keys](#simplified-tip-policy-null-guard). |
| Users are allowed after you enforce a new policy | When each user's session was created, compared with when you turned on the simplified experience | Sessions were created after you turned on the simplified experience | Sessions and command line credentials created earlier don't carry the keys. Ask users to sign in again. |
| An SCP or RCP takes effect | Which account the request is tested from. For an SCP, check the account of the role that makes the request. For an RCP, check the account that owns the resource. | The account is a member account of your organization | SCPs and RCPs don't apply to the management account. Test from a member account. |
