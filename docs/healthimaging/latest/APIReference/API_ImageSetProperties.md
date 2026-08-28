---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_ImageSetProperties.html
---

# ImageSetProperties
<a name="API_ImageSetProperties"></a>

The image set properties.

## Contents
<a name="API_ImageSetProperties_Contents"></a>

 ** imageSetId **   <a name="healthimaging-Type-ImageSetProperties-imageSetId"></a>
The image set identifier.
Type: String
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** imageSetState **   <a name="healthimaging-Type-ImageSetProperties-imageSetState"></a>
The image set state.
Type: String
Valid Values: `ACTIVE | LOCKED | DELETED`
Required: Yes

 ** versionId **   <a name="healthimaging-Type-ImageSetProperties-versionId"></a>
The image set version identifier.
Type: String
Pattern: `\d+`
Required: Yes

 ** createdAt **   <a name="healthimaging-Type-ImageSetProperties-createdAt"></a>
The timestamp when the image set properties were created.
Type: Timestamp
Required: No

 ** deletedAt **   <a name="healthimaging-Type-ImageSetProperties-deletedAt"></a>
The timestamp when the image set properties were deleted.
Type: Timestamp
Required: No

 ** ImageSetWorkflowStatus **   <a name="healthimaging-Type-ImageSetProperties-ImageSetWorkflowStatus"></a>
The image set workflow status.
Type: String
Valid Values: `CREATED | COPIED | COPYING | COPYING_WITH_READ_ONLY_ACCESS | COPY_FAILED | UPDATING | UPDATING_FOR_STUDY_CONSISTENCY | UPDATED | UPDATE_FAILED | DELETING | DELETED | IMPORTING | IMPORTED | IMPORT_FAILED`
Required: No

 ** isPrimary **   <a name="healthimaging-Type-ImageSetProperties-isPrimary"></a>
The flag to determine whether the image set is primary or not.
Type: Boolean
Required: No

 ** message **   <a name="healthimaging-Type-ImageSetProperties-message"></a>
The error message thrown if an image set action fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w -:`]+`
Required: No

 ** overrides **   <a name="healthimaging-Type-ImageSetProperties-overrides"></a>
Contains details on overrides used when creating the returned version of an image set. For example, if `forced` exists, the `forced` flag was used when creating the image set.
Type: [Overrides](API_Overrides.md) object
Required: No

 ** updatedAt **   <a name="healthimaging-Type-ImageSetProperties-updatedAt"></a>
The timestamp when the image set properties were updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ImageSetProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/ImageSetProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/ImageSetProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/ImageSetProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
