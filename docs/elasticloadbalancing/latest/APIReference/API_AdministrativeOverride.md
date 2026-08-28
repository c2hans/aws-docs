---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AdministrativeOverride.html
---

# AdministrativeOverride
<a name="API_AdministrativeOverride"></a>

Information about the override status applied to a target.

## Contents
<a name="API_AdministrativeOverride_Contents"></a>

 ** Description **
A description of the override state that provides additional details.
Type: String
Required: No

 ** Reason **
The reason code for the state.
Type: String
Valid Values: `AdministrativeOverride.Unknown | AdministrativeOverride.NoOverride | AdministrativeOverride.ZonalShiftActive | AdministrativeOverride.ZonalShiftDelegatedToDns`
Required: No

 ** State **
The state of the override.
Type: String
Valid Values: `unknown | no_override | zonal_shift_active | zonal_shift_delegated_to_dns`
Required: No

## See Also
<a name="API_AdministrativeOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/AdministrativeOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/AdministrativeOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/AdministrativeOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
