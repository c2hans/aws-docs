---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PartnerAppSummary.html
---

# PartnerAppSummary
<a name="API_PartnerAppSummary"></a>

A subset of information related to a SageMaker Partner AI App. This information is used as part of the `ListPartnerApps` API response.

## Contents
<a name="API_PartnerAppSummary_Contents"></a>

 ** Arn **   <a name="sagemaker-Type-PartnerAppSummary-Arn"></a>
The ARN of the SageMaker Partner AI App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:partner-app\/app-[A-Z0-9]{12}`
Required: No

 ** CreationTime **   <a name="sagemaker-Type-PartnerAppSummary-CreationTime"></a>
The creation time of the SageMaker Partner AI App.
Type: Timestamp
Required: No

 ** Name **   <a name="sagemaker-Type-PartnerAppSummary-Name"></a>
The name of the SageMaker Partner AI App.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9]+`
Required: No

 ** Status **   <a name="sagemaker-Type-PartnerAppSummary-Status"></a>
The status of the SageMaker Partner AI App.
Type: String
Valid Values: `Creating | Updating | Deleting | Available | Failed | UpdateFailed | Deleted`
Required: No

 ** Type **   <a name="sagemaker-Type-PartnerAppSummary-Type"></a>
The type of SageMaker Partner AI App to create. Must be one of the following: `lakera-guard`, `comet`, `deepchecks-llm-evaluation`, or `fiddler`.
Type: String
Valid Values: `lakera-guard | comet | deepchecks-llm-evaluation | fiddler`
Required: No

## See Also
<a name="API_PartnerAppSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PartnerAppSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PartnerAppSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PartnerAppSummary)
