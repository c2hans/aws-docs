---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupFilter.html
---

# GroupFilter
<a name="API_GroupFilter"></a>

A filter collection that you can use to restrict the results from a `List` operation to only those you want to include.

## Contents
<a name="API_GroupFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="ARG-Type-GroupFilter-Name"></a>
The name of the filter. Filter names are case-sensitive.
Type: String
Valid Values: `resource-type | configuration-type | owner | display-name | criticality`
Required: Yes

 ** Values **   <a name="ARG-Type-GroupFilter-Values"></a>
One or more filter values. Allowed filter values vary by group filter name, and are case-sensitive.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `AWS::(AllSupported|[a-zA-Z0-9]+::[a-zA-Z0-9]+)|[\s\p{L}0-9_\.-]*`
Required: Yes

## See Also
<a name="API_GroupFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/GroupFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/GroupFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/GroupFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
