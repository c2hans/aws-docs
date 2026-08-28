---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentCapacitySize.html
---

# InferenceComponentCapacitySize
<a name="API_InferenceComponentCapacitySize"></a>

Specifies the type and size of the endpoint capacity to activate for a rolling deployment or a rollback strategy. You can specify your batches as either of the following:
+ A count of inference component copies
+ The overall percentage or your fleet

For a rollback strategy, if you don't specify the fields in this object, or if you set the `Value` parameter to 100%, then SageMaker AI uses a blue/green rollback strategy and rolls all traffic back to the blue fleet.

## Contents
<a name="API_InferenceComponentCapacitySize_Contents"></a>

 ** Type **   <a name="sagemaker-Type-InferenceComponentCapacitySize-Type"></a>
Specifies the endpoint capacity type.
COPY\_COUNT
The endpoint activates based on the number of inference component copies.
CAPACITY\_PERCENT
The endpoint activates based on the specified percentage of capacity.
Type: String
Valid Values: `COPY_COUNT | CAPACITY_PERCENT`
Required: Yes

 ** Value **   <a name="sagemaker-Type-InferenceComponentCapacitySize-Value"></a>
Defines the capacity size, either as a number of inference component copies or a capacity percentage.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_InferenceComponentCapacitySize_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentCapacitySize)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentCapacitySize)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentCapacitySize)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
