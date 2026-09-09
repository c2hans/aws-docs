---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrialComponent.html
---

# TrialComponent
<a name="API_TrialComponent"></a>

The properties of a trial component as returned by the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API.

## Contents
<a name="API_TrialComponent_Contents"></a>

 ** CreatedBy **   <a name="sagemaker-Type-TrialComponent-CreatedBy"></a>
Who created the trial component.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** DisplayName **   <a name="sagemaker-Type-TrialComponent-DisplayName"></a>
The name of the component as displayed. If `DisplayName` isn't specified, `TrialComponentName` is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** InputArtifacts **   <a name="sagemaker-Type-TrialComponent-InputArtifacts"></a>
The input artifacts of the component.
Type: String to [TrialComponentArtifact](API_TrialComponentArtifact.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 60 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Key Pattern: `.*`
Required: No

 ** LastModifiedBy **   <a name="sagemaker-Type-TrialComponent-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** LineageGroupArn **   <a name="sagemaker-Type-TrialComponent-LineageGroupArn"></a>
The Amazon Resource Name (ARN) of the lineage group resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:lineage-group/.*`
Required: No

 ** MetadataProperties **   <a name="sagemaker-Type-TrialComponent-MetadataProperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
Type: [MetadataProperties](API_MetadataProperties.md) object
Required: No

 ** Metrics **   <a name="sagemaker-Type-TrialComponent-Metrics"></a>
The metrics for the component.
Type: Array of [TrialComponentMetricSummary](API_TrialComponentMetricSummary.md) objects
Required: No

 ** OutputArtifacts **   <a name="sagemaker-Type-TrialComponent-OutputArtifacts"></a>
The output artifacts of the component.
Type: String to [TrialComponentArtifact](API_TrialComponentArtifact.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 60 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Key Pattern: `.*`
Required: No

 ** Parameters **   <a name="sagemaker-Type-TrialComponent-Parameters"></a>
The hyperparameters of the component.
Type: String to [TrialComponentParameterValue](API_TrialComponentParameterValue.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 300 items.
Key Length Constraints: Minimum length of 0. Maximum length of 320.
Key Pattern: `.*`
Required: No

 ** Parents **   <a name="sagemaker-Type-TrialComponent-Parents"></a>
An array of the parents of the component. A parent is a trial the component is associated with and the experiment the trial is part of. A component might not have any parents.
Type: Array of [Parent](API_Parent.md) objects
Required: No

 ** RunName **   <a name="sagemaker-Type-TrialComponent-RunName"></a>
The name of the experiment run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** Source **   <a name="sagemaker-Type-TrialComponent-Source"></a>
The Amazon Resource Name (ARN) and job type of the source of the component.
Type: [TrialComponentSource](API_TrialComponentSource.md) object
Required: No

 ** SourceDetail **   <a name="sagemaker-Type-TrialComponent-SourceDetail"></a>
Details of the source of the component.
Type: [TrialComponentSourceDetail](API_TrialComponentSourceDetail.md) object
Required: No

 ** Status **   <a name="sagemaker-Type-TrialComponent-Status"></a>
The status of the trial component.
Type: [TrialComponentStatus](API_TrialComponentStatus.md) object
Required: No

 ** Tags **   <a name="sagemaker-Type-TrialComponent-Tags"></a>
The list of tags that are associated with the component. You can use [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search on the tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** TrialComponentArn **   <a name="sagemaker-Type-TrialComponent-TrialComponentArn"></a>
The Amazon Resource Name (ARN) of the trial component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial-component/.*`
Required: No

 ** TrialComponentName **   <a name="sagemaker-Type-TrialComponent-TrialComponentName"></a>
The name of the trial component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

## See Also
<a name="API_TrialComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrialComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrialComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrialComponent)
