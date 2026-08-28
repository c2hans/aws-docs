---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelQualityJobInput.html
---

# ModelQualityJobInput
<a name="API_ModelQualityJobInput"></a>

The input for the model quality monitoring job. Currently endpoints are supported for input for model quality monitoring jobs.

## Contents
<a name="API_ModelQualityJobInput_Contents"></a>

 ** GroundTruthS3Input **   <a name="sagemaker-Type-ModelQualityJobInput-GroundTruthS3Input"></a>
The ground truth label provided for the model.
Type: [MonitoringGroundTruthS3Input](API_MonitoringGroundTruthS3Input.md) object
Required: Yes

 ** BatchTransformInput **   <a name="sagemaker-Type-ModelQualityJobInput-BatchTransformInput"></a>
Input object for the batch transform job.
Type: [BatchTransformInput](API_BatchTransformInput.md) object
Required: No

 ** EndpointInput **   <a name="sagemaker-Type-ModelQualityJobInput-EndpointInput"></a>
Input object for the endpoint
Type: [EndpointInput](API_EndpointInput.md) object
Required: No

## See Also
<a name="API_ModelQualityJobInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelQualityJobInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelQualityJobInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelQualityJobInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
