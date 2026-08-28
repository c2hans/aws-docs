---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsClusterDefaultCapacityProviderStrategyDetails.html
---

# AwsEcsClusterDefaultCapacityProviderStrategyDetails
<a name="API_AwsEcsClusterDefaultCapacityProviderStrategyDetails"></a>

The default capacity provider strategy for the cluster. The default capacity provider strategy is used when services or tasks are run without a specified launch type or capacity provider strategy.

## Contents
<a name="API_AwsEcsClusterDefaultCapacityProviderStrategyDetails_Contents"></a>

 ** Base **   <a name="securityhub-Type-AwsEcsClusterDefaultCapacityProviderStrategyDetails-Base"></a>
The minimum number of tasks to run on the specified capacity provider.
Type: Integer
Required: No

 ** CapacityProvider **   <a name="securityhub-Type-AwsEcsClusterDefaultCapacityProviderStrategyDetails-CapacityProvider"></a>
The name of the capacity provider.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Weight **   <a name="securityhub-Type-AwsEcsClusterDefaultCapacityProviderStrategyDetails-Weight"></a>
The relative percentage of the total number of tasks launched that should use the capacity provider.
Type: Integer
Required: No

## See Also
<a name="API_AwsEcsClusterDefaultCapacityProviderStrategyDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsClusterDefaultCapacityProviderStrategyDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsClusterDefaultCapacityProviderStrategyDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsClusterDefaultCapacityProviderStrategyDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
