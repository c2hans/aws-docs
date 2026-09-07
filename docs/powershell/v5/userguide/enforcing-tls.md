---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/enforcing-tls.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Enforcing a minimum TLS version in the Tools for PowerShell
<a name="enforcing-tls"></a>

To increase security when communicating with AWS services, you should configure the Tools for PowerShell to use the appropriate TLS version. For information about how to do this, see [Enforcing a minimum TLS version](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/enforcing-tls.html#enforcing-tls-ps) in the [AWS SDK for .NET Developer Guide](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/).

TLS 1.3 is the prerequisite to enable post-quantum cryptography, which may require additional actions or configurations. To learn more, see [Enabling hybrid post-quantum TLS](https://docs.aws.amazon.com/sdkref/latest/guide/pqtls-details.html) in the *AWS SDKs and Tools Reference Guide*.
