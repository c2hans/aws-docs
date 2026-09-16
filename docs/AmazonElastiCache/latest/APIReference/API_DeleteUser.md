---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DeleteUser.html
---

# DeleteUser
<a name="API_DeleteUser"></a>

For Valkey engine version 7.2 onwards and Redis OSS 6.0 onwards: Deletes a user. The user will be removed from all user groups and in turn removed from all replication groups. For more information, see [Using Role Based Access Control (RBAC)](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.RBAC.html).

## Request Parameters
<a name="API_DeleteUser_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** UserId **
The ID of the user.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: Yes

## Response Elements
<a name="API_DeleteUser_ResponseElements"></a>

The following elements are returned by the service.

 ** AccessString **
Access permissions string used for this user.
Type: String

 ** ARN **
The Amazon Resource Name (ARN) of the user.
Type: String

 ** Authentication **
Denotes whether the user requires a password to authenticate.
Type: [Authentication](API_Authentication.md) object

 ** Engine **
The options are valkey or redis.
Type: String
Pattern: `[a-zA-Z]*`

 ** MinimumEngineVersion **
The minimum engine version required, which is Redis OSS 6.0
Type: String

 ** Status **
Indicates the user status. Can be "active", "modifying" or "deleting".
Type: String

 **UserGroupIds.member.N**
Returns a list of the user group IDs the user belongs to.
Type: Array of strings
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`

 ** UserId **
The ID of the user.
Type: String

 ** UserName **
The username of the user.
Type: String

## Errors
<a name="API_DeleteUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DefaultUserAssociatedToUserGroup **
The default user assigned to the user group.
HTTP Status Code: 400

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** InvalidUserState **
The user is not in active state.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

 ** UserNotFound **
The user does not exist or could not be found.
HTTP Status Code: 404

## See Also
<a name="API_DeleteUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DeleteUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DeleteUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DeleteUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DeleteUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DeleteUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DeleteUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DeleteUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DeleteUser)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DeleteUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DeleteUser)
