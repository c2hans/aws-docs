---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_Participant.html
---

# Participant
<a name="API_account_Participant"></a>

Represents a participant in a partner connection, containing their profile and account information.

## Contents
<a name="API_account_Participant_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Account **   <a name="AWSPartnerCentral-Type-account_Participant-Account"></a>
The AWS account information for the participant.
Type: [AccountSummary](API_account_AccountSummary.md) object
Required: No

 ** PartnerProfile **   <a name="AWSPartnerCentral-Type-account_Participant-PartnerProfile"></a>
The partner profile information for the participant.
Type: [PartnerProfileSummary](API_account_PartnerProfileSummary.md) object
Required: No

 ** SellerProfile **   <a name="AWSPartnerCentral-Type-account_Participant-SellerProfile"></a>
The seller profile information for the participant.
Type: [SellerProfileSummary](API_account_SellerProfileSummary.md) object
Required: No

## See Also
<a name="API_account_Participant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/Participant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/Participant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/Participant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
