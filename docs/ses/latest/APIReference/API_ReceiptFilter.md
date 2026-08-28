---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ReceiptFilter.html
---

# ReceiptFilter
<a name="API_ReceiptFilter"></a>

A receipt IP address filter enables you to specify whether to accept or reject mail originating from an IP address or range of IP addresses.

For information about setting up IP address filters, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-ip-filtering-console-walkthrough.html).

## Contents
<a name="API_ReceiptFilter_Contents"></a>

 ** IpFilter **
A structure that provides the IP addresses to block or allow, and whether to block or allow incoming mail from them.
Type: [ReceiptIpFilter](API_ReceiptIpFilter.md) object
Required: Yes

 ** Name **
The name of the IP address filter. The name must meet the following requirements:
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (\_), or dashes (-).
+ Start and end with a letter or number.
+ Contain 64 characters or fewer.
Type: String
Required: Yes

## See Also
<a name="API_ReceiptFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ReceiptFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ReceiptFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ReceiptFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
