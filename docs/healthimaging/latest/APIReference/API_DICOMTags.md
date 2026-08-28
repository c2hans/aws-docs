---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DICOMTags.html
---

# DICOMTags
<a name="API_DICOMTags"></a>

The DICOM attributes returned as a part of a response. Each image set has these properties as part of a search result.

## Contents
<a name="API_DICOMTags_Contents"></a>

 ** DICOMAccessionNumber **   <a name="healthimaging-Type-DICOMTags-DICOMAccessionNumber"></a>
The accession number for the DICOM study.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** DICOMNumberOfStudyRelatedInstances **   <a name="healthimaging-Type-DICOMTags-DICOMNumberOfStudyRelatedInstances"></a>
The total number of instances in the DICOM study.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.
Required: No

 ** DICOMNumberOfStudyRelatedSeries **   <a name="healthimaging-Type-DICOMTags-DICOMNumberOfStudyRelatedSeries"></a>
The total number of series in the DICOM study.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000000.
Required: No

 ** DICOMPatientBirthDate **   <a name="healthimaging-Type-DICOMTags-DICOMPatientBirthDate"></a>
The patient birth date.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 36.
Required: No

 ** DICOMPatientId **   <a name="healthimaging-Type-DICOMTags-DICOMPatientId"></a>
The unique identifier for a patient in a DICOM Study.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** DICOMPatientName **   <a name="healthimaging-Type-DICOMTags-DICOMPatientName"></a>
The patient name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** DICOMPatientSex **   <a name="healthimaging-Type-DICOMTags-DICOMPatientSex"></a>
The patient sex.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Required: No

 ** DICOMSeriesBodyPart **   <a name="healthimaging-Type-DICOMTags-DICOMSeriesBodyPart"></a>
The DICOM provided identifier for the series Body Part Examined.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** DICOMSeriesInstanceUID **   <a name="healthimaging-Type-DICOMTags-DICOMSeriesInstanceUID"></a>
The DICOM provided identifier for the Series Instance UID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[0-9.]+`
Required: No

 ** DICOMSeriesModality **   <a name="healthimaging-Type-DICOMTags-DICOMSeriesModality"></a>
The DICOM provided identifier for the series Modality.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: No

 ** DICOMSeriesNumber **   <a name="healthimaging-Type-DICOMTags-DICOMSeriesNumber"></a>
The DICOM provided identifier for the Series Number.
Type: Integer
Valid Range: Minimum value of -2147483648. Maximum value of 2147483647.
Required: No

 ** DICOMStudyDate **   <a name="healthimaging-Type-DICOMTags-DICOMStudyDate"></a>
The study date.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 36.
Required: No

 ** DICOMStudyDescription **   <a name="healthimaging-Type-DICOMTags-DICOMStudyDescription"></a>
The DICOM provided Study Description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** DICOMStudyId **   <a name="healthimaging-Type-DICOMTags-DICOMStudyId"></a>
The DICOM provided identifier for the Study ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** DICOMStudyInstanceUID **   <a name="healthimaging-Type-DICOMTags-DICOMStudyInstanceUID"></a>
The DICOM provided identifier for the Study Instance UID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[0-9.]+`
Required: No

 ** DICOMStudyTime **   <a name="healthimaging-Type-DICOMTags-DICOMStudyTime"></a>
The study time.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 56.
Required: No

## See Also
<a name="API_DICOMTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/DICOMTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/DICOMTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/DICOMTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
