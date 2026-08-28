---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PriceSchedule.html
---

# PriceSchedule
<a name="API_PriceSchedule"></a>

Describes the price for a Reserved Instance.

## Contents
<a name="API_PriceSchedule_Contents"></a>

 ** active **
The current price schedule, as determined by the term remaining for the Reserved Instance in the listing.
A specific price schedule is always in effect, but only one price schedule can be active at any time. Take, for example, a Reserved Instance listing that has five months remaining in its term. When you specify price schedules for five months and two months, this means that schedule 1, covering the first three months of the remaining term, will be active during months 5, 4, and 3. Then schedule 2, covering the last two months of the term, will be active for months 2 and 1.
Type: Boolean
Required: No

 ** currencyCode **
The currency for transacting the Reserved Instance resale. At this time, the only supported currency is `USD`.
Type: String
Valid Values: `USD`
Required: No

 ** price **
The fixed price for the term.
Type: Double
Required: No

 ** term **
The number of months remaining in the reservation. For example, 2 is the second to the last month before the capacity reservation expires.
Type: Long
Required: No

## See Also
<a name="API_PriceSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PriceSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PriceSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PriceSchedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
