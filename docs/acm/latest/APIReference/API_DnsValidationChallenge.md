---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_DnsValidationChallenge.html
---

# DnsValidationChallenge
<a name="API_DnsValidationChallenge"></a>

Contains the CNAME record that you must add to your DNS configuration to validate domain ownership using DNS validation.

## Contents
<a name="API_DnsValidationChallenge_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ResourceRecord **   <a name="ACM-Type-DnsValidationChallenge-ResourceRecord"></a>
The CNAME record that ACM creates for DNS validation. Add this record to your DNS configuration to prove that you own or control the domain.
Type: [ResourceRecord](API_ResourceRecord.md) object
Required: No

## See Also
<a name="API_DnsValidationChallenge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/DnsValidationChallenge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/DnsValidationChallenge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/DnsValidationChallenge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
