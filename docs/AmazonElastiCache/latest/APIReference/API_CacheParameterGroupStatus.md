---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CacheParameterGroupStatus.html
---

# CacheParameterGroupStatus
<a name="API_CacheParameterGroupStatus"></a>

Status of the cache parameter group.

## Contents
<a name="API_CacheParameterGroupStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CacheNodeIdsToReboot.CacheNodeId.N **
A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).
Type: Array of strings
Required: No

 ** CacheParameterGroupName **
The name of the cache parameter group.
Type: String
Required: No

 ** ParameterApplyStatus **
The status of parameter updates.
Type: String
Required: No

## See Also
<a name="API_CacheParameterGroupStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CacheParameterGroupStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CacheParameterGroupStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CacheParameterGroupStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
