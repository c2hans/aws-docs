---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecord.html
---

# ResourceRecord
<a name="API_ResourceRecord"></a>

Information specific to the resource record.

**Note**
If you're creating an alias resource record set, omit `ResourceRecord`.

## Contents
<a name="API_ResourceRecord_Contents"></a>

 ** Value **   <a name="Route53-Type-ResourceRecord-Value"></a>
The current or new DNS record value, not to exceed 4,000 characters. In the case of a `DELETE` action, if the current value does not match the actual value, an error is returned. For descriptions about how to format `Value` for different record types, see [Supported DNS Resource Record Types](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html) in the *Amazon Route 53 Developer Guide*.
You can specify more than one value for all record types except `CNAME` and `SOA`.
If you're creating an alias resource record set, omit `Value`.
Type: String
Length Constraints: Maximum length of 4000.
Required: Yes

## See Also
<a name="API_ResourceRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ResourceRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ResourceRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ResourceRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
