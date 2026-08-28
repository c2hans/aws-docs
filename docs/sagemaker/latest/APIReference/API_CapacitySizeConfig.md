---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CapacitySizeConfig.html
---

# CapacitySizeConfig
<a name="API_CapacitySizeConfig"></a>

The configuration of the size measurements of the AMI update. Using this configuration, you can specify whether SageMaker should update your instance group by an amount or percentage of instances.

## Contents
<a name="API_CapacitySizeConfig_Contents"></a>

 ** Type **   <a name="sagemaker-Type-CapacitySizeConfig-Type"></a>
Specifies whether SageMaker should process the update by amount or percentage of instances.
Type: String
Valid Values: `INSTANCE_COUNT | CAPACITY_PERCENTAGE`
Required: Yes

 ** Value **   <a name="sagemaker-Type-CapacitySizeConfig-Value"></a>
Specifies the amount or percentage of instances SageMaker updates at a time.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_CapacitySizeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CapacitySizeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CapacitySizeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CapacitySizeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
