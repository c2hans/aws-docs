---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_UsageLimit.html
---

# UsageLimit
<a name="API_UsageLimit"></a>

Describes a usage limit object for a cluster.

## Contents
<a name="API_UsageLimit_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Amount **
The limit amount. If time-based, this amount is in minutes. If data-based, this amount is in terabytes (TB).
Type: Long
Required: No

 ** BreachAction **
The action that Amazon Redshift takes when the limit is reached. Possible values are:
+  **log** - To log an event in a system table. The default is log.
+  **emit-metric** - To emit CloudWatch metrics.
+  **disable** - To disable the feature until the next usage period begins.
Type: String
Valid Values: `log | emit-metric | disable`
Required: No

 ** ClusterIdentifier **
The identifier of the cluster with a usage limit.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** FeatureType **
The Amazon Redshift feature to which the limit applies.
Type: String
Valid Values: `spectrum | concurrency-scaling | cross-region-datasharing | extra-compute-for-automatic-optimization`
Required: No

 ** LimitType **
The type of limit. Depending on the feature type, this can be based on a time duration or data size.
Type: String
Valid Values: `time | data-scanned`
Required: No

 ** Period **
The time period that the amount applies to. A `weekly` period begins on Sunday. The default is `monthly`.
Type: String
Valid Values: `daily | weekly | monthly`
Required: No

 ** Tags.Tag.N **
A list of tag instances.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** UsageLimitId **
The identifier of the usage limit.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

## See Also
<a name="API_UsageLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/UsageLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/UsageLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/UsageLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
