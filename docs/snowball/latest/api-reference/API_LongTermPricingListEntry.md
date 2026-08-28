---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_LongTermPricingListEntry.html
---

# LongTermPricingListEntry
<a name="API_LongTermPricingListEntry"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Each `LongTermPricingListEntry` object contains information about a long-term pricing type.

## Contents
<a name="API_LongTermPricingListEntry_Contents"></a>

 ** CurrentActiveJob **   <a name="Snowball-Type-LongTermPricingListEntry-CurrentActiveJob"></a>
The current active jobs on the device the long-term pricing type.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** IsLongTermPricingAutoRenew **   <a name="Snowball-Type-LongTermPricingListEntry-IsLongTermPricingAutoRenew"></a>
If set to `true`, specifies that the current long-term pricing type for the device should be automatically renewed before the long-term pricing contract expires.
Type: Boolean
Required: No

 ** JobIds **   <a name="Snowball-Type-LongTermPricingListEntry-JobIds"></a>
The IDs of the jobs that are associated with a long-term pricing type.
Type: Array of strings
Length Constraints: Fixed length of 39.
Pattern: `(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** LongTermPricingEndDate **   <a name="Snowball-Type-LongTermPricingListEntry-LongTermPricingEndDate"></a>
The end date the long-term pricing contract.
Type: Timestamp
Required: No

 ** LongTermPricingId **   <a name="Snowball-Type-LongTermPricingListEntry-LongTermPricingId"></a>
The ID of the long-term pricing type for the device.
Type: String
Length Constraints: Fixed length of 41.
Pattern: `LTPID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** LongTermPricingStartDate **   <a name="Snowball-Type-LongTermPricingListEntry-LongTermPricingStartDate"></a>
The start date of the long-term pricing contract.
Type: Timestamp
Required: No

 ** LongTermPricingStatus **   <a name="Snowball-Type-LongTermPricingListEntry-LongTermPricingStatus"></a>
The status of the long-term pricing type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** LongTermPricingType **   <a name="Snowball-Type-LongTermPricingListEntry-LongTermPricingType"></a>
The type of long-term pricing that was selected for the device.
Type: String
Valid Values: `OneYear | ThreeYear | OneMonth`
Required: No

 ** ReplacementJob **   <a name="Snowball-Type-LongTermPricingListEntry-ReplacementJob"></a>
A new device that replaces a device that is ordered with long-term pricing.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `(M|J)ID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** SnowballType **   <a name="Snowball-Type-LongTermPricingListEntry-SnowballType"></a>
The type of Snow Family devices associated with this long-term pricing job.
Type: String
Valid Values: `STANDARD | EDGE | EDGE_C | EDGE_CG | EDGE_S | SNC1_HDD | SNC1_SSD | V3_5C | V3_5S | RACK_5U_C`
Required: No

## See Also
<a name="API_LongTermPricingListEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/LongTermPricingListEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/LongTermPricingListEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/LongTermPricingListEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
