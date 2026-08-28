---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_SecurityGroupMembership.html
---

# SecurityGroupMembership
<a name="API_SecurityGroupMembership"></a>

Represents a single cache security group and its status.

## Contents
<a name="API_SecurityGroupMembership_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SecurityGroupId **
The identifier of the cache security group.
Type: String
Required: No

 ** Status **
The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.
Type: String
Required: No

## See Also
<a name="API_SecurityGroupMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/SecurityGroupMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/SecurityGroupMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/SecurityGroupMembership)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
