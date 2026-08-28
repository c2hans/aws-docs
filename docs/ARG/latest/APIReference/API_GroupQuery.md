---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupQuery.html
---

# GroupQuery
<a name="API_GroupQuery"></a>

A mapping of a query attached to a resource group that determines the AWS resources that are members of the group.

## Contents
<a name="API_GroupQuery_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GroupName **   <a name="ARG-Type-GroupQuery-GroupName"></a>
The name of the resource group that is associated with the specified resource query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}`
Required: Yes

 ** ResourceQuery **   <a name="ARG-Type-GroupQuery-ResourceQuery"></a>
The resource query that determines which AWS resources are members of the associated resource group.
Type: [ResourceQuery](API_ResourceQuery.md) object
Required: Yes

## See Also
<a name="API_GroupQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/GroupQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/GroupQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/GroupQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
