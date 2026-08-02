---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProjectSummary.html
---

# ProjectSummary
<a name="API_ProjectSummary"></a>

Information about a project.

## Contents
<a name="API_ProjectSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-ProjectSummary-CreationTime"></a>
The time that the project was created.
Type: Timestamp
Required: Yes

 ** ProjectArn **   <a name="sagemaker-Type-ProjectSummary-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:project/[\S]{1,2048}`
Required: Yes

 ** ProjectId **   <a name="sagemaker-Type-ProjectSummary-ProjectId"></a>
The ID of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** ProjectName **   <a name="sagemaker-Type-ProjectSummary-ProjectName"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: Yes

 ** ProjectStatus **   <a name="sagemaker-Type-ProjectSummary-ProjectStatus"></a>
The status of the project.
Type: String
Valid Values: `Pending | CreateInProgress | CreateCompleted | CreateFailed | DeleteInProgress | DeleteFailed | DeleteCompleted | UpdateInProgress | UpdateCompleted | UpdateFailed`
Required: Yes

 ** ProjectDescription **   <a name="sagemaker-Type-ProjectSummary-ProjectDescription"></a>
The description of the project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

## See Also
<a name="API_ProjectSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProjectSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProjectSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProjectSummary)
