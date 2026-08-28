---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelBiasJobInput.html
---

# ModelBiasJobInput
<a name="API_ModelBiasJobInput"></a>

Inputs for the model bias job.

## Contents
<a name="API_ModelBiasJobInput_Contents"></a>

 ** GroundTruthS3Input **   <a name="sagemaker-Type-ModelBiasJobInput-GroundTruthS3Input"></a>
Location of ground truth labels to use in model bias job.
Type: [MonitoringGroundTruthS3Input](API_MonitoringGroundTruthS3Input.md) object
Required: Yes

 ** BatchTransformInput **   <a name="sagemaker-Type-ModelBiasJobInput-BatchTransformInput"></a>
Input object for the batch transform job.
Type: [BatchTransformInput](API_BatchTransformInput.md) object
Required: No

 ** EndpointInput **   <a name="sagemaker-Type-ModelBiasJobInput-EndpointInput"></a>
Input object for the endpoint
Type: [EndpointInput](API_EndpointInput.md) object
Required: No

## See Also
<a name="API_ModelBiasJobInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelBiasJobInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelBiasJobInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelBiasJobInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
