---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/system-authentication.html
---

# SAP system authentication on AWS
<a name="system-authentication"></a>

Before an SAP system can make calls to AWS on behalf of SAP users, the SAP system must authenticate itself to AWS. AWS SDK for SAP ABAP supports the following three base authentication methods that are selected in the SDK profile settings in `IMG`.

AWS SDK for SAP ABAP - BTP edition can only be authenticated with the [Secret access key authentication](#key-authentication) method using SAP Credential Store.

For cross-account access scenarios, SDK for SAP ABAP also supports source profile, which enables chaining multiple IAM role assumptions across accounts using any of the base authentication methods. For more information, see [Source profile authentication for cross-account access](#source-profile-auth).

**Topics**
+ [Amazon EC2 instance metadata authentication](#metadata-authentication)
+ [Secret access key authentication](#key-authentication)
+ [Certificate-based authentication using IAM Roles Anywhere](#iam-auth)
+ [Source profile authentication for cross-account access](#source-profile-auth)
+ [Next step](#next-step)

## Amazon EC2 instance metadata authentication
<a name="metadata-authentication"></a>

SAP systems running on Amazon EC2 can acquire short-lived, automatically-rotating credentials from Amazon EC2 instance metadata. For more information, see [Using credentials for Amazon EC2 instance metadata](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-metadata.html).

We strongly recommend this method of authentication while using SDK for SAP ABAP. To enable, the Basis administrator must enable outbound HTTP communication. No further Basis configuration is required.

**Note**
This method of authentication applies only if your SAP systems are running on Amazon EC2. SAP systems hosted on-premises or in other cloud environments cannot authenticate using this method.

## Secret access key authentication
<a name="key-authentication"></a>

With this method, you use an Access Key ID and a Secret Access Key to authenticate your SAP system on AWS. The SAP system logs into AWS using an IAM user. For more information, see [Managing Access Keys for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

The Basis administrator receives an Access Key ID and a Secret Access Key from the AWS IAM administrator. Your SAP system must be configured to store the Access Key ID and Secret Access Key.
+ **Secure, store, and forward (SSF)**
  + Use the SSF functionality to authenticate AWS SDK for SAP ABAP. For more information, see [Digital Signatures and Encryption](https://help.sap.com/docs/SAP_NETWEAVER_750/cf1026f0534f408e849ee7feed288a66/53251a355d0c4d78e10000009b38f83b.html).
  + You can also test SSF’s `envelope` and `develope` functionality with the `SSF02` report. For more information, see [Testing the SSF Installation](https://help.sap.com/docs/SAP_NETWEAVER_750/cf1026f0534f408e849ee7feed288a66/43b948d4f32c11d2a6100000e835363f.html).
  + The steps for configuring SSF for SDK for SAP ABAP are described in the `/AWS1/IMG` transaction. Go to **Technical Prerequisites**, and then select **Additional Settings** for On-Premises Systems. For detailed configuration steps, see [Using Secret Access Key Authentication with SSF Encryption](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/ssf-authentication.html).
+ **SAP Credential Store**
  + Use SAP Credential Store to authenticate AWS SDK for SAP ABAP - BTP edition. For more information, see [What Is SAP Credential Store?](https://help.sap.com/docs/credential-store/sap-credential-store/what-is-sap-credential-store)
  + See [Using SAP Credential Store](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/credential-store.html) for configuration steps.

## Certificate-based authentication using IAM Roles Anywhere
<a name="iam-auth"></a>

An X.509 certificate issued by your certificate authority (CA) can be used for authentication with AWS Identity and Access Management Roles Anywhere. The certificate must be configured in `STRUST`. The CA must be registered with IAM Roles Anywhere as a trust anchor, and a profile must be created to specify the roles and policies that IAM Roles Anywhere would assume. For more information, see [Creating a trust anchor and profile in AWS Identity and Access Management Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/getting-started.html).

For detailed steps on how to use IAM Roles Anywhere with SDK for SAP ABAP, see [Using certificates with IAM Roles Anywhere](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/using-iam.html).

**Note**
Certificate revocation is only supported through the use of imported certificate revocation lists. For more information, see [Revocation](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/trust-model.html#revocationenecccbjjgtgentfriblgthntkkbilrejgclhlttdlff           ).

## Source profile authentication for cross-account access
<a name="source-profile-auth"></a>

Source profile is an advanced feature that enables you to chain multiple IAM role assumptions across AWS accounts. With this method, one profile assumes a role, which then assumes another role, and so on, similar to the `source_profile` parameter in AWS CLI.

Source profile works with any of the three base authentication methods (instance metadata, secret access key, or certificate-based). The first profile in the chain must use one of these base methods, and subsequent profiles in the chain use the credentials from the previous profile to assume the next role.

This is useful for cross-account access scenarios where you need to traverse multiple AWS accounts to reach your target resources. For detailed configuration steps, see [Using Source Profile for Cross-Account Access](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/source-profile.html).

## Next step
<a name="next-step"></a>

After authenticating your SAP system in AWS, SDK for SAP ABAP automatically performs an `sts:assumeRole` to assume the appropriate IAM role for the SAP user’s business function.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
