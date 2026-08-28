---
source_url: https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_Tag.html
---

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/).

# Tag
<a name="API_Tag"></a>

A tag is a key-value pair that can be added to a resource as metadata.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="LookoutForEquipment-Type-Tag-Key"></a>
The key for the specified tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Required: Yes

 ** Value **   <a name="LookoutForEquipment-Type-Tag-Value"></a>
The value for the specified tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\w+-=\.:/@]*`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/Tag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lookout for Equipment. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lookout-for-equipment` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
