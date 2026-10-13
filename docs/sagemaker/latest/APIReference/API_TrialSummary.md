---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrialSummary.html
---

# TrialSummary
<a name="API_TrialSummary"></a>

A summary of the properties of a trial. To get the complete set of properties, call the [DescribeTrial](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrial.html) API and provide the `TrialName`.

## Contents
<a name="API_TrialSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-TrialSummary-CreationTime"></a>
When the trial was created.
Type: Timestamp
Required: No

 ** DisplayName **   <a name="sagemaker-Type-TrialSummary-DisplayName"></a>
The name of the trial as displayed. If `DisplayName` isn't specified, `TrialName` is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-TrialSummary-LastModifiedTime"></a>
When the trial was last modified.
Type: Timestamp
Required: No

 ** TrialArn **   <a name="sagemaker-Type-TrialSummary-TrialArn"></a>
The Amazon Resource Name (ARN) of the trial.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial/.*`
Required: No

 ** TrialName **   <a name="sagemaker-Type-TrialSummary-TrialName"></a>
The name of the trial.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** TrialSource **   <a name="sagemaker-Type-TrialSummary-TrialSource"></a>
The source of the trial.
Type: [TrialSource](API_TrialSource.md) object
Required: No

## See Also
<a name="API_TrialSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrialSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrialSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrialSummary)
