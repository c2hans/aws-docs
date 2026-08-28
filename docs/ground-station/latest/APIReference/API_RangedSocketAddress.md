---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_RangedSocketAddress.html
---

# RangedSocketAddress
<a name="API_RangedSocketAddress"></a>

A socket address with a port range.

## Contents
<a name="API_RangedSocketAddress_Contents"></a>

 ** name **   <a name="groundstation-Type-RangedSocketAddress-name"></a>
IPv4 socket address.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 16.
Pattern: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`
Required: Yes

 ** portRange **   <a name="groundstation-Type-RangedSocketAddress-portRange"></a>
Port range of a socket address.
Type: [IntegerRange](API_IntegerRange.md) object
Required: Yes

## See Also
<a name="API_RangedSocketAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/RangedSocketAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/RangedSocketAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/RangedSocketAddress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
