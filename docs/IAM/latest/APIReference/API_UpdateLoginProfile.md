---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateLoginProfile.html
---

# UpdateLoginProfile
<a name="API_UpdateLoginProfile"></a>

Changes the password for the specified IAM user. You can use the AWS CLI, the AWS API, or the **Users** page in the IAM console to change the password for any IAM user. Use [ChangePassword](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ChangePassword.html) to change your own password in the **My Security Credentials** page in the AWS Management Console.

For more information about modifying passwords, see [Managing passwords](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html) in the *IAM User Guide*.

## Request Parameters
<a name="API_UpdateLoginProfile_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Password **
The new password for the specified IAM user.
The [regex pattern](http://wikipedia.org/wiki/regex) used to validate this parameter is a string of characters consisting of the following:
+ Any printable ASCII character ranging from the space character (`\u0020`) through the end of the ASCII character range
+ The printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF`)
+ The special characters tab (`\u0009`), line feed (`\u000A`), and carriage return (`\u000D`)
However, the format can be further restricted by the account administrator by setting a password policy on the AWS account. For more information, see [UpdateAccountPasswordPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAccountPasswordPolicy.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** PasswordResetRequired **
Allows this new password to be used only once by requiring the specified IAM user to set a new password on next sign-in.
Type: Boolean
Required: No

 ** UserName **
The name of the user whose password you want to update.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

## Errors
<a name="API_UpdateLoginProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityTemporarilyUnmodifiable **
The request was rejected because it referenced an entity that is temporarily unmodifiable, such as a user name that was deleted and then recreated. The error indicates that the request is likely to succeed if you try again after waiting several minutes. The error message describes the entity.
HTTP Status Code: 409

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
<a name="API_UpdateLoginProfile_Examples"></a>

### Example
<a name="API_UpdateLoginProfile_Example_1"></a>

This example illustrates one usage of UpdateLoginProfile.

#### Sample Request
<a name="API_UpdateLoginProfile_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=UpdateLoginProfile
&UserName=Bob
&Password=^L[p*#Z*8o)K
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_UpdateLoginProfile_Example_1_Response"></a>

```
<UpdateLoginProfileResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
 <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
 </ResponseMetadata>
</UpdateLoginProfileResponse>
```

## See Also
<a name="API_UpdateLoginProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/UpdateLoginProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/UpdateLoginProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/UpdateLoginProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/UpdateLoginProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/UpdateLoginProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/UpdateLoginProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/UpdateLoginProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/UpdateLoginProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/UpdateLoginProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/UpdateLoginProfile)
