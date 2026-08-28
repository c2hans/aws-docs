---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ContextKeySelector.html
---

# ContextKeySelector
<a name="API_ContextKeySelector"></a>

An object that contains information types to be included in CloudTrail enriched events.

## Contents
<a name="API_ContextKeySelector_Contents"></a>

 ** Equals **   <a name="awscloudtrail-Type-ContextKeySelector-Equals"></a>
A list of keys defined by Type to be included in CloudTrail enriched events.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Type **   <a name="awscloudtrail-Type-ContextKeySelector-Type"></a>
Specifies the type of the event record field in ContextKeySelector. Valid values include RequestContext, TagContext.
Type: String
Valid Values: `TagContext | RequestContext`
Required: Yes

## See Also
<a name="API_ContextKeySelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ContextKeySelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ContextKeySelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ContextKeySelector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
