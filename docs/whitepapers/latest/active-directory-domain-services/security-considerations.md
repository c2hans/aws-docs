---
source_url: https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/security-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security considerations
<a name="security-considerations"></a>

## Trust relationships with on-premises Active Directory
<a name="trust-relationships-with-on-premises-active-directory"></a>

 Whether you are deploying Active Directory on EC2 instances or using AWS Managed Microsoft AD, these are the three common deployment patterns seen on AWS.

1.  Deploy a standalone forest/domain on AWS with no trust. In this model, you set up a new forest and domain on AWS which is different and separate from the current Active Directory that is running on-premises. In this deployment, both accounts (user credentials, service accounts) and resources (computer objects) reside in Active Directory running on AWS and most or all of the member servers run on AWS in single or multiple Regions. For this deployment, there is no network connectivity requirement between on-premises and AWS for the purposes of Active Directory as nothing is shared between the two Active Directory forests.

1.  Deploy a new forest/domain on AWS with one-way trust. If you are planning on leveraging credentials from an on-premises Active Directory on AWS member servers, you must establish at least a one-way trust to the Active Directory running on AWS. In this model, the AWS domain becomes the resource domain where computer objects are located and on-premises domain becomes the account domain.

 **Note:** You must have robust connectivity between your data center and AWS. A connectivity issue can break the authentication and make the whole solution not accessible for users. Consider to extend your Active Directory domains to AWS to eliminate dependency on connectivity with on-premises infrastructure or deploy a multi-path AWS Direct Connect or VPN connection.

1.  **Extend your existing domain to AWS**. In this model, you extend your existing Active Directory deployment from on-premises to AWS which means adding additional domain controllers (running on Amazon EC2) to your existing domain and placing them in multiple AZs within your Amazon VPC. If you are operating in multiple Regions, add domain controllers in each of these Regions. This deployment is easy, flexible, and provides the following advantages:
+  You are not required to set up additional trusts.
+  DCs in AWS are handling both accounts and resources.
+  More resilient to network connectivity issues.
+  You can seamlessly set up and use AWS Cloud in a hybrid scenario with least impact to the applications. (Note that network connectivity is required between your data center and AWS for initial and on-going replication of data between the domain controllers.)

 When you use cross-forest trust relationships in Active Directory, you need to use consistent Active Directory site names in both forests to have optimal performance. Refer to the article [Domain Locator Across a Forest Trust](https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/domain-locator-across-a-forest-trust/ba-p/395689) for more information.

 See [How Domain and Forest Trusts Work](https://technet.microsoft.com/pt-pt/library/cc773178(v%3Dws.10).aspx) on the Microsoft Documentation website for more information.

## Multi-factor authentication
<a name="multi-factor-authentication"></a>

 Multi-factor authentication (MFA) is a simple best practice that adds an extra layer of protection on top of your sign-in credentials. With MFA enabled, when users sign in to the AWS Management Console, they are prompted for their sign-in credentials (the first factor—what they “know”), then prompted for an authentication response from their AWS MFA device (the second factor—what they “have”). Taken together, these multiple factors provide increased security for your AWS account settings and resources. We recommend enabling MFA on all of your privileged accounts regardless of whether you are using IAM or federating through SSO.

## AWS account security
<a name="aws-account-security"></a>

 Since you are running your domain controllers on Amazon EC2, securing your AWS account is an important process in securing your Active Directory domain. Follow these recommendations to make sure your AWS account is secure.
+  Enable MFA and then lock away your AWS root user credential
+  Use IAM groups to manage permission if you are using IAM users
+  Grant least privilege to all your users within AWS
+  Enable MFA for all privileged users
+  Use EC2 roles for applications that run on EC2 instances
+  Do not share access keys
+  Rotate credentials regularly
+  Turn on and analyze log files in AWS CloudTrail, VPC Flow Logs and Amazon S3 bucket logs
+  Turn on encryption for data at rest and in transit where necessary

## Domain controller security
<a name="domain-controller-security"></a>

 Domain controllers provide the physical storage for the AD DS database, in addition to providing the services and data that allow enterprises to effectively manage their servers, workstations, users, and applications. If privileged access to a domain controller is obtained by a malicious user, that user can modify, corrupt, or destroy the AD DS database and, by extension, all of the systems and accounts that are managed by Active Directory. Make sure your domain controller is secure to avoid compromising your Active Directory data.

 The following points are some of the best practices to secure domain controllers running on AWS:
+  Secure the AWS account where the domain controllers are running by following least privilege and role-based access control.
+  Ensure unauthorized users don’t have access in your AWS account to create/access Amazon Elastic Block Store (Amazon EBS) snapshots, launch or terminate EC2 Instances, or create/copy EBS volumes.
+  Ensure you are deploying your domain controllers in a private subnet without internet access. Ensure that subnets where domain controllers are running don’t have a route to a NAT gateway or other device that would provide outbound internet access.
+  Keep your security patches up-to-date on your domain controllers. We recommend you first test the security patches in a non-production environment.
+  Restrict ports and protocols that are allowed into the domain controllers by using security groups. Allow remote management like remote desktop protocol (RDP) only from trusted networks.
+  Leverage the Amazon EBS encryption feature to encrypt the root and additional volumes of your domain controllers and use [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms) for key management.
+  Follow [Microsoft-recommended security configuration baselines](https://www.microsoft.com/en-us/download/details.aspx?id=55319) and [Best Practices for Securing Active Directory](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
