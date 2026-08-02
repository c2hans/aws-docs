---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityDkimEnabled.html
---

# SetIdentityDkimEnabled
<a name="API_SetIdentityDkimEnabled"></a>

Enables or disables Easy DKIM signing of email sent from an identity. If Easy DKIM signing is enabled for a domain, then Amazon SES uses DKIM to sign all email that it sends from addresses on that domain. If Easy DKIM signing is enabled for an email address, then Amazon SES uses DKIM to sign all email it sends from that address.

**Note**
For email addresses (for example, `user@example.com`), you can only enable DKIM signing if the corresponding domain (in this case, `example.com`) has been set up to use Easy DKIM.

You can enable DKIM signing for an identity at any time after you start the verification process for the identity, even if the verification process isn't complete.

You can execute this operation no more than once per second.

For more information about Easy DKIM signing, go to the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html).

## Request Parameters
<a name="API_SetIdentityDkimEnabled_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DkimEnabled **
Sets whether DKIM signing is enabled for an identity. Set to `true` to enable DKIM signing for this identity; `false` to disable it.
Type: Boolean
Required: Yes

 ** Identity **
The identity for which DKIM signing should be enabled or disabled.
Type: String
Required: Yes

## Errors
<a name="API_SetIdentityDkimEnabled_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_SetIdentityDkimEnabled_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/SetIdentityDkimEnabled)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/SetIdentityDkimEnabled)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/SetIdentityDkimEnabled)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/SetIdentityDkimEnabled)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/SetIdentityDkimEnabled)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/SetIdentityDkimEnabled)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/SetIdentityDkimEnabled)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/SetIdentityDkimEnabled)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/SetIdentityDkimEnabled)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/SetIdentityDkimEnabled)
