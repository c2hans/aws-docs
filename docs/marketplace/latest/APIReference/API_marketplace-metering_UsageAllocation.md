---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_UsageAllocation.html
---

# UsageAllocation
<a name="API_marketplace-metering_UsageAllocation"></a>

Usage allocations allow you to split usage into buckets by tags.

Each `UsageAllocation` indicates the usage quantity for a specific set of tags.

## Contents
<a name="API_marketplace-metering_UsageAllocation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AllocatedUsageQuantity **   <a name="AWSMarketplaceService-Type-marketplace-metering_UsageAllocation-AllocatedUsageQuantity"></a>
The total quantity allocated to this bucket of usage.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** Tags **   <a name="AWSMarketplaceService-Type-marketplace-metering_UsageAllocation-Tags"></a>
The set of tags that define the bucket of usage. For the bucket of items with no tags, this parameter can be left out.
Type: Array of [Tag](API_marketplace-metering_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_marketplace-metering_UsageAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/meteringmarketplace-2016-01-14/UsageAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/meteringmarketplace-2016-01-14/UsageAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/meteringmarketplace-2016-01-14/UsageAllocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
