---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Trial.html
---

# Trial
<a name="API_Trial"></a>

The properties of a trial as returned by the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API.

## Contents
<a name="API_Trial_Contents"></a>

 ** CreatedBy **   <a name="sagemaker-Type-Trial-CreatedBy"></a>
Who created the trial.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** CreationTime **   <a name="sagemaker-Type-Trial-CreationTime"></a>
When the trial was created.
Type: Timestamp
Required: No

 ** DisplayName **   <a name="sagemaker-Type-Trial-DisplayName"></a>
The name of the trial as displayed. If `DisplayName` isn't specified, `TrialName` is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** ExperimentName **   <a name="sagemaker-Type-Trial-ExperimentName"></a>
The name of the experiment the trial is part of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** LastModifiedBy **   <a name="sagemaker-Type-Trial-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-Trial-LastModifiedTime"></a>
Who last modified the trial.
Type: Timestamp
Required: No

 ** MetadataProperties **   <a name="sagemaker-Type-Trial-MetadataProperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
Type: [MetadataProperties](API_MetadataProperties.md) object
Required: No

 ** Source **   <a name="sagemaker-Type-Trial-Source"></a>
The source of the trial.
Type: [TrialSource](API_TrialSource.md) object
Required: No

 ** Tags **   <a name="sagemaker-Type-Trial-Tags"></a>
The list of tags that are associated with the trial. You can use [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search on the tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** TrialArn **   <a name="sagemaker-Type-Trial-TrialArn"></a>
The Amazon Resource Name (ARN) of the trial.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial/.*`
Required: No

 ** TrialComponentSummaries **   <a name="sagemaker-Type-Trial-TrialComponentSummaries"></a>
A list of the components associated with the trial. For each component, a summary of the component's properties is included.
Type: Array of [TrialComponentSimpleSummary](API_TrialComponentSimpleSummary.md) objects
Required: No

 ** TrialName **   <a name="sagemaker-Type-Trial-TrialName"></a>
The name of the trial.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

## See Also
<a name="API_Trial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Trial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Trial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Trial)
