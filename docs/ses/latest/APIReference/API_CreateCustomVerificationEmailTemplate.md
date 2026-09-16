---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateCustomVerificationEmailTemplate.html
---

# CreateCustomVerificationEmailTemplate
<a name="API_CreateCustomVerificationEmailTemplate"></a>

Creates a new custom verification email template.

For more information about custom verification email templates, see [Using Custom Verification Email Templates](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom) in the *Amazon SES Developer Guide*.

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_CreateCustomVerificationEmailTemplate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** FailureRedirectionURL **
The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.
Type: String
Required: Yes

 ** FromEmailAddress **
The email address that the custom verification email is sent from.
Type: String
Required: Yes

 ** SuccessRedirectionURL **
The URL that the recipient of the verification email is sent to if his or her address is successfully verified.
Type: String
Required: Yes

 ** TemplateContent **
The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see [Custom Verification Email Frequently Asked Questions](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom) in the *Amazon SES Developer Guide*.
Type: String
Required: Yes

 ** TemplateName **
The name of the custom verification email template.
Type: String
Required: Yes

 ** TemplateSubject **
The subject line of the custom verification email.
Type: String
Required: Yes

## Errors
<a name="API_CreateCustomVerificationEmailTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CustomVerificationEmailInvalidContent **
Indicates that custom verification email template provided content is invalid.
HTTP Status Code: 400

 ** CustomVerificationEmailTemplateAlreadyExists **
Indicates that a custom verification email template with the name you specified already exists.
 ** CustomVerificationEmailTemplateName **
Indicates that the provided custom verification email template with the specified template name already exists.
HTTP Status Code: 400

 ** FromEmailAddressNotVerified **
Indicates that the sender address specified for a custom verification email is not verified, and is therefore not eligible to send the custom verification email.
 ** FromEmailAddress **
Indicates that the from email address associated with the custom verification email template is not verified.
HTTP Status Code: 400

 ** LimitExceeded **
Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html).
HTTP Status Code: 400

## See Also
<a name="API_CreateCustomVerificationEmailTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/CreateCustomVerificationEmailTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/CreateCustomVerificationEmailTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/CreateCustomVerificationEmailTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/CreateCustomVerificationEmailTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/CreateCustomVerificationEmailTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/CreateCustomVerificationEmailTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/CreateCustomVerificationEmailTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/CreateCustomVerificationEmailTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/CreateCustomVerificationEmailTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/CreateCustomVerificationEmailTemplate)
