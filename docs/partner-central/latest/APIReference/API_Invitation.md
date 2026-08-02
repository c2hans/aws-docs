---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_Invitation.html
---

# Invitation
<a name="API_Invitation"></a>

 The Invitation structure represents an invitation exchanged between partners and AWS. It includes a message, receiver information, and a payload providing context for the invitation.

## Contents
<a name="API_Invitation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Message **   <a name="AWSPartnerCentral-Type-Invitation-Message"></a>
 A message accompanying the invitation.
Type: String
Pattern: `(?s).{1,255}`
Required: Yes

 ** Payload **   <a name="AWSPartnerCentral-Type-Invitation-Payload"></a>
Contains the data payload associated with the Engagement Invitation. This payload includes essential details related to the AWS opportunity and is used by partners to evaluate whether to accept or reject the engagement.
Type: [Payload](API_Payload.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Receiver **   <a name="AWSPartnerCentral-Type-Invitation-Receiver"></a>
Represents the entity that received the Engagement Invitation, including account and company details. This field is essential for tracking the partner who is being invited to collaborate.
Type: [Receiver](API_Receiver.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_Invitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/Invitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/Invitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/Invitation)
