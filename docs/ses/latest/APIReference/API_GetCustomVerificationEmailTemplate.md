---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_GetCustomVerificationEmailTemplate.html
---

# GetCustomVerificationEmailTemplate
<a name="API_GetCustomVerificationEmailTemplate"></a>

Returns the custom email verification template for the template name you specify.

For more information about custom verification email templates, see [Using Custom Verification Email Templates](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom) in the *Amazon SES Developer Guide*.

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_GetCustomVerificationEmailTemplate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** TemplateName **
The name of the custom verification email template to retrieve.
Type: String
Required: Yes

## Response Elements
<a name="API_GetCustomVerificationEmailTemplate_ResponseElements"></a>

The following elements are returned by the service.

 ** FailureRedirectionURL **
The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.
Type: String

 ** FromEmailAddress **
The email address that the custom verification email is sent from.
Type: String

 ** SuccessRedirectionURL **
The URL that the recipient of the verification email is sent to if his or her address is successfully verified.
Type: String

 ** TemplateContent **
The content of the custom verification email.
Type: String

 ** TemplateName **
The name of the custom verification email template.
Type: String

 ** TemplateSubject **
The subject line of the custom verification email.
Type: String

## Errors
<a name="API_GetCustomVerificationEmailTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CustomVerificationEmailTemplateDoesNotExist **
Indicates that a custom verification email template with the name you specified does not exist.
 ** CustomVerificationEmailTemplateName **
Indicates that the provided custom verification email template does not exist.
HTTP Status Code: 400

## See Also
<a name="API_GetCustomVerificationEmailTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/GetCustomVerificationEmailTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/GetCustomVerificationEmailTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/GetCustomVerificationEmailTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/GetCustomVerificationEmailTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/GetCustomVerificationEmailTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/GetCustomVerificationEmailTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/GetCustomVerificationEmailTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/GetCustomVerificationEmailTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/GetCustomVerificationEmailTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/GetCustomVerificationEmailTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
