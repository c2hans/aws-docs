---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ListCustomVerificationEmailTemplates.html
---

# ListCustomVerificationEmailTemplates
<a name="API_ListCustomVerificationEmailTemplates"></a>

Lists the existing custom verification email templates for your account in the current AWS Region.

For more information about custom verification email templates, see [Using Custom Verification Email Templates](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom) in the *Amazon SES Developer Guide*.

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_ListCustomVerificationEmailTemplates_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** MaxResults **
The maximum number of custom verification email templates to return. This value must be at least 1 and less than or equal to 50. If you do not specify a value, or if you specify a value less than 1 or greater than 50, the operation returns up to 50 results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** NextToken **
An array the contains the name and creation time stamp for each template in your Amazon SES account.
Type: String
Required: No

## Response Elements
<a name="API_ListCustomVerificationEmailTemplates_ResponseElements"></a>

The following elements are returned by the service.

 **CustomVerificationEmailTemplates.member.N**
A list of the custom verification email templates that exist in your account.
Type: Array of [CustomVerificationEmailTemplate](API_CustomVerificationEmailTemplate.md) objects

 ** NextToken **
A token indicating that there are additional custom verification email templates available to be listed. Pass this token to a subsequent call to `ListTemplates` to retrieve the next 50 custom verification email templates.
Type: String

## Errors
<a name="API_ListCustomVerificationEmailTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListCustomVerificationEmailTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/ListCustomVerificationEmailTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/ListCustomVerificationEmailTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ListCustomVerificationEmailTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/ListCustomVerificationEmailTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ListCustomVerificationEmailTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/ListCustomVerificationEmailTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/ListCustomVerificationEmailTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/ListCustomVerificationEmailTemplates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/ListCustomVerificationEmailTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ListCustomVerificationEmailTemplates)
