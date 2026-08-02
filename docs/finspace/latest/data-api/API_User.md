---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_User.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# User
<a name="API_User"></a>

The details of the user.

## Contents
<a name="API_User_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** apiAccess **   <a name="finspace-Type-User-apiAccess"></a>
Indicates whether the user can use the `GetProgrammaticAccessCredentials` API to obtain credentials that can then be used to access other FinSpace Data API operations.
+  `ENABLED` – The user has permissions to use the APIs.
+  `DISABLED` – The user does not have permissions to use any APIs.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** apiAccessPrincipalArn **   <a name="finspace-Type-User-apiAccessPrincipalArn"></a>
The ARN identifier of an AWS user or role that is allowed to call the `GetProgrammaticAccessCredentials` API to obtain a credentials token for a specific FinSpace user. This must be an IAM role within your FinSpace account.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** createTime **   <a name="finspace-Type-User-createTime"></a>
The timestamp at which the user was created in FinSpace. The value is determined as epoch time in milliseconds.
Type: Long
Required: No

 ** emailAddress **   <a name="finspace-Type-User-emailAddress"></a>
The email address of the user. The email address serves as a uniquer identifier for each user and cannot be changed after it's created.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 320.
Pattern: `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}`
Required: No

 ** firstName **   <a name="finspace-Type-User-firstName"></a>
The first name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `.*\S.*`
Required: No

 ** lastDisabledTime **   <a name="finspace-Type-User-lastDisabledTime"></a>
Describes the last time the user was deactivated. The value is determined as epoch time in milliseconds.
Type: Long
Required: No

 ** lastEnabledTime **   <a name="finspace-Type-User-lastEnabledTime"></a>
 Describes the last time the user was activated. The value is determined as epoch time in milliseconds.
Type: Long
Required: No

 ** lastLoginTime **   <a name="finspace-Type-User-lastLoginTime"></a>
Describes the last time that the user logged into their account. The value is determined as epoch time in milliseconds.
Type: Long
Required: No

 ** lastModifiedTime **   <a name="finspace-Type-User-lastModifiedTime"></a>
Describes the last time the user was updated. The value is determined as epoch time in milliseconds.
Type: Long
Required: No

 ** lastName **   <a name="finspace-Type-User-lastName"></a>
 The last name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `.*\S.*`
Required: No

 ** status **   <a name="finspace-Type-User-status"></a>
The current status of the user.
+  `CREATING` – The user creation is in progress.
+  `ENABLED` – The user is created and is currently active.
+  `DISABLED` – The user is currently inactive.
Type: String
Valid Values: `CREATING | ENABLED | DISABLED`
Required: No

 ** type **   <a name="finspace-Type-User-type"></a>
 Indicates the type of user.
+  `SUPER_USER` – A user with permission to all the functionality and data in FinSpace.
+  `APP_USER` – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.
Type: String
Valid Values: `SUPER_USER | APP_USER`
Required: No

 ** userId **   <a name="finspace-Type-User-userId"></a>
The unique identifier for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/User)
