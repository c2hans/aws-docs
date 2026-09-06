---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrialComponentSummary.html
---

# TrialComponentSummary
<a name="API_TrialComponentSummary"></a>

A summary of the properties of a trial component. To get all the properties, call the [DescribeTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrialComponent.html) API and provide the `TrialComponentName`.

## Contents
<a name="API_TrialComponentSummary_Contents"></a>

 ** CreatedBy **   <a name="sagemaker-Type-TrialComponentSummary-CreatedBy"></a>
Who created the trial component.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** CreationTime **   <a name="sagemaker-Type-TrialComponentSummary-CreationTime"></a>
When the component was created.
Type: Timestamp
Required: No

 ** DisplayName **   <a name="sagemaker-Type-TrialComponentSummary-DisplayName"></a>
The name of the component as displayed. If `DisplayName` isn't specified, `TrialComponentName` is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** EndTime **   <a name="sagemaker-Type-TrialComponentSummary-EndTime"></a>
When the component ended.
Type: Timestamp
Required: No

 ** LastModifiedBy **   <a name="sagemaker-Type-TrialComponentSummary-LastModifiedBy"></a>
Who last modified the component.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-TrialComponentSummary-LastModifiedTime"></a>
When the component was last modified.
Type: Timestamp
Required: No

 ** StartTime **   <a name="sagemaker-Type-TrialComponentSummary-StartTime"></a>
When the component started.
Type: Timestamp
Required: No

 ** Status **   <a name="sagemaker-Type-TrialComponentSummary-Status"></a>
The status of the component. States include:
+ InProgress
+ Completed
+ Failed
Type: [TrialComponentStatus](API_TrialComponentStatus.md) object
Required: No

 ** TrialComponentArn **   <a name="sagemaker-Type-TrialComponentSummary-TrialComponentArn"></a>
The Amazon Resource Name (ARN) of the trial component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial-component/.*`
Required: No

 ** TrialComponentName **   <a name="sagemaker-Type-TrialComponentSummary-TrialComponentName"></a>
The name of the trial component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** TrialComponentSource **   <a name="sagemaker-Type-TrialComponentSummary-TrialComponentSource"></a>
The Amazon Resource Name (ARN) and job type of the source of a trial component.
Type: [TrialComponentSource](API_TrialComponentSource.md) object
Required: No

## See Also
<a name="API_TrialComponentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrialComponentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrialComponentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrialComponentSummary)
