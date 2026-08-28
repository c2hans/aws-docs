---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_VerificationResponseDetails.html
---

# VerificationResponseDetails
<a name="API_account_VerificationResponseDetails"></a>

A union structure containing the response details specific to different types of verification processes, providing type-specific information and results.

## Contents
<a name="API_account_VerificationResponseDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BusinessVerificationResponse **   <a name="AWSPartnerCentral-Type-account_VerificationResponseDetails-BusinessVerificationResponse"></a>
The response details from a business verification process, including verification results and any additional business information discovered.
Type: [BusinessVerificationResponse](API_account_BusinessVerificationResponse.md) object
Required: No

 ** RegistrantVerificationResponse **   <a name="AWSPartnerCentral-Type-account_VerificationResponseDetails-RegistrantVerificationResponse"></a>
The response details from a registrant verification process, including verification results and any additional steps required for identity confirmation.
Type: [RegistrantVerificationResponse](API_account_RegistrantVerificationResponse.md) object
Required: No

## See Also
<a name="API_account_VerificationResponseDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/VerificationResponseDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/VerificationResponseDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/VerificationResponseDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
