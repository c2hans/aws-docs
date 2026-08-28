---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/client-tools-and-libraries.html
---

# Client SDKs for AWS CloudHSM
<a name="client-tools-and-libraries"></a>

When using AWS CloudHSM, you perform cryptographic operations with [AWS CloudHSM Client Software Development Kits (SDKs)](use-hsm.md). AWS CloudHSM Client SDKs include:
+ Public Key Cryptography Standards \#11 (PKCS \#11)
+ JCE provider
+ OpenSSL Dynamic Engine
+ Key Storage Provider (KSP) for Microsoft Windows

You can use any or all of these SDKS in your AWS CloudHSM cluster. Write your application code to use these SDKs to perform cryptographic operations in your HSMs. To see what platforms and HSM types support each SDK, see [AWS CloudHSM Client SDK 5 supported platforms](client-supported-platforms.md)

Utility and command line tools are needed not only to use SDKs but also to configure the credentials, policies, and settings of your application. For more information, refer to [AWS CloudHSM command line tools](command-line-tools.md).

 For more information about installing and using the Client SDK or the security of the client connection, see [Client SDKs](use-hsm.md) and [End-to-end encryption](client-end-to-end-encryption.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
