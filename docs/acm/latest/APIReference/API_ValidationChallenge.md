---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_ValidationChallenge.html
---

# ValidationChallenge
<a name="API_ValidationChallenge"></a>

Contains the challenge details that you use to prove domain ownership. Only one member is set, depending on the validation method.

## Contents
<a name="API_ValidationChallenge_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** DnsValidationChallenge **   <a name="ACM-Type-ValidationChallenge-DnsValidationChallenge"></a>
Contains the CNAME record that you must add to your DNS configuration to validate domain ownership using DNS validation.
Type: [DnsValidationChallenge](API_DnsValidationChallenge.md) object
Required: No

 ** EmailValidationChallenge **   <a name="ACM-Type-ValidationChallenge-EmailValidationChallenge"></a>
Contains the email addresses used for email-based domain validation.
Type: [EmailValidationChallenge](API_EmailValidationChallenge.md) object
Required: No

## See Also
<a name="API_ValidationChallenge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/ValidationChallenge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/ValidationChallenge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/ValidationChallenge)
