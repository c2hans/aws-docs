---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/simplified-tip-prerequisites.html
---

# Prerequisites and considerations for the simplified experience

For most customers, no changes are needed before turning on the simplified experience, and existing workflows continue to function. Review each prerequisite to confirm.

Before you turn on the simplified experience, complete the following prerequisites:

1. Review the general [Prerequisites and considerations](trustedidentitypropagation-overall-prerequisites.md) for trusted identity propagation.

1. Make sure that the usernames in your IAM Identity Center Identity Store meet the requirements for the Subject key. If a username doesn't meet them, the user can't sign in. See [Where the Subject key comes from](#simplified-tip-subject).

1. If your users access AWS services in more than one AWS Region, use a multi-Region organization instance of IAM Identity Center configured with a multi-Region customer managed KMS key. See [Considerations for cross-Region trusted identity propagation](trustedidentitypropagation-overall-prerequisites.md#cross-region-tip-considerations).

1. Find any OAuth scopes with authorized targets that you use to control access. See [Check your current configuration](#simplified-tip-prereq-how-to-check).

1. If you used OAuth scopes with authorized targets to restrict access, replace them with IAM policies. See [Move authorized target scope restrictions to IAM policies](#simplified-tip-prereq-authorized-targets).

1. Make sure that your logging and retention policies allow usernames in AWS CloudTrail events. See [Review logging and retention policies](#simplified-tip-prereq-logging).

1. Review where the identity context propagates in your current setup with trusted identity propagation. If your workflows assume roles outside your organization, or in cross-account scenarios where your instance's account isn't part of an organization, the simplified experience doesn't propagate the identity context in those scenarios. Continue to use the legacy experience, or re-architect your workflows, before you turn on the simplified experience. See [Where the identity context propagates](simplified-tip-overview.md#simplified-tip-propagation).

Keep the following considerations in mind:
+ How the simplified experience uses the username. See [How the simplified experience uses the username](#simplified-tip-prereq-username).
+ Sessions created before you turn on the simplified experience don't carry the new context keys. See [Existing sessions don't carry the new context keys](#simplified-tip-prereq-existing-sessions).
+ Configuration that remains in your account. See [What remains configured (no action needed)](#simplified-tip-prereq-what-remains).
+ If you use trusted identity propagation with an IAM identity provider. See [Trusted identity propagation with an IAM identity provider](simplified-tip-enabling.md#tip-iam-federation).

## Check your current configuration
<a name="simplified-tip-prereq-how-to-check"></a>

Use the IAM Identity Center APIs to review your configuration before you turn on the simplified experience:
+ [ListApplications](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplications.html): list IAM Identity Center applications for your instance.
+ [ListApplicationAccessScopes](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAccessScopes.html): review the OAuth scopes configured on each application.
+ [ListApplicationAssignments](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAssignments.html): review user and group assignments on each application.

If you see only default scopes (for example, `s3:access_grants:read_write`, `lakeformation:query`, `redshift:connect`) and no assignments beyond your front-end web applications, nothing was restricting access beyond what IAM already enforces, and no additional action is needed. Manually added scopes or authorized targets are the ones to review and replace. Examples include a scope that you added to an application with the `PutApplicationAccessScope` API, or a list of authorized targets that limits a scope to specific applications, such as an application that can reach only two Amazon Redshift clusters even though more exist in the account.

## Move authorized target scope restrictions to IAM policies
<a name="simplified-tip-prereq-authorized-targets"></a>

If you deliberately configured OAuth scopes with authorized targets to restrict which applications can call which services in a propagation chain (application-to-application scoping), those restrictions stop being enforced for identity-propagated requests. Before you turn on the simplified experience:
+ Implement equivalent controls using IAM policies or service native authorization (AWS Lake Formation grants, Amazon S3 Access Grants, Amazon Redshift role-based access control).
+ Review the IAM roles used on those propagation paths. Make sure that each role grants only the access you configured with scopes in the legacy experience. Where a role is broader than the authorized targets were, tighten it to match the access you intend.
+ Validate the equivalent controls in a test IAM Identity Center instance before you turn on the simplified experience in production.

### Sample IAM policies
<a name="simplified-tip-prereq-sample-policies"></a>

The following examples show how to replace an authorized target scope with an equivalent resource restriction on the IAM role policy. Replace `service:ActionOne` with the actual service action, and replace the placeholder tag key and value (for example, `aws:ResourceTag/access`) or resource ARNs with your own values. Choose the option that matches how your scoped resources are identified.

**Option 1: the scoped resources share a tag**

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowScopedByTag",
            "Effect": "Allow",
            "Action": "service:ActionOne",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/access": "authorized"
                }
            }
        }
    ]
}
```

**Option 2: the resources have resource ARNs (recommended)**

If the downstream service provides resource ARNs, list them in the `Resource` element instead of using `"*"`.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowScopedResources",
            "Effect": "Allow",
            "Action": "service:ActionOne",
            "Resource": ["resource1Arn", "resource2Arn"]
        }
    ]
}
```

## Review logging and retention policies
<a name="simplified-tip-prereq-logging"></a>

With the simplified experience, AWS CloudTrail events include usernames, which your organization might treat as personal data. Make sure that your logging and retention policies allow this before you turn on the simplified experience.

## Considerations
<a name="simplified-tip-prereq-considerations"></a>

### How the simplified experience uses the username
<a name="simplified-tip-prereq-username"></a>

When you turn on the simplified experience for trusted identity propagation, IAM Identity Center includes each user's username in the AWS temporary security credentials for that user's session, as the subject. IAM Identity Center takes this value from the username attribute in your IAM Identity Center Identity Store. You can use the username to manage access to your AWS resources, for example in IAM policies and data grants, and AWS can use it to authorize requests, record activity in AWS CloudTrail and service logs, calculate fees, and enable you to allocate cost to users.

The subject value does not constitute your content, and we recommend that you do not include sensitive, confidential, or personally identifiable information in it. The username travels with each request to the AWS accounts and AWS Regions your users access, and is also processed in default AWS Regions required to fulfill the request.

**Important**
As a best practice, use an immutable value for the username.

### Where the Subject key comes from
<a name="simplified-tip-subject"></a>

The `aws:OriginIdentity/Subject` key always holds the value of the username field for the user in your IAM Identity Center Identity Store. The username must meet the following requirements:
+ It has no more than 128 characters
+ It contains only letters from any script, numbers, spaces, and the characters `_ . : / = + - @`
+ It can't contain an accent written as a separate character, or a vowel sign used in scripts such as Devanagari and Tamil. An accented letter stored as a single character, such as é, is accepted
+ It doesn't start or end with a space

If a username doesn't meet these requirements, the affected user can't sign in after you turn on the simplified experience. Before you turn on the simplified experience, review the usernames in your IAM Identity Center Identity Store and update any that don't meet the requirements in your identity source.

### Existing sessions don't carry the new context keys
<a name="simplified-tip-prereq-existing-sessions"></a>

The IAM Identity Center context keys apply only to sessions created after you turn on the simplified experience. Sessions and command line credentials created earlier don't carry them, so a policy that requires the keys denies those requests. Ask users to sign in again before you enforce such policies.

### What remains configured (no action needed)
<a name="simplified-tip-prereq-what-remains"></a>

After you turn on the simplified experience, the following remain in your account but have no impact on identity propagation:
+ **`sts:SetContext` on roles** is no longer required and is safe to leave in place.
+ **Scope configurations** are not enforced for SigV4 identity-propagated requests. Do not remove them if you also use OAuth bearer token flows, because scopes remain enforced for those paths. In an OAuth bearer token flow, an application presents an OAuth access token directly to a service, for example a JDBC or ODBC connection to Amazon Redshift that uses an access token, instead of signing the request with SigV4 credentials.
