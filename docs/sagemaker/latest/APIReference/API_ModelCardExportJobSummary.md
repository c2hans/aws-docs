---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelCardExportJobSummary.html
---

# ModelCardExportJobSummary
<a name="API_ModelCardExportJobSummary"></a>

The summary of the Amazon SageMaker Model Card export job.

## Contents
<a name="API_ModelCardExportJobSummary_Contents"></a>

 ** CreatedAt **   <a name="sagemaker-Type-ModelCardExportJobSummary-CreatedAt"></a>
The date and time that the model card export job was created.
Type: Timestamp
Required: Yes

 ** LastModifiedAt **   <a name="sagemaker-Type-ModelCardExportJobSummary-LastModifiedAt"></a>
The date and time that the model card export job was last modified..
Type: Timestamp
Required: Yes

 ** ModelCardExportJobArn **   <a name="sagemaker-Type-ModelCardExportJobSummary-ModelCardExportJobArn"></a>
The Amazon Resource Name (ARN) of the model card export job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-card/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}/export-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ModelCardExportJobName **   <a name="sagemaker-Type-ModelCardExportJobSummary-ModelCardExportJobName"></a>
The name of the model card export job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ModelCardName **   <a name="sagemaker-Type-ModelCardExportJobSummary-ModelCardName"></a>
The name of the model card that the export job exports.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** ModelCardVersion **   <a name="sagemaker-Type-ModelCardExportJobSummary-ModelCardVersion"></a>
The version of the model card that the export job exports.
Type: Integer
Required: Yes

 ** Status **   <a name="sagemaker-Type-ModelCardExportJobSummary-Status"></a>
The completion status of the model card export job.
Type: String
Valid Values: `InProgress | Completed | Failed`
Required: Yes

## See Also
<a name="API_ModelCardExportJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelCardExportJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelCardExportJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelCardExportJobSummary)
