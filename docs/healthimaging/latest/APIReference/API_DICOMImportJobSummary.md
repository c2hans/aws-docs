---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DICOMImportJobSummary.html
---

# DICOMImportJobSummary
<a name="API_DICOMImportJobSummary"></a>

Summary of import job.

## Contents
<a name="API_DICOMImportJobSummary_Contents"></a>

 ** datastoreId **   <a name="healthimaging-Type-DICOMImportJobSummary-datastoreId"></a>
The data store identifier.
Type: String
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** jobId **   <a name="healthimaging-Type-DICOMImportJobSummary-jobId"></a>
The import job identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9a-z]+`
Required: Yes

 ** jobName **   <a name="healthimaging-Type-DICOMImportJobSummary-jobName"></a>
The import job name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/#-]+`
Required: Yes

 ** jobStatus **   <a name="healthimaging-Type-DICOMImportJobSummary-jobStatus"></a>
The filters for listing import jobs based on status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | FAILED`
Required: Yes

 ** dataAccessRoleArn **   <a name="healthimaging-Type-DICOMImportJobSummary-dataAccessRoleArn"></a>
The Amazon Resource Name (ARN) that grants permissions to access medical imaging resources.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: No

 ** endedAt **   <a name="healthimaging-Type-DICOMImportJobSummary-endedAt"></a>
The timestamp when an import job ended.
Type: Timestamp
Required: No

 ** message **   <a name="healthimaging-Type-DICOMImportJobSummary-message"></a>
The error message thrown if an import job fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w -:`]+`
Required: No

 ** submittedAt **   <a name="healthimaging-Type-DICOMImportJobSummary-submittedAt"></a>
The timestamp when an import job was submitted.
Type: Timestamp
Required: No

## See Also
<a name="API_DICOMImportJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/DICOMImportJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/DICOMImportJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/DICOMImportJobSummary)
