---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_User.html
---

# User
<a name="API_User"></a>

Describes a user in the user pool.

## Contents
<a name="API_User_Contents"></a>

 ** AuthenticationType **   <a name="WorkSpacesApplications-Type-User-AuthenticationType"></a>
The authentication type for the user.
Type: String
Valid Values: `API | SAML | USERPOOL | AWS_AD`
Required: Yes

 ** Arn **   <a name="WorkSpacesApplications-Type-User-Arn"></a>
The ARN of the user.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** CreatedTime **   <a name="WorkSpacesApplications-Type-User-CreatedTime"></a>
The date and time the user was created in the user pool.
Type: Timestamp
Required: No

 ** Enabled **   <a name="WorkSpacesApplications-Type-User-Enabled"></a>
Specifies whether the user in the user pool is enabled.
Type: Boolean
Required: No

 ** FirstName **   <a name="WorkSpacesApplications-Type-User-FirstName"></a>
The first name, or given name, of the user.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[A-Za-z0-9_\-\s]+$`
Required: No

 ** LastName **   <a name="WorkSpacesApplications-Type-User-LastName"></a>
The last name, or surname, of the user.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[A-Za-z0-9_\-\s]+$`
Required: No

 ** Status **   <a name="WorkSpacesApplications-Type-User-Status"></a>
The status of the user in the user pool. The status can be one of the following:
+ UNCONFIRMED – The user is created but not confirmed.
+ CONFIRMED – The user is confirmed.
+ ARCHIVED – The user is no longer active.
+ COMPROMISED – The user is disabled because of a potential security threat.
+ UNKNOWN – The user status is not known.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** UserName **   <a name="WorkSpacesApplications-Type-User-UserName"></a>
The email address of the user.
Users' email addresses are case-sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/User)
