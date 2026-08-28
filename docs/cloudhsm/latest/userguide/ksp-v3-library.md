---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-v3-library.html
---

# Cryptography API: Next Generation (CNG) and key storage providers (KSP) for AWS CloudHSM
<a name="ksp-v3-library"></a>

The AWS CloudHSM client for Windows includes CNG and KSP providers.

*Key storage providers* (KSPs) enable key storage and retrieval. For example, if you add the Microsoft Active Directory Certificate Services (AD CS) role to your Windows server and choose to create a new private key for your certificate authority (CA), you can choose the KSP that will manage key storage. When you configure the AD CS role, you can choose this KSP. For more information, see [Create Windows Server CA](win-ca-overview-sdk5.md#win-ca-setup-sdk5).

*Cryptography API: Next Generation (CNG)* is a cryptographic API specific to the Microsoft Windows operating system. CNG enables developers to use cryptographic techniques to secure Windows-based applications. At a high level, the AWS CloudHSM implementation of CNG provides the following functionality:
+ **Cryptographic Primitives** – enable you to perform fundamental cryptographic operations.
+ **Key Import and Export** – enables you to import and export asymmetric keys.
+ **Data Protection API (CNG DPAPI)** – enables you to easily encrypt and decrypt data.
+ **Key Storage and Retrieval** -–enables you to securely store and isolate the private key of an asymmetric key pair.

**Topics**
+ [Verify the KSP and CNG Providers for AWS CloudHSM](ksp-v3-library-install.md)
+ [Prerequisites for using the AWS CloudHSM Windows Client](ksp-library-prereq.md)
+ [Associate an AWS CloudHSM key with a certificate](ksp-library-associate-key-certificate.md)
+ [Code sample for CNG provider for AWS CloudHSM](ksp-library-sample.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
