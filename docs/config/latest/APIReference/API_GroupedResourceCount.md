---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GroupedResourceCount.html
---

# GroupedResourceCount
<a name="API_GroupedResourceCount"></a>

The count of resources that are grouped by the group name.

## Contents
<a name="API_GroupedResourceCount_Contents"></a>

 ** GroupName **   <a name="config-Type-GroupedResourceCount-GroupName"></a>
The name of the group that can be region, account ID, or resource type. For example, region1, region2 if the region was chosen as `GroupByKey`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ResourceCount **   <a name="config-Type-GroupedResourceCount-ResourceCount"></a>
The number of resources in the group.
Type: Long
Required: Yes

## See Also
<a name="API_GroupedResourceCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GroupedResourceCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GroupedResourceCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GroupedResourceCount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
