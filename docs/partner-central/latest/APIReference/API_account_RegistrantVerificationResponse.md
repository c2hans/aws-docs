---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_RegistrantVerificationResponse.html
---

# RegistrantVerificationResponse
<a name="API_account_RegistrantVerificationResponse"></a>

Contains the response information from a registrant verification process, including any verification-specific data and next steps for the individual verification workflow.

## Contents
<a name="API_account_RegistrantVerificationResponse_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CompletionUrl **   <a name="AWSPartnerCentral-Type-account_RegistrantVerificationResponse-CompletionUrl"></a>
A secure URL where the registrant can complete additional verification steps, such as document upload or identity confirmation through a third-party verification service.
Type: String
Required: Yes

 ** CompletionUrlExpiresAt **   <a name="AWSPartnerCentral-Type-account_RegistrantVerificationResponse-CompletionUrlExpiresAt"></a>
The timestamp when the completion URL expires and is no longer valid for accessing the verification workflow.
Type: Timestamp
Required: Yes

## See Also
<a name="API_account_RegistrantVerificationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/RegistrantVerificationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/RegistrantVerificationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/RegistrantVerificationResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
