---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CentralizationRule.html
---

# CentralizationRule
<a name="API_CentralizationRule"></a>

Defines how telemetry data should be centralized across an AWS Organization, including source and destination configurations.

## Contents
<a name="API_CentralizationRule_Contents"></a>

 ** Destination **   <a name="cwoa-Type-CentralizationRule-Destination"></a>
Configuration determining where the telemetry data should be centralized, backed up, as well as encryption configuration for the primary and backup destinations.
Type: [CentralizationRuleDestination](API_CentralizationRuleDestination.md) object
Required: Yes

 ** Source **   <a name="cwoa-Type-CentralizationRule-Source"></a>
Configuration determining the source of the telemetry data to be centralized.
Type: [CentralizationRuleSource](API_CentralizationRuleSource.md) object
Required: Yes

## See Also
<a name="API_CentralizationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/CentralizationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/CentralizationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/CentralizationRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
