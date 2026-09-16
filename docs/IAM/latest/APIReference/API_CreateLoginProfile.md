---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateLoginProfile.html
---

# CreateLoginProfile
<a name="API_CreateLoginProfile"></a>

Creates a password for the specified IAM user. A password allows an IAM user to access AWS services through the AWS Management Console.

You can use the AWS CLI, the AWS API, or the **Users** page in the IAM console to create a password for any IAM user. Use [ChangePassword](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ChangePassword.html) to update your own existing password in the **My Security Credentials** page in the AWS Management Console.

For more information about managing passwords, see [Managing passwords](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html) in the *IAM User Guide*.

## Request Parameters
<a name="API_CreateLoginProfile_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Password **
The new password for the user.
This parameter must be omitted when you make the request with an [AssumeRoot](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoot.html) session. It is required in all other cases.
The [regex pattern](http://wikipedia.org/wiki/regex) that is used to validate this parameter is a string of characters. That string can include almost any printable ASCII character from the space (`\u0020`) through the end of the ASCII character range (`\u00FF`). You can also include the tab (`\u0009`), line feed (`\u000A`), and carriage return (`\u000D`) characters. Any of these characters are valid in a password. However, many tools, such as the AWS Management Console, might restrict the ability to type certain characters because they have special meaning within that tool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** PasswordResetRequired **
Specifies whether the user is required to set a new password on next sign-in.
Type: Boolean
Required: No

 ** UserName **
The name of the IAM user to create a password for. The user must already exist.
This parameter is optional. If no user name is included, it defaults to the principal making the request. When you make this request with root user credentials, you must use an [AssumeRoot](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoot.html) session to omit the user name.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: No

## Response Elements
<a name="API_CreateLoginProfile_ResponseElements"></a>

The following element is returned by the service.

 ** LoginProfile **
A structure containing the user name and password create date.
Type: [LoginProfile](API_LoginProfile.md) object

## Errors
<a name="API_CreateLoginProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityAlreadyExists **
The request was rejected because it attempted to create a resource that already exists.
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
<a name="API_CreateLoginProfile_Examples"></a>

### Example
<a name="API_CreateLoginProfile_Example_1"></a>

This example illustrates one usage of CreateLoginProfile.

#### Sample Request
<a name="API_CreateLoginProfile_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=CreateLoginProfile
&UserName=Bob
&Password=h]6EszR}vJ*m
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateLoginProfile_Example_1_Response"></a>

```
<CreateLoginProfileResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <CreateLoginProfileResult>
    <LoginProfile>
      <PasswordResetRequired>false</PasswordResetRequired>
      <UserName>Bob</UserName>
      <CreateDate>2015-03-25T20:48:52.558Z</CreateDate>
    </LoginProfile>
  </CreateLoginProfileResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</CreateLoginProfileResponse>
```

## See Also
<a name="API_CreateLoginProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/CreateLoginProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/CreateLoginProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/CreateLoginProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/CreateLoginProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/CreateLoginProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/CreateLoginProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/CreateLoginProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/CreateLoginProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/CreateLoginProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/CreateLoginProfile)
