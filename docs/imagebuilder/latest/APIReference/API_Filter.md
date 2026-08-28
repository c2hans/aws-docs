---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A filter name and value pair that is used to return a more specific list of results from a list operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

## Contents
<a name="API_Filter_Contents"></a>

 ** name **   <a name="imagebuilder-Type-Filter-name"></a>
The name of the filter. Filter names are case-sensitive.
Type: String
Pattern: `^[a-zA-Z]{1,1024}$`
Required: No

 ** values **   <a name="imagebuilder-Type-Filter-values"></a>
The filter values. Filter values are case-sensitive.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `^[0-9a-zA-Z./_ :,{}"-]{1,1024}$`
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
