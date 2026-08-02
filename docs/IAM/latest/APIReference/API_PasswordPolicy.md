---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_PasswordPolicy.html
---

# PasswordPolicy
<a name="API_PasswordPolicy"></a>

Contains information about the account password policy.

 This data type is used as a response element in the [GetAccountPasswordPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountPasswordPolicy.html) operation.

## Contents
<a name="API_PasswordPolicy_Contents"></a>

 ** AllowUsersToChangePassword **
Specifies whether IAM users are allowed to change their own password. Gives IAM users permissions to `iam:ChangePassword` for only their user and to the `iam:GetAccountPasswordPolicy` action. This option does not attach a permissions policy to each user, rather the permissions are applied at the account-level for all users by IAM.
Type: Boolean
Required: No

 ** ExpirePasswords **
Indicates whether passwords in the account expire. Returns true if `MaxPasswordAge` contains a value greater than 0. Returns false if MaxPasswordAge is 0 or not present.
Type: Boolean
Required: No

 ** HardExpiry **
Specifies whether IAM users are prevented from setting a new password via the AWS Management Console after their password has expired. The IAM user cannot access the console until an administrator resets the password. IAM users with `iam:ChangePassword` permission and active access keys can reset their own expired console password using the AWS CLI or API.
Type: Boolean
Required: No

 ** MaxPasswordAge **
The number of days that an IAM user password is valid.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1095.
Required: No

 ** MinimumPasswordLength **
Minimum length to require for IAM user passwords.
Type: Integer
Valid Range: Minimum value of 6. Maximum value of 128.
Required: No

 ** PasswordReusePrevention **
Specifies the number of previous passwords that IAM users are prevented from reusing.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 24.
Required: No

 ** RequireLowercaseCharacters **
Specifies whether IAM user passwords must contain at least one lowercase character (a to z).
Type: Boolean
Required: No

 ** RequireNumbers **
Specifies whether IAM user passwords must contain at least one numeric character (0 to 9).
Type: Boolean
Required: No

 ** RequireSymbols **
Specifies whether IAM user passwords must contain at least one of the following symbols:
\! @ \# $ % ^ & \* ( ) \_ \+ - = [ ] { } \| '
Type: Boolean
Required: No

 ** RequireUppercaseCharacters **
Specifies whether IAM user passwords must contain at least one uppercase character (A to Z).
Type: Boolean
Required: No

## See Also
<a name="API_PasswordPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/PasswordPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/PasswordPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/PasswordPolicy)
