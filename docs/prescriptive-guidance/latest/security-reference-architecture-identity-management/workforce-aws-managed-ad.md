---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/workforce-aws-managed-ad.html
---

# AWS Managed Microsoft AD
<a name="workforce-aws-managed-ad"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) is an AWS managed service that provides a managed Active Directory solution based on Microsoft Windows Server Active Directory Domain Services (AD DS). The domain controllers run in different Availability Zones in a Region of your choice. Host monitoring and recovery, data replication, snapshots, and software updates are automatically configured and managed for you. You can configure a trust relationship between AWS Managed Microsoft AD in the AWS Cloud and your existing on-premises Microsoft Active Directory. This gives users and groups access to resources in either domain by using IAM Identity Center.

For strict access restriction, you can create a separate AWS account or AWS organizational unit (OU) within your organization for identity services such as Active Directory, including AWS Managed Microsoft AD, and give only a very limited group of administrators access to this account. Generally, we recommend that you treat Active Directory on AWS in the same manner as on-premises Active Directory. Make sure to limit administrative access to the AWS account, similar to how you would limit access to a physical data center. Whoever owns the AWS account that contains Active Directory can own the Active Directory. For more information, see [Design consideration for AWS Managed Microsoft AD](https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/design-consideration-for-aws-managed-microsoft-active-directory.html) in the *Active Directory Domain Services on AWS* whitepaper.

When you use AWS Managed Microsoft AD sharing by using AWS Organizations, you must deploy AWS Managed Microsoft AD to the Org Management account as shown in the following diagram.

![AWS Managed Microsoft AD in Org Management account](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/b586e69e-2989-4b58-b25c-8b67a64b8386.png)

If you use sharing by using the handshake method, where consumer accounts accept the directory sharing request, you can deploy AWS Managed Microsoft AD to any account within or outside your organization in AWS Organizations. In the AWS SRA, AWS Managed Microsoft AD is deployed in the Shared Services account, as shown in the following diagram. This AWS Organizations sharing method makes it easier to share the directory within your organization because you can browse and validate the Active Directory consumer accounts.

![AWS Managed Microsoft AD in Shared Services account.](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/cf401e11-cf93-4966-8763-cf5e803ac600.png)

All AWS services observe a [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/). This model divides the responsibilities for AWS Managed Microsoft AD between AWS and customers.

AWS responsibility:
+ Directory availability
+ Directory patching and service improvements
+ Security of directory infrastructure
+ Domain controller security posture through group policy objects (GPOs) and other methods
+ Improving security posture when needed; for example, for Server Message Block (SMB) version 1 depreciation
+ Management and creation of objects outside the customer's OU

Customer responsibility:
+ Setting fine-grained password policies for users
+ Security of objects within the customer's OU
+ Initializing a directory restore operation
+ Active Directory trust creation and security
+ Server-side and client-side Lightweight Directory Access Protocol (LDAP) over SSL implementation
+ Implementing multi-factor authentication (MFA)
+ Disabling legacy network ciphers and protocols

Based on these responsibilities, you have some influence over the security of your directory. Because AWS provides managed services, it doesn't give customers full control. In this model, the security controls you manage are smaller in scope than for a self-managed Active Directory.

**Design considerations:**
+ Use [fine-grained password policies ](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_password_policies.html)to set advanced password policies. The default password policy in AWS Managed Microsoft AD offers compatibility with this practice, but it is relatively weak because of a short password length. We recommend that you use passwords that contain 15 or more characters so that Active Directory won't store LAN Manager (LM) hashes for your account. For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/prevent-windows-store-lm-hash-password).
+ Disable any unused network and protocol ciphers on AWS Managed Microsoft AD. For details, see [Editing AWS Managed Microsoft AD directory security settings](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_directory_settings.html) in the Directory Service documentation.
+ To further enhance the security of your AWS Managed AD, you can restrict the network ports and sources of the AWS security group that's attached to your AWS Managed Microsoft AD. For more information, see [Enhancing your AWS Managed Microsoft AD network security configuration](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_network_security.html) in the Directory Service documentation.
+ Enable [log forwarding](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_enable_log_forwarding.html) for your AWS Managed Microsoft AD. This allows AWS Managed Microsoft AD to forward the raw Windows security event logs of your AWS Managed Microsoft AD domain controllers to an Amazon CloudWatch log group in your account.
+ Create a group policy object (GPO) that denies domain and enterprise administrators network or remote access rights to domain-joined computer accounts. For more information, see the Microsoft documentation for the security policy settings [Deny log on locally](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/deny-log-on-locally) and [Deny log on through Remote Desktop Services](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/deny-log-on-through-remote-desktop-services).
+ Implement a public key infrastructure (PKI) to issue certificates to their domain controllers to encrypt LDAP traffic. For more information, see the AWS blog post [How to enable server-side LDAPS for your AWS Managed Microsoft AD directory](https://aws.amazon.com/blogs/security/how-to-enable-ldaps-for-your-aws-microsoft-ad-directory/).
+ To establish Active Directory trust relationships with AWS Managed Microsoft AD, create a forest trust. This type of trust allows for maximum Kerberos compatibility. We recommend that you use a one-way trust whenever possible, although some use cases require a two-way trust. Another option for trust security is to enable selective authentication on the trust. When you enable selective authentication, you must set the **Allowed to Authenticate** permission on each computer object the trusted user will access in addition to any other permissions that are required to access the computer object. For details, see the AWS blog post [Everything you wanted to know about trusts with AWS Managed Microsoft AD](https://aws.amazon.com/blogs/security/everything-you-wanted-to-know-about-trusts-with-aws-managed-microsoft-ad/).
+ Each AWS Managed Microsoft AD deployment has an Active Directory account that's provisioned to administer the directory. This account is named *Admin*. After you deploy the directory, we recommend that you create individual Active Directory user accounts for each elevated person who needs to access the directory. After you create these accounts, we recommend that you set the account credentials for the Admin to a random password and store it for break-glass scenarios. Do not use shared or generic accounts such as the Admin account for standard administration. Otherwise, it will be difficult to audit the directory.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
