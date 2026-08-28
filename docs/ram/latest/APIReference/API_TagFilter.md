---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_TagFilter.html
---

# TagFilter
<a name="API_TagFilter"></a>

A tag key and optional list of possible values that you can use to filter results for tagged resources.

**Note**
Multiple tag filters are evaluated as an OR condition.

## Contents
<a name="API_TagFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** tagKey **   <a name="ram-Type-TagFilter-tagKey"></a>
The tag key. This must have a valid string value and can't be empty.
Type: String
Required: No

 ** tagValues **   <a name="ram-Type-TagFilter-tagValues"></a>
A list of zero or more tag values. If no values are provided, then the filter matches any tag with the specified key, regardless of its value.
Type: Array of strings
Required: No

## See Also
<a name="API_TagFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/TagFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/TagFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/TagFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
