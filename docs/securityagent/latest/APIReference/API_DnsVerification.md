---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_DnsVerification.html
---

# DnsVerification
<a name="API_DnsVerification"></a>

Contains DNS verification details for a target domain, including the DNS record to create for domain ownership verification.

## Contents
<a name="API_DnsVerification_Contents"></a>

 ** dnsRecordName **   <a name="securityagent-Type-DnsVerification-dnsRecordName"></a>
The name of the DNS record to create for verification.
Type: String
Required: No

 ** dnsRecordType **   <a name="securityagent-Type-DnsVerification-dnsRecordType"></a>
The type of DNS record to create. Currently, only TXT is supported.
Type: String
Valid Values: `TXT`
Required: No

 ** token **   <a name="securityagent-Type-DnsVerification-token"></a>
The verification token to include in the DNS record value.
Type: String
Required: No

## See Also
<a name="API_DnsVerification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/DnsVerification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/DnsVerification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/DnsVerification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
