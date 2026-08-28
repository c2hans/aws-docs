---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_ImageSetsMetadataSummary.html
---

# ImageSetsMetadataSummary
<a name="API_ImageSetsMetadataSummary"></a>

Summary of the image set metadata.

## Contents
<a name="API_ImageSetsMetadataSummary_Contents"></a>

 ** imageSetId **   <a name="healthimaging-Type-ImageSetsMetadataSummary-imageSetId"></a>
The image set identifier.
Type: String
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** createdAt **   <a name="healthimaging-Type-ImageSetsMetadataSummary-createdAt"></a>
The time an image set is created. Sample creation date is provided in `1985-04-12T23:20:50.52Z` format.
Type: Timestamp
Required: No

 ** DICOMTags **   <a name="healthimaging-Type-ImageSetsMetadataSummary-DICOMTags"></a>
The DICOM tags associated with the image set.
Type: [DICOMTags](API_DICOMTags.md) object
Required: No

 ** isPrimary **   <a name="healthimaging-Type-ImageSetsMetadataSummary-isPrimary"></a>
The flag to determine whether the image set is primary or not.
Type: Boolean
Required: No

 ** lastAccessedAt **   <a name="healthimaging-Type-ImageSetsMetadataSummary-lastAccessedAt"></a>
When the image set was last accessed.
Type: Timestamp
Required: No

 ** storageTier **   <a name="healthimaging-Type-ImageSetsMetadataSummary-storageTier"></a>
The image set's storage tier.
Type: String
Valid Values: `FREQUENT_ACCESS | ARCHIVE_INSTANT_ACCESS`
Required: No

 ** updatedAt **   <a name="healthimaging-Type-ImageSetsMetadataSummary-updatedAt"></a>
The time an image set was last updated.
Type: Timestamp
Required: No

 ** version **   <a name="healthimaging-Type-ImageSetsMetadataSummary-version"></a>
The image set version.
Type: Integer
Required: No

## See Also
<a name="API_ImageSetsMetadataSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/ImageSetsMetadataSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/ImageSetsMetadataSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/ImageSetsMetadataSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
