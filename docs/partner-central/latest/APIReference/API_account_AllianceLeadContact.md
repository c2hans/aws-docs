---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_AllianceLeadContact.html
---

# AllianceLeadContact
<a name="API_account_AllianceLeadContact"></a>

Contains contact information for the primary alliance lead responsible for partnership activities.

## Contents
<a name="API_account_AllianceLeadContact_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BusinessTitle **   <a name="AWSPartnerCentral-Type-account_AllianceLeadContact-BusinessTitle"></a>
The business title or role of the alliance lead contact person.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

 ** Email **   <a name="AWSPartnerCentral-Type-account_AllianceLeadContact-Email"></a>
The email address of the alliance lead contact person.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 320.
Pattern: `[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*`
Required: Yes

 ** FirstName **   <a name="AWSPartnerCentral-Type-account_AllianceLeadContact-FirstName"></a>
The first name of the alliance lead contact person.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

 ** LastName **   <a name="AWSPartnerCentral-Type-account_AllianceLeadContact-LastName"></a>
The last name of the alliance lead contact person.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

## See Also
<a name="API_account_AllianceLeadContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/AllianceLeadContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/AllianceLeadContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/AllianceLeadContact)
