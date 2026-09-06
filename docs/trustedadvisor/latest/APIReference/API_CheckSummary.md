---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_CheckSummary.html
---

# CheckSummary
<a name="API_CheckSummary"></a>

A summary of an AWS Trusted Advisor Check

## Contents
<a name="API_CheckSummary_Contents"></a>

 ** arn **   <a name="ta-Type-CheckSummary-arn"></a>
The ARN of the AWS Trusted Advisor Check
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w-]+:trustedadvisor:::check\/[\w-]+`
Required: Yes

 ** awsServices **   <a name="ta-Type-CheckSummary-awsServices"></a>
The AWS Services that the Check applies to
Type: Array of strings
Length Constraints: Minimum length of 2. Maximum length of 30.
Required: Yes

 ** description **   <a name="ta-Type-CheckSummary-description"></a>
A description of what the AWS Trusted Advisor Check is monitoring
Type: String
Required: Yes

 ** id **   <a name="ta-Type-CheckSummary-id"></a>
The unique identifier of the AWS Trusted Advisor Check
Type: String
Required: Yes

 ** metadata **   <a name="ta-Type-CheckSummary-metadata"></a>
The column headings for the metadata returned in the resource
Type: String to string map
Required: Yes

 ** name **   <a name="ta-Type-CheckSummary-name"></a>
The name of the AWS Trusted Advisor Check
Type: String
Required: Yes

 ** pillars **   <a name="ta-Type-CheckSummary-pillars"></a>
The Recommendation pillars that the AWS Trusted Advisor Check falls under
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Valid Values: `cost_optimizing | performance | security | service_limits | fault_tolerance | operational_excellence`
Required: Yes

 ** source **   <a name="ta-Type-CheckSummary-source"></a>
The source of the Recommendation
Type: String
Valid Values: `aws_config | compute_optimizer | cost_explorer | lse | manual | pse | rds | resilience | resilience_hub | security_hub | stir | ta_check | well_architected | cost_optimization_hub`
Required: Yes

 ** awsResourceTypes **   <a name="ta-Type-CheckSummary-awsResourceTypes"></a>
The AWS resource types that this check evaluates (for example, AWS::EC2::Instance).
Type: Array of strings
Required: No

 ** checkGranularity **   <a name="ta-Type-CheckSummary-checkGranularity"></a>
The granularity level at which the check operates: resource, account, or account\_region.
Type: String
Required: No

 ** recommendationId **   <a name="ta-Type-CheckSummary-recommendationId"></a>
The recommendation identifier associated with the check.
Type: String
Required: No

 ** resourceArnQueryable **   <a name="ta-Type-CheckSummary-resourceArnQueryable"></a>
Indicates whether this check is supported by the ListRecommendationsForResource API.
Type: Boolean
Required: No

## See Also
<a name="API_CheckSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/CheckSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/CheckSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/CheckSummary)
