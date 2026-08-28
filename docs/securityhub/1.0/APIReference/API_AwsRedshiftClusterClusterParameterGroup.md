---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRedshiftClusterClusterParameterGroup.html
---

# AwsRedshiftClusterClusterParameterGroup
<a name="API_AwsRedshiftClusterClusterParameterGroup"></a>

A cluster parameter group that is associated with an Amazon Redshift cluster.

## Contents
<a name="API_AwsRedshiftClusterClusterParameterGroup_Contents"></a>

 ** ClusterParameterStatusList **   <a name="securityhub-Type-AwsRedshiftClusterClusterParameterGroup-ClusterParameterStatusList"></a>
The list of parameter statuses.
Type: Array of [AwsRedshiftClusterClusterParameterStatus](API_AwsRedshiftClusterClusterParameterStatus.md) objects
Required: No

 ** ParameterApplyStatus **   <a name="securityhub-Type-AwsRedshiftClusterClusterParameterGroup-ParameterApplyStatus"></a>
The status of updates to the parameters.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ParameterGroupName **   <a name="securityhub-Type-AwsRedshiftClusterClusterParameterGroup-ParameterGroupName"></a>
The name of the parameter group.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRedshiftClusterClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRedshiftClusterClusterParameterGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRedshiftClusterClusterParameterGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRedshiftClusterClusterParameterGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
