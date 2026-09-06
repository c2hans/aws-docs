---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ExperimentSummary.html
---

# ExperimentSummary
<a name="API_ExperimentSummary"></a>

A summary of the properties of an experiment. To get the complete set of properties, call the [DescribeExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeExperiment.html) API and provide the `ExperimentName`.

## Contents
<a name="API_ExperimentSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-ExperimentSummary-CreationTime"></a>
When the experiment was created.
Type: Timestamp
Required: No

 ** DisplayName **   <a name="sagemaker-Type-ExperimentSummary-DisplayName"></a>
The name of the experiment as displayed. If `DisplayName` isn't specified, `ExperimentName` is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** ExperimentArn **   <a name="sagemaker-Type-ExperimentSummary-ExperimentArn"></a>
The Amazon Resource Name (ARN) of the experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment/.*`
Required: No

 ** ExperimentName **   <a name="sagemaker-Type-ExperimentSummary-ExperimentName"></a>
The name of the experiment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** ExperimentSource **   <a name="sagemaker-Type-ExperimentSummary-ExperimentSource"></a>
The source of the experiment.
Type: [ExperimentSource](API_ExperimentSource.md) object
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-ExperimentSummary-LastModifiedTime"></a>
When the experiment was last modified.
Type: Timestamp
Required: No

## See Also
<a name="API_ExperimentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ExperimentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ExperimentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ExperimentSummary)
