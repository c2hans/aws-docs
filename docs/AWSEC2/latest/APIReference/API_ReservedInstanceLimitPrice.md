---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReservedInstanceLimitPrice.html
---

# ReservedInstanceLimitPrice
<a name="API_ReservedInstanceLimitPrice"></a>

Describes the limit price of a Reserved Instance offering.

## Contents
<a name="API_ReservedInstanceLimitPrice_Contents"></a>

 ** Amount **
Used for Reserved Instance Marketplace offerings. Specifies the limit price on the total order (instanceCount \* price).
Type: Double
Required: No

 ** CurrencyCode **
The currency in which the `limitPrice` amount is specified. At this time, the only supported currency is `USD`.
Type: String
Valid Values: `USD`
Required: No

## See Also
<a name="API_ReservedInstanceLimitPrice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReservedInstanceLimitPrice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReservedInstanceLimitPrice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReservedInstanceLimitPrice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
