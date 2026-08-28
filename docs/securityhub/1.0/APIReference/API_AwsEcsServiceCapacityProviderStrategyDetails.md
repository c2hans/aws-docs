---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsServiceCapacityProviderStrategyDetails.html
---

# AwsEcsServiceCapacityProviderStrategyDetails
<a name="API_AwsEcsServiceCapacityProviderStrategyDetails"></a>

Strategy item for the capacity provider strategy that the service uses.

## Contents
<a name="API_AwsEcsServiceCapacityProviderStrategyDetails_Contents"></a>

 ** Base **   <a name="securityhub-Type-AwsEcsServiceCapacityProviderStrategyDetails-Base"></a>
The minimum number of tasks to run on the capacity provider. Only one strategy item can specify a value for `Base`.
The value must be between 0 and 100000.
Type: Integer
Required: No

 ** CapacityProvider **   <a name="securityhub-Type-AwsEcsServiceCapacityProviderStrategyDetails-CapacityProvider"></a>
The short name of the capacity provider.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Weight **   <a name="securityhub-Type-AwsEcsServiceCapacityProviderStrategyDetails-Weight"></a>
The relative percentage of the total number of tasks that should use the capacity provider.
If no weight is specified, the default value is 0. At least one capacity provider must have a weight greater than 0.
The value can be between 0 and 1000.
Type: Integer
Required: No

## See Also
<a name="API_AwsEcsServiceCapacityProviderStrategyDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsServiceCapacityProviderStrategyDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsServiceCapacityProviderStrategyDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsServiceCapacityProviderStrategyDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
