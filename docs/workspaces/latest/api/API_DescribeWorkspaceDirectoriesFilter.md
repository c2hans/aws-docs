---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceDirectoriesFilter.html
---

# DescribeWorkspaceDirectoriesFilter
<a name="API_DescribeWorkspaceDirectoriesFilter"></a>

Describes the filter conditions for the WorkSpaces to return.

## Contents
<a name="API_DescribeWorkspaceDirectoriesFilter_Contents"></a>

 ** Name **   <a name="WorkSpaces-Type-DescribeWorkspaceDirectoriesFilter-Name"></a>
The name of the WorkSpaces to filter.
Type: String
Valid Values: `USER_IDENTITY_TYPE | WORKSPACE_TYPE`
Required: Yes

 ** Values **   <a name="WorkSpaces-Type-DescribeWorkspaceDirectoriesFilter-Values"></a>
The values for filtering WorkSpaces
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Pattern: `^[0-9a-zA-Z\*\.\\/\?-_]{0,64}$`
Required: Yes

## See Also
<a name="API_DescribeWorkspaceDirectoriesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeWorkspaceDirectoriesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeWorkspaceDirectoriesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeWorkspaceDirectoriesFilter)
