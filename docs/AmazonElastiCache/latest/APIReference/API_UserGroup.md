---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_UserGroup.html
---

# UserGroup
<a name="API_UserGroup"></a>

## Contents
<a name="API_UserGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ARN **
The Amazon Resource Name (ARN) of the user group.
Type: String
Required: No

 ** Engine **
The options are valkey or redis.
Type: String
Pattern: `[a-zA-Z]*`
Required: No

 ** MinimumEngineVersion **
The minimum engine version required, which is Redis OSS 6.0
Type: String
Required: No

 ** PendingChanges **
A list of updates being applied to the user group.
Type: [UserGroupPendingChanges](API_UserGroupPendingChanges.md) object
Required: No

 ** ReplicationGroups.member.N **
A list of replication groups that the user group can access.
Type: Array of strings
Required: No

 ** ServerlessCaches.member.N **
Indicates which serverless caches the specified user group is associated with. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: Array of strings
Required: No

 ** Status **
Indicates user group status. Can be "creating", "active", "modifying", "deleting".
Type: String
Required: No

 ** UserGroupId **
The ID of the user group.
Type: String
Required: No

 ** UserIds.member.N **
The list of user IDs that belong to the user group.
Type: Array of strings
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

## See Also
<a name="API_UserGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/UserGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/UserGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/UserGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
