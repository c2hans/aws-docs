---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ResourceCount.html
---

# ResourceCount
<a name="API_ResourceCount"></a>

Information about the number of results that match the query. At this time, AWS Resource Explorer doesn't count more than 1,000 matches for any query. This structure provides information about whether the query exceeded this limit.

This field is included in every page when you paginate the results.

## Contents
<a name="API_ResourceCount_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Complete **   <a name="resourceexplorer-Type-ResourceCount-Complete"></a>
Indicates whether the `TotalResources` value represents an exhaustive count of search results.
+ If `True`, it indicates that the search was exhaustive. Every resource that matches the query was counted.
+ If `False`, then the search reached the limit of 1,000 matching results, and stopped counting.
Type: Boolean
Required: No

 ** TotalResources **   <a name="resourceexplorer-Type-ResourceCount-TotalResources"></a>
The number of resources that match the search query. This value can't exceed 1,000. If there are more than 1,000 resources that match the query, then only 1,000 are counted and the `Complete` field is set to false. We recommend that you refine your query to return a smaller number of results.
Type: Long
Required: No

## See Also
<a name="API_ResourceCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/ResourceCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/ResourceCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/ResourceCount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
