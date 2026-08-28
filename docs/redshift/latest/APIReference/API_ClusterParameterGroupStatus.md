---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ClusterParameterGroupStatus.html
---

# ClusterParameterGroupStatus
<a name="API_ClusterParameterGroupStatus"></a>

Describes the status of a parameter group.

## Contents
<a name="API_ClusterParameterGroupStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClusterParameterStatusList.member.N **
The list of parameter statuses.
 For more information about parameters and parameter groups, go to [Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Cluster Management Guide*.
Type: Array of [ClusterParameterStatus](API_ClusterParameterStatus.md) objects
Required: No

 ** ParameterApplyStatus **
The status of parameter updates.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ParameterGroupName **
The name of the cluster parameter group.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

## See Also
<a name="API_ClusterParameterGroupStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterParameterGroupStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterParameterGroupStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterParameterGroupStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
