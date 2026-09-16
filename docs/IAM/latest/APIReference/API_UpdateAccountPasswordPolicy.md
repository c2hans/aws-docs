---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAccountPasswordPolicy.html
---

# UpdateAccountPasswordPolicy
<a name="API_UpdateAccountPasswordPolicy"></a>

Updates the password policy settings for the AWS account.

**Note**
This operation does not support partial updates. No parameters are required, but if you do not specify a parameter, that parameter's value reverts to its default value. See the **Request Parameters** section for each parameter's default value. Also note that some parameters do not allow the default parameter to be explicitly set. Instead, to invoke the default value, do not include that parameter when you invoke the operation.

 For more information about using a password policy, see [Managing an IAM password policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingPasswordPolicies.html) in the *IAM User Guide*.

## Request Parameters
<a name="API_UpdateAccountPasswordPolicy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AllowUsersToChangePassword **
 Allows all IAM users in your account to use the AWS Management Console to change their own passwords. For more information, see [Permitting IAM users to change their own passwords](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_enable-user-change.html) in the *IAM User Guide*.
If you do not specify a value for this parameter, then the operation uses the default value of `false`. The result is that IAM users in the account do not automatically have permissions to change their own password.
Type: Boolean
Required: No

 ** HardExpiry **
 Prevents IAM users who are accessing the account via the AWS Management Console from setting a new console password after their password has expired. The IAM user cannot access the console until an administrator resets the password.
If you do not specify a value for this parameter, then the operation uses the default value of `false`. The result is that IAM users can change their passwords after they expire and continue to sign in as the user.
 In the AWS Management Console, the custom password policy option **Allow users to change their own password** gives IAM users permissions to `iam:ChangePassword` for only their user and to the `iam:GetAccountPasswordPolicy` action. This option does not attach a permissions policy to each user, rather the permissions are applied at the account-level for all users by IAM. IAM users with `iam:ChangePassword` permission and active access keys can reset their own expired console password using the AWS CLI or API.
Type: Boolean
Required: No

 ** MaxPasswordAge **
The number of days that an IAM user password is valid.
If you do not specify a value for this parameter, then the operation uses the default value of `0`. The result is that IAM user passwords never expire.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1095.
Required: No

 ** MinimumPasswordLength **
The minimum number of characters allowed in an IAM user password.
If you do not specify a value for this parameter, then the operation uses the default value of `6`.
Type: Integer
Valid Range: Minimum value of 6. Maximum value of 128.
Required: No

 ** PasswordReusePrevention **
Specifies the number of previous passwords that IAM users are prevented from reusing.
If you do not specify a value for this parameter, then the operation uses the default value of `0`. The result is that IAM users are not prevented from reusing previous passwords.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 24.
Required: No

 ** RequireLowercaseCharacters **
Specifies whether IAM user passwords must contain at least one lowercase character from the ISO basic Latin alphabet (a to z).
If you do not specify a value for this parameter, then the operation uses the default value of `false`. The result is that passwords do not require at least one lowercase character.
Type: Boolean
Required: No

 ** RequireNumbers **
Specifies whether IAM user passwords must contain at least one numeric character (0 to 9).
If you do not specify a value for this parameter, then the operation uses the default value of `false`. The result is that passwords do not require at least one numeric character.
Type: Boolean
Required: No

 ** RequireSymbols **
Specifies whether IAM user passwords must contain at least one of the following non-alphanumeric characters:
\! @ \# $ % ^ & \* ( ) \_ \+ - = [ ] { } \| '
If you do not specify a value for this parameter, then the operation uses the default value of `false`. The result is that passwords do not require at least one symbol character.
Type: Boolean
Required: No

 ** RequireUppercaseCharacters **
Specifies whether IAM user passwords must contain at least one uppercase character from the ISO basic Latin alphabet (A to Z).
If you do not specify a value for this parameter, then the operation uses the default value of `false`. The result is that passwords do not require at least one uppercase character.
Type: Boolean
Required: No

## Errors
<a name="API_UpdateAccountPasswordPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceeded **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error message describes the limit exceeded.
HTTP Status Code: 409

 ** MalformedPolicyDocument **
The request was rejected because the policy document was malformed. The error message describes the specific error.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_UpdateAccountPasswordPolicy_Examples"></a>

### Example
<a name="API_UpdateAccountPasswordPolicy_Example_1"></a>

This example illustrates one usage of UpdateAccountPasswordPolicy.

#### Sample Request
<a name="API_UpdateAccountPasswordPolicy_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=UpdateAccountPasswordPolicy
&AllowUsersToChangePassword=true
&HardExpiry=false
&MaxPasswordAge=90
&MinimumPasswordLength=12
&PasswordReusePrevention=12
&RequireLowercaseCharacters=true
&RequireNumbers=true
&RequireSymbols=true
&RequireUppercaseCharacters=true
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_UpdateAccountPasswordPolicy_Example_1_Response"></a>

```
<UpdateAccountPasswordPolicyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
 <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
 </ResponseMetadata>
</UpdateAccountPasswordPolicyResponse>
```

## See Also
<a name="API_UpdateAccountPasswordPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/UpdateAccountPasswordPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/UpdateAccountPasswordPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/UpdateAccountPasswordPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/UpdateAccountPasswordPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/UpdateAccountPasswordPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/UpdateAccountPasswordPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/UpdateAccountPasswordPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/UpdateAccountPasswordPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/UpdateAccountPasswordPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/UpdateAccountPasswordPolicy)
