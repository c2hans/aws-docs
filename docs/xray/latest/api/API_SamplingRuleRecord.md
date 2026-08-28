---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_SamplingRuleRecord.html
---

# SamplingRuleRecord
<a name="API_SamplingRuleRecord"></a>

A [SamplingRule](https://docs.aws.amazon.com/xray/latest/api/API_SamplingRule.html) and its metadata.

## Contents
<a name="API_SamplingRuleRecord_Contents"></a>

 ** CreatedAt **   <a name="xray-Type-SamplingRuleRecord-CreatedAt"></a>
When the rule was created, in Unix time seconds.
Type: Timestamp
Required: No

 ** ModifiedAt **   <a name="xray-Type-SamplingRuleRecord-ModifiedAt"></a>
When the rule was last modified, in Unix time seconds.
Type: Timestamp
Required: No

 ** SamplingRule **   <a name="xray-Type-SamplingRuleRecord-SamplingRule"></a>
The sampling rule.
Type: [SamplingRule](API_SamplingRule.md) object
Required: No

## See Also
<a name="API_SamplingRuleRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/SamplingRuleRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/SamplingRuleRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/SamplingRuleRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
