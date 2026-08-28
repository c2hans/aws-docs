---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_QualificationsAssociationPartner.html
---

# QualificationsAssociationPartner
<a name="API_account_QualificationsAssociationPartner"></a>

Identifies a partner in a qualifications association group. Contains the partner's profile identifier and AWS account identifier. In requests, provide at least one of `ProfileId` or `AccountId`. In responses, both fields are populated.

## Contents
<a name="API_account_QualificationsAssociationPartner_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccountId **   <a name="AWSPartnerCentral-Type-account_QualificationsAssociationPartner-AccountId"></a>
The 12-digit AWS account ID linked to the partner profile. Required in requests if `ProfileId` is not provided.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** ProfileId **   <a name="AWSPartnerCentral-Type-account_QualificationsAssociationPartner-ProfileId"></a>
The unique identifier for the partner profile, in the format `pprofile-*`. Required in requests if `AccountId` is not provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `pprofile-[A-Za-z0-9]{13}`
Required: No

## See Also
<a name="API_account_QualificationsAssociationPartner_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/QualificationsAssociationPartner)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/QualificationsAssociationPartner)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/QualificationsAssociationPartner)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
