---
source_url: https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_ResourceTag.html
---

# ResourceTag
<a name="API_ResourceTag"></a>

[Tag-level retention rules only] Information about the resource tags used to identify resources that are retained by the retention rule.

## Contents
<a name="API_ResourceTag_Contents"></a>

 ** ResourceTagKey **   <a name="recyclebin-Type-ResourceTag-ResourceTagKey"></a>
The tag key.
Type: String
Pattern: `^[\S\s]{1,128}$`
Required: Yes

 ** ResourceTagValue **   <a name="recyclebin-Type-ResourceTag-ResourceTagValue"></a>
The tag value.
Type: String
Pattern: `^[\S\s]{0,256}$`
Required: No

## See Also
<a name="API_ResourceTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rbin-2021-06-15/ResourceTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rbin-2021-06-15/ResourceTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rbin-2021-06-15/ResourceTag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Recycle Bin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recyclebin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
