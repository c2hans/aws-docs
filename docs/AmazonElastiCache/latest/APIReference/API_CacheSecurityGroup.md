---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CacheSecurityGroup.html
---

# CacheSecurityGroup
<a name="API_CacheSecurityGroup"></a>

Represents the output of one of the following operations:
+  `AuthorizeCacheSecurityGroupIngress`
+  `CreateCacheSecurityGroup`
+  `RevokeCacheSecurityGroupIngress`

## Contents
<a name="API_CacheSecurityGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ARN **
The ARN of the cache security group,
Type: String
Required: No

 ** CacheSecurityGroupName **
The name of the cache security group.
Type: String
Required: No

 ** Description **
The description of the cache security group.
Type: String
Required: No

 ** EC2SecurityGroups.EC2SecurityGroup.N **
A list of Amazon EC2 security groups that are associated with this cache security group.
Type: Array of [EC2SecurityGroup](API_EC2SecurityGroup.md) objects
Required: No

 ** OwnerId **
The Amazon account ID of the cache security group owner.
Type: String
Required: No

## See Also
<a name="API_CacheSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CacheSecurityGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CacheSecurityGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CacheSecurityGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
