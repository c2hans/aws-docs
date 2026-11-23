---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AccountPlanningInvitationPayload.html
---

# AccountPlanningInvitationPayload

The content of an account-planning invitation. It carries what the invited party needs to identify which account the plan concerns, because the receiver can't read the account resource directly. The account can be named by its identifier, by a customer identity snapshot, or both.

## Contents
<a name="API_AccountPlanningInvitationPayload_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccountIdentifier **   <a name="AWSPartnerCentral-Type-AccountPlanningInvitationPayload-AccountIdentifier"></a>
The identifier of the customer account that the plan concerns, as an Amazon Resource Name (ARN) or a customer account identifier.
Type: String
Pattern: `(arn:.*|cust-acc-[0-9a-z]{13})`
Required: No

 ** Customer **   <a name="AWSPartnerCentral-Type-AccountPlanningInvitationPayload-Customer"></a>
A caller-supplied snapshot of the customer company's identity, so that the receiver can tell which account the plan concerns even when the account isn't yet mapped to an AWS account.
Type: [AccountCustomer](API_AccountCustomer.md) object
Required: No

 ** PreferredContact **   <a name="AWSPartnerCentral-Type-AccountPlanningInvitationPayload-PreferredContact"></a>
When the sender prefers to be contacted about this account plan. This information is advisory.
Type: [PreferredContactWindow](API_PreferredContactWindow.md) object
Required: No

 ** SenderContacts **   <a name="AWSPartnerCentral-Type-AccountPlanningInvitationPayload-SenderContacts"></a>
The sender's contact information for this account plan.
Type: Array of [SenderContact](API_SenderContact.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: No

## See Also
<a name="API_AccountPlanningInvitationPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AccountPlanningInvitationPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AccountPlanningInvitationPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AccountPlanningInvitationPayload)
