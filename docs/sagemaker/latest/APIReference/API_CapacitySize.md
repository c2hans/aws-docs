---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CapacitySize.html
---

# CapacitySize
<a name="API_CapacitySize"></a>

Specifies the type and size of the endpoint capacity to activate for a blue/green deployment, a rolling deployment, or a rollback strategy. You can specify your batches as either instance count or the overall percentage or your fleet.

For a rollback strategy, if you don't specify the fields in this object, or if you set the `Value` to 100%, then SageMaker uses a blue/green rollback strategy and rolls all traffic back to the blue fleet.

## Contents
<a name="API_CapacitySize_Contents"></a>

 ** Type **   <a name="sagemaker-Type-CapacitySize-Type"></a>
Specifies the endpoint capacity type.
+  `INSTANCE_COUNT`: The endpoint activates based on the number of instances.
+  `CAPACITY_PERCENT`: The endpoint activates based on the specified percentage of capacity.
Type: String
Valid Values: `INSTANCE_COUNT | CAPACITY_PERCENT`
Required: Yes

 ** Value **   <a name="sagemaker-Type-CapacitySize-Value"></a>
Defines the capacity size, either as a number of instances or a capacity percentage.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_CapacitySize_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CapacitySize)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CapacitySize)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CapacitySize)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
