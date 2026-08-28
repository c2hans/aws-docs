---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DBClusterParameterGroup.html
---

# DBClusterParameterGroup
<a name="API_DBClusterParameterGroup"></a>

Contains the details of an Amazon Neptune DB cluster parameter group.

This data type is used as a response element in the [DescribeDBClusterParameterGroups](API_DescribeDBClusterParameterGroups.md) action.

## Contents
<a name="API_DBClusterParameterGroup_Contents"></a>

 ** DBClusterParameterGroupArn **
The Amazon Resource Name (ARN) for the DB cluster parameter group.
Type: String
Required: No

 ** DBClusterParameterGroupName **
Provides the name of the DB cluster parameter group.
Type: String
Required: No

 ** DBParameterGroupFamily **
Provides the name of the DB parameter group family that this DB cluster parameter group is compatible with.
Type: String
Required: No

 ** Description **
Provides the customer-specified description for this DB cluster parameter group.
Type: String
Required: No

## See Also
<a name="API_DBClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DBClusterParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DBClusterParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DBClusterParameterGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
