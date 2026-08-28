---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A key-value pair to filter results.

## Contents
<a name="API_Filter_Contents"></a>

 ** Key **   <a name="quicksetup-Type-Filter-Key"></a>
The key for the filter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[A-Za-z0-9+=@_\/\s-]*`
Required: Yes

 ** Values **   <a name="quicksetup-Type-Filter-Values"></a>
The values for the filter keys.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[A-Za-z0-9+=@_\/\s-]*`
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quick Setup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick-setup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
