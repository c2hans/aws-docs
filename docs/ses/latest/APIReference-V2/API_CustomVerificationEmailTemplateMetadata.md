---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_CustomVerificationEmailTemplateMetadata.html
---

# CustomVerificationEmailTemplateMetadata
<a name="API_CustomVerificationEmailTemplateMetadata"></a>

Contains information about a custom verification email template.

## Contents
<a name="API_CustomVerificationEmailTemplateMetadata_Contents"></a>

 ** FailureRedirectionURL **   <a name="SES-Type-CustomVerificationEmailTemplateMetadata-FailureRedirectionURL"></a>
The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.
Type: String
Required: No

 ** FromEmailAddress **   <a name="SES-Type-CustomVerificationEmailTemplateMetadata-FromEmailAddress"></a>
The email address that the custom verification email is sent from.
Type: String
Required: No

 ** SuccessRedirectionURL **   <a name="SES-Type-CustomVerificationEmailTemplateMetadata-SuccessRedirectionURL"></a>
The URL that the recipient of the verification email is sent to if his or her address is successfully verified.
Type: String
Required: No

 ** TemplateName **   <a name="SES-Type-CustomVerificationEmailTemplateMetadata-TemplateName"></a>
The name of the custom verification email template.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** TemplateSubject **   <a name="SES-Type-CustomVerificationEmailTemplateMetadata-TemplateSubject"></a>
The subject line of the custom verification email.
Type: String
Required: No

## See Also
<a name="API_CustomVerificationEmailTemplateMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/CustomVerificationEmailTemplateMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/CustomVerificationEmailTemplateMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/CustomVerificationEmailTemplateMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
