---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ClusterSecurityGroup.html
---

# ClusterSecurityGroup
<a name="API_ClusterSecurityGroup"></a>

Describes a security group.

## Contents
<a name="API_ClusterSecurityGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClusterSecurityGroupName **
The name of the cluster security group to which the operation was applied.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Description **
A description of the security group.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** EC2SecurityGroups.EC2SecurityGroup.N **
A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.
Type: Array of [EC2SecurityGroup](API_EC2SecurityGroup.md) objects
Required: No

 ** IPRanges.IPRange.N **
A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group.
Type: Array of [IPRange](API_IPRange.md) objects
Required: No

 ** Tags.Tag.N **
The list of tags for the cluster security group.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ClusterSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterSecurityGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterSecurityGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterSecurityGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
