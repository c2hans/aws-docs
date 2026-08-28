---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateUser.html
---

# UpdateUser
<a name="API_UpdateUser"></a>

Updates the name and/or the path of the specified IAM user.

**Important**
 You should understand the implications of changing an IAM user's path or name. For more information, see [Renaming an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_renaming) and [Renaming an IAM group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_rename.html) in the *IAM User Guide*.

**Note**
 To change a user name, the requester must have appropriate permissions on both the source object and the target object. For example, to change Bob to Robert, the entity making the request must have permission on Bob and Robert, or must have permission on all (\*). For more information about permissions, see [Permissions and policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/PermissionsAndPolicies.html).

## Request Parameters
<a name="API_UpdateUser_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** NewPath **
New path for the IAM user. Include this parameter only if you're changing the user's path.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the \! (`\u0021`) through the DEL character (`\u007F`), including most punctuation characters, digits, and upper and lowercased letters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(\u002F)|(\u002F[\u0021-\u007E]+\u002F)`
Required: No

 ** NewUserName **
New name for the user. Include this parameter only if you're changing the user's name.
IAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both "MyResource" and "myresource".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: No

 ** UserName **
Name of the user to update. If you're changing the name of the user, this is the original user name.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

## Errors
<a name="API_UpdateUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
HTTP Status Code: 409

 ** EntityAlreadyExists **
The request was rejected because it attempted to create a resource that already exists.
HTTP Status Code: 409

 ** EntityTemporarilyUnmodifiable **
The request was rejected because it referenced an entity that is temporarily unmodifiable, such as a user name that was deleted and then recreated. The error indicates that the request is likely to succeed if you try again after waiting several minutes. The error message describes the entity.
HTTP Status Code: 409

 ** LimitExceeded **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error message describes the limit exceeded.
HTTP Status Code: 409

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_UpdateUser_Examples"></a>

### Example
<a name="API_UpdateUser_Example_1"></a>

This example illustrates one usage of UpdateUser.

#### Sample Request
<a name="API_UpdateUser_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=UpdateUser
&UserName=Bob
&NewUserName=Robert
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_UpdateUser_Example_1_Response"></a>

```
<UpdateUserResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
 <UpdateUserResult>
 <User>
    <Path>/division_abc/subdivision_xyz/</Path>
    <UserName>Robert</UserName>
    <UserId>AIDACKCEVSQ6C2EXAMPLE</UserId>
    <Arn>arn:aws::123456789012:user/division_abc/subdivision_xyz/Robert
    </Arn>
 </User>
 </UpdateUserResult>
 <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
 </ResponseMetadata>
</UpdateUserResponse>
```

## See Also
<a name="API_UpdateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/UpdateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/UpdateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/UpdateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/UpdateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/UpdateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/UpdateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/UpdateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/UpdateUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/UpdateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/UpdateUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
