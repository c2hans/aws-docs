---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_ConnectionTypeDetail.html
---

# ConnectionTypeDetail
<a name="API_account_ConnectionTypeDetail"></a>

Detailed information about a specific connection type within a connection.

## Contents
<a name="API_account_ConnectionTypeDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreatedAt **   <a name="AWSPartnerCentral-Type-account_ConnectionTypeDetail-CreatedAt"></a>
The timestamp when this connection type was created.
Type: Timestamp
Required: Yes

 ** InviterEmail **   <a name="AWSPartnerCentral-Type-account_ConnectionTypeDetail-InviterEmail"></a>
The email address of the person who initiated this connection type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 320.
Pattern: `[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*`
Required: Yes

 ** InviterName **   <a name="AWSPartnerCentral-Type-account_ConnectionTypeDetail-InviterName"></a>
The name of the person who initiated this connection type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`
Required: Yes

 ** OtherParticipant **   <a name="AWSPartnerCentral-Type-account_ConnectionTypeDetail-OtherParticipant"></a>
Information about the other participant in this connection type.
Type: [Participant](API_account_Participant.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Status **   <a name="AWSPartnerCentral-Type-account_ConnectionTypeDetail-Status"></a>
The current status of this connection type.
Type: String
Valid Values: `ACTIVE | CANCELED`
Required: Yes

 ** CanceledAt **   <a name="AWSPartnerCentral-Type-account_ConnectionTypeDetail-CanceledAt"></a>
The timestamp when this connection type was cancelled, if applicable.
Type: Timestamp
Required: No

 ** CanceledBy **   <a name="AWSPartnerCentral-Type-account_ConnectionTypeDetail-CanceledBy"></a>
The AWS account ID of the participant who cancelled this connection type.
Type: String
Pattern: `[0-9]{12}`
Required: No

## See Also
<a name="API_account_ConnectionTypeDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/ConnectionTypeDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/ConnectionTypeDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/ConnectionTypeDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
