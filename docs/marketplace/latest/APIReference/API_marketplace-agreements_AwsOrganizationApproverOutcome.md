---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AwsOrganizationApproverOutcome.html
---

# AwsOrganizationApproverOutcome

The decision of the administrators of the buyer's AWS organization. The management account or a delegated administrator of the organization makes this decision.

## Contents
<a name="API_marketplace-agreements_AwsOrganizationApproverOutcome_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** status **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AwsOrganizationApproverOutcome-status"></a>
The decision status of the approver. Possible values include `QUEUED`, `PENDING_APPROVAL`, `APPROVED`, `REJECTED`, `EXPIRED`, and `SKIPPED`.
Type: String
Valid Values: `QUEUED | PENDING_APPROVAL | APPROVED | REJECTED | EXPIRED | SKIPPED`
Required: Yes

 ** updatedAt **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AwsOrganizationApproverOutcome-updatedAt"></a>
The date and time when the decision was last updated.
Type: Timestamp
Required: Yes

 ** approverOutcomeId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AwsOrganizationApproverOutcome-approverOutcomeId"></a>
The unique identifier of this approver in the agreement approval.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `aprout-[A-Za-z0-9-]+`
Required: No

 ** note **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AwsOrganizationApproverOutcome-note"></a>
The note that the approver provided with the decision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** purchaseOrders **   <a name="AWSMarketplaceService-Type-marketplace-agreements_AwsOrganizationApproverOutcome-purchaseOrders"></a>
The purchase order references that the approver provided with the decision.
Type: Array of [AgreementApprovalPurchaseOrder](API_marketplace-agreements_AgreementApprovalPurchaseOrder.md) objects
Array Members: Minimum number of 1 item. Maximum number of 86 items.
Required: No

## See Also
<a name="API_marketplace-agreements_AwsOrganizationApproverOutcome_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AwsOrganizationApproverOutcome)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AwsOrganizationApproverOutcome)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AwsOrganizationApproverOutcome)
