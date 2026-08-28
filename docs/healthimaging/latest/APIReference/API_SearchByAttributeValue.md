---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_SearchByAttributeValue.html
---

# SearchByAttributeValue
<a name="API_SearchByAttributeValue"></a>

The search input attribute value.

## Contents
<a name="API_SearchByAttributeValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** createdAt **   <a name="healthimaging-Type-SearchByAttributeValue-createdAt"></a>
The created at time of the image set provided for search.
Type: Timestamp
Required: No

 ** DICOMAccessionNumber **   <a name="healthimaging-Type-SearchByAttributeValue-DICOMAccessionNumber"></a>
The DICOM accession number for search.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** DICOMPatientId **   <a name="healthimaging-Type-SearchByAttributeValue-DICOMPatientId"></a>
The patient ID input for search.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** DICOMSeriesInstanceUID **   <a name="healthimaging-Type-SearchByAttributeValue-DICOMSeriesInstanceUID"></a>
The Series Instance UID input for search.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[0-9.]+`
Required: No

 ** DICOMStudyDateAndTime **   <a name="healthimaging-Type-SearchByAttributeValue-DICOMStudyDateAndTime"></a>
The aggregated structure containing DICOM study date and study time for search.
Type: [DICOMStudyDateAndTime](API_DICOMStudyDateAndTime.md) object
Required: No

 ** DICOMStudyId **   <a name="healthimaging-Type-SearchByAttributeValue-DICOMStudyId"></a>
The DICOM study ID for search.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** DICOMStudyInstanceUID **   <a name="healthimaging-Type-SearchByAttributeValue-DICOMStudyInstanceUID"></a>
The DICOM study instance UID for search.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[0-9.]+`
Required: No

 ** isPrimary **   <a name="healthimaging-Type-SearchByAttributeValue-isPrimary"></a>
The primary image set flag provided for search.
Type: Boolean
Required: No

 ** updatedAt **   <a name="healthimaging-Type-SearchByAttributeValue-updatedAt"></a>
The timestamp input for search.
Type: Timestamp
Required: No

## See Also
<a name="API_SearchByAttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/SearchByAttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/SearchByAttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/SearchByAttributeValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
