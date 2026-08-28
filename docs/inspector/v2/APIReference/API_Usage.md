---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Usage.html
---

# Usage
<a name="API_Usage"></a>

Contains usage information about the cost of Amazon Inspector operation.

## Contents
<a name="API_Usage_Contents"></a>

 ** cloudProvider **   <a name="inspector2-Type-Usage-cloudProvider"></a>
The cloud provider associated with the usage information.
Type: String
Valid Values: `AWS | AZURE | NOT_APPLICABLE`
Required: No

 ** currency **   <a name="inspector2-Type-Usage-currency"></a>
The currency type used when calculating usage data.
Type: String
Valid Values: `USD`
Required: No

 ** estimatedMonthlyCost **   <a name="inspector2-Type-Usage-estimatedMonthlyCost"></a>
The estimated monthly cost of Amazon Inspector.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** total **   <a name="inspector2-Type-Usage-total"></a>
The total of usage.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** type **   <a name="inspector2-Type-Usage-type"></a>
The type scan.
Type: String
Valid Values: `EC2_INSTANCE_HOURS | ECR_INITIAL_SCAN | ECR_RESCAN | LAMBDA_FUNCTION_HOURS | LAMBDA_FUNCTION_CODE_HOURS | CODE_REPOSITORY_SAST | CODE_REPOSITORY_IAC | CODE_REPOSITORY_SCA | EC2_AGENTLESS_INSTANCE_HOURS | AZURE_CONTAINER_IMAGE_INITIAL_SCAN | AZURE_CONTAINER_IMAGE_RESCAN | AZURE_VM_AGENT_BASED_INSTANCE_HOURS | AZURE_SERVERLESS_FUNCTION_HOURS`
Required: No

## See Also
<a name="API_Usage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Usage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Usage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Usage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
