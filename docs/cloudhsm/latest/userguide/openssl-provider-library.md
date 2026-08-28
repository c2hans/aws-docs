---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-provider-library.html
---

# OpenSSL Provider for AWS CloudHSM Client SDK 5
<a name="openssl-provider-library"></a>

The AWS CloudHSM OpenSSL Provider allows you to offload TLS cryptographic operations to your CloudHSM cluster through the OpenSSL Provider API. The Provider interface is the recommended approach for new deployments using OpenSSL 3.2 and later.

Use the following sections to install and configure the AWS CloudHSM OpenSSL Provider, using Client SDK 5.

**OpenSSL version requirement for ML-DSA**
ML-DSA key types require OpenSSL 3.5 or later.

## Supported platforms
<a name="openssl-provider-supported-platforms"></a>

The OpenSSL Provider requires OpenSSL 3.2 or later, available on EL9\+, EL10\+, Ubuntu 26.04 LTS, and Amazon Linux 2023\+.

Verify compatibility: `openssl version`

**Topics**
+ [Supported platforms](#openssl-provider-supported-platforms)
+ [Install the OpenSSL Provider for AWS CloudHSM Client SDK 5](openssl-provider-install.md)
+ [Supported key types for OpenSSL Provider for AWS CloudHSM Client SDK 5](openssl-provider-key-types.md)
+ [OpenSSL Provider Supported Mechanisms](openssl-provider-mechanisms.md)
+ [OpenSSL Provider Advanced Configuration](openssl-provider-advanced-config.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
