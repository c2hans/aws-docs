---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_SendCustomVerificationEmail.html
---

# SendCustomVerificationEmail
<a name="API_SendCustomVerificationEmail"></a>

Adds an email address to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it. As a result of executing this operation, a customized verification email is sent to the specified address.

To use this operation, you must first create a custom verification email template. For more information about creating and using custom verification email templates, see [Using Custom Verification Email Templates](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom) in the *Amazon SES Developer Guide*.

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_SendCustomVerificationEmail_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ConfigurationSetName **
Name of a configuration set to use when sending the verification email.
Type: String
Required: No

 ** EmailAddress **
The email address to verify.
Type: String
Required: Yes

 ** TemplateName **
The name of the custom verification email template to use when sending the verification email.
Type: String
Required: Yes

## Response Elements
<a name="API_SendCustomVerificationEmail_ResponseElements"></a>

The following element is returned by the service.

 ** MessageId **
The unique message identifier returned from the `SendCustomVerificationEmail` operation.
Type: String

## Errors
<a name="API_SendCustomVerificationEmail_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConfigurationSetDoesNotExist **
Indicates that the configuration set does not exist.
 ** ConfigurationSetName **
Indicates that the configuration set does not exist.
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

 ** MessageRejected **
Indicates that the action failed, and the message could not be sent. Check the error stack for more information about what caused the error.
HTTP Status Code: 400

 ** ProductionAccessNotGranted **
Indicates that the account has not been granted production access.
HTTP Status Code: 400

## See Also
<a name="API_SendCustomVerificationEmail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/SendCustomVerificationEmail)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/SendCustomVerificationEmail)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/SendCustomVerificationEmail)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/SendCustomVerificationEmail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/SendCustomVerificationEmail)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/SendCustomVerificationEmail)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/SendCustomVerificationEmail)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/SendCustomVerificationEmail)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/SendCustomVerificationEmail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/SendCustomVerificationEmail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
