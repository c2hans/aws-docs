---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_UsageRecordResult.html
---

# UsageRecordResult
<a name="API_marketplace-metering_UsageRecordResult"></a>

A `UsageRecordResult` indicates the status of a given `UsageRecord` processed by `BatchMeterUsage`.

## Contents
<a name="API_marketplace-metering_UsageRecordResult_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MeteringRecordId **   <a name="AWSMarketplaceService-Type-marketplace-metering_UsageRecordResult-MeteringRecordId"></a>
The `MeteringRecordId` is a unique identifier for this metering event.
Type: String
Required: No

 ** Status **   <a name="AWSMarketplaceService-Type-marketplace-metering_UsageRecordResult-Status"></a>
The `UsageRecordResult` `Status` indicates the status of an individual `UsageRecord` processed by `BatchMeterUsage`.
+  *Success*- The `UsageRecord` was accepted and honored by `BatchMeterUsage`.
+  *CustomerNotSubscribed*- The `CustomerIdentifier` specified is not able to use your product. The `UsageRecord` was not honored. There are three causes for this result:
  + The customer identifier is invalid.
  + The customer identifier provided in the metering record does not have an active agreement or subscription with this product. Future `UsageRecords` for this customer will fail until the customer subscribes to your product.
  + The customer's AWS account was suspended.
+  *DuplicateRecord*- Indicates that the `UsageRecord` was invalid and not honored. A previously metered `UsageRecord` had the same customer, dimension, and time, but a different quantity.
Type: String
Valid Values: `Success | CustomerNotSubscribed | DuplicateRecord`
Required: No

 ** UsageRecord **   <a name="AWSMarketplaceService-Type-marketplace-metering_UsageRecordResult-UsageRecord"></a>
The `UsageRecord` that was part of the `BatchMeterUsage` request.
Type: [UsageRecord](API_marketplace-metering_UsageRecord.md) object
Required: No

## See Also
<a name="API_marketplace-metering_UsageRecordResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/meteringmarketplace-2016-01-14/UsageRecordResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/meteringmarketplace-2016-01-14/UsageRecordResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/meteringmarketplace-2016-01-14/UsageRecordResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
