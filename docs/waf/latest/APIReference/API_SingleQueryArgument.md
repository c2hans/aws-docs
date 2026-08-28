---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_SingleQueryArgument.html
---

# SingleQueryArgument
<a name="API_SingleQueryArgument"></a>

Inspect one query argument in the web request, identified by name, for example *UserName* or *SalesRegion*. The name isn't case sensitive.

This is used to indicate the web request component to inspect, in the [FieldToMatch](API_FieldToMatch.md) specification.

Example JSON: `"SingleQueryArgument": { "Name": "myArgument" }`

## Contents
<a name="API_SingleQueryArgument_Contents"></a>

 ** Name **   <a name="WAF-Type-SingleQueryArgument-Name"></a>
The name of the query argument to inspect.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_SingleQueryArgument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/SingleQueryArgument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/SingleQueryArgument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/SingleQueryArgument)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
