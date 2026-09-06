---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyUserGroup.html
---

# ModifyUserGroup
<a name="API_ModifyUserGroup"></a>

Changes the list of users that belong to the user group.

## Request Parameters
<a name="API_ModifyUserGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** UserGroupId **
The ID of the user group.
Type: String
Required: Yes

 ** Engine **
Modifies the engine listed in a user group. The options are valkey or redis.
Type: String
Pattern: `[a-zA-Z]*`
Required: No

 **UserIdsToAdd.member.N**
The list of user IDs to add to the user group.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

 **UserIdsToRemove.member.N**
The list of user IDs to remove from the user group.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

## Response Elements
<a name="API_ModifyUserGroup_ResponseElements"></a>

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
<a name="API_ModifyUserGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DefaultUserRequired **
You must add default user to a user group.
HTTP Status Code: 400

 ** DuplicateUserName **
A user with this username already exists.
HTTP Status Code: 400

 ** InvalidParameterCombination **
Two or more incompatible parameters were specified.
 ** message **
Two or more parameters that must not be used together were used together.
HTTP Status Code: 400

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** InvalidUserGroupState **
The user group is not in an active state.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

 ** UserGroupNotFound **
The user group was not found or does not exist
HTTP Status Code: 404

 ** UserNotFound **
The user does not exist or could not be found.
HTTP Status Code: 404

## See Also
<a name="API_ModifyUserGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/ModifyUserGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/ModifyUserGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ModifyUserGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/ModifyUserGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ModifyUserGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/ModifyUserGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/ModifyUserGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/ModifyUserGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/ModifyUserGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ModifyUserGroup)
