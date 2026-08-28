---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspacesPoolsFilter.html
---

# DescribeWorkspacesPoolsFilter
<a name="API_DescribeWorkspacesPoolsFilter"></a>

Describes the filter conditions for WorkSpaces Pools to return.

## Contents
<a name="API_DescribeWorkspacesPoolsFilter_Contents"></a>

 ** Name **   <a name="WorkSpaces-Type-DescribeWorkspacesPoolsFilter-Name"></a>
The name of the pool to filter.
Type: String
Valid Values: `PoolName`
Required: Yes

 ** Operator **   <a name="WorkSpaces-Type-DescribeWorkspacesPoolsFilter-Operator"></a>
The operator values for filtering WorkSpaces Pools.
Type: String
Valid Values: `EQUALS | NOTEQUALS | CONTAINS | NOTCONTAINS`
Required: Yes

 ** Values **   <a name="WorkSpaces-Type-DescribeWorkspacesPoolsFilter-Values"></a>
The values for filtering WorkSpaces Pools.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[A-Za-z0-9][A-Za-z0-9_.-]+$`
Required: Yes

## See Also
<a name="API_DescribeWorkspacesPoolsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeWorkspacesPoolsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeWorkspacesPoolsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeWorkspacesPoolsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
