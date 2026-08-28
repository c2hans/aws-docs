---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Route53HealthCheckConfiguration.html
---

# Route53HealthCheckConfiguration
<a name="API_Route53HealthCheckConfiguration"></a>

The Amazon Route 53 health check configuration.

## Contents
<a name="API_Route53HealthCheckConfiguration_Contents"></a>

 ** hostedZoneId **   <a name="regionswitch-Type-Route53HealthCheckConfiguration-hostedZoneId"></a>
The Amazon Route 53 health check configuration hosted zone ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** recordName **   <a name="regionswitch-Type-Route53HealthCheckConfiguration-recordName"></a>
The Amazon Route 53 health check configuration record name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** crossAccountRole **   <a name="regionswitch-Type-Route53HealthCheckConfiguration-crossAccountRole"></a>
The cross account role for the configuration.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** externalId **   <a name="regionswitch-Type-Route53HealthCheckConfiguration-externalId"></a>
The external ID (secret key) for the configuration.
Type: String
Required: No

 ** recordSets **   <a name="regionswitch-Type-Route53HealthCheckConfiguration-recordSets"></a>
The Amazon Route 53 health check configuration record sets.
Type: Array of [Route53ResourceRecordSet](API_Route53ResourceRecordSet.md) objects
Required: No

 ** timeoutMinutes **   <a name="regionswitch-Type-Route53HealthCheckConfiguration-timeoutMinutes"></a>
The Amazon Route 53 health check configuration time out (in minutes).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_Route53HealthCheckConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/Route53HealthCheckConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/Route53HealthCheckConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/Route53HealthCheckConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
