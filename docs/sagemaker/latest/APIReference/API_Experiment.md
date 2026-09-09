---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Experiment.html
---

# Experiment
<a name="API_Experiment"></a>

The properties of an experiment as returned by the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API. For information about experiments, see the [CreateExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateExperiment.html) API.

## Contents
<a name="API_Experiment_Contents"></a>

 ** CreatedBy **   <a name="sagemaker-Type-Experiment-CreatedBy"></a>
Who created the experiment.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** Description **   <a name="sagemaker-Type-Experiment-Description"></a>
The description of the experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** DisplayName **   <a name="sagemaker-Type-Experiment-DisplayName"></a>
The name of the experiment as displayed. If `DisplayName` isn't specified, `ExperimentName` is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** ExperimentArn **   <a name="sagemaker-Type-Experiment-ExperimentArn"></a>
The Amazon Resource Name (ARN) of the experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment/.*`
Required: No

 ** ExperimentName **   <a name="sagemaker-Type-Experiment-ExperimentName"></a>
The name of the experiment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** LastModifiedBy **   <a name="sagemaker-Type-Experiment-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** Source **   <a name="sagemaker-Type-Experiment-Source"></a>
The source of the experiment.
Type: [ExperimentSource](API_ExperimentSource.md) object
Required: No

 ** Tags **   <a name="sagemaker-Type-Experiment-Tags"></a>
The list of tags that are associated with the experiment. You can use [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search on the tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_Experiment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Experiment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Experiment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Experiment)
