---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateUserGroup.html
---

# CreateUserGroup
<a name="API_CreateUserGroup"></a>

For Valkey engine version 7.2 onwards and Redis OSS 6.0 to 7.1: Creates a user group. For more information, see [Using Role Based Access Control (RBAC)](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.RBAC.html)

## Request Parameters
<a name="API_CreateUserGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Engine **
Sets the engine listed in a user group. The options are valkey or redis.
Type: String
Pattern: `[a-zA-Z]*`
Required: Yes

 ** UserGroupId **
The ID of the user group. This value is stored as a lowercase string.
Type: String
Required: Yes

 **Tags.Tag.N**
A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted. Available for Valkey and Redis OSS only.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 **UserIds.member.N**
The list of user IDs that belong to the user group.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

## Response Elements
<a name="API_CreateUserGroup_ResponseElements"></a>

The following elements are returned by the service.

 ** ARN **
The Amazon Resource Name (ARN) of the user group.
Type: String

 ** Engine **
The options are valkey or redis.
Type: String
Pattern: `[a-zA-Z]*`

 ** MinimumEngineVersion **
The minimum engine version required, which is Redis OSS 6.0
Type: String

 ** PendingChanges **
A list of updates being applied to the user group.
Type: [UserGroupPendingChanges](API_UserGroupPendingChanges.md) object

 **ReplicationGroups.member.N**
A list of replication groups that the user group can access.
Type: Array of strings

 **ServerlessCaches.member.N**
Indicates which serverless caches the specified user group is associated with. Available for Valkey, Redis OSS and Serverless Memcached only.
Type: Array of strings

 ** Status **
Indicates user group status. Can be "creating", "active", "modifying", "deleting".
Type: String

 ** UserGroupId **
The ID of the user group.
Type: String

 **UserIds.member.N**
The list of user IDs that belong to the user group.
Type: Array of strings
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`

## Errors
<a name="API_CreateUserGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DefaultUserRequired **
You must add default user to a user group.
HTTP Status Code: 400

 ** DuplicateUserName **
A user with this username already exists.
HTTP Status Code: 400

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **
The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.
HTTP Status Code: 400

 ** UserGroupAlreadyExists **
The user group with this ID already exists.
HTTP Status Code: 400

 ** UserGroupQuotaExceeded **
The number of users exceeds the user group limit.
HTTP Status Code: 400

 ** UserNotFound **
The user does not exist or could not be found.
HTTP Status Code: 404

## See Also
<a name="API_CreateUserGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/CreateUserGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/CreateUserGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CreateUserGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/CreateUserGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CreateUserGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/CreateUserGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/CreateUserGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/CreateUserGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/CreateUserGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CreateUserGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
