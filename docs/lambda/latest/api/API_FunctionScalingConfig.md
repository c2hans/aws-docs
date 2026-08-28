---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_FunctionScalingConfig.html
---

# FunctionScalingConfig
<a name="API_FunctionScalingConfig"></a>

Configuration that defines the scaling behavior for a Lambda Managed Instances function, including the minimum and maximum number of execution environments that can be provisioned.

## Contents
<a name="API_FunctionScalingConfig_Contents"></a>

 ** MaxExecutionEnvironments **   <a name="lambda-Type-FunctionScalingConfig-MaxExecutionEnvironments"></a>
The maximum number of execution environments that can be provisioned for the function.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15000.
Required: No

 ** MinExecutionEnvironments **   <a name="lambda-Type-FunctionScalingConfig-MinExecutionEnvironments"></a>
The minimum number of execution environments to maintain for the function.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15000.
Required: No

## See Also
<a name="API_FunctionScalingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/FunctionScalingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/FunctionScalingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/FunctionScalingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
