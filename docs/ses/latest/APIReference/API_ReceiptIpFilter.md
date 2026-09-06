---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ReceiptIpFilter.html
---

# ReceiptIpFilter
<a name="API_ReceiptIpFilter"></a>

A receipt IP address filter enables you to specify whether to accept or reject mail originating from an IP address or range of IP addresses.

For information about setting up IP address filters, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-ip-filtering-console-walkthrough.html).

## Contents
<a name="API_ReceiptIpFilter_Contents"></a>

 ** Cidr **
A single IP address or a range of IP addresses to block or allow, specified in Classless Inter-Domain Routing (CIDR) notation. An example of a single email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For more information about CIDR notation, see [RFC 2317](https://tools.ietf.org/html/rfc2317).
Type: String
Required: Yes

 ** Policy **
Indicates whether to block or allow incoming mail from the specified IP addresses.
Type: String
Valid Values: `Block | Allow`
Required: Yes

## See Also
<a name="API_ReceiptIpFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ReceiptIpFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ReceiptIpFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ReceiptIpFilter)
