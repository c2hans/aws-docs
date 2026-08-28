---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_QuoteCapacity.html
---

# QuoteCapacity
<a name="API_QuoteCapacity"></a>

A capacity requirement for a quote. Specifies the type of capacity, the unit, and the quantity.

## Contents
<a name="API_QuoteCapacity_Contents"></a>

 ** Quantity **   <a name="outposts-Type-QuoteCapacity-Quantity"></a>
The quantity of the specified capacity unit. For Amazon EC2, this is the number of additional instances to add to the Outpost. For Amazon EBS and Amazon S3, this is the total desired end-state capacity of the Outpost.
Type: Float
Required: No

 ** QuoteCapacityType **   <a name="outposts-Type-QuoteCapacity-QuoteCapacityType"></a>
The type of capacity. Valid values are `EC2`, `EBS`, and `S3`.
Type: String
Valid Values: `EC2 | EBS | S3`
Required: No

 ** Unit **   <a name="outposts-Type-QuoteCapacity-Unit"></a>
The unit of measurement for the capacity. For Amazon EC2, this is the instance type (for example, `c5.24xlarge`). For Amazon EBS and Amazon S3, this is the storage unit (for example, `TiB` for tebibytes).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[\S \n]+$`
Required: No

## See Also
<a name="API_QuoteCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/QuoteCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/QuoteCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/QuoteCapacity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
