---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_CustomVerificationEmailTemplate.html
---

# CustomVerificationEmailTemplate
<a name="API_CustomVerificationEmailTemplate"></a>

Contains information about a custom verification email template.

## Contents
<a name="API_CustomVerificationEmailTemplate_Contents"></a>

 ** FailureRedirectionURL **
The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.
Type: String
Required: No

 ** FromEmailAddress **
The email address that the custom verification email is sent from.
Type: String
Required: No

 ** SuccessRedirectionURL **
The URL that the recipient of the verification email is sent to if his or her address is successfully verified.
Type: String
Required: No

 ** TemplateName **
The name of the custom verification email template.
Type: String
Required: No

 ** TemplateSubject **
The subject line of the custom verification email.
Type: String
Required: No

## See Also
<a name="API_CustomVerificationEmailTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/CustomVerificationEmailTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/CustomVerificationEmailTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/CustomVerificationEmailTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
