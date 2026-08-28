---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ResourceTag.html
---

# ResourceTag
<a name="API_ResourceTag"></a>

The resource tag of the project.

## Contents
<a name="API_ResourceTag_Contents"></a>

 ** key **   <a name="datazone-Type-ResourceTag-key"></a>
The key of the resource tag of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w \.:/=+@-]+`
Required: Yes

 ** source **   <a name="datazone-Type-ResourceTag-source"></a>
The source of the resource tag of the project.
Type: String
Valid Values: `PROJECT | PROJECT_PROFILE`
Required: Yes

 ** value **   <a name="datazone-Type-ResourceTag-value"></a>
The value of the resource tag of the project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\w \.:/=+@-]*`
Required: Yes

## See Also
<a name="API_ResourceTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ResourceTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ResourceTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ResourceTag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
