---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DeploymentPolicies.html
---

# DeploymentPolicies
<a name="API_DeploymentPolicies"></a>

Contains information about policies that define how a deployment updates components and handles failure.

## Contents
<a name="API_DeploymentPolicies_Contents"></a>

 ** componentUpdatePolicy **   <a name="greengrassv2-Type-DeploymentPolicies-componentUpdatePolicy"></a>
The component update policy for the configuration deployment. This policy defines when it's safe to deploy the configuration to devices.
Type: [DeploymentComponentUpdatePolicy](API_DeploymentComponentUpdatePolicy.md) object
Required: No

 ** configurationValidationPolicy **   <a name="greengrassv2-Type-DeploymentPolicies-configurationValidationPolicy"></a>
The configuration validation policy for the configuration deployment. This policy defines how long each component has to validate its configure updates.
Type: [DeploymentConfigurationValidationPolicy](API_DeploymentConfigurationValidationPolicy.md) object
Required: No

 ** failureHandlingPolicy **   <a name="greengrassv2-Type-DeploymentPolicies-failureHandlingPolicy"></a>
The failure handling policy for the configuration deployment. This policy defines what to do if the deployment fails.
Default: `ROLLBACK`
Type: String
Valid Values: `ROLLBACK | DO_NOTHING`
Required: No

## See Also
<a name="API_DeploymentPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/DeploymentPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/DeploymentPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/DeploymentPolicies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
