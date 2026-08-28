---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DICOMImportJobProperties.html
---

# DICOMImportJobProperties
<a name="API_DICOMImportJobProperties"></a>

Properties of the import job.

## Contents
<a name="API_DICOMImportJobProperties_Contents"></a>

 ** dataAccessRoleArn **   <a name="healthimaging-Type-DICOMImportJobProperties-dataAccessRoleArn"></a>
The Amazon Resource Name (ARN) that grants permissions to access medical imaging resources.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: Yes

 ** datastoreId **   <a name="healthimaging-Type-DICOMImportJobProperties-datastoreId"></a>
The data store identifier.
Type: String
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** inputS3Uri **   <a name="healthimaging-Type-DICOMImportJobProperties-inputS3Uri"></a>
The input prefix path for the S3 bucket that contains the DICOM P10 files to be imported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

 ** jobId **   <a name="healthimaging-Type-DICOMImportJobProperties-jobId"></a>
The import job identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9a-z]+`
Required: Yes

 ** jobName **   <a name="healthimaging-Type-DICOMImportJobProperties-jobName"></a>
The import job name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/#-]+`
Required: Yes

 ** jobStatus **   <a name="healthimaging-Type-DICOMImportJobProperties-jobStatus"></a>
The filters for listing import jobs based on status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | FAILED`
Required: Yes

 ** outputS3Uri **   <a name="healthimaging-Type-DICOMImportJobProperties-outputS3Uri"></a>
The output prefix of the S3 bucket to upload the results of the DICOM import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

 ** endedAt **   <a name="healthimaging-Type-DICOMImportJobProperties-endedAt"></a>
The timestamp for when the import job was ended.
Type: Timestamp
Required: No

 ** importConfiguration **   <a name="healthimaging-Type-DICOMImportJobProperties-importConfiguration"></a>
The object containing `DicomJsonMetadataImportConfiguration`.
Type: [ImportConfiguration](API_ImportConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** message **   <a name="healthimaging-Type-DICOMImportJobProperties-message"></a>
The error message thrown if an import job fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w -:`]+`
Required: No

 ** submittedAt **   <a name="healthimaging-Type-DICOMImportJobProperties-submittedAt"></a>
The timestamp for when the import job was submitted.
Type: Timestamp
Required: No

## See Also
<a name="API_DICOMImportJobProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/DICOMImportJobProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/DICOMImportJobProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/DICOMImportJobProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
