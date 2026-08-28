---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_IndexingRuleValue.html
---

# IndexingRuleValue
<a name="API_IndexingRuleValue"></a>

 The indexing rule configuration.

## Contents
<a name="API_IndexingRuleValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Probabilistic **   <a name="xray-Type-IndexingRuleValue-Probabilistic"></a>
 Indexing rule configuration that is used to probabilistically sample traceIds.
Type: [ProbabilisticRuleValue](API_ProbabilisticRuleValue.md) object
Required: No

## See Also
<a name="API_IndexingRuleValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/IndexingRuleValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/IndexingRuleValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/IndexingRuleValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
