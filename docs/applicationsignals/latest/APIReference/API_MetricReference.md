---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_MetricReference.html
---

# MetricReference
<a name="API_MetricReference"></a>

This structure contains information about one CloudWatch metric associated with this entity discovered by Application Signals.

## Contents
<a name="API_MetricReference_Contents"></a>

 ** MetricName **   <a name="applicationsignals-Type-MetricReference-MetricName"></a>
The name of the metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** MetricType **   <a name="applicationsignals-Type-MetricReference-MetricType"></a>
Used to display the appropriate statistics in the CloudWatch console.
Type: String
Pattern: `[A-Za-z0-9 -]+`
Required: Yes

 ** Namespace **   <a name="applicationsignals-Type-MetricReference-Namespace"></a>
The namespace of the metric. For more information, see [CloudWatchNamespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*[^:].*`
Required: Yes

 ** AccountId **   <a name="applicationsignals-Type-MetricReference-AccountId"></a>
 AWS account ID.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** Dimensions **   <a name="applicationsignals-Type-MetricReference-Dimensions"></a>
An array of one or more dimensions that further define the metric. For more information, see [CloudWatchDimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension).
Type: Array of [Dimension](API_Dimension.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

## See Also
<a name="API_MetricReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/MetricReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/MetricReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/MetricReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
