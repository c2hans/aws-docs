---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_MailboxValidation.html
---

# MailboxValidation
<a name="API_MailboxValidation"></a>

Contains detailed validation information about an email address.

## Contents
<a name="API_MailboxValidation_Contents"></a>

 ** Evaluations **   <a name="SES-Type-MailboxValidation-Evaluations"></a>
Specific validation checks performed on the email address.
Type: [EmailAddressInsightsMailboxEvaluations](API_EmailAddressInsightsMailboxEvaluations.md) object
Required: No

 ** IsValid **   <a name="SES-Type-MailboxValidation-IsValid"></a>
Overall validity assessment with a conﬁdence verdict.
Type: [EmailAddressInsightsVerdict](API_EmailAddressInsightsVerdict.md) object
Required: No

## See Also
<a name="API_MailboxValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/MailboxValidation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/MailboxValidation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/MailboxValidation)
