---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_LambdaManagedInstancesCapacityProviderConfig.html
---

# LambdaManagedInstancesCapacityProviderConfig
<a name="API_LambdaManagedInstancesCapacityProviderConfig"></a>

Configuration for Lambda-managed instances used by the capacity provider.

## Contents
<a name="API_LambdaManagedInstancesCapacityProviderConfig_Contents"></a>

 ** CapacityProviderArn **   <a name="lambda-Type-LambdaManagedInstancesCapacityProviderConfig-CapacityProviderArn"></a>
The Amazon Resource Name (ARN) of the capacity provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `arn:aws[a-zA-Z-]*:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:capacity-provider:[a-zA-Z0-9-_]+`
Required: Yes

 ** ExecutionEnvironmentMemoryGiBPerVCpu **   <a name="lambda-Type-LambdaManagedInstancesCapacityProviderConfig-ExecutionEnvironmentMemoryGiBPerVCpu"></a>
The amount of memory in GiB allocated per vCPU for execution environments.
Type: Double
Valid Range: Minimum value of 2.0. Maximum value of 8.0.
Required: No

 ** PerExecutionEnvironmentMaxConcurrency **   <a name="lambda-Type-LambdaManagedInstancesCapacityProviderConfig-PerExecutionEnvironmentMaxConcurrency"></a>
The maximum number of concurrent execution environments that can run on each compute instance.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1600.
Required: No

## See Also
<a name="API_LambdaManagedInstancesCapacityProviderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/LambdaManagedInstancesCapacityProviderConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/LambdaManagedInstancesCapacityProviderConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/LambdaManagedInstancesCapacityProviderConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
