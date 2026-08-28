---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DICOMUpdates.html
---

# DICOMUpdates
<a name="API_DICOMUpdates"></a>

The object containing `removableAttributes` and `updatableAttributes`.

## Contents
<a name="API_DICOMUpdates_Contents"></a>

 ** removableAttributes **   <a name="healthimaging-Type-DICOMUpdates-removableAttributes"></a>
The DICOM tags to be removed from `ImageSetMetadata`.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

 ** updatableAttributes **   <a name="healthimaging-Type-DICOMUpdates-updatableAttributes"></a>
The DICOM tags that need to be updated in `ImageSetMetadata`.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

## See Also
<a name="API_DICOMUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/DICOMUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/DICOMUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/DICOMUpdates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
