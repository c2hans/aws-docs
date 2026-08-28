---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_Permission.html
---

# Permission
<a name="API_Permission"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Permission granted to a user, group, or resource to access a certain aspect of another user, group, or resource mailbox.

## Contents
<a name="API_Permission_Contents"></a>

 ** GranteeId **   <a name="workmail-Type-Permission-GranteeId"></a>
The identifier of the user, group, or resource to which the permissions are granted.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.
Required: Yes

 ** GranteeType **   <a name="workmail-Type-Permission-GranteeType"></a>
The type of user, group, or resource referred to in GranteeId.
Type: String
Valid Values: `GROUP | USER`
Required: Yes

 ** PermissionValues **   <a name="workmail-Type-Permission-PermissionValues"></a>
The permissions granted to the grantee. SEND\_AS allows the grantee to send email as the owner of the mailbox (the grantee is not mentioned on these emails). SEND\_ON\_BEHALF allows the grantee to send email on behalf of the owner of the mailbox (the grantee is not mentioned as the physical sender of these emails). FULL\_ACCESS allows the grantee full access to the mailbox, irrespective of other folder-level permissions set on the mailbox.
Type: Array of strings
Valid Values: `FULL_ACCESS | SEND_AS | SEND_ON_BEHALF`
Required: Yes

## See Also
<a name="API_Permission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/Permission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/Permission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/Permission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
