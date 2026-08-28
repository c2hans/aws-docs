---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceMapFilter.html
---

# ResourceMapFilter
<a name="API_ResourceMapFilter"></a>

A resource map filter for a software bill of material report.

## Contents
<a name="API_ResourceMapFilter_Contents"></a>

 ** comparison **   <a name="inspector2-Type-ResourceMapFilter-comparison"></a>
The filter's comparison.
Type: String
Valid Values: `EQUALS`
Required: Yes

 ** key **   <a name="inspector2-Type-ResourceMapFilter-key"></a>
The filter's key.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** value **   <a name="inspector2-Type-ResourceMapFilter-value"></a>
The filter's value.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ResourceMapFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ResourceMapFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ResourceMapFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ResourceMapFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
