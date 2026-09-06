---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserPoolReplicaType.html
---

# UserPoolReplicaType
<a name="API_UserPoolReplicaType"></a>

Contains information about a replica user pool, including Region, status, role, and ARN.

This data type is a response parameter of [CreateUserPoolReplica](API_CreateUserPoolReplica.md), [ListUserPoolReplicas](API_ListUserPoolReplicas.md), [UpdateUserPoolReplica](API_UpdateUserPoolReplica.md), and [DeleteUserPoolReplica](API_DeleteUserPoolReplica.md).

## Contents
<a name="API_UserPoolReplicaType_Contents"></a>

 ** RegionName **   <a name="CognitoUserPools-Type-UserPoolReplicaType-RegionName"></a>
The AWS Region where the replica is located.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 32.
Required: No

 ** Role **   <a name="CognitoUserPools-Type-UserPoolReplicaType-Role"></a>
The role of the user pool replica that determines which API operations are enabled.
PRIMARY
The primary replica supports all end user and administrator operations.
SECONDARY
The secondary replica supports a limited set of end user and administrator operations. Generally, only administrator operations that set configurations specific to the replica, and only end-user operations that do not create or change attributes of a user are supported.
Type: String
Valid Values: `PRIMARY | SECONDARY`
Required: No

 ** Status **   <a name="CognitoUserPools-Type-UserPoolReplicaType-Status"></a>
The current status of the replica.
CREATING
The replica is being created.
INACTIVE
The replica has been created, but is not accepting requests for end-users. Administrator configuration operations are supported.
ACTIVE
The replica is available for both end-user and administrator operations.
DELETING
The replica is being deleted.
Type: String
Valid Values: `CREATING | ACTIVE | INACTIVE | DELETING`
Required: No

 ** UserPoolArn **   <a name="CognitoUserPools-Type-UserPoolReplicaType-UserPoolArn"></a>
The Amazon Resource Name (ARN) of the replica user pool.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

## See Also
<a name="API_UserPoolReplicaType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UserPoolReplicaType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UserPoolReplicaType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UserPoolReplicaType)
