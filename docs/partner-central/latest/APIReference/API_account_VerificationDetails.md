---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_VerificationDetails.html
---

# VerificationDetails
<a name="API_account_VerificationDetails"></a>

A union structure containing the specific details required for different types of verification processes supported by AWS Partner Central.

## Contents
<a name="API_account_VerificationDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BusinessVerificationDetails **   <a name="AWSPartnerCentral-Type-account_VerificationDetails-BusinessVerificationDetails"></a>
The business verification details to be used when starting a business verification process.
Type: [BusinessVerificationDetails](API_account_BusinessVerificationDetails.md) object
Required: No

 ** RegistrantVerificationDetails **   <a name="AWSPartnerCentral-Type-account_VerificationDetails-RegistrantVerificationDetails"></a>
The registrant verification details to be used when starting an individual identity verification process.
Type: [RegistrantVerificationDetails](API_account_RegistrantVerificationDetails.md) object
Required: No

## See Also
<a name="API_account_VerificationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/VerificationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/VerificationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/VerificationDetails)
