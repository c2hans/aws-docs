---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_BusinessVerificationResponse.html
---

# BusinessVerificationResponse
<a name="API_account_BusinessVerificationResponse"></a>

Contains the response information and results from a business verification process, including any verification-specific data returned by the verification service.

## Contents
<a name="API_account_BusinessVerificationResponse_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BusinessVerificationDetails **   <a name="AWSPartnerCentral-Type-account_BusinessVerificationResponse-BusinessVerificationDetails"></a>
The business verification details that were processed and verified, potentially including additional information discovered during the verification process.
Type: [BusinessVerificationDetails](API_account_BusinessVerificationDetails.md) object
Required: Yes

 ** CompletionUrl **   <a name="AWSPartnerCentral-Type-account_BusinessVerificationResponse-CompletionUrl"></a>
A secure URL where the registrant can complete additional verification steps, such as document upload or identity confirmation through a third-party verification service.
Type: String
Required: No

 ** CompletionUrlExpiresAt **   <a name="AWSPartnerCentral-Type-account_BusinessVerificationResponse-CompletionUrlExpiresAt"></a>
The timestamp when the completion URL expires and is no longer valid for accessing the verification workflow.
Type: Timestamp
Required: No

## See Also
<a name="API_account_BusinessVerificationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/BusinessVerificationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/BusinessVerificationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/BusinessVerificationResponse)
