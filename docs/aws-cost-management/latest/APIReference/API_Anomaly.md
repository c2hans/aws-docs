---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Anomaly.html
---

# Anomaly
<a name="API_Anomaly"></a>

An unusual cost pattern. This consists of the detailed metadata and the current status of the anomaly object.

## Contents
<a name="API_Anomaly_Contents"></a>

 ** AnomalyId **   <a name="awscostmanagement-Type-Anomaly-AnomalyId"></a>
The unique identifier for the anomaly.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** AnomalyScore **   <a name="awscostmanagement-Type-Anomaly-AnomalyScore"></a>
The latest and maximum score for the anomaly.
Type: [AnomalyScore](API_AnomalyScore.md) object
Required: Yes

 ** Impact **   <a name="awscostmanagement-Type-Anomaly-Impact"></a>
The dollar impact for the anomaly.
Type: [Impact](API_Impact.md) object
Required: Yes

 ** MonitorArn **   <a name="awscostmanagement-Type-Anomaly-MonitorArn"></a>
The Amazon Resource Name (ARN) for the cost monitor that generated this anomaly.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** AnomalyEndDate **   <a name="awscostmanagement-Type-Anomaly-AnomalyEndDate"></a>
The last day the anomaly is detected.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40.
Pattern: `(\d{4}-\d{2}-\d{2})(T\d{2}:\d{2}:\d{2}Z)?`
Required: No

 ** AnomalyStartDate **   <a name="awscostmanagement-Type-Anomaly-AnomalyStartDate"></a>
The first day the anomaly is detected.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40.
Pattern: `(\d{4}-\d{2}-\d{2})(T\d{2}:\d{2}:\d{2}Z)?`
Required: No

 ** DimensionValue **   <a name="awscostmanagement-Type-Anomaly-DimensionValue"></a>
The dimension for the anomaly (for example, an AWS service in a service monitor).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Feedback **   <a name="awscostmanagement-Type-Anomaly-Feedback"></a>
The feedback value.
Type: String
Valid Values: `YES | NO | PLANNED_ACTIVITY`
Required: No

 ** RootCauses **   <a name="awscostmanagement-Type-Anomaly-RootCauses"></a>
The list of identified root causes for the anomaly.
Type: Array of [RootCause](API_RootCause.md) objects
Required: No

## See Also
<a name="API_Anomaly_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/Anomaly)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/Anomaly)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/Anomaly)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
