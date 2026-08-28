---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LicenseRecommendation.html
---

# LicenseRecommendation
<a name="API_LicenseRecommendation"></a>

 Describes a license recommendation for an EC2 instance.

## Contents
<a name="API_LicenseRecommendation_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-LicenseRecommendation-accountId"></a>
 The AWS account ID of the license.
Type: String
Required: No

 ** currentLicenseConfiguration **   <a name="computeoptimizer-Type-LicenseRecommendation-currentLicenseConfiguration"></a>
 An object that describes the current configuration of an instance that runs on a license.
Type: [LicenseConfiguration](API_LicenseConfiguration.md) object
Required: No

 ** finding **   <a name="computeoptimizer-Type-LicenseRecommendation-finding"></a>
 The finding classification for an instance that runs on a license.
Findings include:
+  `InsufficentMetrics` — When Compute Optimizer detects that your CloudWatch Application Insights isn't enabled or is enabled with insufficient permissions.
+  `NotOptimized` — When Compute Optimizer detects that your EC2 infrastructure isn't using any of the SQL server license features you're paying for, a license is considered not optimized.
+  `Optimized` — When Compute Optimizer detects that all specifications of your license meet the performance requirements of your workload.
Type: String
Valid Values: `InsufficientMetrics | Optimized | NotOptimized`
Required: No

 ** findingReasonCodes **   <a name="computeoptimizer-Type-LicenseRecommendation-findingReasonCodes"></a>
 The reason for the finding classification for an instance that runs on a license.
Finding reason codes include:
+  `Optimized` — All specifications of your license meet the performance requirements of your workload.
+  `LicenseOverprovisioned` — A license is considered over-provisioned when your license can be downgraded while still meeting the performance requirements of your workload.
+  `InvalidCloudwatchApplicationInsights` — CloudWatch Application Insights isn't configured properly.
+  `CloudwatchApplicationInsightsError` — There is a CloudWatch Application Insights error.
Type: Array of strings
Valid Values: `InvalidCloudWatchApplicationInsightsSetup | CloudWatchApplicationInsightsError | LicenseOverprovisioned | Optimized`
Required: No

 ** lastRefreshTimestamp **   <a name="computeoptimizer-Type-LicenseRecommendation-lastRefreshTimestamp"></a>
 The timestamp of when the license recommendation was last generated.
Type: Timestamp
Required: No

 ** licenseRecommendationOptions **   <a name="computeoptimizer-Type-LicenseRecommendation-licenseRecommendationOptions"></a>
 An array of objects that describe the license recommendation options.
Type: Array of [LicenseRecommendationOption](API_LicenseRecommendationOption.md) objects
Required: No

 ** lookbackPeriodInDays **   <a name="computeoptimizer-Type-LicenseRecommendation-lookbackPeriodInDays"></a>
 The number of days for which utilization metrics were analyzed for an instance that runs on a license.
Type: Double
Required: No

 ** resourceArn **   <a name="computeoptimizer-Type-LicenseRecommendation-resourceArn"></a>
 The ARN that identifies the Amazon EC2 instance.
Type: String
Required: No

 ** tags **   <a name="computeoptimizer-Type-LicenseRecommendation-tags"></a>
 A list of tags assigned to an EC2 instance.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_LicenseRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/LicenseRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/LicenseRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/LicenseRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
