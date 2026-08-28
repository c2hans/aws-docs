---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_ItemizedCharge.html
---

# ItemizedCharge
<a name="API_marketplace-agreements_ItemizedCharge"></a>

A breakdown of individual charges or line items within a billing or pricing context.

## Contents
<a name="API_marketplace-agreements_ItemizedCharge_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** chargeReference **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ItemizedCharge-chargeReference"></a>
The identifier of the expected charge that this itemized charge contributes to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** dimensionKey **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ItemizedCharge-dimensionKey"></a>
The dimension key as specified in the accepted term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** incrementalChargeAmount **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ItemizedCharge-incrementalChargeAmount"></a>
The total incremental charge amount for this dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** newQuantity **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ItemizedCharge-newQuantity"></a>
The requested quantity for this dimension.
Type: Integer
Required: No

 ** oldQuantity **   <a name="AWSMarketplaceService-Type-marketplace-agreements_ItemizedCharge-oldQuantity"></a>
The existing quantity for this dimension from the source agreement. This value is `0` for NEW intent.
Type: Integer
Required: No

## See Also
<a name="API_marketplace-agreements_ItemizedCharge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/ItemizedCharge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ItemizedCharge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/ItemizedCharge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
