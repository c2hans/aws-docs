---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_FreeTierUsage.html
---

# FreeTierUsage
<a name="API_freetier_FreeTierUsage"></a>

Consists of a AWS Free Tier offer’s metadata and your data usage for the offer.

## Contents
<a name="API_freetier_FreeTierUsage_Contents"></a>

 ** actualUsageAmount **   <a name="awscostmanagement-Type-freetier_FreeTierUsage-actualUsageAmount"></a>
Describes the actual usage accrued month-to-day (MTD) that you've used so far.
Type: Double
Required: No

 ** description **   <a name="awscostmanagement-Type-freetier_FreeTierUsage-description"></a>
The description of the Free Tier offer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** forecastedUsageAmount **   <a name="awscostmanagement-Type-freetier_FreeTierUsage-forecastedUsageAmount"></a>
Describes the forecasted usage by the month that you're expected to use.
Type: Double
Required: No

 ** freeTierType **   <a name="awscostmanagement-Type-freetier_FreeTierUsage-freeTierType"></a>
Describes the type of the Free Tier offer. For example, the offer can be `"12 Months Free"`, `"Always Free"`, and `"Free Trial"`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** limit **   <a name="awscostmanagement-Type-freetier_FreeTierUsage-limit"></a>
Describes the maximum usage allowed in Free Tier.
Type: Double
Required: No

 ** operation **   <a name="awscostmanagement-Type-freetier_FreeTierUsage-operation"></a>
Describes `usageType` more granularly with the specific AWS service API operation. For example, this can be the `RunInstances` API operation for Amazon Elastic Compute Cloud.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** region **   <a name="awscostmanagement-Type-freetier_FreeTierUsage-region"></a>
Describes the AWS Region for which this offer is applicable
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** service **   <a name="awscostmanagement-Type-freetier_FreeTierUsage-service"></a>
The name of the AWS service providing the Free Tier offer. For example, this can be Amazon Elastic Compute Cloud.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** unit **   <a name="awscostmanagement-Type-freetier_FreeTierUsage-unit"></a>
Describes the unit of the `usageType`, such as `Hrs`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** usageType **   <a name="awscostmanagement-Type-freetier_FreeTierUsage-usageType"></a>
Describes the usage details of the offer. For example, this might be `Global-BoxUsage:freetrial`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_freetier_FreeTierUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/freetier-2023-09-07/FreeTierUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/freetier-2023-09-07/FreeTierUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/freetier-2023-09-07/FreeTierUsage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
