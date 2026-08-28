---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A filter that can use conditional operators.

For more information about filters, see [Querying Discovered Configuration Items](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html) in the * AWS Application Discovery Service User Guide*.

## Contents
<a name="API_Filter_Contents"></a>

 ** condition **   <a name="DiscServ-Type-Filter-condition"></a>
A conditional operator. The following operators are valid: EQUALS, NOT\_EQUALS, CONTAINS, NOT\_CONTAINS. If you specify multiple filters, the system utilizes all filters as though concatenated by *AND*. If you specify multiple values for a particular filter, the system differentiates the values using *OR*. Calling either *DescribeConfigurations* or *ListConfigurations* returns attributes of matching configuration items.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S+`
Required: Yes

 ** name **   <a name="DiscServ-Type-Filter-name"></a>
The name of the filter.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`
Required: Yes

 ** values **   <a name="DiscServ-Type-Filter-values"></a>
A string value on which to filter. For example, if you choose the `destinationServer.osVersion` filter name, you could specify `Ubuntu` for the value.
Type: Array of strings
Length Constraints: Maximum length of 1000.
Pattern: `(^$|[\s\S]*\S[\s\S]*)`
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
