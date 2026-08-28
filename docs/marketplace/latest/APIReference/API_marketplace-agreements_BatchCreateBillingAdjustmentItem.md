---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_BatchCreateBillingAdjustmentItem.html
---

# BatchCreateBillingAdjustmentItem
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentItem"></a>

A successfully created billing adjustment request item.

## Contents
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** billingAdjustmentRequestId **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BatchCreateBillingAdjustmentItem-billingAdjustmentRequestId"></a>
The unique identifier of the created billing adjustment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ba-[a-zA-Z0-9]+`
Required: Yes

 ** clientToken **   <a name="AWSMarketplaceService-Type-marketplace-agreements_BatchCreateBillingAdjustmentItem-clientToken"></a>
The client token provided in the corresponding request entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## See Also
<a name="API_marketplace-agreements_BatchCreateBillingAdjustmentItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/BatchCreateBillingAdjustmentItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
