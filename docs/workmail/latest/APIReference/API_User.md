---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_User.html
---

# User
<a name="API_User"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

The representation of an WorkMail user.

## Contents
<a name="API_User_Contents"></a>

 ** DisabledDate **   <a name="workmail-Type-User-DisabledDate"></a>
The date indicating when the user was disabled from WorkMail use.
Type: Timestamp
Required: No

 ** DisplayName **   <a name="workmail-Type-User-DisplayName"></a>
The display name of the user.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** Email **   <a name="workmail-Type-User-Email"></a>
The email of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Pattern: `[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]+\.[a-zA-Z-]{2,}`
Required: No

 ** EnabledDate **   <a name="workmail-Type-User-EnabledDate"></a>
The date indicating when the user was enabled for WorkMail use.
Type: Timestamp
Required: No

 ** Id **   <a name="workmail-Type-User-Id"></a>
The identifier of the user.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.
Required: No

 ** IdentityProviderIdentityStoreId **   <a name="workmail-Type-User-IdentityProviderIdentityStoreId"></a>
Identity store ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^d-[0-9a-f]{10}$|^[0-9a-f]{8}\\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\\b[0-9a-f]{12}$`
Required: No

 ** IdentityProviderUserId **   <a name="workmail-Type-User-IdentityProviderUserId"></a>
User ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
Required: No

 ** Name **   <a name="workmail-Type-User-Name"></a>
The name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w\-.]+(@[a-zA-Z0-9.\-]+\.[a-zA-Z0-9-]{2,})?`
Required: No

 ** State **   <a name="workmail-Type-User-State"></a>
The state of the user, which can be ENABLED, DISABLED, or DELETED.
Type: String
Valid Values: `ENABLED | DISABLED | DELETED`
Required: No

 ** UserRole **   <a name="workmail-Type-User-UserRole"></a>
The role of the user.
Type: String
Valid Values: `USER | RESOURCE | SYSTEM_USER | REMOTE_USER`
Required: No

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/User)
