---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateCustomVerificationEmailTemplate.html
---

# UpdateCustomVerificationEmailTemplate
<a name="API_UpdateCustomVerificationEmailTemplate"></a>

Updates an existing custom verification email template.

For more information about custom verification email templates, see [Using Custom Verification Email Templates](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom) in the *Amazon SES Developer Guide*.

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_UpdateCustomVerificationEmailTemplate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

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

 ** TemplateContent **
The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see [Custom Verification Email Frequently Asked Questions](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom) in the *Amazon SES Developer Guide*.
Type: String
Required: No

 ** TemplateName **
The name of the custom verification email template to update.
Type: String
Required: Yes

 ** TemplateSubject **
The subject line of the custom verification email.
Type: String
Required: No

## Errors
<a name="API_UpdateCustomVerificationEmailTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CustomVerificationEmailInvalidContent **
Indicates that custom verification email template provided content is invalid.
HTTP Status Code: 400

 ** CustomVerificationEmailTemplateDoesNotExist **
Indicates that a custom verification email template with the name you specified does not exist.
 ** CustomVerificationEmailTemplateName **
Indicates that the provided custom verification email template does not exist.
HTTP Status Code: 400

 ** FromEmailAddressNotVerified **
Indicates that the sender address specified for a custom verification email is not verified, and is therefore not eligible to send the custom verification email.
 ** FromEmailAddress **
Indicates that the from email address associated with the custom verification email template is not verified.
HTTP Status Code: 400

## See Also
<a name="API_UpdateCustomVerificationEmailTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/UpdateCustomVerificationEmailTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/UpdateCustomVerificationEmailTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/UpdateCustomVerificationEmailTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/UpdateCustomVerificationEmailTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/UpdateCustomVerificationEmailTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/UpdateCustomVerificationEmailTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/UpdateCustomVerificationEmailTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/UpdateCustomVerificationEmailTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/UpdateCustomVerificationEmailTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/UpdateCustomVerificationEmailTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
