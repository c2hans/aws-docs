---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/certificate-based-access-controls/concepts.html
---

# Key concepts for using certificate-based access controls in AWS
<a name="concepts"></a>

Certificate-based access controls in AWS require understanding several interdependent authentication and authorization concepts. For example, the principle of least privilege determines the scope of permissions granted through certificate-based authentication, which directly affects AWS Identity and Access Management (IAM) role and policy design. Certificate-based authentication itself relies on digital certificate (X.509 or ML-DSA) validation against configured trust anchors, which define the cryptographic trust chain for certificate verification. The temporary security credentials generated through this process have specific lifecycle characteristics that impact session management and credential rotation strategies. Additionally, AWS Identity and Access Management Roles Anywhere implements a dual-layer permission model where both IAM role policies and profile configurations must authorize access. Without understanding how these concepts interact, implementations can result in authentication failures, over-privileged access, or security gaps in the certificate-validation chain. These concepts form the technical foundation required to correctly configure trust relationships, permission boundaries, and credential lifecycles in certificate-based AWS access control systems.

**This section contains the following topics:**
+ [Least privilege](#concepts-least-privilege)
+ [Certificate-based authentication](#concepts-certificate-based-authentication)
+ [Trust anchors and trust models](#concepts-trust-models)
+ [Temporary security credentials](#concepts-temp-sec-creds)
+ [Dual-layer permissions in IAM](#concepts-dual-layers-permissions)
+ [AWS Credential Helper](#concepts-credential-helper)

## Least privilege
<a name="concepts-least-privilege"></a>

The principle of* least privilege* is a security concept that advises granting the minimal level of access (or *permissions*) necessary for users, programs, or systems to perform their tasks. The guiding philosophy is simple—the fewer permissions an entity has, the lower the risk of malicious or accidental damage.

In the context of AWS, this principle is particularly relevant. AWS provides a wide range of resources and services, from virtual machines to storage resources. As you build and manage your AWS infrastructure, applying the principle of least privilege makes sure that each entity (a user, service, or application) has only the permissions necessary to function correctly, and nothing more.

Implementing the least privilege in AWS offers the following benefits:
+ **Security** – By limiting access, you reduce the potential impact of a security breach. If a user or service has minimum permissions, then the scope for damage is significantly reduced.
+ **Compliance** – Many regulatory frameworks require strict access controls. Adhering to the least privilege principle helps you meet these compliance requirements.
+ **Operational simplicity** – Managing permissions can become complex. Applying least privilege can keep configurations as simple and as manageable as possible.

## Certificate-based authentication
<a name="concepts-certificate-based-authentication"></a>

Certificate-based authentication uses digital certificates to verify the identity of a device, service, or application. Digital certificates (X.509 or ML-DSA) contain attributes that identify the entity and are signed by a trusted certificate authority. This authentication method eliminates the need for static credentials and provides a cryptographically secure way to establish trust.

Whereas identity-based authentication relies on credentials that are directly associated with an IAM [role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) or [user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html), certificate-based authentication uses digital certificates (X.509 or ML-DSA) to establish identity. Certificate-based authentication offers advantages in hybrid environments by providing a stronger security posture, automated credential rotation, and the ability to encode attributes that can be used for fine-grained access control.

## Trust anchors and trust models
<a name="concepts-trust-models"></a>

You establish trust between IAM Roles Anywhere and your certificate authority (CA) by creating a *trust anchor*. A trust anchor is a reference to either [AWS Private CA](https://docs.aws.amazon.com/acm-pca/latest/userguide/PcaWelcome.html) or an external CA source. Your workloads outside of AWS authenticate with the trust anchor by using certificates that are issued by the trusted CA in exchange for temporary AWS credentials. There can be several trust anchors in one AWS account. For more information, see [IAM Roles Anywhere trust model](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/trust-model.html). The *trust model* defines how certificates are validated and which certificate attributes are required for successful authentication.

## Temporary security credentials
<a name="concepts-temp-sec-creds"></a>

*Temporary security credentials* provide time-limited access to AWS resources, typically lasting from a few minutes to several hours. Unlike long-term access keys, these credentials automatically expire. This significantly reduces the risk of credential compromise and simplifies access management across distributed systems. For more information about temporary credentials, see the [Require workloads to use temporary credentials with IAM roles to access AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-workloads-use-roles) best practice in the IAM documentation.

## Dual-layer permissions in IAM
<a name="concepts-dual-layers-permissions"></a>

IAM Roles Anywhere implements a dual-layer permission model through the combination of IAM roles and profiles. In a *profile*, you can define IAM session policies that limit the permissions created for a session. A profile can have many IAM roles but only one session policy. The dual-layer permission model provides enhanced security by requiring permissions to be explicitly allowed at both layers before access is granted. The following are the two layers:
+ The *IAM roles layer* defines the following:
  + Trust policies that determine which entity can assume the role
  + Permission policies that specify which AWS resources the role can access and which actions it can perform
  + Condition elements that can further restrict access based on specific criteria
+ The *IAM Roles Anywhere profiles layer* does the following:
  + Defines which IAM roles can be assumed through IAM Roles Anywhere
  + Provides additional controls for role assumption
  + Act as a permission filter, even if the IAM role itself allows broader access

For example, if an IAM role allows access to Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB but the profile allows only Amazon S3 access, the application can access only Amazon S3 resources. This dual-layer approach enforces the principle of least privilege by requiring explicit permission in both layers.

## AWS Credential Helper
<a name="concepts-credential-helper"></a>

By using [Credential Helper](https://github.com/aws/rolesanywhere-credential-helper) (GitHub) for IAM Roles Anywhere, you define through the AWS Command Line Interface (AWS CLI) which trust anchor, profile, and role you want to use when allowing the application to access the AWS resources. The following is an example call that uses the AWS Credential Helper tool:

```
./aws_signing_helper credential-process
   \--certificate <Path to certificate>
   \--private-key <Path to private key>
   \--trust-anchor-arn <Trust anchor ARN>
   \--profile-arn <Profile 1 ARN>
   \--role-arn <Role 1 ARN>
```

This tool is compatible with the `credential_process` feature available across the language SDKs. When used with an AWS SDK, these credentials automatically refresh before they expire, requiring no additional implementation for credential renewal. Credential Helper manages the process of creating a signature with the certificate and calling the endpoint to obtain session credentials. Then, it returns the temporary security credentials to the calling process in a standard JSON format.

For more information, see [Get temporary security credentials from IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/credential-helper.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
