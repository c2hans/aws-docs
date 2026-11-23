---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_Approver.html
---

# Approver

An approver in an approval plan.

## Contents
<a name="API_marketplace-agreements_Approver_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsOrganizationAdminApprover **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Approver-awsOrganizationAdminApprover"></a>
The administrators of the buyer's AWS organization.
Type: [AwsOrganizationAdminApprover](API_marketplace-agreements_AwsOrganizationAdminApprover.md) object
Required: No

 ** emailApprover **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Approver-emailApprover"></a>
An approver who is identified by an email address.
Type: [EmailApprover](API_marketplace-agreements_EmailApprover.md) object
Required: No

 ** procurementToolApprover **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Approver-procurementToolApprover"></a>
A procurement system that approves through the buyer's procurement integration.
Type: [ProcurementToolApprover](API_marketplace-agreements_ProcurementToolApprover.md) object
Required: No

## See Also
<a name="API_marketplace-agreements_Approver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/Approver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/Approver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/Approver)
