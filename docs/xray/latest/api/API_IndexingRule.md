---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_IndexingRule.html
---

# IndexingRule
<a name="API_IndexingRule"></a>

 Rule used to determine the server-side sampling rate for spans ingested through the CloudWatchLogs destination and indexed by X-Ray.

## Contents
<a name="API_IndexingRule_Contents"></a>

 ** ModifiedAt **   <a name="xray-Type-IndexingRule-ModifiedAt"></a>
 Displays when the rule was last modified, in Unix time seconds.
Type: Timestamp
Required: No

 ** Name **   <a name="xray-Type-IndexingRule-Name"></a>
 The name of the indexing rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** Rule **   <a name="xray-Type-IndexingRule-Rule"></a>
 The indexing rule.
Type: [IndexingRuleValue](API_IndexingRuleValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_IndexingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/IndexingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/IndexingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/IndexingRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
