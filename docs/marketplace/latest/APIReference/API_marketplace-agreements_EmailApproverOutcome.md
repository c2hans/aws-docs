---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_EmailApproverOutcome.html
---

# EmailApproverOutcome

The decision of an approver who is identified by an email address.

## Contents
<a name="API_marketplace-agreements_EmailApproverOutcome_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** emailAddress **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EmailApproverOutcome-emailAddress"></a>
The email address of the approver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}`
Required: Yes

 ** status **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EmailApproverOutcome-status"></a>
The decision status of the approver. Possible values include `QUEUED`, `PENDING_APPROVAL`, `APPROVED`, `REJECTED`, `EXPIRED`, and `SKIPPED`.
Type: String
Valid Values: `QUEUED | PENDING_APPROVAL | APPROVED | REJECTED | EXPIRED | SKIPPED`
Required: Yes

 ** updatedAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EmailApproverOutcome-updatedAt"></a>
The date and time when the decision was last updated.
Type: Timestamp
Required: Yes

 ** approverOutcomeId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EmailApproverOutcome-approverOutcomeId"></a>
The unique identifier of this approver in the agreement approval. An administrator of the buyer's AWS organization passes it as `approverOutcomeIdToOverride` to decide on the approver's behalf.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `aprout-[A-Za-z0-9-]+`
Required: No

 ** name **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EmailApproverOutcome-name"></a>
The name of the approver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** note **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EmailApproverOutcome-note"></a>
The note that the approver provided with the decision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** overriddenBy **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EmailApproverOutcome-overriddenBy"></a>
The identity that decided on the approver's behalf. This field is empty unless an administrator of the buyer's AWS organization decided for the approver.
Type: [CallerIdentity](API_marketplace-agreements_CallerIdentity.md) object
Required: No

 ** purchaseOrders **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EmailApproverOutcome-purchaseOrders"></a>
The purchase order references that the approver provided with the decision.
Type: Array of [AgreementApprovalPurchaseOrder](API_marketplace-agreements_AgreementApprovalPurchaseOrder.md) objects
Array Members: Minimum number of 1 item. Maximum number of 86 items.
Required: No

## See Also
<a name="API_marketplace-agreements_EmailApproverOutcome_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/EmailApproverOutcome)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/EmailApproverOutcome)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/EmailApproverOutcome)
