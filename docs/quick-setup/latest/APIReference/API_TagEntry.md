---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_TagEntry.html
---

# TagEntry
<a name="API_TagEntry"></a>

Key-value pairs of metadata.

## Contents
<a name="API_TagEntry_Contents"></a>

 ** Key **   <a name="quicksetup-Type-TagEntry-Key"></a>
The key for the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9 _=@:.+-/]+`
Required: No

 ** Value **   <a name="quicksetup-Type-TagEntry-Value"></a>
The value for the tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[A-Za-z0-9 _=@:.+-/]+`
Required: No

## See Also
<a name="API_TagEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/TagEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/TagEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/TagEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quick Setup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick-setup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
