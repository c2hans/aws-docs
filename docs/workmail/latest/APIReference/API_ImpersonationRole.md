---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_ImpersonationRole.html
---

# ImpersonationRole
<a name="API_ImpersonationRole"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

An impersonation role for the given WorkMail organization.

## Contents
<a name="API_ImpersonationRole_Contents"></a>

 ** DateCreated **   <a name="workmail-Type-ImpersonationRole-DateCreated"></a>
The date when the impersonation role was created.
Type: Timestamp
Required: No

 ** DateModified **   <a name="workmail-Type-ImpersonationRole-DateModified"></a>
The date when the impersonation role was last modified.
Type: Timestamp
Required: No

 ** ImpersonationRoleId **   <a name="workmail-Type-ImpersonationRole-ImpersonationRoleId"></a>
The identifier of the impersonation role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** Name **   <a name="workmail-Type-ImpersonationRole-Name"></a>
The impersonation role name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\x00-\x1F\x7F\x3C\x3E\x5C]+`
Required: No

 ** Type **   <a name="workmail-Type-ImpersonationRole-Type"></a>
The impersonation role type.
Type: String
Valid Values: `FULL_ACCESS | READ_ONLY`
Required: No

## See Also
<a name="API_ImpersonationRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/ImpersonationRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/ImpersonationRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/ImpersonationRole)
