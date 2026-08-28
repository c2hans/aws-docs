---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/theme-4.html
---

# Theme 4: Manage identities
<a name="theme-4"></a>

**Essential Eight strategies covered**: Restrict administrative privileges, multi-factor authentication

Robust management of identity and permissions is a critical aspect of managing security in the cloud. Strong identity practices balance necessary access and least privilege. This helps development teams move quickly without compromising security.

Use identity federation to centralise management of identities. This makes it easier to manage access across multiple applications and services because you are managing access from a single location. This also helps you implement temporary permissions and multi-factor authentication (MFA).

Grant users only the permissions that they require to perform their tasks. AWS Identity and Access Management Access Analyzer can validate policies and verify public and cross-account access. Features such as AWS Organizations service control policies (SCPs), IAM policy conditions, IAM permissions boundaries, and AWS IAM Identity Center permission sets can help you configure fine-grained access control.

When doing any type of authentication, it is best to use temporary credentials to reduce or eliminate risks—such as credentials being inadvertently disclosed, shared, or stolen. Use IAM roles instead of IAM users.

Use strong sign-in mechanisms, such as MFA, to mitigate the risk where sign-in credentials have been inadvertently disclosed or are easily guessed. Require MFA for the root user, and you can also require it at a federation level. If use of IAM users is unavoidable, enforce MFA.

To monitor and report on compliance, you must continually work to reduce permissions, monitor findings from IAM Access Analyzer, and remove unused IAM resources. Use AWS Config rules to make sure that strong sign-in mechanisms are enforced, credentials are short-lived, and IAM resources are in use.

## Related best practices in the AWS Well-Architected Framework
<a name="theme-4-best-practices"></a>
+ [SEC02-BP01 Use strong sign-in mechanisms](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_enforce_mechanisms.html)
+ [SEC02-BP02 Use temporary credentials](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_unique.html)
+ [SEC02-BP03 Store and use secrets securely](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_secrets.html)
+ [SEC02-BP04 Rely on a centralized identity provider](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_identity_provider.html)
+ [SEC02-BP05 Audit and rotate credentials periodically](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_audit.html)
+ [SEC02-BP06 Employ user groups and attributes](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_groups_attributes.html)
+ [SEC03-BP01 Define access requirements](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define.html)
+ [SEC03-BP02 Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html)
+ [SEC03-BP03 Establish emergency access process](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_emergency_process.html)
+ [SEC03-BP04 Reduce permissions continuously](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_continuous_reduction.html)
+ [SEC03-BP05 Define permission guardrails for your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define_guardrails.html)
+ [SEC03-BP06 Manage access based on lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_lifecycle.html)
+ [SEC03-BP07 Analyse public and cross-account access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_analyze_cross_account.html)
+ [SEC03-BP08 Share resources securely within your organization](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_share_securely.html)

## Implementing this theme
<a name="theme-4-implementation"></a>

### Implement identity federation
<a name="implement-identity-federation.4f272d44-af7e-59cd-84d6-c1697e4d2955"></a>
+ [Require human users to federate with an identity provider to access AWS by using temporary credentials](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source.html)
+ [Implement temporary elevated access to your AWS environments](https://aws.amazon.com/blogs/security/managing-temporary-elevated-access-to-your-aws-environment/)

### Apply least privilege permissions
<a name="apply-least-privilege-permissions.5abcb6d3-ec43-55b4-b70f-f9c12c277715"></a>
+ [Safeguard your root user credentials and don't use them for everyday tasks](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html)
+ [Use IAM Access Analyzer to generate least-privilege policies based on access activity](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/dynamically-generate-an-iam-policy-with-iam-access-analyzer-by-using-step-functions.html)
+ [Verify public and cross-account access to resources with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html)
+ [Use IAM Access Analyzer to validate your IAM policies for secure and functional permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html)
+ [Establish permissions guardrails across multiple accounts](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/organizations.html)
+ [Use permissions boundaries to set the maximum permissions that an identity-based policy can grant](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
+ [Use conditions in IAM policies to further restrict access](https://aws.amazon.com/blogs/apn/top-recommendations-for-working-with-iam-from-our-aws-heroes-part-3-permissions-boundaries-and-conditions/)
+ [Regularly review and remove unused users, roles, permissions, policies, and credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html)
+ [Use the permission sets feature in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html)

### Rotate credentials
<a name="rotate-credentials.b51f386e-d818-5e77-8b57-b35c6ec05fe8"></a>
+ [Require workloads to use IAM roles to access AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
+ [Automate deletion of unused IAM roles](https://aws.amazon.com/blogs/security/how-to-centralize-findings-and-automate-deletion-for-unused-iam-roles/)
+ [Rotate access keys regularly for use cases that require long-term credentials](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-rotate-iam-user-access-keys-at-scale-with-aws-organizations-and-aws-secrets-manager.html)

### Enforce MFA
<a name="enforce-mfa.fe6c20cf-be78-52ee-9f92-3c6c9af3297d"></a>
+ [Require MFA for the root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
+ [Require MFA through IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-configure-mfa-device-enforcement.html)
+ [Consider requiring MFA to service-specific API actions](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-mfa)

## Monitoring this theme
<a name="theme-4-monitoring"></a>

### Monitor least privilege access
<a name="monitor-least-privilege-access.8faacf0f-fa0d-52b5-8c65-97eb5faf5f38"></a>
+ [Send IAM Access Analyzer findings to AWS Security Hub CSPM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-securityhub-integration.html)
+ [Consider setting up notifications for critical IAM Identity Center findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-eventbridge.html)
+ [Regularly review credential reports for your AWS accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

### Implement the following AWS Config rules
<a name="implement-the-following-9999999999999999cc--rules.03bb65f0-7a1c-5ac8-bd7f-45fc9ea2f136"></a>
+ `ACCESS_KEYS_ROTATED`
+ `IAM_ROOT_ACCESS_KEY_CHECK`
+ `IAM_USER_MFA_ENABLED`
+ `IAM_USER_UNUSED_CREDENTIALS_CHECK`
+ `IAM_PASSWORD_POLICY`
+ `ROOT_ACCOUNT_HARDWARE_MFA_ENABLED`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
