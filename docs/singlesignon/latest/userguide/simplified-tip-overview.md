---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/simplified-tip-overview.html
---

# Simplified experience for trusted identity propagation

With the simplified experience for trusted identity propagation, each user's username is added to the identity context that travels with their requests, on every IAM Identity Center federation access path. You can view the username in AWS CloudTrail events, and use any of the identity context keys in IAM policy conditions. This identity context is available across more than 250 AWS services. For more information about the AWS services where you can use the identity context in IAM policies, see [AWS services that support TIP](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_tip_services.html) in the *IAM User Guide*.

The username is an identifier provided by your identity source, such as your external identity provider (IdP), and stored in the username attribute of your IAM Identity Center Identity Store (for example, `example-user-1`). For guidance on what to include in usernames, see [How the simplified experience uses the username](simplified-tip-prerequisites.md#simplified-tip-prereq-username). For an introduction to trusted identity propagation, see [Trusted identity propagation overview](trustedidentitypropagation-overview.md).

## Key benefits
<a name="simplified-tip-benefits"></a>

The simplified experience provides the following key benefits:

1. [Username-based audit and access control](#simplified-tip-benefit-audit)

1. [The same identity on every access path](#simplified-tip-benefit-paths)

1. [Simpler setup](#simplified-tip-benefit-roles)

### Username-based audit and access control
<a name="simplified-tip-benefit-audit"></a>

You can use the username in IAM policy conditions to allow or deny access for specific users in your organization. For how to write policies on the username and the other propagated identity fields, see [Use the identity context for IAM policies](simplified-tip-iam-policies.md).

These identity context fields, including the username, are also recorded in AWS CloudTrail. With CloudTrail, you can identify the user behind an action without first looking up the user's IAM Identity Center user ID, because the username, the identifier from your identity source, is recorded consistently on every access path. For the full list of identity context fields that CloudTrail records, see [Identity context fields in AWS CloudTrail (simplified experience)](sso-info-in-cloudtrail.md#sso-cloudtrail-simplified-tip-fields).

### The same identity on every access path
<a name="simplified-tip-benefit-paths"></a>

Workforce users who federate through IAM Identity Center reach AWS through several paths. These include web applications such as Amazon SageMaker Unified Studio or Amazon EMR Studio, and AWS accounts in the AWS access portal, where users assume IAM roles that are created from permission sets or assigned with IAM account access manager. In the simplified experience, all of these paths carry the same identity context, including the username, so auditing of that user's actions in AWS is consistent regardless of path. As an outcome, a single IAM policy condition on a username applies across every path.

### Simpler setup
<a name="simplified-tip-benefit-roles"></a>

When you create or update IAM roles used for trusted identity propagation, you no longer need to add the `sts:SetContext` permission to the role trust policy. For requests signed with Signature Version 4 (SigV4), the user's identity context propagates through these roles automatically.

You also don't have to configure OAuth scopes for any application. With the simplified experience for trusted identity propagation, OAuth scope validation is now turned off for Signature Version 4 (SigV4) requests that carry the user's identity context. Scopes are only enforced for OAuth bearer token flows. In an OAuth bearer token flow, an application presents an OAuth access token directly to a service instead of signing the request with SigV4 credentials, for example Amazon Redshift JDBC or ODBC connections that use `ACCESS_TOKEN`, or Amazon OpenSearch Service with a JWT.

## Where the identity context propagates
<a name="simplified-tip-propagation"></a>

The identity context carries context keys that you can use in IAM policy conditions. Some of these keys include:
+ `aws:OriginIdentity/Subject`: the user's username.
+ `aws:OriginIdentity/Issuer`: the ARN of your IAM Identity Center instance.
+ `aws:OriginIdentity/IdentityProviderOrgID`: the AWS Organization ID for your IAM Identity Center instance. This key is present only if the account that owns your IAM Identity Center instance is in an organization.
+ `aws:OriginIdentity/IdentityProviderAccount`: the AWS account ID where you created your IAM Identity Center instance. This key is present only for IAM Identity Center account instances.

For the full list of context keys, see [Available context keys](simplified-tip-iam-policies.md#simplified-tip-condition-keys).

AWS Security Token Service (AWS STS) uses the account and organization keys to decide where the identity context carries when a user in a session assumes another role.

| Account that owns your instance | Account that owns the target role | Result |
| --- | --- | --- |
| Belongs to an AWS organization | That account, or another account in the same organization | AWS STS carries the identity context into the new role session. |
| Belongs to an AWS organization | A standalone account, or an account in a different organization | AWS STS doesn't propagate the identity context when the role is assumed. The role assumption will still succeed if the permissions and the trust policy of the target role allow it. |
| Does not belong to an organization | Same as the account that owns your instance | AWS STS carries the identity context into the new role session. |
| Does not belong to an organization | Belongs to any other account | AWS STS doesn't propagate the identity context when the role is assumed. The role assumption will still succeed if the permissions and the trust policy of the target role allow it. |

When a supported AWS service uses its own credentials to assume an IAM service role in your account, AWS STS applies the same boundary. AWS STS uses the account that owns your instance and, when present, its organization in the identity context, not the account of the AWS service. If the service role is within the boundary, AWS STS adds the identity context to the service role session.

A direct request to a resource in another organization uses the original credentials, and IAM can evaluate the context keys if a resource policy references them.

## Background sessions
<a name="simplified-tip-background-sessions"></a>

Services that support the simplified experience can use user background sessions to keep long-running jobs and sessions running after a user signs out. User background sessions are turned on by default for new IAM Identity Center instances, with a default duration of 7 days. For existing IAM Identity Center instances, when you turn on the simplified experience, the instance keeps its current user background sessions setting. For more information about the capability, see [User background sessions](user-background-sessions.md).

## How the simplified experience differs from the legacy experience
<a name="simplified-tip-how-it-differs"></a>

Your IAM Identity Center instance uses the legacy experience until you turn on the simplified experience. The simplified experience removes most of the setup that the legacy experience requires. The following table lists the differences.

Before you turn on the simplified experience, review [Prerequisites and considerations for the simplified experience](simplified-tip-prerequisites.md).

To move to the simplified experience, see [Moving from the legacy experience to the simplified experience](simplified-tip-migration.md).

### Key differences
<a name="simplified-tip-key-differences"></a>

| Configuration | Legacy experience | Simplified experience |
| --- | --- | --- |
| OAuth scopes for SigV4 requests that carry the user's identity context | Enforced | Not enforced, for both AWS managed and customer-configured scopes. Access is governed by IAM policies and service native access controls, such as AWS Lake Formation grants, Amazon S3 Access Grants, and Amazon Redshift role-based access control. |
| sts:SetContext on role trust policies | Required | Not needed (ignored; safe to leave) |
| Identity propagation across role chains | Trust policy update on every role; did not carry when a service assumed a role on the user's behalf | Automatic through the full chain, including IAM roles that users assume, and requests that AWS services make on the user's behalf with forward access sessions (FAS) |
| CloudTrail user identity fields | + `userId` (Identity Store user ID)<br />+ `identityStoreArn`<br />+ `identityCenterInstanceArn` | + `subject` (the username) (new)<br />+ `subjectType` (new)<br />+ `issuer` (new)<br />+ `userId` (Identity Store user ID)<br />+ `identityStoreArn`<br />+ `identityCenterInstanceArn` |
| IAM policy context keys for the user | + `aws:IdentityStoreArn`<br />+ `aws:IdentityCenterInstanceArn`<br />+ `identitystore:UserId`<br />+ `identitystore:IdentityStoreArn`<br />+ `aws:OriginIdentity/IdentityProviderAccount`<br />+ `aws:OriginIdentity/IdentityProviderOrgID` | The same keys, plus these new keys:+ `aws:OriginIdentity/Subject`<br />+ `aws:OriginIdentity/SubjectType`<br />+ `aws:OriginIdentity/Issuer`<br />See [Available context keys](simplified-tip-iam-policies.md#simplified-tip-condition-keys). |
| User background sessions | Not turned on by default. You turn on user background sessions and set the duration in the IAM Identity Center console. | Turned on by default for new IAM Identity Center instances, with a default duration of 7 days. Existing instances keep their current setting when you turn on the simplified experience. |

### Key similarities
<a name="simplified-tip-key-similarities"></a>

The following table lists what stays the same in the legacy experience and the simplified experience.

| Configuration | Legacy experience | Simplified experience |
| --- | --- | --- |
| IAM Identity Center application registration for web applications that users sign in to | Required | Required |
| User and group assignments on front-end web applications | Optional (still controls sign-in) | Optional (still controls sign-in) |
| OAuth bearer token flows (Redshift ACCESS\_TOKEN, OpenSearch JWT) | Scopes enforced | Scopes still enforced (unchanged) |

**Topics**
+ [Key benefits](#simplified-tip-benefits)
+ [Where the identity context propagates](#simplified-tip-propagation)
+ [Background sessions](#simplified-tip-background-sessions)
+ [How the simplified experience differs from the legacy experience](#simplified-tip-how-it-differs)
+ [Control access with the identity context](tip-access-control.md)
+ [Use the identity context for IAM policies](simplified-tip-iam-policies.md)
