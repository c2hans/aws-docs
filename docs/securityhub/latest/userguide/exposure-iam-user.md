---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/exposure-iam-user.html
---

# Remediating exposures for IAM users
<a name="exposure-iam-user"></a>

AWS Security Hub can generate exposure findings for AWS Identity and Access Management (IAM) users.

On the Security Hub console, the IAM user involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the [https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html) operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait.

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**
 The remediation guidance provided in this topic might require additional consultation in other AWS resources.

IAM best practices recommend that you create IAM roles or use federation with an identity provider to access AWS using temporary credentials instead of creating individual IAM users. If that's an option for your organization and use case, we recommend switching to roles or federation instead of using IAM users. For more information, see [IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) in the *IAM User Guide*.

**Contents**
+ [Misconfiguration traits for IAM users](#iam-user-misconfiguration)
  + [The IAM user does not have MFA enabled](#user-mfa-disabled)
  + [The AWS account for the IAM user has weak password policies](#weak-password-policies)
  + [The IAM user has unrotated access keys](#unrotated-access-keys)
  + [The IAM user has a policy that allows unrestricted access to KMS key decryption](#unrestricted-kms-decryption-allowed)
+ [Unused access traits for IAM users](#iam-user-unused-access)
+ [Impact traits for IAM users](#iam-user-impact)
  + [Full control privileged executor](#full-control-privileged-executor)
  + [Direct policy escalation](#direct-policy-escalation)
  + [Trust policy hijack](#trust-policy-hijack)
  + [Data ransomware](#data-ransomware)
  + [Remove restriction](#remove-restriction)
  + [Pass role create executor](#pass-role-create-executor)
  + [Swap role existing executor](#swap-role-existing-executor)
  + [Role chain escalation](#role-chain-escalation)
  + [Inject code privileged executor](#inject-code-privileged-executor)
  + [Disable audit trail](#disable-audit-trail)
  + [Access existing executor](#access-existing-executor)
  + [Credential minting](#credential-minting)
  + [Pass role data access](#pass-role-data-access)
  + [Pass role task hijack](#pass-role-task-hijack)
  + [Single hop data access](#single-hop-data-access)
  + [Capability advancing](#capability-advancing)

## Misconfiguration traits for IAM users
<a name="iam-user-misconfiguration"></a>

Here are misconfiguration traits for IAM users and suggested remediation steps.

### The IAM user does not have MFA enabled
<a name="user-mfa-disabled"></a>

 Multi-factor authentication (MFA) adds an extra layer of protection on top of a user name and password. When MFA is enabled and an IAM user signs in to an AWS website, they are prompted for their user name, password, and an authentication code from their AWS MFA device. The authenticating principal must possess a device that emits a time-sensitive key and must have knowledge of a credential. Without MFA, if a user’s password is compromised, an attacker gains full access to the user’s AWS permissions. Following standard security principles, AWS recommends enabling MFA for all accounts and users that have AWS Management Console access.

**Review MFA types**
 AWS supports the following [MFA types](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html#id_credentials_mfa-types):
+ Passkeys and security keys
+ Virtual authenticator applications
+ Hardware TOTP tokens

 Although authentication with a physical device typically provides more stringent security protection, using any type of MFA is more secure than having MFA disabled.

**Enable MFA**
 To enable the MFA type that suits your requirements, see [AWS multi-factor authentication in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) in the *IAM User Guide*. Follow the steps for the specific MFA type you want to implement. For organizations managing many users, you may want to enforce MFA usage by requiring MFA to access sensitive resources.

### The AWS account for the IAM user has weak password policies
<a name="weak-password-policies"></a>

 Password policies help protect against unauthorized access by enforcing minimum complexity requirements for IAM user passwords. Without strong password policies, there’s an increased risk that user accounts could be compromised through password guessing or brute force attacks. Following standard security principles, AWS recommends implementing a strong password policy to ensure users create complex passwords that are difficult to guess.

**Configure a strong password policy**
 Go to the IAM dashboard and navigate to Account settings. Review the current password policy settings for your account, including minimum length, character types required, and password expiration settings.

 At a minimum, AWS recommends following these best practices when setting your password policy:
+ Require at least one uppercase character.
+ Require at least one lowercase character.
+ Require at least one symbol.
+ Require at least one number.
+ Require at least eight characters.

**Additional security considerations**
 Consider these additional security measures in addition to a strong password policy:
+  MFA adds an additional security layer by requiring an additional form of authentication. This helps prevent unauthorized access even if credentials are compromised.
+  Setting up condition elements to restrict when and how administrative permissions can be used based on factors like source IP or MFA age.

### The IAM user has unrotated access keys
<a name="unrotated-access-keys"></a>

 Access keys consist of an access key ID and a secret access key that enable programmatic access to AWS resources. When access keys remain unchanged for extended periods of time, they increase the risk of unauthorized access if they are compromised. Following security best practices, AWS recommends rotating access keys every 90 days to minimize the window of opportunity for attackers to use compromised credentials.

**Rotate access keys**
 In the exposure finding, open the resource. This will open the user details window. To rotate access keys, see [Manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) in the *IAM User Guide*.

### The IAM user has a policy that allows unrestricted access to KMS key decryption
<a name="unrestricted-kms-decryption-allowed"></a>

 AWS KMS enables you to create and manage cryptographic keys that are used to protect your data. IAM policies that allow unrestricted AWS KMS decryption permissions (e.g., `kms:Decrypt` or `kms:ReEncryptFrom`) on all KMS keys can lead to unauthorized data access if an IAM user’s credentials are compromised. If an attacker gains access to these credentials, they could potentially decrypt any encrypted data in your environment, which could include sensitive data. Following security best practices, AWS recommends implementing least privilege by limiting AWS KMS decryption permissions to only specific keys that users need for their job functions.

**Implement least-privilege access**
 In the exposure finding, open the resource. This will open the IAM Policy window. Look for permissions in KMS that allow kms:Decrypt or `kms:ReEncryptFrom` or `KMS:*` with a resource specification of `"*"`. Update the policy to restrict AWS KMS decryption permissions to only the specific keys needed. Modify the policy to replace the `"*"` resource with the specific ARNs of required AWS KMS keys.

**Secure configuration considerations**
 Consider adding conditions to further restrict when these permissions can be used. For example, you can limit decryption operations to specific VPC endpoints or source IP ranges. You can also configure key policies to further restrict who can use specific KMS keys.

## Unused access traits for IAM users
<a name="iam-user-unused-access"></a>

 When an IAM user has unused permissions, access keys, or passwords, Security Hub may include these as contextual traits in exposure findings for that user. These traits are generated by the service-managed IAM Access Analyzer and provide additional context about the user's security posture. Unused access traits are not the primary cause of the exposure finding, but they indicate that the user has more permissions than needed, which increases the potential impact if the user's credentials are compromised.

 For unused permissions specifically, you can generate a least-privilege policy recommendation that shows you a scoped-down replacement policy. For more information, see [Generating policy recommendations for unused access findings](unused-access-recommendations.md).

## Impact traits for IAM users
<a name="iam-user-impact"></a>

Impact traits describe the potential blast radius of an exposure. Security Hub analyzes the effective permissions of the AWS Identity and Access Management principal associated with the IAM user to determine the downstream resources an attacker could reach if the IAM user is compromised. Each impact trait identifies a specific privilege escalation pattern. To reduce your blast radius, review the permission paths described in each trait and remove any unnecessary privileges.

Following standard security principles, AWS recommends that you grant least privilege — only the permissions required to perform a task. Replace broad policies with scoped-down policies that grant only the specific actions and resources needed. To identify unused permissions to remove, use IAM Access Analyzer to generate recommendations based on access history. For more information, see [Findings for external and unused access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html) and [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the *IAM User Guide*.

### Full control privileged executor
<a name="full-control-privileged-executor"></a>

The associated principal can pass a role to and inject code into a compute resource that already has elevated permissions. This allows the principal to gain full control over the executor and perform any action that the executor's role permits.

### Direct policy escalation
<a name="direct-policy-escalation"></a>

The associated principal can directly modify IAM policies to grant itself additional permissions, escalating its own privileges without intermediate resources.

### Trust policy hijack
<a name="trust-policy-hijack"></a>

The associated principal can modify the trust policy of an IAM role to allow itself to assume that role, gaining the role's permissions.

### Data ransomware
<a name="data-ransomware"></a>

The associated principal can encrypt or delete data in a way that could be used for ransomware, such as encrypting Amazon S3 objects with a customer-managed AWS KMS key and then modifying the key policy.

### Remove restriction
<a name="remove-restriction"></a>

The associated principal can remove security restrictions such as permission boundaries, service control policies, or resource-based policy deny statements, expanding what other principals or the resource itself can do.

### Pass role create executor
<a name="pass-role-create-executor"></a>

The associated principal can create a new compute resource (such as a Lambda function or Amazon EC2 instance) and pass it a privileged role, effectively laundering its own permissions through the new resource.

### Swap role existing executor
<a name="swap-role-existing-executor"></a>

The associated principal can change the IAM role attached to an existing compute resource, replacing it with a more privileged role to escalate access.

### Role chain escalation
<a name="role-chain-escalation"></a>

The associated principal can assume a sequence of roles, where each role in the chain has progressively broader permissions, ultimately reaching a highly privileged role.

### Inject code privileged executor
<a name="inject-code-privileged-executor"></a>

The associated principal can inject code into a running compute resource that has elevated permissions, executing arbitrary operations under that resource's privileged role.

### Disable audit trail
<a name="disable-audit-trail"></a>

The associated principal can disable logging or monitoring services such as CloudTrail, effectively covering its tracks during or after an escalation.

### Access existing executor
<a name="access-existing-executor"></a>

The associated principal can invoke or connect to an existing compute resource and use its attached role to perform privileged actions.

### Credential minting
<a name="credential-minting"></a>

The associated principal can create new long-term credentials (such as access keys or login profiles) for other principals, establishing persistent access paths that survive password rotations or session expirations.

### Pass role data access
<a name="pass-role-data-access"></a>

The associated principal can create a service resource and pass it a role that has access to sensitive data, gaining indirect access to that data through the new resource.

### Pass role task hijack
<a name="pass-role-task-hijack"></a>

The associated principal can pass a role to a scheduled or event-driven task (such as a Lambda function triggered by an event), allowing it to execute arbitrary code with that role's permissions.

### Single hop data access
<a name="single-hop-data-access"></a>

The associated principal can directly access sensitive data resources (such as Amazon S3 buckets or DynamoDB tables) through its existing permissions, without needing intermediate escalation steps.

### Capability advancing
<a name="capability-advancing"></a>

The associated principal has a privilege escalation path that advances its overall capabilities beyond what its directly assigned permissions would suggest. This is a general classification for paths that do not match a more specific pattern.
