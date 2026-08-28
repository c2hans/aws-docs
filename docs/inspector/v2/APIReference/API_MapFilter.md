---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_MapFilter.html
---

# MapFilter
<a name="API_MapFilter"></a>

An object that describes details of a map filter.

## Contents
<a name="API_MapFilter_Contents"></a>

 ** comparison **   <a name="inspector2-Type-MapFilter-comparison"></a>
The operator to use when comparing values in the filter.
Type: String
Valid Values: `EQUALS`
Required: Yes

 ** key **   <a name="inspector2-Type-MapFilter-key"></a>
The tag key used in the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** value **   <a name="inspector2-Type-MapFilter-value"></a>
The tag value used in the filter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_MapFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/MapFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/MapFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/MapFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
