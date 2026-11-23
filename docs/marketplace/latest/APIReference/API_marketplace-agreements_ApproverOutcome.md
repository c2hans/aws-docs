---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ApproverOutcome.html
---

# ApproverOutcome

An approver in an agreement approval and the approver's decision.

## Contents
<a name="API_marketplace-agreements_ApproverOutcome_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsOrganizationApproverOutcome **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ApproverOutcome-awsOrganizationApproverOutcome"></a>
The decision of the administrators of the buyer's AWS organization.
Type: [AwsOrganizationApproverOutcome](API_marketplace-agreements_AwsOrganizationApproverOutcome.md) object
Required: No

 ** emailApproverOutcome **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ApproverOutcome-emailApproverOutcome"></a>
The decision of an approver who is identified by an email address.
Type: [EmailApproverOutcome](API_marketplace-agreements_EmailApproverOutcome.md) object
Required: No

 ** procurementToolApproverOutcome **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ApproverOutcome-procurementToolApproverOutcome"></a>
The decision of a procurement system.
Type: [ProcurementToolApproverOutcome](API_marketplace-agreements_ProcurementToolApproverOutcome.md) object
Required: No

## See Also
<a name="API_marketplace-agreements_ApproverOutcome_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ApproverOutcome)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ApproverOutcome)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ApproverOutcome)
