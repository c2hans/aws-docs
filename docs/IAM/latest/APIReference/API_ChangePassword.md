---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ChangePassword.html
---

# ChangePassword
<a name="API_ChangePassword"></a>

Changes the password of the IAM user who is calling this operation. This operation can be performed using the AWS CLI, the AWS API, or the **My Security Credentials** page in the AWS Management Console. The AWS account root user password is not affected by this operation.

Use [UpdateLoginProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateLoginProfile.html) to use the AWS CLI, the AWS API, or the **Users** page in the IAM console to change the password for any IAM user. For more information about modifying passwords, see [Managing passwords](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html) in the *IAM User Guide*.

## Request Parameters
<a name="API_ChangePassword_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** NewPassword **
The new password. The new password must conform to the AWS account's password policy, if one exists.
The [regex pattern](http://wikipedia.org/wiki/regex) that is used to validate this parameter is a string of characters. That string can include almost any printable ASCII character from the space (`\u0020`) through the end of the ASCII character range (`\u00FF`). You can also include the tab (`\u0009`), line feed (`\u000A`), and carriage return (`\u000D`) characters. Any of these characters are valid in a password. However, many tools, such as the AWS Management Console, might restrict the ability to type certain characters because they have special meaning within that tool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

 ** OldPassword **
The IAM user's current password.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

## Errors
<a name="API_ChangePassword_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityTemporarilyUnmodifiable **
The request was rejected because it referenced an entity that is temporarily unmodifiable, such as a user name that was deleted and then recreated. The error indicates that the request is likely to succeed if you try again after waiting several minutes. The error message describes the entity.
HTTP Status Code: 409

 ** InvalidUserType **
The request was rejected because the type of user for the transaction was incorrect.
HTTP Status Code: 400

 ** LimitExceeded **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error message describes the limit exceeded.
HTTP Status Code: 409

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** PasswordPolicyViolation **
The request was rejected because the provided password did not meet the requirements imposed by the account password policy.
HTTP Status Code: 400

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_ChangePassword_Examples"></a>

### Example
<a name="API_ChangePassword_Example_1"></a>

This example illustrates one usage of ChangePassword.

#### Sample Request
<a name="API_ChangePassword_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ChangePassword
&OldPassword=U79}kgds4?
&NewPassword=Lb0*1(9xpN
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ChangePassword_Example_1_Response"></a>

```
<ChangePasswordResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</ChangePasswordResponse>
```

## See Also
<a name="API_ChangePassword_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ChangePassword)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ChangePassword)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ChangePassword)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ChangePassword)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ChangePassword)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ChangePassword)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ChangePassword)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ChangePassword)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ChangePassword)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ChangePassword)
