---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_RuleConfiguration.html
---

# RuleConfiguration
<a name="API_RuleConfiguration"></a>

Provides configuration information about a rule.

## Contents
<a name="API_RuleConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** contentBlockerRule **   <a name="qbusiness-Type-RuleConfiguration-contentBlockerRule"></a>
A rule for configuring how Amazon Q Business responds when it encounters a a blocked topic.
Type: [ContentBlockerRule](API_ContentBlockerRule.md) object
Required: No

 ** contentRetrievalRule **   <a name="qbusiness-Type-RuleConfiguration-contentRetrievalRule"></a>
Rules for retrieving content from data sources connected to a Amazon Q Business application for a specific topic control configuration.
Type: [ContentRetrievalRule](API_ContentRetrievalRule.md) object
Required: No

## See Also
<a name="API_RuleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/RuleConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/RuleConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/RuleConfiguration)
