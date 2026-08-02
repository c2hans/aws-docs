---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityVerificationAttributes.html
---

# GetIdentityVerificationAttributes
<a name="API_GetIdentityVerificationAttributes"></a>

Given a list of identities (email addresses and/or domains), returns the verification status and (for domain identities) the verification token for each identity.

The verification status of an email address is "Pending" until the email address owner clicks the link within the verification email that Amazon SES sent to that address. If the email address owner clicks the link within 24 hours, the verification status of the email address changes to "Success". If the link is not clicked within 24 hours, the verification status changes to "Failed." In that case, to verify the email address, you must restart the verification process from the beginning.

For domain identities, the domain's verification status is "Pending" as Amazon SES searches for the required TXT record in the DNS settings of the domain. When Amazon SES detects the record, the domain's verification status changes to "Success". If Amazon SES is unable to detect the record within 72 hours, the domain's verification status changes to "Failed." In that case, to verify the domain, you must restart the verification process from the beginning.

This operation is throttled at one request per second and can only get verification attributes for up to 100 identities at a time.

## Request Parameters
<a name="API_GetIdentityVerificationAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Identities.member.N**
A list of identities.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_GetIdentityVerificationAttributes_ResponseElements"></a>

The following element is returned by the service.

 **VerificationAttributes** VerificationAttributes.entry.N.key (key)VerificationAttributes.entry.N.value (value)
A map of Identities to IdentityVerificationAttributes objects.
Type: String to [IdentityVerificationAttributes](API_IdentityVerificationAttributes.md) object map

## Errors
<a name="API_GetIdentityVerificationAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetIdentityVerificationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/GetIdentityVerificationAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/GetIdentityVerificationAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/GetIdentityVerificationAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/GetIdentityVerificationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/GetIdentityVerificationAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/GetIdentityVerificationAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/GetIdentityVerificationAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/GetIdentityVerificationAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/GetIdentityVerificationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/GetIdentityVerificationAttributes)
