---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sdk5-advanced-configs.html
---

# Advanced configurations for the Client SDK 5 configure tool
<a name="configure-sdk5-advanced-configs"></a>

The AWS CloudHSM Client SDK 5 configure tool includes advanced configurations that are not part of the general features most customers utilize. Advanced configurations provide additional capabilities.

**Important**
After making any changes to your configuration, you need to restart your application for the changes to take effect.
+ Advanced configurations for PKCS \#11
  + [Multiple slot configuration with PKCS \#11 library for AWS CloudHSM](pkcs11-library-configs-multi-slot.md)
  + [Retry commands for PKCS \#11 library for AWS CloudHSM](pkcs11-library-configs-retry.md)
+ Advanced configurations for OpenSSL
  + [Retry commands for OpenSSL for AWS CloudHSM](openssl-library-configs-retry.md)
+ Advanced configurations for KSP
  + [SDK3 compatibility mode for Key Storage Provider (KSP) for AWS CloudHSM](ksp-library-configs-sdk3-compatibility-mode.md)
+ Advanced configurations for JCE
  + [Connecting to multiple AWS CloudHSM clusters with the JCE provider](java-lib-configs-multi.md)
  + [Retry commands for JCE for AWS CloudHSM](java-lib-configs-retry.md)
  + [Key extraction using JCE for AWS CloudHSM](java-lib-configs-getencoded.md)
+ Advanced configurations for AWS CloudHSM Command Line Interface (CLI)
  + [Connecting to multiple clusters with CloudHSM CLI](cloudhsm_cli-configs-multi-cluster.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
