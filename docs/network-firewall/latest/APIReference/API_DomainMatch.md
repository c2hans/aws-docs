---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DomainMatch.html
---

# DomainMatch

The domains that a [ServerCertificateScope](API_ServerCertificateScope.md) matches for SSL/TLS inspection on a proxy mode firewall.

## Contents
<a name="API_DomainMatch_Contents"></a>

 ** Domains **   <a name="networkfirewall-Type-DomainMatch-Domains"></a>
The domains to match. You can specify an exact domain, such as `example.com`, or a domain with a single leading wildcard label, such as `*.example.com`. You can specify from 1 to 50 domains, and each domain can be up to 255 characters long.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_DomainMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DomainMatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DomainMatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DomainMatch)
