---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LabelCounters.html
---

# LabelCounters
<a name="API_LabelCounters"></a>

Provides a breakdown of the number of objects labeled.

## Contents
<a name="API_LabelCounters_Contents"></a>

 ** FailedNonRetryableError **   <a name="sagemaker-Type-LabelCounters-FailedNonRetryableError"></a>
The total number of objects that could not be labeled due to an error.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** HumanLabeled **   <a name="sagemaker-Type-LabelCounters-HumanLabeled"></a>
The total number of objects labeled by a human worker.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MachineLabeled **   <a name="sagemaker-Type-LabelCounters-MachineLabeled"></a>
The total number of objects labeled by automated data labeling.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TotalLabeled **   <a name="sagemaker-Type-LabelCounters-TotalLabeled"></a>
The total number of objects labeled.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Unlabeled **   <a name="sagemaker-Type-LabelCounters-Unlabeled"></a>
The total number of objects not yet labeled.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_LabelCounters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LabelCounters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LabelCounters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LabelCounters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
