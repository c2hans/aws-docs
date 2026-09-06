---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_UsageRecord.html
---

# UsageRecord
<a name="API_marketplace-metering_UsageRecord"></a>

A `UsageRecord` indicates a quantity of usage for a given product, customer, dimension and time.

Multiple requests with the same `UsageRecords` as input will be de-duplicated to prevent double charges.

## Contents
<a name="API_marketplace-metering_UsageRecord_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Dimension **   <a name="AWSMarketplaceService-Type-marketplace-metering_UsageRecord-Dimension"></a>
During the process of registering a product on AWS Marketplace, dimensions are specified. These represent different units of value in your application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\s\S]+`
Required: Yes

 ** Timestamp **   <a name="AWSMarketplaceService-Type-marketplace-metering_UsageRecord-Timestamp"></a>
Timestamp, in UTC, for which the usage is being reported.
Your application can meter usage for up to 24 hours in the past. Make sure the `timestamp` value is not before the start of the software usage.
At the end of each billing cycle, you have a 6-hour grace period to submit usage records for the previous billing month before 06:00 UTC on the first day of the next month.
Type: Timestamp
Required: Yes

 ** CustomerAWSAccountId **   <a name="AWSMarketplaceService-Type-marketplace-metering_UsageRecord-CustomerAWSAccountId"></a>
The `CustomerAWSAccountId` parameter specifies the AWS account ID of the buyer.
If you have an existing integration and need the `CustomerAWSAccountId` that corresponds to a `CustomerIdentifier`, contact [AWS Marketplace Seller Operations](https://aws.amazon.com/marketplace/management/contact-us/) to obtain the mapping. Do not request the `CustomerAWSAccountId` directly from buyers. We cannot verify that a buyer-provided account ID is authentic, which can result in incorrect metering or billing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[0-9]+$`
Required: No

 ** CustomerIdentifier **   <a name="AWSMarketplaceService-Type-marketplace-metering_UsageRecord-CustomerIdentifier"></a>
The `CustomerIdentifier` is obtained through the `ResolveCustomer` operation and represents an individual buyer in your application.
 `CustomerIdentifier` is not supported for new SaaS product integrations. Use `CustomerAWSAccountId` to identify the buyer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\s\S]*`
Required: No

 ** LicenseArn **   <a name="AWSMarketplaceService-Type-marketplace-metering_UsageRecord-LicenseArn"></a>
The `LicenseArn` is a unique identifier for a specific granted license. These are used for software purchased through AWS Marketplace.
To access your `CustomerAWSAccountId` and `LicenseArn` mapping, visit [Agreements Feeds](https://docs.aws.amazon.com/marketplace/latest/userguide/data-feed-agreements.html).
Type: String
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** Quantity **   <a name="AWSMarketplaceService-Type-marketplace-metering_UsageRecord-Quantity"></a>
The quantity of usage consumed by the customer for the given dimension and time. Defaults to `0` if not specified.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** UsageAllocations **   <a name="AWSMarketplaceService-Type-marketplace-metering_UsageRecord-UsageAllocations"></a>
The set of `UsageAllocations` to submit. The sum of all `UsageAllocation` quantities must equal the Quantity of the `UsageRecord`.
Type: Array of [UsageAllocation](API_marketplace-metering_UsageAllocation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2500 items.
Required: No

## See Also
<a name="API_marketplace-metering_UsageRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/meteringmarketplace-2016-01-14/UsageRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/meteringmarketplace-2016-01-14/UsageRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/meteringmarketplace-2016-01-14/UsageRecord)
