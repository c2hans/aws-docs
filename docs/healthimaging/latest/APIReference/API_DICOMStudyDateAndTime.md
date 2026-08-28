---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DICOMStudyDateAndTime.html
---

# DICOMStudyDateAndTime
<a name="API_DICOMStudyDateAndTime"></a>

The aggregated structure to store DICOM study date and study time for search capabilities.

## Contents
<a name="API_DICOMStudyDateAndTime_Contents"></a>

 ** DICOMStudyDate **   <a name="healthimaging-Type-DICOMStudyDateAndTime-DICOMStudyDate"></a>
The DICOM study date provided in `yyMMdd` format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 36.
Required: Yes

 ** DICOMStudyTime **   <a name="healthimaging-Type-DICOMStudyDateAndTime-DICOMStudyTime"></a>
The DICOM study time provided in `HHmmss.FFFFFF` format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 56.
Required: No

## See Also
<a name="API_DICOMStudyDateAndTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/DICOMStudyDateAndTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/DICOMStudyDateAndTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/DICOMStudyDateAndTime)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
