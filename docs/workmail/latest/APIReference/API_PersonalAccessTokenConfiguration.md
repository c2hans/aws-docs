---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_PersonalAccessTokenConfiguration.html
---

# PersonalAccessTokenConfiguration
<a name="API_PersonalAccessTokenConfiguration"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

 Displays the Personal Access Token status.

## Contents
<a name="API_PersonalAccessTokenConfiguration_Contents"></a>

 ** Status **   <a name="workmail-Type-PersonalAccessTokenConfiguration-Status"></a>
 The status of the Personal Access Token allowed for the organization.
+  *Active* - Mailbox users can login to the web application and choose *Settings* to see the new *Personal Access Tokens* page to create and delete the Personal Access Tokens. Mailbox users can use the Personal Access Tokens to set up mailbox connection from desktop or mobile email clients.
+  *Inactive* - Personal Access Tokens are disabled for your organization. Mailbox users can’t create, list, or delete Personal Access Tokens and can’t use them to connect to their mailboxes from desktop or mobile email clients.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

 ** LifetimeInDays **   <a name="workmail-Type-PersonalAccessTokenConfiguration-LifetimeInDays"></a>
 The validity of the Personal Access Token status in days.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3653.
Required: No

## See Also
<a name="API_PersonalAccessTokenConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/PersonalAccessTokenConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/PersonalAccessTokenConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/PersonalAccessTokenConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
