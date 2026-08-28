---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_Tag.html
---

# Tag
<a name="API_automation_Tag"></a>

A key-value pair used to categorize and organize AWS resources and automation rules.

## Contents
<a name="API_automation_Tag_Contents"></a>

 ** key **   <a name="computeoptimizer-Type-automation_Tag-key"></a>
The tag key, which can be up to 128 characters long.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w\s\.\-\:\/\=\+\@]+`
Required: Yes

 ** value **   <a name="computeoptimizer-Type-automation_Tag-value"></a>
The tag value, which can be up to 256 characters long.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\w\s\.\-\:\/\=\+\@]*`
Required: Yes

## See Also
<a name="API_automation_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/Tag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
