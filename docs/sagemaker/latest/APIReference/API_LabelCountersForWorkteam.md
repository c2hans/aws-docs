---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LabelCountersForWorkteam.html
---

# LabelCountersForWorkteam
<a name="API_LabelCountersForWorkteam"></a>

Provides counts for human-labeled tasks in the labeling job.

## Contents
<a name="API_LabelCountersForWorkteam_Contents"></a>

 ** HumanLabeled **   <a name="sagemaker-Type-LabelCountersForWorkteam-HumanLabeled"></a>
The total number of data objects labeled by a human worker.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PendingHuman **   <a name="sagemaker-Type-LabelCountersForWorkteam-PendingHuman"></a>
The total number of data objects that need to be labeled by a human worker.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Total **   <a name="sagemaker-Type-LabelCountersForWorkteam-Total"></a>
The total number of tasks in the labeling job.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_LabelCountersForWorkteam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LabelCountersForWorkteam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LabelCountersForWorkteam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LabelCountersForWorkteam)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
