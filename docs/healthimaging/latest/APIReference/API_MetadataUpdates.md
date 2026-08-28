---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_MetadataUpdates.html
---

# MetadataUpdates
<a name="API_MetadataUpdates"></a>

Contains DICOMUpdates.

## Contents
<a name="API_MetadataUpdates_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** DICOMUpdates **   <a name="healthimaging-Type-MetadataUpdates-DICOMUpdates"></a>
The object containing `removableAttributes` and `updatableAttributes`.
Type: [DICOMUpdates](API_DICOMUpdates.md) object
Required: No

 ** revertToVersionId **   <a name="healthimaging-Type-MetadataUpdates-revertToVersionId"></a>
Specifies the previous image set version ID to revert the current image set back to.
You must provide either `revertToVersionId` or `DICOMUpdates` in your request. A `ValidationException` error is thrown if both parameters are provided at the same time.
Type: String
Pattern: `\d+`
Required: No

## See Also
<a name="API_MetadataUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/MetadataUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/MetadataUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/MetadataUpdates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
