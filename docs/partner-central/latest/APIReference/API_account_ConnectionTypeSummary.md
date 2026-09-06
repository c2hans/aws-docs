---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_ConnectionTypeSummary.html
---

# ConnectionTypeSummary
<a name="API_account_ConnectionTypeSummary"></a>

Summary information about a specific connection type between partners.

## Contents
<a name="API_account_ConnectionTypeSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** OtherParticipant **   <a name="AWSPartnerCentral-Type-account_ConnectionTypeSummary-OtherParticipant"></a>
Information about the other participant in this connection type.
Type: [Participant](API_account_Participant.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Status **   <a name="AWSPartnerCentral-Type-account_ConnectionTypeSummary-Status"></a>
The current status of this connection type (active, canceled, etc.).
Type: String
Valid Values: `ACTIVE | CANCELED`
Required: Yes

## See Also
<a name="API_account_ConnectionTypeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/ConnectionTypeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/ConnectionTypeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/ConnectionTypeSummary)
