---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Route53HealthCheck.html
---

# Route53HealthCheck
<a name="API_Route53HealthCheck"></a>

The Amazon Route 53 health check.

## Contents
<a name="API_Route53HealthCheck_Contents"></a>

 ** hostedZoneId **   <a name="regionswitch-Type-Route53HealthCheck-hostedZoneId"></a>
The Amazon Route 53 health check hosted zone ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** recordName **   <a name="regionswitch-Type-Route53HealthCheck-recordName"></a>
The Amazon Route 53 record name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** region **   <a name="regionswitch-Type-Route53HealthCheck-region"></a>
The Amazon Route 53 Region.
Type: String
Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: Yes

 ** healthCheckId **   <a name="regionswitch-Type-Route53HealthCheck-healthCheckId"></a>
The Amazon Route 53 health check ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** status **   <a name="regionswitch-Type-Route53HealthCheck-status"></a>
The Amazon Route 53 health check status.
Type: String
Valid Values: `healthy | unhealthy | unknown`
Required: No

## See Also
<a name="API_Route53HealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/Route53HealthCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/Route53HealthCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/Route53HealthCheck)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
