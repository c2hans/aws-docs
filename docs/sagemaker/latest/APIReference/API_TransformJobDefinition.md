---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TransformJobDefinition.html
---

# TransformJobDefinition
<a name="API_TransformJobDefinition"></a>

Defines the input needed to run a transform job using the inference specification specified in the algorithm.

## Contents
<a name="API_TransformJobDefinition_Contents"></a>

 ** TransformInput **   <a name="sagemaker-Type-TransformJobDefinition-TransformInput"></a>
A description of the input source and the way the transform job consumes it.
Type: [TransformInput](API_TransformInput.md) object
Required: Yes

 ** TransformOutput **   <a name="sagemaker-Type-TransformJobDefinition-TransformOutput"></a>
Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.
Type: [TransformOutput](API_TransformOutput.md) object
Required: Yes

 ** TransformResources **   <a name="sagemaker-Type-TransformJobDefinition-TransformResources"></a>
Identifies the ML compute instances for the transform job.
Type: [TransformResources](API_TransformResources.md) object
Required: Yes

 ** BatchStrategy **   <a name="sagemaker-Type-TransformJobDefinition-BatchStrategy"></a>
A string that determines the number of records included in a single mini-batch.
 `SingleRecord` means only one record is used per mini-batch. `MultiRecord` means a mini-batch is set to contain as many records that can fit within the `MaxPayloadInMB` limit.
Type: String
Valid Values: `MultiRecord | SingleRecord`
Required: No

 ** Environment **   <a name="sagemaker-Type-TransformJobDefinition-Environment"></a>
The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 16 items.
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]{0,1023}`
Value Length Constraints: Minimum length of 0. Maximum length of 10240.
Value Pattern: `[\S\s]*`
Required: No

 ** MaxConcurrentTransforms **   <a name="sagemaker-Type-TransformJobDefinition-MaxConcurrentTransforms"></a>
The maximum number of parallel requests that can be sent to each instance in a transform job. The default value is 1.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MaxPayloadInMB **   <a name="sagemaker-Type-TransformJobDefinition-MaxPayloadInMB"></a>
The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata).
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_TransformJobDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TransformJobDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TransformJobDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TransformJobDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
