---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UserStackAssociation.html
---

# UserStackAssociation
<a name="API_UserStackAssociation"></a>

Describes a user in the user pool and the associated stack.

## Contents
<a name="API_UserStackAssociation_Contents"></a>

 ** AuthenticationType **   <a name="WorkSpacesApplications-Type-UserStackAssociation-AuthenticationType"></a>
The authentication type for the user.
Type: String
Valid Values: `API | SAML | USERPOOL | AWS_AD`
Required: Yes

 ** StackName **   <a name="WorkSpacesApplications-Type-UserStackAssociation-StackName"></a>
The name of the stack that is associated with the user.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** UserName **   <a name="WorkSpacesApplications-Type-UserStackAssociation-UserName"></a>
The email address of the user who is associated with the stack.
Users' email addresses are case-sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** SendEmailNotification **   <a name="WorkSpacesApplications-Type-UserStackAssociation-SendEmailNotification"></a>
Specifies whether a welcome email is sent to a user after the user is created in the user pool.
Type: Boolean
Required: No

## See Also
<a name="API_UserStackAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/UserStackAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/UserStackAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/UserStackAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
