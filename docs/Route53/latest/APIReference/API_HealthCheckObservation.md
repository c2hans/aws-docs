---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckObservation.html
---

# HealthCheckObservation
<a name="API_HealthCheckObservation"></a>

A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker.

## Contents
<a name="API_HealthCheckObservation_Contents"></a>

 ** IPAddress **   <a name="Route53-Type-HealthCheckObservation-IPAddress"></a>
The IP address of the Amazon Route 53 health checker that provided the failure reason in `StatusReport`.
Type: String
Length Constraints: Maximum length of 45.
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`
Required: No

 ** Region **   <a name="Route53-Type-HealthCheckObservation-Region"></a>
The region of the Amazon Route 53 health checker that provided the status in `StatusReport`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `us-east-1 | us-west-1 | us-west-2 | eu-west-1 | ap-southeast-1 | ap-southeast-2 | ap-northeast-1 | sa-east-1`
Required: No

 ** StatusReport **   <a name="Route53-Type-HealthCheckObservation-StatusReport"></a>
A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker and the time of the failed health check.
Type: [StatusReport](API_StatusReport.md) object
Required: No

## See Also
<a name="API_HealthCheckObservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/HealthCheckObservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/HealthCheckObservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/HealthCheckObservation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
