---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_TagFilter.html
---

# TagFilter
<a name="API_TagFilter"></a>

The tag filter. Valid names are: `tagKey`, `tagValue`, `configurationId`.

## Contents
<a name="API_TagFilter_Contents"></a>

 ** name **   <a name="DiscServ-Type-TagFilter-name"></a>
A name of the tag filter.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\s\S]*\S[\s\S]*`
Required: Yes

 ** values **   <a name="DiscServ-Type-TagFilter-values"></a>
Values for the tag filter. The length constraint is 1000 characters per value. The maximum number of values is 50.
Type: Array of strings
Length Constraints: Maximum length of 1000.
Pattern: `(^$|[\s\S]*\S[\s\S]*)`
Required: Yes

## See Also
<a name="API_TagFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/TagFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/TagFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/TagFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
